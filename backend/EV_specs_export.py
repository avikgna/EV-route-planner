import json
import psycopg2


def retrieve_car_trimid(cursor, reference):

    year_produced = reference.get("year")
    make = reference.get("make")
    model = reference.get("model")
    trim = reference.get("trim")

    trim_id_SQL = """SELECT t.id FROM 
    ev_trims t JOIN ev_models m ON t.ev_model_id = m.id 
    JOIN ev_manufacturers mo ON m.manufacturer_id = mo.id 
    WHERE t.trim = %s AND m.model = %s AND m.year_produced = %s AND mo.make = %s"""

    cursor.execute(trim_id_SQL, (trim, model, year_produced, make))

    result = cursor.fetchone()
    if result:
        return result[0]
    else: 
        print("no match")
        return None           


def parse_int(value, units=""):
    if isinstance(value, str):
        if "pg_foreign_server_name_index" in value or "pg_foreign_data_wrapper_name_index" in value:
            return None
        # Check if the unwanted substring appears anywhere in the value.
        cleaned = value.replace(units, "").strip()
        if not cleaned:
            return None
        parts = cleaned.split()
        if not parts:
            return None
        try:
            return int(parts[0])
        except ValueError:
            return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parse_float(value, units=""):
    if isinstance(value, str):
        if "pg_foreign_server_name_index" in value or "pg_foreign_data_wrapper_name_index" in value:
            return None
        cleaned = value.replace(units, "").strip()
        if not cleaned:
            return None
        parts = cleaned.split()
        if not parts:
            return None
        try:
            return float(parts[0])
        except ValueError:
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def insert_charging_specs(cursor, trim_id, reference):
    
    all_electric_range = parse_int(reference.get("All Electric Range", ""), "miles")
    battery_capacity = parse_float(reference.get("Battery Capacity (kWh)", ""))
    charge_time_240V = parse_float(reference.get("Charge Time (hrs @ 240V)", ""))
    dc_connector_type = reference.get("DC Fast Charge Connector", None)
    peak_charge_rate_kw = parse_float(reference.get("Peak DC Fast Charge Rate (kW)", ""))
    peak_charge_rate_min = parse_int(reference.get("Peak DC Fast Charge Time (minutes)", ""))
            
    power_output_kw = reference.get("Power Output (kW)", "").strip().lower()

    if power_output_kw in["not provided", ""]:
            power_output_kw = None
    else:
        power_output_kw = parse_float(reference.get("Power Output (kW)", ""))

    if reference.get("Battery Type", None) == "pg_foreign_data_wrapper_name_index":
        battery_type = None
            
    battery_type = reference.get("Battery Type", None)

    
    battery_voltage = parse_int(reference.get("Battery Voltage", ""))

    ev_specs_sql = """INSERT INTO ev_specs (
        trim_id, all_electric_range, battery_capacity_kwh, 
        charge_time_240V_hrs, dc_connector_type, 
        peak_charge_rate_kw, peak_charge_time_minutes, kw_power_output, battery, battery_voltage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    cursor.execute(ev_specs_sql, (
        trim_id,
        all_electric_range,
        battery_capacity,
        charge_time_240V,
        dc_connector_type,
        peak_charge_rate_kw,
        peak_charge_rate_min,
        power_output_kw,
        battery_type,
        battery_voltage
    ))

def main(filename="ev_specs_output.json"):

    connection = psycopg2.connect(
        host = "localhost",
        database = "EV_Specifications",
        user = "postgres",
        password = "Year-75763"
    )

    cursor = connection.cursor()

    with open(filename, "r") as ev_specs_file:
        ev_references = json.load(ev_specs_file)

        for reference in ev_references:
            trim_id = retrieve_car_trimid(cursor, reference)
            if trim_id and trim_id != "pg_foreign_data_wrapper_name_index" and trim_id != "pg_foreign_server_name_index":
                insert_charging_specs(cursor, trim_id, reference)
                connection.commit()
                print(f"Inserted specs for record: {reference.get('year')} {reference.get('make')} {reference.get('model')} {reference.get('trim')}")



main()



            






        
    


            
        




