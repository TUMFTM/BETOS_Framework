# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-10-04
# Last update: MX-2023-07-02
#
# Function Description
# Part of the Operation Strategy Module M9
# Dynamic Programming Operation Strategy wiht the handling of occupied charging stations
# _________________________________

# import libraries
import numpy as np
from scipy import interpolate
import math


# Dynamic Charging Strategy with the handling of occupied charging stations
def betos_dynamic_programming_ad(sim, env, vehicle):
    # Initialize convergence check
    no_convergence = True
    # Searching critical PoI due to mandatory break
    sim = finding_critical_poi(sim, env)
    # Composition Properties
    n_poi, poi_id_crit, poi_id_current = composition(sim, vehicle, env)
    # Setting up state space
    soc_state, rest_time_state, cost_matrix, best_decision_charge_time, best_decision_rest_time = state_space_definition(sim, vehicle, env, n_poi, poi_id_crit, poi_id_current)
    # Setting up decision space
    decision_1_charge, decision_2_rest = decision_space_definition(sim, vehicle, env)
    # Calculate Cost Matrix (Just due to decision taken)
    decision_cost_map = decision_cost(vehicle, decision_1_charge, decision_2_rest)
    # Calculate DP Data Matrix
    dp_data = dp_data_func(sim, env)

    # <><><>
    # Perform Backward DP
    # for PoI backward from destination to current poi
    for poi in range(n_poi - 2, -1, -1):
        # Index for soc state
        soc_int = 0
        # for states in soc:
        for soc in soc_state:
            # Index for states in remaining rest time
            rest_int = 0
            # for states in remaining rest time:
            for rest in rest_time_state:
                # Next state for taken decision
                next_state_soc, next_state_rest = next_state(sim, vehicle, env, decision_1_charge, decision_2_rest,
                                                             poi, soc, rest, dp_data, rest_int, poi_id_current)
                # lowest cumulative cost when taking best decision in current state
                cost_matrix, best_decision_charge_time, best_decision_rest_time = cost_next_state(sim, vehicle, env, next_state_soc, next_state_rest, soc_int, rest_int,
                                                                                                  decision_cost_map, cost_matrix, poi, best_decision_charge_time,
                                                                                                  best_decision_rest_time, soc_state, dp_data)
                # Update Index in rest state
                rest_int = rest_int + 1
                # Update Index in soc state
            soc_int = soc_int + 1
        # Manipulate Costs of State 1 and 2 in Rest Dimension at one POI after Critical PoI due to mandatory rest time
        if poi == poi_id_crit - poi_id_current + 1:
            cost_matrix[poi, :, 1:3] = 1000
        # Manipulate Cost Matrix, if Destination is POI after critical POI
        elif poi_id_crit == env.infra_number_poi - 2:
            cost_matrix[-1, :, 1:3] = 1000

    # <><><>
    # Perform Forward DP for current PoI
    # Set PoI: Current Poi is PoI 0 in situational framing
    current_poi = 0

    # identify current SoC State
    soc = sim.bat_soc_dis[sim.step_dis]

    # identify current Rest State
    rest_remain = vehicle.mandatory_rest_time - (sum(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis + 1]) / 60)  # in min
    if rest_remain <= 0 and (max(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis + 1]) / 60 >= 45 or
                             (max(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis + 1]) / 60 >= 30 and
                             max(sim.rest_time_dis[sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis] / 60 < 30]) / 60 >= 15)):
        # all rest done --> state = 0
        rest_remain = rest_time_state[0]
        rest_int = 0
    elif rest_remain < rest_time_state[2] and max(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis + 1]) / 60 >= 15:
        # less than 45 Minutes but greater than 15 min already --> 30 Minutes required
        rest_remain = rest_time_state[1]
        rest_int = 1
    else:
        rest_remain = rest_time_state[2]
        rest_int = 2  # All rest required

    # Get possible next state
    next_state_soc, next_state_rest = next_state(sim, vehicle, env, decision_1_charge, decision_2_rest, current_poi,
                                                 soc, rest_remain, dp_data, rest_int, poi_id_current)

    # Choose best decision
    charging_time_index, rest_time_index, target_soc = best_decision_fdp(sim, vehicle, env, soc_state,
                                                                         next_state_soc, next_state_rest,
                                                                         cost_matrix, decision_cost_map,
                                                                         current_poi, soc, current_poi, poi_id_current)

    # <><><>
    # BETOS Variables
    # Betos Charging Time
    sim.betos_charge_time[sim.step_dis] = decision_1_charge[int(charging_time_index)]

    # Set sim_betos_rest_target
    sim.betos_rest_time[sim.step_dis] = decision_2_rest[int(rest_time_index)] * 60  # in sec

    # Set sim_betos_soc_target
    sim.betos_soc_target[sim.step_dis] = target_soc / 100

    # Check for action
    if sim.betos_rest_time[sim.step_dis] > 0 or sim.betos_charge_time[sim.step_dis] > 0:
        # Set BETOS action
        sim.betos_action[sim.step_dis] = 1
        # Safe new stop
        sim.betos_stops = sim.betos_stops + 1
        # Availability of this Poi
        sim.betos_poi_availability[sim.step_dis] = env.cs_data_availability(sim.daytime)[int(env.infra_array_poi_type[sim.step_dis])]
        # Track average power
        sim.betos_power[sim.step_dis] = env.cs_power
    else:
        sim.betos_action[sim.step_dis] = 0
    
    return sim


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Help functions:
# Extract Data for DP Approach
# dp_data[i,0] which charging power is at PoI i available in kW
# dp_data[i,1] how far is it from PoI i-1 to PoI i in meter
# dp_data[i,2] how much energy do we need driving from PoI i-1 to PoI i in kWh
# dp_data[i,3] what is the daytime when reaching this PoI
# dp_data[i,4] what is the availability probability of this PoI at the arrival time
# dp_data[i,5] what is the predicted waiting time at this PoI
# i=0: current PoI
def dp_data_func(sim, env):
    # Number PoI Total
    poi_id_current = int(env.infra_array_poi_id[sim.step_dis])
    poi_id_destination = int(env.infra_array_poi_id[-1])
    number_poi = poi_id_destination - poi_id_current
    # Initialization of data: dp_data=[Charging Power, Distance to this PoI from last PoI,
    # Energy Consumption to this PoI]
    dp_data = np.zeros((number_poi+1, 6))
    # Fill in data
    for i in range(0, number_poi+1):
        # Power
        dp_data[i, 0] = env.cs_data_power[int(env.infra_array_poi_type[int(env.infra_array_poi_pos[poi_id_current + i])])]
        # Time
        dp_data[i, 3] = sim.daytime

        # Distance and Average energy consumption between this and next POI
        if i > 0:
            # Distance
            dp_data[i, 1] = env.infra_array_poi_pos[poi_id_current+i] - env.infra_array_poi_pos[poi_id_current+i-1]
            # energy consumption (5 % Saftey)
            dp_data[i, 2] = (sum(sim.betos_energy_cons_dis_prediction[int(env.infra_array_poi_pos[poi_id_current+i-1]):
                                                                     int(env.infra_array_poi_pos[poi_id_current+i])]) /\
                                                                     (1000*60*60))  # in kWh
            # Arrival time at PoI
            dp_data[i, 3] = dp_data[i-1, 3] + (sum(sim.betos_time_dis_prediction[int(env.infra_array_poi_pos[poi_id_current+i-1]):
                            int(env.infra_array_poi_pos[poi_id_current+i])])) / 3600  # in h

        # Availability of PoI
        dp_data[i, 4] = env.cs_data_availability(dp_data[i, 3])[int(env.infra_array_poi_type[int(env.infra_array_poi_pos[poi_id_current + i])])]

        # Waiting Time at PoI at arrival time
        dp_data[i, 5] = env.cs_data_waiting_time(dp_data[i, 3])

    return dp_data


