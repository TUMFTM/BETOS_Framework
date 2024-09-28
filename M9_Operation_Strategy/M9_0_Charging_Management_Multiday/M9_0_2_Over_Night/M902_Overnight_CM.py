# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-07-04
#
# Function Description
# Part of the Operation Strategy Module M9
# Overnight Charging Simulation, in future with V2G Integration
# Implementation of overnight charging simulation
# _________________________________


# import libraries
import numpy as np

# import functions:
from Modules.M10_Evaluation import M10_Evaluation_Aging

# used sources in this file:


# Overnight charging simulation main:
def overnight_charging(sim, env, vehicle):
    # <>
    # Aging Evaluation
    sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] = 0      # Driving before overnight Charging
    sim, env, vehicle = M10_Evaluation_Aging.aging_evaluation(sim, env, vehicle)
    # <>
    if sim.betos_version != 31:
        # Call easy slow charge function
        sim = slow_charging(sim, env, vehicle)
    else:
        # Use advanced overnight charging function
        sim = slow_charging_heuristic(sim, env, vehicle)
    # <>
    # Set overnight stay position
    sim.pos_overnight_stay = sim.step_dis
    # Set pos poi max to high value, new pos poi max is calculated new
    sim.pos_poi_max = 3000000
    # Set sim pos rest done
    sim.pos_rest_done = sim.step_dis

    # <>
    # Aging Evaluation
    sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] = 2      # Overnight Charging
    sim, env, vehicle = M10_Evaluation_Aging.aging_evaluation(sim, env, vehicle)

    return sim


# Slow Charging Function:
def slow_charging(sim, env, vehicle):
    # <>
    # Save arrival time at POI
    sim.betos_poi_arrival_time[int(env.infra_array_poi_id[sim.step_dis])] = sim.daytime
    # Get current SOC
    current_soc = sim.bat_soc_dis[sim.step_dis]
    # Get target SOC
    target_soc = env.freight_start_soc
    # Get current time
    arrival_time = sim.daytime
    # Next full hour
    next_full_hour = np.ceil(arrival_time)
    # Get start time next day
    start_time = env.freight_mission_start
    # Calculate constant charging power
    charge_time = 24-next_full_hour+start_time
    # Constant charging power to achieve start SOC at next morning
    charging_power_const = (vehicle.battery_capacity * (target_soc-current_soc)) / charge_time  # in kW
    # Save power in track variable
    sim.betos_power[sim.step_dis] = charging_power_const
    # Save total time of overnight stay
    sim.betos_overnight_stay_time_dis[sim.step_dis] = charge_time + (next_full_hour - sim.daytime)  # in h
    # Save position of overnight stay
    sim.betos_overnight_stay_pos_dis[sim.step_dis] = sim.step_dis

    # <>
    # Resting up to next full hour
    r_time = 0
    step_size = 1  # sec
    while r_time < (next_full_hour - sim.daytime) * 3600:
        sim.time_time[sim.step_time] = step_size  # in sec
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update Battery Parameter
        # SoC while resting is not changing
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time]
        # Update time step for timebased variables
        sim.step_time = sim.step_time + 1
        # Update inner step
        r_time = r_time + step_size

    # <>
    # Perform charging
    step_size = 1  # in sec
    c_time = 0
    while c_time < charge_time*3600:
        # Battery SOC
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time] + \
                                          ((charging_power_const*step_size/3600)/vehicle.battery_capacity)
        # Other Parameters

        # Increment
        sim.time_time[sim.step_time] = step_size
        sim.step_time = sim.step_time + 1
        c_time = c_time + step_size

    # Save SOC in distance based variables
    sim.bat_soc_dis[sim.step_dis] = min(sim.bat_soc_time[sim.step_time], 1.0)
    # Update daytime after overnight stay
    sim.daytime = env.freight_mission_start

    # Save amount of recharged energy in kWh
    sim.betos_charge_amount[int(env.infra_array_poi_id[sim.step_dis])] = (target_soc-current_soc) * vehicle.battery_capacity

    return sim


