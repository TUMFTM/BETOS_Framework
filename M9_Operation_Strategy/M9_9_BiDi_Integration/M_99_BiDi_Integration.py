# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-12-17
#
# Function Description
# Part of the Operation Strategy for Bidirectionally Integrated Trucks
# Implementation of revenue optimization in case of bidi grid integration
# BiDi Charging
# _________________________________


# import functions:
import matplotlib.pyplot as plt
# import libraries:
import math
import numpy as np
from scipy import interpolate
import pandas


# Main Function for V2G Charging and Trading:
# ______________________________________________________________________________________________________________________
def bidi_revenue_optim():
    # Read Market Data
    market_data = read_market_data()
    # First day of data
    day_start = 2           # data start on 1.1.2019, Tuesday

    # Properties
    battery_size = 500    # Battery Capacity in kWh
    charging_power = 250  # Constant Charging Power in kW
    efficiency_charge = 0.9  # Charging Efficiency
    power_levy = 0  # ct/kWh Umlage
    net_fee = 0 # ct/kWh Netzentgeld

    # Initialize single Trading Events
    trading_events = np.zeros((900, 3))

    # Read Boundary Conditions
    soc_max, soc_min, soc_day_start, soc_day_end, startdays, enddays, start_time, arrive_time, day_length, slot_time, \
    max_efc = boundary_conditions()

    # Initial Charging Event up to 90% SoC
    revenue, battery_soc, battery_efc = initial_charge(battery_size, charging_power, soc_max, market_data)
    # Loop over Days, Weeks, Years
    end = 1
    run = 50
    count_events = 0
    while end > 0:
        if market_data[run, 3] == 2 and market_data[run, 4] == 17.0: # Arrive on Tuesday
            # Extract Data
            data_slot = extract_data_slots(market_data, 2, run)
            # Trade
            trade = 0
        elif market_data[run, 3] == 3 and market_data[run, 4] == 17.0: # Arrive on Wednesday
            # Extract Data
            data_slot = extract_data_slots(market_data, 3, run)
            # Trade
            trade = 0
        elif market_data[run, 3] == 5 and market_data[run, 4] == 17.0: # Arrive on Friday
            # Extract Data
            data_slot = extract_data_slots(market_data, 5, run)
            # Trade
            trade = 1
        else:
            trade = 0

        # Trade and Depot Charge if possible
        if trade == 1:
            # Call trading function
            revenue, battery_efc, trading_events = charge_trade(data_slot, charging_power, battery_size, soc_day_start,
                                                                soc_day_end, battery_efc, revenue, slot_time,
                                                                trading_events, count_events, efficiency_charge,
                                                                power_levy, max_efc)
            # Call depot charging function
            #revenue, battery_efc = optim_charge(data_slot, charging_power, battery_size, soc_day_start, soc_day_end,
                                                #battery_efc, revenue, slot_time, efficiency_charge, power_levy)
            # Update Events Count
            count_events = count_events + 1

        run = run + 1
        # Check for end
        if run == len(market_data):
            end = 0

    # Slice Trading Events
    trading_events = trading_events[0:count_events, :]
    # Store Trading Events
    np.savetxt('Modules/M13_SimulationTask/M13_Results/V2X/2019_1efc_500kwh_250kw_weekend.csv', trading_events, delimiter=",")

    return revenue, battery_efc, trading_events


# <><><> Help Functions
# ______________________________________________________________________________________________________________________
# Boundary Conditions of Vehicle usage
def boundary_conditions():
    soc_max = 0.9          # Maximum SoC of Battery
    soc_min = 0.1          # Minimum SoC of Battery
    soc_day_start = 0.9    # Soc at Start 90%
    soc_day_end = 0.3      # Soc at end of the day 30%
    startdays = [1, 3, 4]  # Departure on Monday, Wednesday and Thursday
    enddays = [2, 3, 5]    # Arrival on Tuesday, Wednesday and Friday
    start_time = 7.0       # Departure at 7  in morning
    arrive_time = 17.0     # Arrival at 17 in the evening
    day_length = 24.0      # Day has 24 hours
    slot_time = 0.25
    max_efc = 1            # 100 EFC for Trading per year

    return soc_max, soc_min, soc_day_start, soc_day_end, startdays, enddays, start_time, arrive_time, day_length, slot_time, max_efc


