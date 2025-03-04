import math

MILES_TO_KM_RATE = 1.6
KM_TO_M_RATE = 1000
M_TO_KM_RATE = 0.001

def convert_meters_to_km(x):
    return x * M_TO_KM_RATE

def convert_miles_to_meters(x):
    return x * MILES_TO_KM_RATE * KM_TO_M_RATE

def calc_energy_consumption_rate(capacity, full_range):
    full_range_km = full_range * MILES_TO_KM_RATE
    return capacity / full_range_km  

def calc_energy_used(distance, consumption_rate):
    return distance * consumption_rate

def calc_energy_capacity_level(capacity, battery_percent):
    return (battery_percent / 100) * capacity

def require_charging_stop(distance, full_range, battery_capacity, initBattery, dstBattery):
    energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
    required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
    energy_consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)
    distance_m = convert_meters_to_km(distance)

    total_energy_usage = distance_m * energy_consumption_rate
    remaining_energy = energy_available - total_energy_usage

    return remaining_energy < required_energy_end  # True if charge needed

def locate_charging_stop_point_bbox(start, end, distance, battery_capacity, full_range, initBattery, dstBattery, box_radius=10):
    energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
    required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
    energy_consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)
    distance_m = convert_meters_to_km(distance)

    usable_energy = energy_available - required_energy_end
    distance_to_travel_before_charge = usable_energy / energy_consumption_rate

    if distance_m < distance_to_travel_before_charge:
        return None  # No charging stop needed

    fraction_traveled = distance_to_travel_before_charge / distance_m
    charging_stop_coord = interpolate_point(start, end, fraction_traveled)
    bbox = bounding_box(charging_stop_coord, box_radius)

    return {
        "charging_stop_needed_point": charging_stop_coord,
        "bounding_box_parameters": bbox
    }

def plan_trip_and_waypoints(distance, startCoords, destinationCoords, car):
    chargingSpecs = car.get("chargingSpecs", {})
    battery_capacity = float(chargingSpecs.get("battery_capacity_kwh", 0))
    full_range = float(chargingSpecs.get("all_electric_range", 0))
    initBattery = float(car.get("initialBatteryPercentage", 0))
    dstBattery = float(car.get("requiredBatteryPercentage", 0))

    distance_m = convert_meters_to_km(distance)

    consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)
    expected_consumption = calc_energy_used(distance_m, consumption_rate)
    energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
    required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)

    charging_stop_needed = require_charging_stop(distance, full_range, battery_capacity, initBattery, dstBattery)

    result = {
        "Consumption Rate": consumption_rate,
        "expectedConsumption_kWh": expected_consumption,
        "energyAvailable_kWh": energy_available,
        "requiredEnergy__at_end_kWh": required_energy_end,
        "chargingStopNeeded": charging_stop_needed,
        "chargingStops": []
    }

    if charging_stop_needed:
        charging_stop = locate_charging_stop_point_bbox(startCoords, destinationCoords, distance, battery_capacity, full_range, initBattery, dstBattery, box_radius=10)
        if charging_stop:
            result["chargingStops"].append(charging_stop)

    return result

def interpolate_point(start, end, fraction):
    return {
        "lat": start["lat"] + fraction * (end["lat"] - start["lat"]),
        "lng": start["lng"] + fraction * (end["lng"] - start["lng"])
    }

def bounding_box(center, radius_km):
    lat, lng = center["lat"], center["lng"]
    delta_lat = radius_km / 111.0
    delta_lng = radius_km / (111.0 * math.cos(math.radians(lat)))
    return (lng - delta_lng, lat - delta_lat, lng + delta_lng, lat + delta_lat)



# import math

# MILES_TO_KM_RATE = 1.6
# KM_TO_M_RATE = 1000

# def convert_miles_to_meters(x):
#     km_val = x * MILES_TO_KM_RATE
#     m_val = km_val * KM_TO_M_RATE

#     return m_val

# def calc_energy_consumption_rate(capacity, range):
#     full_range_km  = range * MILES_TO_KM_RATE
#     energy_consumption_rate = capacity / full_range_km

#     return energy_consumption_rate

# def calc_energy_used(distance, consumption_rate):
#     return distance / consumption_rate