# ______________________________________________________________________________________________________________________
# Finding critical PoI from current Position:
def finding_critical_poi(sim, env):
    # Get driving time: Total Time minus Rest Time
    time_driven = sum(sim.time_dis[sim.pos_rest_done+1:sim.step_dis])
    # Shorten Prediction Vector in time
    time_prediction = sim.betos_time_dis_prediction[sim.step_dis:]
    steps = len(time_prediction)
    # Cumulated Time Prediction
    time_cum_prediction = np.cumsum(time_prediction)
    # Remaining driving time till 4.5h
    time_remain = (4.5 * 3600)-time_driven   # in sec
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

    return sim


# ______________________________________________________________________________________________________________________
# Estimation of composition properties:
def composition(sim, vehicle, env):
    # ID of current PoI
    poi_id_current = int(env.infra_array_poi_id[sim.step_dis])
    # ID of critical PoI
    poi_id_crit = int(env.infra_array_poi_id[sim.pos_poi_crit])
    # ID of destination PoI
    poi_id_destination = int(env.infra_array_poi_id[-1])
    # n PoI for Consideration
    n_poi = poi_id_destination-poi_id_current + 1

    return n_poi, poi_id_crit, poi_id_current


# ______________________________________________________________________________________________________________________
# State Space Definition:
# States are SOC Niveau and remaining rest time when leaving PoI
def state_space_definition(sim, vehicle, env, n_poi, poi_id_crit, poi_id_current):
    # Target SoC Discretization in 101 steps between 0.0 and 1.0: [0.0, 0.01, 0.02, 0.03, ..., 1.0]
    soc_state = np.linspace(0.0, 1.0, num=101)

    # Remaining rest time discretization: States are 0 min, 30 min, 45 min
    rest_time_state = np.array([0, 30, 45])

    # Initialization Cost Matrix for Problem
    cost_matrix = np.zeros((n_poi, len(soc_state), len(rest_time_state)))

    # Initialization Best Decision matrix for problem
    best_decision_charge_time = np.zeros((n_poi, len(soc_state), len(rest_time_state)))
    best_decision_rest_time = np.zeros((n_poi, len(soc_state), len(rest_time_state)))

    # Fill in not allowed states in SoC below min SoC at every PoI for Subproblem 2
    min_soc = int(vehicle.battery_soc_min * 100)
    buffer = int(vehicle.battery_soc_buffer * 100)
    cost_matrix[:, 0:min_soc + 1 - buffer, :] = 1000
    cost_matrix[:, min_soc - buffer + 1:min_soc + 1, :] = 1000

    # SOC at Destination
    cost_matrix[-1, 0:int(env.freight_destination_soc * 100) + 1, :] = 0.1   #(one stop to charge one minute is 0.1667 h)
    cost_matrix[-1, 0:int(env.freight_destination_soc * 100) + 1 - buffer, :] = 1000

    # Rest states at critical POI
    if (poi_id_crit - poi_id_current + 1) <= (n_poi - 1):
        cost_matrix[poi_id_crit - poi_id_current + 1, :, 1:3] = 1000

    return soc_state, rest_time_state, cost_matrix, best_decision_charge_time, best_decision_rest_time