# ______________________________________________________________________________________________________________________
# Read Market Data
def read_market_data():
    raw_data = pandas.read_csv('prices.csv', header=1)
    data = raw_data.to_numpy()
    data = np.nan_to_num(data)
    # Extract one Year 2019[0:35039] 2020[35136:70175] 2021[70272:105215] 2022[105312:len(data)+1]
    data_daiaic = data[105312:len(data)+1, 1:4] / 10  # ct/kWh
    # Extend market data for weekday
    n_slots = len(data_daiaic)
    # Init
    data_extend = np.zeros((n_slots, 5))
    # Fill in known
    data_extend[:, 0:3] = data_daiaic
    i = 0  # run
    day = 2  # Data Start on daytype 2 (tue)
    time_vector = np.linspace(0.25, 23.75, 95)  # one day in 15 min slots
    count_slot = 95
    add = 0  # help variable
    while i < n_slots:
        # Colum 3: Weekday 1,...,7, Colum 4: Daytime: 0.0, 0.25, ..., 23.75
        data_extend[i:i+count_slot, 3] = day
        data_extend[i+add:i+count_slot, 4] = time_vector
        day = day+1
        count_slot = 96
        add = 1
        if day == 8:
            day = 1
        if i == 0:
            i = i + 95
        else:
            i = i + 96

    market_data = data_extend

    return market_data


# ______________________________________________________________________________________________________________________
# Initial Charging Event
def initial_charge(battery_size, charging_power, soc_max, market_data):
    # Charging duration in h
    duration_charge = (battery_size * soc_max) / charging_power
    # Number of 0.25 h Slots
    slots_charge = duration_charge / 0.25
    # Integer
    int_slots = math.floor(slots_charge)
    # Charge for int_slots 0.25h slots
    battery_energy_price = np.sum((market_data[0:int_slots, 0]*charging_power*0.25))  # in Eur
    # Charge remaining energy
    revenue = (battery_energy_price + (market_data[int_slots, 0]*charging_power*(slots_charge-int_slots)*0.25)) / 100  # in Eur
    # Battery SoC after initial charging event
    battery_soc = soc_max
    # Battery EFC
    battery_efc = soc_max/2

    return revenue, battery_soc, battery_efc


# ______________________________________________________________________________________________________________________
# Extract data for trading and charging horizon
def extract_data_slots(market_data, day, run):
    # Check for Day
    if day == 2 or day == 3:
        number_slots = 56  # From 17 to 7 on next day
    else:
        number_slots = 56 + 192  # From 17 Friday to 7 Monday
    # Extract Slots
    data_slot = market_data[run:run+number_slots, :]

    return data_slot


# ______________________________________________________________________________________________________________________
# <><><> Trading Module
# Charge Vehicle to Boundary Conditions and trade in remaining slots
def charge_trade(data_slot, charging_power, battery_size, soc_day_start, soc_day_end, battery_efc, revenue,
                 slot_time, trading_events, count_events, efficiency_charge, power_levy, max_efc):
    # Extend data slot: High Sampling in 1 minute slots

    # Use Dynamic Programming for Trading
    soc_state, efc_state, cost_matrix, best_decision, decision_state, efc_decision, res_soc, res_efc = \
        space_definition(data_slot, max_efc)
    cost_matrix, best_decision, efc_decision = backward_dp(data_slot, soc_state, cost_matrix, best_decision,
                                                           decision_state, battery_size, charging_power, slot_time,
                                                           efc_decision, efficiency_charge, power_levy, efc_state,
                                                           max_efc, res_soc, res_efc)

    # Monitor taken decisions in forwards DP
    decision_taken, soc_trail, rev, efc, market_values = forward_dp(data_slot, cost_matrix, best_decision, soc_day_end,
                                                                    res_soc, res_efc, charging_power, battery_size,
                                                                    slot_time, decision_state, soc_state, efc_state,
                                                                    power_levy)
    # Add Revenue and EFC of this trading session
    revenue = revenue + rev
    battery_efc = battery_efc + efc
    # Save single result of trading session
    trading_events[count_events, 0] = rev
    trading_events[count_events, 1] = efc
    trading_events[count_events, 2] = np.nan_to_num(np.max(data_slot[:, 0:3]))-np.nan_to_num(np.min(data_slot[:, 0:3]))

    # Visualize Trading Event
    visualize_trading(data_slot, soc_trail, decision_taken, market_values)

    return revenue, battery_efc, trading_events


