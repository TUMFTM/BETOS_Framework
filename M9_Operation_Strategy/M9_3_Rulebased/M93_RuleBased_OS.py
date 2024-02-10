# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-10-04
#
# Function Description
# Part of the Operation Strategy Module M9
# Rule Based Operation Strategy
# _________________________________

# Assuming following Rules
# The driver takes the full mandatory rest at the upcoming PoI if the driving time to the next PoI exceeds his
# permitted driving time.
# The vehicle is charged at the upcoming PoI with a charging point if the range is less than the distance to the next
# charging station on the route.

# ______________________________________________________________________________________________________________________

# Import own functions

# Import Libraries
import numpy as np


# Main strategy function
def betos_rule_based(sim, env, vehicle):
    # Check for actions
    # Get relevant information about route (i=0: current PoI on Route)
    # dp_data[i,0] which charging power is at PoI i available in kW
    # dp_data[i,1] how far is it from PoI i-1 to PoI i in meter
    # dp_data[i,2] how much energy do we need driving from PoI i-1 to PoI i in kWh
    dp_data = dp_data_func(sim, env)

    # Get critical PoI according to driving time
    sim, second_interval = finding_critical_poi(sim, vehicle, env)

    # Calculate SoC at next PoI
    soc_next_poi = sim.bat_soc_dis[sim.step_dis] - (dp_data[1, 2]/vehicle.battery_capacity) - 0.05  # Buffer of 5 %
    # How much SoC to destination
    energy_to_destination = np.cumsum(dp_data[:, 2])  # in kWh
    soc2destination = energy_to_destination[-1] / vehicle.battery_capacity + env.freight_destination_soc

    # Check Rules:
    if (soc_next_poi < vehicle.battery_soc_min and soc2destination-sim.bat_soc_dis[sim.step_dis] > 0.05)  or sim.step_dis == sim.pos_poi_crit:
        # Action
        action = 1
        stops = 1
        charge_target = min(vehicle.battery_soc_max, soc2destination)
        # Charge and Rest
        if env.cs_power > 0:
            charge = 1
            # Check for primary charge
            if soc_next_poi < vehicle.battery_soc_min:
                soc_target = charge_target
                target_charge_time = np.inf  # Target Soc is dominant
                target_rest_time = 0  # Charging is dominant
            else:
                soc_target = charge_target  # rest time will be dominant
        else:
            charge = 0
            soc_target = 0
            target_charge_time = 0
            target_rest_time = 0
    else:
        action = 0
        stops = 0
        charge = 0
        soc_target = 0
        target_charge_time = 0
        target_rest_time = 0

    if sim.step_dis == sim.pos_poi_crit:
        rest = 1
        if sum(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis] > 15*60):
            target_rest_time = 30*60  # in sec
        else:
            target_rest_time = 45*60  # in sec
        target_charge_time = target_rest_time
    elif charge == 1 and sum(sim.time_dis[0:sim.step_dis]) <= 4.0*60*60:
        rest = 1
        target_rest_time = 15*60  # if charging use rest split due to efficiency (only in first driving interval)
    elif charge == 1 and second_interval is True:
        target_rest_time = 45 * 60  # If second driving interval is needed, than do whole rest in case of charging
    else:
        rest = 0

    # <><><>
    # BETOS Variables
    # BETOS Charging Time: sim.betos_charge_time[sim.step_dis] in sec
    sim.betos_charge_time[sim.step_dis] = target_charge_time
    # BETOS Rest Time: sim.betos_rest_target[sim.step_dis] in sec
    sim.betos_rest_time[sim.step_dis] = target_rest_time
    # BETOS Target Soc: sim.betos_soc_target[sim.step_dis]
    sim.betos_soc_target[sim.step_dis] = soc_target
    # BETOS Action: sim.betos_action[sim.step_dis]
    sim.betos_action[sim.step_dis] = action
    if action > 0:
        sim.betos_power[sim.step_dis] = env.cs_power
        # Availability of this Poi
        sim.betos_poi_availability[sim.step_dis] = env.cs_data_availability(sim.daytime)[int(env.infra_array_poi_type[sim.step_dis])]
    # BETOS Stops: sim.betos_stops
    sim.betos_stops = sim.betos_stops + stops

    return sim