# ______________________________________________________________________________________________________________________
# Decision Space Definition:
# Decisions are charging time and executed rest time at PoI
def decision_space_definition(sim, vehicle, env):
    # Decision 1: Charging time
    # Maximum Charging time in case of 0 to 100 % at slowest charger
    slowest_charger = int(np.argmax(vehicle.charging_time_map[0, :]))
    max_charging_time = sum(vehicle.charging_time_map[:, slowest_charger])
    decision_1_charge = np.ceil(np.linspace(0, 100*60, num=101))  # Use 100 decisions in sec
    # Decision 2: Rest time: 0, 15, 30, 45 min
    decision_2_rest = np.array([0, 15, 30, 45])

    return decision_1_charge, decision_2_rest


# ______________________________________________________________________________________________________________________
# Decision Cost definition
def decision_cost(vehicle, decision_1_charge, decision_2_rest):
    # Initialization of cost matrix
    decision_cost_map = np.zeros((len(decision_1_charge), len(decision_2_rest)))
    # Index
    i = 0
    # For loop over different rest decisions
    for x in decision_2_rest:
        decision_2 = (np.ones(len(decision_1_charge)) * x * 60) + vehicle.rest_space_time  # in sec (Pure rest time plus searching for parking space)
        decision_cost_map[:, i] = np.maximum(decision_1_charge + vehicle.connecting_time + vehicle.rest_space_time, decision_2)  # in sec
        if i == 0:
            # No Connecting time needed due to no charging and no resting
            #decision_cost_map[0, i] = np.maximum(decision_1_charge[0], decision_2[0])  # in sec
            decision_cost_map[0, 0] = 0  # in sec
        # Update Index
        i = i + 1

    return decision_cost_map


