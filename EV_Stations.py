import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def fetch_ev_stations():

    API_KEY = "YUsnZGWQHize4HF9nCLGgSAryMq8Sw1M"
    LAT = 22.3193  
    LON = 114.1694  
    RADIUS = 50000  
    LIMIT = 50  
    OFFSET_STEP = 50  
    MAX_RESULTS = 700 


    all_results = []
    offset = 0

    while len(all_results) < MAX_RESULTS:
        url = f"https://api.tomtom.com/search/2/categorySearch/electric%20vehicle%20station.json"
        params = {
            "key": API_KEY,
            "lat": LAT,
            "lon": LON,
            "radius": RADIUS,
            "limit": LIMIT,
            "offset": offset
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        results = data.get("results", [])
        if not results:
            break 

        all_results.extend(results)  
        offset += OFFSET_STEP  # Move to next batch

        
    return all_results

    

@app.route("/ev_stations_data", methods=["GET"])
def get_processed_ev_station_data():
    raw_data = fetch_ev_stations()

    processed_data = []


    for result in raw_data:
        name = result.get('poi').get('name')
        address = result.get('address')
        lat_pos = result.get('position', {}).get('lat')
        long_pos = result.get('position', {}).get('lon')
        connectors = result.get('chargingPark', {}).get('connectors')

        processed_data.append({"name": name,
                               "address": address,
                                "latitude": lat_pos,
                                "longitude":long_pos,
                                "connectors": connectors} )
    print(len(processed_data))
    
    return jsonify(processed_data)




if __name__ == '__main__':
    app.run(debug=True)
        