# Finding critical PoI from current Position:
# Critical PoI is that PoI at which the whole rest mjust be done at the latest.
def finding_critical_poi(sim, vehicle, env):
    # Initialize pos_poi_max
    pos_poi_max = sim.pos_poi_max
    # Initialize pos_poi_crit
    pos_poi_crit = sim.pos_poi_crit
    # If there is a second driving interval which is needed:
    if sim.pos_rest_done > 0:
        pos_poi_crit = sim.pos_rest_done
    # Get driving time: Total Time minus Rest Time
    time_driven = sum(sim.time_dis[sim.pos_rest_done+1:sim.step_dis])
    # Check for second driving interval to reach destination
    if sim.pos_rest_done > 0 and np.cumsum(sim.betos_time_dis_prediction[sim.pos_rest_done+1:])[-1] > 4.5*60*60:
        second_interval = True
        first_interval = False
    else:
        second_interval = False
        first_interval = True
    # Shorten Prediction Vector in time
    time_prediction = sim.betos_time_dis_prediction[sim.step_dis:]
    steps = len(time_prediction)
    # Cumulated Time Prediction
    time_cum_prediction = np.cumsum(time_prediction)
    # Remaining driving time till 4.5h
    time_remain = (4.5 * 3600) - time_driven  # in sec
    # Index
    i = 0
    # Search for critical PoI if time remain is greater than zero
    if time_remain > 0:
        while time_cum_prediction[i] < time_remain and i < steps - 1:
            # Look for PoI
            if env.infra_array_poi[sim.step_dis + i] == 1:
                sim.pos_poi_crit = sim.step_dis + i

            # Update Index
            i = i + 1
        # Destination is critical PoI
        if steps - i < 2:
            sim.pos_poi_crit = sim.dis_steps - 1

    # <>
    # Search for maximal reachable POI within driving time
    time_remain_max = vehicle.driving_time_max - sum(sim.time_dis[sim.pos_overnight_stay:sim.step_dis])  # in sec
    steps_max = min(len(time_prediction), (vehicle.max_day_distance - (
                sim.step_dis - sim.pos_overnight_stay)))  # maximum daily distance barrier
    # Index
    i = 0
    # Search for critical PoI if time remain is greater than zero
    if time_remain_max > 0:
        while time_cum_prediction[i] < time_remain_max and i < steps_max - 1:
            # Look for PoI
            if env.infra_array_poi[sim.step_dis + i] == 1:
                pos_poi_max = sim.step_dis + i

            # Update Index
            i = i + 1
        # Destination is maximum reachable POI
        if steps - i < 2:
            pos_poi_max = sim.dis_steps - 1

    # Safe sim pos max
    sim.pos_poi_max = pos_poi_max

    return sim, second_interval


# Extract Data for DP Approach
# dp_data[i,0] which charging power is at PoI i available in kW
# dp_data[i,1] how far is it from PoI i-1 to PoI i in meter
# dp_data[i,2] how much energy do we need driving from PoI i-1 to PoI i in kWh
def dp_data_func(sim, env):
    # Number PoI Total
    poi_id_current = int(env.infra_array_poi_id[sim.step_dis])
    poi_id_destination = int(env.infra_array_poi_id[-1])
    number_poi = poi_id_destination - poi_id_current
    # Initialization of data: dp_data=[Charging Power, Distance to this PoI from last PoI,
    # Energy Consumption to this PoI]
    dp_data = np.zeros((number_poi+1, 3))
    # Fill in data
    for i in range(0, number_poi+1):
        # Power
        dp_data[i, 0] = env.cs_data_power[int(env.infra_array_poi_type[int(env.infra_array_poi_pos[poi_id_current + i])])]
        # Distance and Average energy consumption between this and next POI
        if i > 0:
            dp_data[i, 1] = env.infra_array_poi_pos[poi_id_current+i] - env.infra_array_poi_pos[poi_id_current+i-1]
            dp_data[i, 2] = sum(sim.betos_energy_cons_dis_prediction[int(env.infra_array_poi_pos[poi_id_current+i-1]):
                                                                     int(env.infra_array_poi_pos[poi_id_current+i])]) /\
                                                                     (1000*60*60)  # in kWh

    return dp_data