# ______________________________________________________________________________________________________________________
# Next State calculation in soc and remaining rest time
def next_state(sim, vehicle, env, decision_1_charge, decision_2_rest,
               poi, soc, rest, dp_data, rest_int, poi_id_current):
    # Vectorized in decision 1, iteration over decision 2
    # Initialization of next state of soc by decision 1 and 2 from current state
    next_state_rest = np.zeros((len(decision_2_rest), 2))

    # Get right Position for Infrastructure Type
    if poi == 0:  # In Case of forward DP
        pos_type = sim.step_dis
    else:  # In Case of Backward DP
        pos_type = int(env.infra_array_poi_pos[poi+poi_id_current])

    # Next State in SoC (is not depending on occupancy)
    next_state_soc_floor = ((vehicle.charging_map[int(env.infra_array_poi_type[pos_type]), int(np.floor(soc * 100)), :] / 100)) - (dp_data[poi + 1, 2] / vehicle.battery_capacity)
    next_state_soc_ceil = ((vehicle.charging_map[int(env.infra_array_poi_type[pos_type]), int(np.ceil(soc * 100)), :] / 100)) - (dp_data[poi + 1, 2] / vehicle.battery_capacity)
    weights_floor = np.ceil(soc * 100) - (soc * 100)
    next_state_soc = (next_state_soc_floor * weights_floor) + ((1 - weights_floor) * next_state_soc_ceil)

    # Limit next state in Soc between 0 and 1
    next_state_soc = np.maximum(0, next_state_soc)
    next_state_soc = np.minimum(1, next_state_soc)
    # Next state in remaining rest
    # Depend on whether re-parking is allowed during rest time (1) or not (0) (waiting time counts or not)
    # Index for decision in dimension 2
    i = 0
    for decision_2 in decision_2_rest:
        # Next Rest State for available charging stations
        if rest - decision_2 <= 0:  # State 0 (0 minutes remaining)
            next_state_rest[i, 0] = 0
        elif decision_2 > 0:  # State 1 (30 minutes remaining)
            next_state_rest[i, 0] = 1
        elif decision_2 == 0:  # State is not changing
            next_state_rest[i] = rest_int
        else:  # State 2 (45 minutes remaining)
            next_state_rest[i, 0] = 2
        # Next Rest State for occupied charging station (consideration of waiting time)
        if rest - (decision_2+(sim.betos_re_park*dp_data[poi, 5]/60)) <= 0:  # State 0 (0 minutes remaining)
            next_state_rest[i, 1] = 0
        elif decision_2 > 0:  # State 1 (30 minutes remaining)
            next_state_rest[i, 1] = 1
        elif decision_2 == 0:  # State is not changing
            next_state_rest[i, 1] = rest_int
        else:  # State 2 (45 minutes remaining)
            next_state_rest[i, 1] = 2

        # Update Index
        i = i + 1

    return next_state_soc, next_state_rest