# _HELP_Functions_______________________________________________________________________________________________________
# Space definition DP
def space_definition(data_slot, max_efc):
    # Number of slots for Trading and Charging
    n_slots = len(data_slot)
    # SoC State
    res_soc = 20
    soc_state = np.linspace(0, 1, res_soc+1)
    # EFC State
    res_efc = 20
    efc_state = np.linspace(0, max_efc, int(max_efc*res_efc)+1)
    # Cost Matrix
    cost_matrix = np.zeros((n_slots, len(soc_state), len(efc_state)))
    # Best Decision
    best_decision = np.zeros((n_slots, len(soc_state), len(efc_state)))
    efc_decision = np.zeros((n_slots, len(soc_state), len(efc_state)))
    # Not allowed states
    cost_matrix[:, 0:2, :] = 1000  # SoC of 0 is not allowed
    cost_matrix[:, 19:res_soc+1, :] = 1000  # SoC of 1 is not allowed
    cost_matrix[-1, :, :] = 1000  # SoC at End of Slot must >= 0.9
    cost_matrix[-1, 18:res_soc+1, :] = 0
    cost_matrix[:, :, -1] = 1000  # Max EFC must be respected

    # Decision State Definition
    decision_state = np.array([-1, 0, 1])

    return soc_state, efc_state, cost_matrix, best_decision, decision_state, efc_decision, res_soc, res_efc


# Next State Calculation
def next_state_trade(soc, efc, decision_state, battery_size, charging_power, slot_time, max_efc):
    # Next SoC state when charging / discharging for one slot
    next_soc_state = soc + (decision_state*(charging_power*slot_time/battery_size))
    # Limit SoC
    next_soc_state = np.maximum(0, next_soc_state)
    next_soc_state = np.minimum(1, next_soc_state)
    # Next State EFC
    next_efc_state = efc + ((np.abs(decision_state)*charging_power*slot_time/battery_size)/2)
    next_efc_state = np.minimum(max_efc, next_efc_state)

    return next_soc_state, next_efc_state


# Cost of next states and best decision
def best_decision_cost(data_slot, cost_matrix, next_soc_state, decision_state, best_decision, efc_decision, slot_time,
                       charging_power, soc_state, soc, run, battery_size, efficiency_charge, power_levy, next_efc_state,
                       efc, efc_state, res_soc, res_efc):
    # Initialize Cumulative Cost
    cumulative_cost = np.zeros(len(next_soc_state))
    for index in range(0, len(next_efc_state)):
        # relevant cost of cost matrix
        cost_extract = cost_matrix[run+1, :, :]
        # Interpolate landing state by decision
        cost_next_state_func = interpolate.interp2d(soc_state, efc_state, np.transpose(cost_extract), kind='linear')
        cost_next_state = cost_next_state_func(next_soc_state[index], next_efc_state[index])
        # cost of decision discharge/do nothing/charge:
        cost_decision = (((min(data_slot[run, 0:3]) + power_levy) * charging_power * slot_time) / efficiency_charge) * decision_state[index] / 100  # in Eur # Charge
        #cost_decision = ((((data_slot[run, 0]) + power_levy) * charging_power * slot_time) / efficiency_charge) * decision_state[index] / 100  # not using all 3 markets
        if index == 0:  # Discharge
            cost_decision = (max(data_slot[run, 0:3]) * charging_power * slot_time * efficiency_charge) * decision_state[index] / 100  # in Eur  # Discharge
            #cost_decision = ((((data_slot[run, 0]) + power_levy) * charging_power * slot_time) * efficiency_charge) * decision_state[index] / 100  # Not using all 3 markets
        # Cumulative Cost of decision and next state:
        cumulative_cost[index] = cost_next_state + cost_decision
    # Best decision in current state
    cost_matrix[run, int(soc * res_soc), int(efc * res_efc)] = min(cumulative_cost) + cost_matrix[run, int(soc*res_soc), int(efc*res_efc)]
    # Save best decision
    pos = np.argmin(cumulative_cost)
    best_decision[run, int(soc*res_soc), int(efc*res_efc)] = decision_state[pos]
    # Save efc for this best decision: efc in run+1 plus efc through this decision
    efc_next_func = interpolate.interp2d(soc_state, efc_state, np.transpose(efc_decision[run+1, :, :]), kind='linear')
    efc_next = efc_next_func(next_soc_state[pos], next_efc_state[pos])
    efc_decision[run, int(soc*res_soc), int(efc*res_efc)] = efc_next + (np.abs(decision_state[pos])*(charging_power*slot_time/battery_size)/2)

    return cost_matrix, best_decision, efc_decision