# Heuristic Slow charging
def slow_charging_heuristic(sim, env, vehicle):
    # <>
    # Save arrival time at POI
    sim.betos_poi_arrival_time[int(env.infra_array_poi_id[sim.step_dis])] = sim.daytime
    # Get current SOC
    current_soc = sim.bat_soc_dis[sim.step_dis]
    # Get target SOC
    target_soc = env.freight_start_soc
    # Get current time
    arrival_time = sim.daytime
    # Next full hour
    next_full_hour = np.ceil(arrival_time)
    # Get start time next day
    start_time = env.freight_mission_start

    # Set heuristic params
    soc_hold = 0.2  # SOC Hold level
    charging_power_heuristic = (vehicle.battery_capacity / 4)  # Charging power in kW (C/4)
    # Calculate Time to Charge to Hold SOC with C/4
    charge_time_50_percent = (soc_hold - current_soc) * vehicle.battery_capacity / charging_power_heuristic  # in h
    # Calculate Time to charge from Hold SOC to target SOC
    charge_time_target_soc = (target_soc - max(current_soc, soc_hold)) * vehicle.battery_capacity / charging_power_heuristic  # in h

    # Calculate constant charging power
    charge_time = 24-next_full_hour+start_time
    # Constant charging power to achieve start SOC at next morning
    charging_power_const = (vehicle.battery_capacity * (target_soc-current_soc)) / charge_time  # in kW
    # Save power in track variable
    sim.betos_power[sim.step_dis] = charging_power_const
    # Save total time of overnight stay
    sim.betos_overnight_stay_time_dis[sim.step_dis] = charge_time + (next_full_hour - sim.daytime)  # in h
    # Save position of overnight stay
    sim.betos_overnight_stay_pos_dis[sim.step_dis] = sim.step_dis

    # <>
    # Resting up to next full hour
    r_time = 0
    step_size = 1  # sec
    while r_time < (next_full_hour - sim.daytime) * 3600:
        sim.time_time[sim.step_time] = step_size  # in sec
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update Battery Parameter
        # SoC while resting is not changing
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time]
        # Update time step for timebased variables
        sim.step_time = sim.step_time + 1
        # Update inner step
        r_time = r_time + step_size

    # <>
    # Perform charging
    step_size = 1  # in sec
    c_time = 0
    while c_time < charge_time_50_percent*3600:
        # Battery SOC
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time] + \
                                          ((charging_power_heuristic*step_size/3600)/vehicle.battery_capacity)
        # Other Parameters

        # Increment
        sim.time_time[sim.step_time] = step_size
        sim.step_time = sim.step_time + 1
        c_time = c_time + step_size

    # <>
    # Rest till next charging session before leaving
    rest_hold_soc = ((24 - next_full_hour) + start_time) - max(0, charge_time_50_percent) - charge_time_target_soc  # in h
    r_time = 0
    step_size = 1  # sec
    while r_time < rest_hold_soc * 3600:
        sim.time_time[sim.step_time] = step_size  # in sec
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update Battery Parameter
        # SoC while resting is not changing
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time]
        # Update time step for timebased variables
        sim.step_time = sim.step_time + 1
        # Update inner step
        r_time = r_time + step_size

    # <>
    # Charge to Target SOC
    step_size = 1  # in sec
    c_time = 0
    while c_time < charge_time_target_soc * 3600:
        # Battery SOC
        sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_time[sim.step_time] + \
                                            ((charging_power_heuristic * step_size / 3600) / vehicle.battery_capacity)
        # Other Parameters

        # Increment
        sim.time_time[sim.step_time] = step_size
        sim.step_time = sim.step_time + 1
        c_time = c_time + step_size


    # Save SOC in distance based variables
    sim.bat_soc_dis[sim.step_dis] = min(sim.bat_soc_time[sim.step_time], 1.0)
    # Update daytime after overnight stay
    sim.daytime = env.freight_mission_start

    # Save amount of recharged energy in kWh
    sim.betos_charge_amount[int(env.infra_array_poi_id[sim.step_dis])] = (target_soc-current_soc) * vehicle.battery_capacity

    return sim

