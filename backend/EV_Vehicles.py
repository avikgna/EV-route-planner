
import requests
import psycopg2
import json

def get_unique_car():
    connection = psycopg2.connect(
        host="localhost",
        database="EV_Specifications",
        user="postgres",
        password="Year-75763"
    )
    cursor = connection.cursor()
    EV_car_query = (
        "SELECT mo.year_produced, m.make, mo.model, t.trim "
        "FROM EV_MANUFACTURERS m "
        "JOIN EV_MODELS mo ON mo.manufacturer_id = m.id "
        "JOIN EV_TRIMS t ON t.ev_model_id = mo.id"
    )
    cursor.execute(EV_car_query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_ev_specs():
    headers = {"x-AuthKey": "ca3e22b4f1c911ef99d10242ac120002"}
    base_url = "https://api.vehicledatabases.com/electric-vehicle/{year}/{make}/{model}/{trim}"
    
    car_specs = get_unique_car()
    collected_data = []  # List to accumulate data from each API call
    
    for spec in car_specs:
        year_produced, make, model, trim = spec

        # Process only vehicles from 2022 onward.
        if int(year_produced) not in [2020, 2021]:
            continue
        
        url = base_url.format(year=year_produced, make=make, model=model, trim=trim)
        print("Querying URL:", url)

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        powertrain = data.get("data", {}).get("powertrain", {})
        
        # Create a dictionary for this vehicle's data
        entry = {
            "year": year_produced,
            "make": make,
            "model": model,
            "trim": trim,
            "All Electric Range": powertrain.get("Hybrid traction battery all electric range", "Not provided"),
            "Battery Capacity (kWh)": powertrain.get("Hybrid traction battery capacity (kWh)", "Not provided"),
            "Charge Time (hrs @ 240V)": powertrain.get("Hybrid traction battery charge time (hrs) @ 240V", "Not provided"),
            "DC Fast Charge Connector": powertrain.get("Hybrid traction battery DC fast charge connector", "Not provided"),
            "Peak DC Fast Charge Rate (kW)": powertrain.get("Hybrid traction battery peak DC fast charge rate (kW)", "Not provided"),
            "Peak DC Fast Charge Time (minutes)": powertrain.get("Hybrid traction battery peak DC fast charge time (minutes)", "Not provided"),
            "Power Output (kW)": powertrain.get("Hybrid traction battery power output (kW)", "Not provided"),
            "Battery Type": powertrain.get("Hybrid traction battery type", "Not provided"),
            "Battery Voltage": powertrain.get("Hybrid traction battery voltage", "Not provided")
        }
        
        collected_data.append(entry)
    
    return collected_data

def export_data_to_file(data, filename="ev_specs_outputs.json"):
    # Write the collected data to a JSON file with pretty formatting
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    data = get_ev_specs()
    export_data_to_file(data)

# import requests
# import psycopg2

# def get_unique_car():
#     connection = psycopg2.connect(
#         host="localhost",
#         database="EV_Specifications",
#         user="postgres",
#         password="Year-75763"
#     )
#     cursor = connection.cursor()
#     EV_car_query = (
#         "SELECT mo.year_produced, m.make, mo.model, t.trim "
#         "FROM EV_MANUFACTURERS m "
#         "JOIN EV_MODELS mo ON mo.manufacturer_id = m.id "
#         "JOIN EV_TRIMS t ON t.ev_model_id = mo.id"
#     )
#     cursor.execute(EV_car_query)
#     result = cursor.fetchall()
#     cursor.close()
#     connection.close()
#     return result

# def get_ev_specs():
    
#     headers = {"x-AuthKey": "ca3e22b4f1c911ef99d10242ac120002"}
#     base_url = "https://api.vehicledatabases.com/electric-vehicle/{year}/{make}/{model}/{trim}"
    
#     car_specs = get_unique_car()
    
    
#     for spec in car_specs:

#         year_produced, make, model, trim = spec

#         if int(year_produced) < 2022:
#             continue
        
#         url = base_url.format(year=year_produced, make=make, model=model, trim=trim)
#         print(url)

#         response = requests.get(url, headers=headers)
#         response.raise_for_status() 
#         data = response.json()
        
#         results = data.get("results", [])


#         powertrain = data.get("data", {}).get("powertrain", {})

#         battery_range = powertrain.get("Hybrid traction battery all electric range", "Not provided")
#         battery_capacity = powertrain.get("Hybrid traction battery capacity (kWh)", "Not provided")
#         charge_time = powertrain.get("Hybrid traction battery charge time (hrs) @ 240V", "Not provided")
#         dc_connector = powertrain.get("Hybrid traction battery DC fast charge connector", "Not provided")
#         peak_dc_rate = powertrain.get("Hybrid traction battery peak DC fast charge rate (kW)", "Not provided")
#         peak_dc_time = powertrain.get("Hybrid traction battery peak DC fast charge time (minutes)", "Not provided")
#         power_output = powertrain.get("Hybrid traction battery power output (kW)", "Not provided")
#         battery_type = powertrain.get("Hybrid traction battery type", "Not provided")
#         battery_voltage = powertrain.get("Hybrid traction battery voltage", "Not provided")

#         print("All Electric Range:", battery_range)
#         print("Battery Capacity (kWh):", battery_capacity)
#         print("Charge Time (hrs @ 240V):", charge_time)
#         print("DC Fast Charge Connector:", dc_connector)
#         print("Peak DC Fast Charge Rate (kW):", peak_dc_rate)
#         print("Peak DC Fast Charge Time (minutes):", peak_dc_time)
#         print("Power Output (kW):", power_output)
#         print("Battery Type:", battery_type)
#         print("Battery Voltage:", battery_voltage)



# get_ev_specs()