# ______________________________________________________________________________________________________________________
# Calculation of Cost of taken decisions
def cost_next_state(sim, vehicle, env, next_state_soc, next_state_rest, soc_int, rest_int, decision_cost_map, cost_matrix,
                    poi, best_decision_charge_time, best_decision_rest_time, soc_state, dp_data):
    # Iteration over decision of rest time, Vectorized Calculation in charging time decision
    # Initialization of cumulative Cost Matrix
    cumulative_cost = np.zeros((len(next_state_soc), len(next_state_rest)))

    # Iteration over rest time decision.
    for decision_2 in range(0, len(next_state_rest)):
        # Get Cost of landing state by taken decision

        # :::For available Charging station:::
        # Which state in dimension 2 (Remaining Rest Time)
        state_2_remaining_rest_free = next_state_rest[decision_2, 0]
        # Relevant line of state cost map
        cost_map_extract_free = cost_matrix[poi+1, :, int(state_2_remaining_rest_free)]
        # Interpolate costs of landing state (cost map extract) by taken decision in soc
        cost_of_soc_decision_func = interpolate.interp1d(soc_state, cost_map_extract_free, kind='linear')
        cost_of_soc_decision_free = cost_of_soc_decision_func(next_state_soc)

        # :::For occupied charging station:::
        # Which state in dimension 2 (Remaining Rest Time)
        state_2_remaining_rest_occ = next_state_rest[decision_2, 1]
        # Relevant line of state cost map
        cost_map_extract_occ = cost_matrix[poi + 1, :, int(state_2_remaining_rest_occ)]
        # Interpolate costs of landing state (cost map extract) by taken decision in soc
        cost_of_soc_decision_func = interpolate.interp1d(soc_state, cost_map_extract_occ, kind='linear')
        cost_of_soc_decision_occ = cost_of_soc_decision_func(next_state_soc)

        # Expected Cost of decision: Expected cost due to probability of PoI Availability
        poi_availability = dp_data[poi, 4]
        poi_wait_time = dp_data[poi, 5]  # in sec
        wait_time_vec = np.zeros(len(next_state_soc))
        wait_time_vec[1:] = poi_wait_time
        dec_cost_expected = (poi_availability*decision_cost_map[:, decision_2]) + \
                            ((1-poi_availability)*((decision_cost_map[:, decision_2]) + wait_time_vec))
        # Expected Cost of landing state
        lan_cost_expected = (poi_availability*cost_of_soc_decision_free) + (1-poi_availability)*cost_of_soc_decision_occ

        # :::Calculate cumulative cost:::
        # Expected Cost of decision = p_free*Cost_of_decision + (1-p_free)*(cost_of_decision+wait)
        # Expected cost of landing soc state = p_free*Cost of landing state,free + (1-p_free)*cost of landing state, occ
        cumulative_cost[:, decision_2] = dec_cost_expected/3600 + lan_cost_expected    # in h

    # Searching for best decision in current State: minimum in cumulative cost
    cost_matrix[poi, soc_int, rest_int] = np.amin(cumulative_cost) + cost_matrix[poi, soc_int, rest_int]
    index = np.unravel_index(cumulative_cost.argmin(), cumulative_cost.shape)
    # Safe best decision
    best_decision_charge_time[poi, soc_int, rest_int] = index[0]
    best_decision_rest_time[poi, soc_int, rest_int] = index[1]

    return cost_matrix, best_decision_charge_time, best_decision_rest_time