# def calc_energy_capacity_level(capacity, battery_percent):
#     battery_fraction = battery_percent / 100
#     curr_capacity = battery_fraction * capacity
    
#     return curr_capacity
    
# def low_capacity_threshold(capacity, range):
#     low_battery = capacity * 0.1
#     remaining_dist = low_battery * calc_energy_consumption_rate(capacity, range)
    
#     return low_battery, remaining_dist

# def require_charging_stop(distance, full_range, battery_capacity, initBattery, dstBattery):

#     if dstBattery > initBattery:
#         return True

#     energy_consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)

#     energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
#     required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
#     total_energy_usage = distance*energy_consumption_rate

#     if (energy_available - total_energy_usage) < required_energy_end:
#         return True
    
#     return False

# def locate_charging_stop_point_bbox(start, end, distance, battery_capacity, full_range, initBattery, dstBattery, box_radius=10):
#     """
#     Calculate a single charging stop location if needed, without recursion.
#     """
#     energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
#     required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
#     usable_energy = energy_available - required_energy_end
#     energy_consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)

#     distance_to_travel_before_charge = usable_energy / energy_consumption_rate

#     # If we can reach the destination without charging, return an empty list
#     if distance < distance_to_travel_before_charge:
#         return None

#     # Find the first charging stop location
#     route_fraction_traversable = distance_to_travel_before_charge / distance
#     charging_stop_needed_coord = interpolate_point(start, end, route_fraction_traversable)
#     bbox = bounding_box(charging_stop_needed_coord, box_radius)

#     current_stop = {
#         "charging_stop_needed_point": charging_stop_needed_coord,
#         "bounding_box_parameters": bbox
#     }

#     return current_stop

# def plan_trip_and_waypoints(distance, startCoords, destinationCoords, car):
#     """
#     Determines whether a charging stop is needed and returns route details.
#     """
#     chargingSpecs = car.get("chargingSpecs", {})
#     battery_capacity = float(chargingSpecs.get("battery_capacity_kwh", 0))
#     full_range = float(chargingSpecs.get("all_electric_range", 0))
#     initBattery = float(car.get("initialBatteryPercentage", 0))
#     dstBattery = float(car.get("requiredBatteryPercentage", 0))

#     consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)
#     expected_consumption = distance * consumption_rate
#     energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
#     required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)

#     charging_stop_needed = require_charging_stop(distance, full_range, battery_capacity, initBattery, dstBattery)

#     result = {
#         "expectedConsumption_kWh": expected_consumption,
#         "energyAvailable_kWh": energy_available,
#         "requiredEnergy_kWh": required_energy_end,
#         "chargingStopNeeded": charging_stop_needed,
#         "chargingStops": []
#     }

#     # Add only **one** charging stop if needed
#     if charging_stop_needed:
#         charging_stop = locate_charging_stop_point_bbox(startCoords, destinationCoords, distance, battery_capacity, full_range, initBattery, dstBattery, box_radius=10)
#         if charging_stop:
#             result["chargingStops"].append(charging_stop)

#     return result

# def interpolate_point(start, end, fraction):
#     lat = start["lat"] + (fraction * (end["lat"] - start["lat"]))
#     lng = start["lng"] + (fraction * (end["lng"] - start["lng"]))

#     return {"lat": lat, "lng": lng}

# def bounding_box(center, radius_km):

#     lat = center["lat"]
#     lng = center["lng"]

#     #One degree of Latitude corresponds to 111km
#     delta_lat = radius_km/111.0 #gives us how many latitudes needed to correspond to the radius value
    
#     #at the equator one degree of longitude is about 111km but as you move away a longitude is shorter. We need to scale with latitude
#     lat_radians = math.radians(lat)
#     delta_lng = radius_km/(111.0*math.cos(lat_radians))

#     return(lng - delta_lng, lat - delta_lat, lng + delta_lng, lat + delta_lat)


# # def locate_charging_stop_point_bbox(start, end, distance, battery_capacity, full_range, initBattery, dstBattery, box_radius=10):

# #     energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
# #     required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
# #     usable_energy = energy_available - required_energy_end
# #     energy_consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)

