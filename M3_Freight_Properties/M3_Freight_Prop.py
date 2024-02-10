# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-06-14
#
# Function Description
# Part of the Freight Properties M3
# Definition of Freight Properties
# _________________________________


# Import Functions
import numpy as np
from Modules.M3_Freight_Properties import ROUTE_model


# Used Sources in this file


def freight_properties(sim, env, scenario):
    # Get Route (Speed Profile)
    route_array_distance, route_array_speed, route_array_stoptime, route_array_slope = ROUTE_model.freight_model(env, scenario)
    # Adding Slope profile (still to be defined in Driving Cycle Tool)
    # route_array_slope = np.zeros(len(route_array_distance))
    # Start Mission at 8:00
    freight_mission_start = scenario['mission_start'][0]
    # Definition of Freight Payload in t
    freight_payload = scenario['payload'][0]  # t
    # Definition of start SOC
    freight_start_soc = scenario['start_soc'][0]
    # Definition of Target SOC at Destination
    freight_destination_soc = scenario['end_soc'][0]
    # Store all variables in env Object
    env.route_array_distance = route_array_distance
    env.route_array_speed = route_array_speed
    env.route_array_stoptime = route_array_stoptime
    env.route_array_slope = route_array_slope
    env.freight_mission_start = freight_mission_start
    env.freight_payload = freight_payload
    env.freight_destination_soc = freight_destination_soc
    env.freight_start_soc = freight_start_soc

    return sim, env