# ______________________________________________________________________________________________________________________
# Searching for optimal next state according to cost in forward DP
def best_decision_fdp(sim, vehicle, env, soc_state, next_state_soc, next_state_rest, cost_matrix, decision_cost_map,
                      current_poi, soc, poi, poi_id_current):
    # Get availability of current poi
    poi_available = env.cs_availability  # 0: free, 1:occupied
    # Get waiting time of current poi
    poi_wait_time = env.cs_data_waiting_time(sim.daytime)   # in sec

    # Add costs in case of early full rest decision if driving time to destination from this POI is greater than
    # allowable driving time
    add_decision_cost = np.zeros_like(decision_cost_map)
    if sim.betos_driving_time_destination[int(poi + poi_id_current), 1] > 4.5:
        # Add 45 min due to another necessary rest of 45 min in case of such decision
        add_decision_cost[decision_cost_map >= 45 * 60] = 45 * 60  # in seconds

    # Perform standard Forward DP in case of free charging station
    if poi_available == 0:
        # Initialization of cumulative Cost Matrix
        cumulative_cost = np.zeros((len(next_state_soc), len(next_state_rest)))
        for decision_2 in range(0, len(next_state_rest)):
            # Get Cost of next state by taken decision
            # Which state in dimension 2 (Remaining Rest Time)
            state_2_remaining_rest = next_state_rest[decision_2, 0]
            # Relevant line of state cost map for next state
            cost_map_extract = cost_matrix[current_poi+1, :, int(state_2_remaining_rest)]
            # Interpolate costs of landing state (cost map extract) by taken decision in soc
            cost_of_soc_decision_func = interpolate.interp1d(soc_state, cost_map_extract, kind='linear')
            cost_of_soc_decision = cost_of_soc_decision_func(next_state_soc)

            # Cost of decision
            cumulative_cost[:, decision_2] = ((decision_cost_map[:, decision_2] + add_decision_cost[:, decision_2]) / 3600) + cost_of_soc_decision    # in h

        # Search best Option
        index = np.unravel_index(cumulative_cost.argmin(), cumulative_cost.shape)
        # Decision Charging Time
        charging_time_index = index[0]
        # Decision Rest Time
        rest_time_index = index[1]

    # If poi is occupied
    else:
        # What are the expected costs in case of waiting and charging
        # Initialization of cumulative Cost Matrix
        cumulative_cost = np.zeros((len(next_state_soc), len(next_state_rest)))

        # Iteration over rest time decision.
        for decision_2 in range(0, len(next_state_rest)):
            # Get Cost of landing state by taken decision
            # :::For occupied charging station:::
            # Which state in dimension 2 (Remaining Rest Time)
            state_2_remaining_rest_occ = next_state_rest[decision_2, 1]
            # Relevant line of state cost map
            cost_map_extract_occ = cost_matrix[poi + 1, :, int(state_2_remaining_rest_occ)]
            # Interpolate costs of landing state (cost map extract) by taken decision in soc
            cost_of_soc_decision_func = interpolate.interp1d(soc_state, cost_map_extract_occ, kind='linear')
            cost_of_soc_decision_occ = cost_of_soc_decision_func(next_state_soc)

            # Expected Cost of decision: Expected cost due to probability of PoI Availability
            dec_cost_expected = decision_cost_map[:, decision_2] + add_decision_cost[:, decision_2] + poi_wait_time
            # Expected Cost of landing state
            lan_cost_expected = cost_of_soc_decision_occ
            # :::Calculate cumulative cost:::
            cumulative_cost[:, decision_2] = dec_cost_expected / 3600 + lan_cost_expected  # in h
        # Search best Option
        min_cost_occ = np.amin(cumulative_cost)
        index = np.unravel_index(cumulative_cost.argmin(), cumulative_cost.shape)
        # Decision Charging Time
        charging_time_index = index[0]
        # Decision Rest Time
        rest_time_index = index[1]

        # What are the expected costs in case of passing
        soc_passing = int(next_state_soc[0] * 100)
        rest_passing = int(next_state_rest[0, 0])
        cost_passing = cost_matrix[current_poi+1, soc_passing, rest_passing]

        # Compare Waiting to Passing
        if min_cost_occ < cost_passing:
            # Decision Charging Time
            charging_time_index = index[0]
            # Decision Rest Time
            rest_time_index = index[1]
        else:
            charging_time_index = 0
            rest_time_index = 0

    # Get Target SoC
    target_soc = vehicle.charging_map[int(env.infra_array_poi_type[int(env.infra_array_poi_pos[poi+poi_id_current])]),
                                      int(soc*100), int(charging_time_index)]

    return charging_time_index, rest_time_index, target_soc