# #     distance_to_travel_before_charge = usable_energy / energy_consumption_rate

# #     # print(battery_capacity)
# #     # print(initBattery)
# #     # print(dstBattery)

# #     # print(energy_available)
# #     # print(required_energy_end)
# #     # print(usable_energy)
# #     # print(energy_consumption_rate)
# #     # print(distance_to_travel_before_charge)

# #     if distance < distance_to_travel_before_charge:
# #         return []

# #     route_fraction_traversable = distance_to_travel_before_charge/distance
# #     charging_stop_needed_coord = interpolate_point(start, end, route_fraction_traversable)

# #     bbox = bounding_box(charging_stop_needed_coord, box_radius)

# #     current_stop = {
# #         "charging_stop_needed_point": charging_stop_needed_coord,
# #         "bounding_box_paramaters": bbox
# #     }

# #     return current_stop

#     # new_init_battery = 100
#     # new_distance = distance - distance_to_travel_before_charge
#     # print("nd", new_distance)

#     # if new_distance < 0.1:
#     #     return [current_stop]

#     # remaining_stops = locate_charging_stop_point_bbox(charging_stop_needed_coord, end, new_distance, battery_capacity, full_range, new_init_battery, dstBattery, box_radius)
#     # return [current_stop] + remaining_stops



# # def plan_trip_and_waypoints(distance, startCoords, destinationCoords, car):


# #     """
# #     Calculate the energy consumption for the route, determine if charging stops are needed,
# #     and return candidate charging stop points (with bounding boxes) along the route.
    
# #     Parameters:
# #       - startCoords, destinationCoords: dicts with "lat" and "lng"
# #       - car: dict with keys:
# #            "chargingSpecs": { "battery_capacity_kwh", "all_electric_range" (in miles) }
# #            "initialBatteryPercentage"
# #            "requiredBatteryPercentage"
    
# #     Returns:
# #       A dict with overall route info and, if needed, a list of candidate charging stops.
# #     """
    
# #     # Extract car specs.
# #     chargingSpecs = car.get("chargingSpecs", {})
# #     battery_capacity = float(chargingSpecs.get("battery_capacity_kwh", ""))
# #     print(battery_capacity)
# #     full_range = float(chargingSpecs.get("all_electric_range", ""))
# #     print(full_range)
# #     initBattery = float(car.get("initialBatteryPercentage", ""))
# #     print(initBattery)
# #     dstBattery = float(car.get("requiredBatteryPercentage", ""))
# #     print(dstBattery)
    
# #     # Energy consumption rate in kWh per km.
# #     consumption_rate = calc_energy_consumption_rate(battery_capacity, full_range)
    
# #     expected_consumption = distance * consumption_rate
# #     energy_available = calc_energy_capacity_level(battery_capacity, initBattery)
# #     required_energy_end = calc_energy_capacity_level(battery_capacity, dstBattery)
    
# #     charging_stop_needed = require_charging_stop(distance, full_range, battery_capacity, initBattery, dstBattery)
    
# #     result = {
# #         "expectedConsumption_kWh": expected_consumption,
# #         "energyAvailable_kWh": energy_available,
# #         "requiredEnergy_kWh": required_energy_end,
# #         "chargingStopNeeded": charging_stop_needed,
# #         "chargingStops": []
# #     }
    
# #     if charging_stop_needed:
# #         charging_stops = locate_charging_stop_point_bbox(startCoords, destinationCoords, distance,
# #                                                          battery_capacity, full_range, initBattery, dstBattery, box_radius=10)
# #         result["chargingStops"] = charging_stops
    
# #     return result







    


#     #return True or False based on calculation whether charging stop is needed

# # def locate_charging_stops():

#     #call require charging stop, if true then we draw a bounding box for when we estimate a car is around 10% battery
#     # alternatively draw a bounding box at some point of the remaining route if we determine that when we reach the end we will not have AT LEAST the required minimum battery
#     # upon drawing a bounding box set a radius and locate charging stops. Select one which matches connector with our given car and perhaps highest charging time
#     # get its long/lat then include it as a waypoint in our routing api

#     # recursively repeat require chargign stop and locate charging stop on smaller distances until we determine that we dont ened another charge stop until end



    