# Backward DP for Trading
def backward_dp(data_slot, soc_state, cost_matrix, best_decision, decision_state, battery_size, charging_power,
                slot_time, efc_decision, efficiency_charge, power_levy, efc_state, max_efc, res_soc, res_efc):
    # Number of Slots
    n_slots = len(data_slot)
    # From Last Slot Backward
    for run in range(n_slots-2, -1, -1):
        # For soc in soc_state:
        for soc in soc_state:
        # for efc in efc_state:
            for efc in efc_state:
                # Next SoC State when taking decisions
                next_soc_state, next_efc_state = next_state_trade(soc, efc, decision_state, battery_size,
                                                                  charging_power, slot_time, max_efc)
                # Calculate Cost of this next states and choose best possible action
                cost_matrix, best_decision, efc_decision = best_decision_cost(data_slot, cost_matrix, next_soc_state,
                                                                              decision_state, best_decision, efc_decision,
                                                                              slot_time, charging_power, soc_state, soc,
                                                                              run, battery_size, efficiency_charge,
                                                                              power_levy, next_efc_state, efc,
                                                                              efc_state, res_soc, res_efc)

    return cost_matrix, best_decision, efc_decision


# Get Best Decision along trading Event in each time slot
def forward_dp(data_slot, cost_matrix, best_decision, soc_day_end, res_soc, res_efc, charging_power, battery_size,
               slot_time, decision_state, soc_state, efc_state, power_levy):
    # Get number of slots
    n_slot = len(data_slot)
    # Initialize decision taken
    decision_taken = np.zeros(n_slot)
    # Initialize SOC Trail
    soc_trail = np.zeros(n_slot)
    efc_trail = np.zeros(n_slot)
    # Initialize Market Values
    market_values = np.zeros(n_slot)
    # Set two state variables:
    new_soc = soc_day_end
    new_efc = 0
    rev = 0
    # Iteration over Slots
    for count in range(0, n_slot-1):
        # Save SOC Trail
        soc_trail[count] = new_soc
        efc_trail[count] = new_efc
        # Init cost new state and cum cost
        cost_new_state = np.zeros(len(decision_state))
        cum_cost = np.zeros(len(decision_state))
        # Get decision
        for decision in range(0, len(decision_state)):
            # New SoC State
            new_soc = soc_trail[count] + (decision_state[decision] * (charging_power * slot_time / battery_size))
            # New EFC State
            new_efc = efc_trail[count] + ((np.abs(decision_state[decision])*charging_power*slot_time/battery_size)/2)
            # Cost of this new state
            cost_extract = cost_matrix[count + 1, :, :]
            func = interpolate.interp2d(soc_state, efc_state, np.transpose(cost_extract), kind='linear')
            cost_new_state[decision] = func(new_soc, new_efc)
            if decision_state[decision] >= 0:
                cum_cost[decision] = cost_new_state[decision] + (decision_state[decision]*charging_power*slot_time * min(data_slot[count, 0:3] + power_levy))/100
            else:
                cum_cost[decision] = cost_new_state[decision] + (
                            decision_state[decision] * charging_power * slot_time * max(data_slot[count, 0:3])) / 100

        # Best Decision:
        decision_taken[count] = decision_state[np.argmin(cum_cost)]
        # Execute decision --> New State
        new_soc = soc_trail[count] + (decision_taken[count] * (charging_power * slot_time / battery_size))
        new_efc = efc_trail[count] + ((np.abs(decision_taken[count])*charging_power*slot_time/battery_size)/2)
        if decision_taken[count] >= 0:
            rev = rev + (decision_taken[count]*charging_power*slot_time * min(data_slot[count, 0:3]))/100
            market_values[count] = min(data_slot[count, 0:3])
        else:
            rev = rev + (decision_taken[count] * charging_power * slot_time * max(data_slot[count, 0:3]))/100
            market_values[count] = max(data_slot[count, 0:3])

    return decision_taken, soc_trail, rev, new_efc, market_values


