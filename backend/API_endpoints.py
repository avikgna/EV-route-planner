import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS
from energy_model import plan_trip_and_waypoints
import requests

geoapifyKey = "0ff228e397b043d8a388d6f0d6599014"

app = Flask(__name__)
CORS(app)

stored_charging_data = {
    "bounding_box": None,
    "charging_stations": None
}

waypoints = {
    "startLat": None,
    "startLng": None,
    "dstLat": None,
    "dstLng": None,
    "stationLat": None,
    "stationLng": None

}

def get_db_connection():
    connection = psycopg2.connect(
        host = "localhost",
        database = "EV_Specifications",
        user = "postgres",
        password = "Year-75763"
    )

    return connection


@app.route('/api/cars/makes')
def get_makes():
    conn = get_db_connection()
    cursor = conn.cursor()
    makes = []

    makes_sql = "SELECT DISTINCT make FROM EV_MANUFACTURERS ORDER BY make"

    cursor.execute(makes_sql)

    for make in cursor.fetchall():
        print(make[0])
        makes.append(make[0])
    
    print(makes)
    
    return jsonify(makes)



@app.route('/api/cars/models')
def get_models():

    make = request.args.get('make')

    if not make:
        return jsonify({"error": "make not provided"})
    
    conn = get_db_connection()
    cursor = conn.cursor()
    models = []

    models_sql = """SELECT DISTINCT m.model 
    FROM EV_MODELS m JOIN EV_MANUFACTURERS mo 
    ON m.manufacturer_id = mo.id WHERE mo.make = %s ORDER BY m.model"""

    cursor.execute(models_sql, (make,))

    for model in cursor.fetchall():
        models.append(model[0])
    
    return jsonify(models)



@app.route('/api/cars/years')
def get_years():

    make = request.args.get('make')
    model = request.args.get('model')

    if not make or not model:
        return jsonify({"error": "required make or/and model not provided"})
    
    conn = get_db_connection()
    cursor = conn.cursor()
    years = []

    years_sql = """SELECT DISTINCT m.year_produced 
    FROM EV_MODELS m JOIN EV_MANUFACTURERS mo 
    ON m.manufacturer_id = mo.id WHERE mo.make = %s AND m.model = %s ORDER BY m.year_produced"""

    cursor.execute(years_sql, (make,model))

    for year in cursor.fetchall():
        years.append(year[0])
    
    return jsonify(years)

@app.route('/api/cars/trims')
def get_trims():

    make = request.args.get('make')
    model = request.args.get('model')
    year = request.args.get('year')

    if not make or not model or not year:
        return jsonify({"error": "required make, model or/and year not provided"})
    
    conn = get_db_connection()
    cursor = conn.cursor()
    trims = []

    trims_sql = """SELECT DISTINCT t.trim
    FROM EV_MODELS m JOIN EV_MANUFACTURERS mo 
    ON m.manufacturer_id = mo.id  JOIN EV_TRIMS t ON m.id = t.ev_model_id WHERE mo.make = %s AND m.model = %s AND m.year_produced = %s ORDER BY t.trim"""

    cursor.execute(trims_sql, (make,model, year))

    for trim in cursor.fetchall():
        trims.append(trim[0])
    
    return jsonify(trims)

@app.route('/api/cars/specs')
def get_specs():
    make = request.args.get('make')
    model = request.args.get('model')
    year = request.args.get('year')
    trim = request.args.get('trim')

    if not make or not model or not year or not trim:
        return jsonify({"error": "required make, model, trim or/and year not provided"})
    
    conn = get_db_connection()
    cursor = conn.cursor()
    specs = {}

    specs_sql = """SELECT all_electric_range, battery_capacity_kwh, peak_charge_rate_kw, peak_charge_time_minutes, 
    dc_connector_type FROM EV_MODELS m JOIN EV_MANUFACTURERS mo 
    ON m.manufacturer_id = mo.id JOIN EV_TRIMS t ON m.id = t.ev_model_id JOIN EV_SPECS s ON s.trim_id = t.id WHERE 
    mo.make = %s AND m.model = %s AND m.year_produced = %s AND t.trim = %s"""

    cursor.execute(specs_sql,(make, model, year, trim))

    spec = cursor.fetchone()

    if spec is None:
        return jsonify({"error": "No specs found for the given parameters"}), 404

    specs = {"all_electric_range": spec[0] if spec[0] is not None else "N/A",  
            "battery_capacity_kwh" : spec[1] if spec[1] is not None else "N/A", 
            "peak_charge_rate_kw" : spec[2] if spec[2] is not None else "N/A", 
            "peak_charge_time_minutes": spec[3] if spec[3] is not None else "N/A", 
            "dc_connector_type" : spec[4] if spec[4] is not None else "N/A"
            }
    
    return jsonify(specs)


@app.route('/api/ev-route/payload', methods=['POST'])
def get_payload():
    trip_and_car_details = request.get_json()

    startCoords = trip_and_car_details.get("startCoords")
    destinationCoords = trip_and_car_details.get("destinationCoords")
    distanceInMeters = trip_and_car_details.get("distanceInMeters")
    car_details = trip_and_car_details.get("car", {})
    initBattery = car_details.get("initialBatteryPercentage")
    dstBattery =  car_details.get("requiredBatteryPercentage")

    waypoints["startLat"] = startCoords["lat"]
    waypoints["startLng"] = startCoords["lng"]
    waypoints["dstLat"] = destinationCoords["lat"]
    waypoints["dstLng"] = destinationCoords["lng"]
    waypoints["stationLat"] = None
    waypoints["stationLng"] = None

    charge_stop_calculations = plan_trip_and_waypoints(distanceInMeters,startCoords, destinationCoords, car_details) 

    charging_stops = charge_stop_calculations.get("chargingStops", [])
    bounding_box = charging_stops[0].get("bounding_box_parameters")

    stored_charging_data["bounding_box"] = bounding_box
    stored_charging_data["charging_stations"] = None
    
    result = {
        "message": "Trip Details Delivered Successfully",
        "trip_and_car_details" : trip_and_car_details,
        "bounding_box_parameters": bounding_box

    }

    print(result)

    if bounding_box:
        fetch_charging_stations()


    return jsonify(result)

def fetch_charging_stations():
    if not stored_charging_data["bounding_box"]:
        return {"error": "No bounding box available"}

    minLng, minLat, maxLng, maxLat = stored_charging_data["bounding_box"]
    geoapify_url = f"https://api.geoapify.com/v2/places?categories=service.vehicle.charging_station&filter=rect:{minLng},{minLat},{maxLng},{maxLat}&limit=5&apiKey={geoapifyKey}"

    try:
        response = requests.get(geoapify_url)
        response.raise_for_status()
        stations_data = response.json()

        # ✅ Store fetched charging stations
        stored_charging_data["charging_stations"] = stations_data

        if stations_data.get("features"):
            first_station = stations_data["features"][0]
            coordinates = first_station["geometry"]["coordinates"]

            waypoints["stationLat"] = coordinates[1] #lat
            waypoints["stationLng"] = coordinates[0] #lng

        return {"message": "Charging stations updated successfully"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Geoapify API call failed: {str(e)}"}
    
@app.route('/api/charging-stations', methods=['GET'])
def get_charging_stations():
    """ ✅ Calls Geoapify and returns charging stations """
    return jsonify(stored_charging_data)



@app.route('/api/waypoints', methods=['GET'])
def get_waypoints():
    return jsonify(waypoints)


if __name__ == '__main__':
    app.run(debug=True, port=5000)






