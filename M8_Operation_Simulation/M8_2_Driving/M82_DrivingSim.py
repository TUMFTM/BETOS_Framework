# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-02
#
# Function Description
# Part of the Operation Simulation Module M8
# Driving Simulation file of the operation simulation in M84
# Implementation of Driving Simulation
# _________________________________


# import functions:
import numpy as np
from Modules.M8_Operation_Simulation.M8_3_Action import M83_Action
from Modules.M9_Operation_Strategy.M9_6_Decision import M96_Decision
from Modules.M10_Evaluation import M10_Evaluation_Aging

# ______________________________________________________________________________________________________________________
# Driving Simulation distance-based Resolution: 1 m
def driving_sim(sim, vehicle, env):
    # while loop over env.route_array_distance:
    while sim.step_dis < sim.dis_steps - 1 and sim.step_dis < sim.pos_poi_max:

        # Planning using BET.OS (sim.action_dis)
        sim = M96_Decision.betos_decision(sim, env, vehicle)

        # Action = Driving
        if sim.betos_action[sim.step_dis] == 0:
            if sim.driving_version == 1:
                sim = M83_Action.action_fast_driving(sim, env, vehicle)
            else:
                sim = M83_Action.action_driving(sim, env, vehicle)

        # Action = Charging and/or Resting
        else:
            if sim.aging > 0:
                # Aging Evaluation before Charging of last driving sequence
                sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] = 0      # Driving event before charging
                sim, env, vehicle = M10_Evaluation_Aging.aging_evaluation(sim, env, vehicle)

            # Charge / Rest
            sim = M83_Action.action_charge_rest(sim, env, vehicle)

            if sim.aging > 0:
                # Aging Evaluation after Charging
                sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] = 1      # On Route Charging Event
                sim, env, vehicle = M10_Evaluation_Aging.aging_evaluation(sim, env, vehicle)

            # Action = Driving after Charging/Resting
            if sim.driving_version == 1:
                sim = M83_Action.action_fast_driving(sim, env, vehicle)
            else:
                sim = M83_Action.action_driving(sim, env, vehicle)

        # Update Position and Time step:
        sim.step_dis = sim.step_dis + 1
        sim.step_time = sim.step_time + 1

        # Check for low battery soc
        if sim.bat_soc_dis[sim.step_dis] <= 0:
            sim.betos_run_empty = 1
            break

        # Count deep discharge at destination
        if sim.bat_soc_dis[sim.step_dis] < vehicle.battery_soc_min:
            sim.betos_deep_discharge = sim.betos_deep_discharge + 1

    return sim


# ______________________________________________________________________________________________________________________
# Getting results in short form: Trip Length, Duration, Average Consumption, Capacity loss, Extrapolated TCO, etc
def processing_results(sim, vehicle, env, scenario):
    # Check for Multiday Simulation:
    multiday = False
    if sim.betos_version > 2 or sim.betos_version == 0:
        # Overnight Charging takes place:
        if sum(sim.betos_time_dis_prediction) / 3600 > 10:
            multiday = True
            # Position of Overnight Stays:
            pos_overnight = sim.betos_overnight_stay_pos_dis[sim.betos_overnight_stay_pos_dis > 0]
            # Driving times for each times:
            driving_times = np.zeros(len(pos_overnight) + 1)
            driving_times[0] = sum(sim.time_dis[0:int(pos_overnight[0])]) / 3600
            driving_times[-1] = sum(sim.time_dis[int(pos_overnight[-1]):]) / 3600
            for i in range(1, len(pos_overnight)):
                driving_times[i] = sum(sim.time_dis[int(pos_overnight[i-1]):int(pos_overnight[i])]) / 3600

            pos_overnight = np.concatenate((pos_overnight, np.array([sim.dis_steps])))

    # Precalculation of time loss:
    if sum(sim.betos_time_dis_prediction) / 3600 <= 4.5:
        time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 60)
    elif sum(sim.betos_time_dis_prediction) / 3600 <= 9:
        time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 60) - 45
    else:
        time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 60) - 90

    if time_loss < 0:
        a = 1

    # Diesel uses 2 stops, in case of three stops for BET add down time through leaving/passing highway (Data Set Paper: Zaehringer et al.)
    if sim.betos_stops > 2:
        time_loss = time_loss + ((sim.betos_stops - 2) * (vehicle.rest_space_time/60))  # in min

    # In case of multiday simulation
    if (sim.betos_version > 2 or sim.betos_version == 0) and multiday is True:
        results = {
            # scneario id
            'scenario_id': scenario['scenario_id'][0],
            # trip length
            'trip_length_km': sim.dis_steps/1000,
            # operation duration
            'operation_duration_h': sum(sim.time_time)/3600,
            # Arrival time
            'arrival_time_h': sim.daytime,
            # charging time
            'charging_time_h': sum(sim.charge_time_dis)/3600,
            # total downtime
            'down_time_h': ((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600,
            # pure driving time
            'driving_time_h': sum(sim.time_dis)/3600,
            # time loss to ICET
            'time_loss_min': time_loss,
            # Energy Consumption
            'energy_consumption_kWhkm': sum(sim.energy_cons_dis)/sim.step_dis/3600,
            # Predicted Energy Consumption
            'predicted_consumption_kWhkm': sum(sim.betos_energy_cons_dis_prediction)/sim.step_dis/3600,
            # Energy recharged
            'energy_recharged_kWh': sim.betos_charge_amount.tolist(),
            # Downtimes per POI
            'poi_down_time_h': sim.betos_down_time.tolist(),
            # Numper of stops
            'number_stops': sim.betos_stops,
            # SOC at Destination:
            'soc_destination': sim.bat_soc_dis[-1],
            # Number of overnight stays:
            'number_overnight_stay': len(sim.betos_overnight_stay_time_dis[sim.betos_overnight_stay_time_dis > 0]),
            # Position of overnight stays:
            'position_overnight_stay': pos_overnight,
            # Driving time per day:
            'driving_time_day_h': driving_times,
        }
    # Else One Day Simulation
    else:
        results = {
            # scneario id
            'scenario_id': scenario['scenario_id'][0],
            # trip length
            'trip_length_km': sim.dis_steps / 1000,
            # operation duration
            'operation_duration_h': sum(sim.time_time) / 3600,
            # Arrival time
            'arrival_time_h': sim.daytime,
            # charging time
            'charging_time_h': sum(sim.charge_time_dis) / 3600,
            # total downtime
            'down_time_h': ((sum(sim.rest_time_dis)) + (1 - sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600,
            # pure driving time
            'driving_time_h': sum(sim.time_dis) / 3600,
            # time loss to ICET
            'time_loss_min': time_loss,
            # Energy Consumption
            'energy_consumption_kWhkm': sum(sim.energy_cons_dis) / sim.step_dis / 3600,
            # Predicted Energy Consumption
            'predicted_consumption_kWhkm': sum(sim.betos_energy_cons_dis_prediction) / sim.step_dis / 3600,
            # Energy recharged
            'energy_recharged_kWh': sim.betos_charge_amount.tolist(),
            # Downtimes per POI
            'poi_down_time_h': sim.betos_down_time.tolist(),
            # Numper of stops
            'number_stops': sim.betos_stops,
            # SOC at Destination:
            'soc_destination': sim.bat_soc_dis[-1],
            # Average choosen charging power
            'power_chosen_avg_kw': np.mean(sim.betos_power[sim.betos_power > 0]),
            # Number of waiting events
            'number_wait_events': sim.betos_wait_count

        }

    return results

# ______________________________________________________________________________________________________________________