# Visualize one trading event slot
def visualize_trading(data_slot, soc_trail, decision_taken, market_values):
    # Figure Setup for Trading Strategy
    plt.rc('font', family='Times New Roman')
    csfont = {'fontname': 'Times New Roman'}
    fig = plt.figure(figsize=(10, 6))
    n = len(data_slot)
    x_axes = np.linspace(0, n-1, n)
    # Plot Market
    plt.plot(x_axes, data_slot[:, 2], color='#331E36', linewidth=2, label='Intraday Continuous')
    plt.plot(x_axes, data_slot[:, 1], color='#41337A', linewidth=2, label='Intraday Auction')
    plt.plot(x_axes, data_slot[:, 0], color='#6EA4BF', linewidth=2, label='Day Ahead')
    charge_y = market_values[decision_taken == 1]
    charge_x = x_axes[decision_taken == 1]
    discharge_y = market_values[decision_taken == -1]
    discharge_x = x_axes[decision_taken == -1]
    plt.scatter(charge_x, charge_y, marker='*', s=80, color='#9EC1A3', label='charge slot')
    plt.scatter(discharge_x, discharge_y, marker='o', s=80, color='#DB2960', label='discharge slot')
    #for x in range(0, n):
    #    if decision_taken[x] == 1:
    #        plt.plot(x_axes[x], market_values[x], marker='+', 'g')
    #    elif decision_taken[x] == -1:
    #        plt.plot(x_axes[x], market_values[x], 'ro')

    plt.xlabel('Slots of 15 minutes starting at 5 pm friday', **csfont, fontsize=18)
    plt.xlim((0, n-1))
    plt.xticks(**csfont, fontsize=16)
    plt.ylabel('market data in ct/kWh', **csfont, fontsize=18)
    plt.yticks(**csfont, fontsize=16)
    plt.ylim((-10, 60))
    plt.title('Trading strategy along V2G trading event (2022)', **csfont, fontsize=20, y=1.05)
    plt.legend()
    plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/Trading_Performance_Example.png', dpi=400)
    plt.show()

    # Figure Setup for SOC Trail

    return


# _END_Help _Functions__________________________________________________________________________________________________
# <><><>
# ______________________________________________________________________________________________________________________
# <><><>
# Grid Optimized Charging, no trading: Using DP Approach, just limit decision to do nothing or charge
def optim_charge(data_slot, charging_power, battery_size, soc_day_start, soc_day_end, battery_efc, revenue,
                 slot_time, efficiency_charge, power_levy):
    # Extend data slot: High Sampling in 1 minute slots

    # Use Dynamic Programming for Trading
    soc_state, cost_matrix, best_decision, decision_state, efc_decision = space_definition_oc(data_slot)
    cost_matrix, best_decision, efc_decision = backward_dp_charge(data_slot, soc_state, cost_matrix, best_decision,
                                                                  decision_state,
                                                                  battery_size, charging_power, slot_time, efc_decision,
                                                                  efficiency_charge, power_levy)

    revenue = revenue + cost_matrix[0, int(soc_day_end * 20)]
    battery_efc = battery_efc + efc_decision[0, int(soc_day_end * 20)]/2

    return revenue, battery_efc


# Space Definition
def space_definition_oc(data_slot):
    # Number of slots for Trading and Charging
    n_slots = len(data_slot)
    # SoC State
    soc_state = np.linspace(0, 1, 21)
    # Cost Matrix
    cost_matrix = np.zeros((n_slots, len(soc_state)))
    # Best Decision
    best_decision = np.zeros((n_slots, len(soc_state)))
    efc_decision = np.zeros((n_slots, len(soc_state)))
    # Not allowed states
    cost_matrix[0:2, 0] = 1000  # SoC of 0 is not allowed
    cost_matrix[:, 19:21] = 1000  # SoC of 1 is not allowed
    cost_matrix[-1, :] = 1000  # SoC at End of Slot must be 0.9
    cost_matrix[-1, 19:21] = 0

    # Decision State Definition
    decision_state = np.array([0, 1])

    return soc_state, cost_matrix, best_decision, decision_state, efc_decision


# DP Approach for optimized charging
def backward_dp_charge(data_slot, soc_state, cost_matrix, best_decision, decision_state, battery_size, charging_power,
                       slot_time, efc_decision, efficiency_charge, power_lewy):
    # Number of Slots
    n_slots = len(data_slot)
    # From Last Slot Backward
    for run in range(n_slots - 2, -1, -1):
        # For soc in soc_state:
        for soc in soc_state:
            # Next SoC State when taking decisions
            next_soc_state = soc + (decision_state * (charging_power * slot_time / battery_size))
            # Limit SoC
            next_soc_state = np.maximum(0, next_soc_state)
            next_soc_state = np.minimum(1, next_soc_state)
            # Get Relevant Cost Matrix Extract
            cost_extract = cost_matrix[run + 1, :]
            # Build Interpolation
            func = interpolate.interp1d(soc_state, cost_extract, kind='linear')
            # Cost next State
            cost_new_state = func(next_soc_state) + ((decision_state*charging_power*slot_time * (min(data_slot[run, 0:3]))+ power_lewy)/100)
            # Best Decision
            pos_decision = np.argmin(cost_new_state)
            cost_matrix[run, int(soc*20)] = min(cost_new_state)
            best_decision[run, int(soc*20)] = decision_state[pos_decision]
            #efc_decision[run, int(soc*20)] = decision_state[pos_decision]*charging_power*slot_time/battery_size/2

    return cost_matrix, best_decision, efc_decision


