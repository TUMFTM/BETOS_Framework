# _________________________________
# BET.OS Function #
# Operation Scenario Block #
# Designed by MX-2022-05-20
# Function Description
# Definition of Infrastructure
# Definition of PoI along Route Profile
# Definition of CS Type of one PoI
# Part of the static Environment Module
# _________________________________

# Sources:
# Distribution of Availability and Charging Costs per kWh from Excel File

# Imports:
import numpy as np
import pandas
from scipy.interpolate import interp1d
import random


# _________________________________
# Main Function INFRA Model
def infra_static_model(env, scenario):
    # Positioning of PoI along Route/Scenario Cycle
    infra_array_poi, infra_array_poi_id, infra_array_poi_pos, number_poi = infra_poi_definition_func(env.route_array_distance, env.route_array_stoptime, env.route_array_speed, scenario)
    # Type Definition for PoI along Route
    infra_array_poi_type = infra_poi_type_definition_func(infra_array_poi, env.route_array_speed, scenario)

    return infra_array_poi, infra_array_poi_id, infra_array_poi_pos, infra_array_poi_type, number_poi
# _________________________________


# PoI Definition
# Function for setting PoI along route profile
def infra_poi_definition_func(route_array_distance, route_array_stoptime, route_array_speed, scenario):
    # Read Excel File for PoI Definition
    #data_raw = pandas.read_excel('BET.OS.Plan.xlsx', sheet_name='ReadDataPoI', index_col=None, header=None)
    # Preprocess data
    #data_array = data_raw.to_numpy()
    # Interpolate Probability of being PoI knowing the stoptime
    #poi_probability = interp1d(np.transpose(data_array[:, 0]), np.transpose(data_array[:, 2]), kind='linear')
    # Initialize Output
    distance = route_array_distance.size
    infra_array_poi = np.zeros(distance)
    infra_array_poi_id = np.zeros(distance)
    # Set PoI for required Stops due to Scenario
    # Set PoI at the beginning end of Scenario
    infra_array_poi[0] = 1
    infra_array_poi[-1] = 1
    # Set PoI according to Probability
    # Set PoI at End of one Microtrip
    choices = [0, 1]
    for x in range(distance-1):
        # if route_array_stoptime[x] > 0:
        if route_array_speed[x] == 0.5:
            # Get PoI Probability
            # prob_poi = poi_probability(route_array_stoptime[x])
            prob_poi = 1  # Setting PoI where two microtrips intersect
            choice_poi_raw = random.choices(choices, weights=((1-prob_poi)*100, prob_poi*100), k=1)
            choice_poi = np.array(choice_poi_raw)
            if choice_poi == 1:
                infra_array_poi[x] = 1

    # Set additional PoI
    i = 0  # Run Variable
    n_poi_tot = int(np.sum(infra_array_poi))
    # Position of currently set POI along route
    pos_poi = np.zeros(n_poi_tot)
    for x in range(distance):
        if infra_array_poi[x] == 1:
            pos_poi[i] = x
            i = i + 1

    # Additional PoI
    #choices_add = data_array[0:4, 3].tolist()
    choices_add = np.array([1, 2, 3, 4]).tolist()
    weights_add = (np.array([scenario['1_per_100km'][0], scenario['2_per_100km'][0],
                             scenario['3_per_100km'][0], scenario['4_per_100km'][0]])*100).tolist()
    # Get distance between current PoI
    for x in range(n_poi_tot):
        # Get distance between current PoI and last PoI
        if x == 0:
            dis_poi = pos_poi[x]  # in m
        else:
            dis_poi = pos_poi[x] - pos_poi[x-1]  # in m

        # Get number of additional PoI between the two considered PoI
        # Get number of PoI per 100 km from distribution
        #n_poi_100km = np.array(random.choices(choices_add, weights=(data_array[0:4, 4] * 100).tolist(), k=1))
        n_poi_100km = np.array(random.choices(choices_add, weights=weights_add, k=1))
        # Round number of PoI and subtract one
        n_poi = np.ceil((dis_poi/1000/100) * n_poi_100km) - 1
        if n_poi > 0:
            # Get distance step between new PoI
            step_poi = np.round(dis_poi/(n_poi + 1))
            # Positioning of new additional PoI
            i = n_poi  # Run Variable
            n = 1  # Run Variable
            while i > 0:
                infra_array_poi[int(pos_poi[x] - (step_poi * n))] = 1
                i = i - 1
                n = n + 1

    # Poi ID Allocation
    number_poi_total = np.sum(infra_array_poi)
    infra_array_poi_pos = np.zeros(int(number_poi_total))
    ident = 0
    for x in range(distance):
        if infra_array_poi[int(x)] == 1:
            infra_array_poi_pos[ident] = x
            infra_array_poi_id[int(x)] = ident
            ident = ident + 1

    return infra_array_poi, infra_array_poi_id, infra_array_poi_pos, number_poi_total
# _________________________________


# PoI Type Definition
# Function for PoI Type Definition
# type = 0: Rest area without charging possibility
# type = 1: Charging Possibility with lower power in private area
# type = 2: Charging Possibility with lower power in urban area
# type = 3: Charging Possibility with mid power in rural or highway area
# type = 4: Charging Possibility with high power in rural or highway area
# type = 5: Charging Possibility with MCS in highway area
def infra_poi_type_definition_func(infra_array_poi, route_array_speed, scenario):
    # Read Excel File for PoI Type Definition
    #data_raw = pandas.read_excel('BET.OS.Plan.xlsx', sheet_name='ReadDataPoIType', index_col=None, header=None)
    # Preprocess data
    #data_array = data_raw.to_numpy()
    # Number of Total PoI
    n_poi_tot = int(np.sum(infra_array_poi))
    # Initialize position and average velocity of/before PoI
    pos_poi = np.zeros(n_poi_tot)
    vel_poi = np.zeros(n_poi_tot)
    vel_poi_max = np.zeros(n_poi_tot)

    # Initialize Output
    distance = infra_array_poi.size
    infra_array_poi_type = np.zeros(distance)
    # Set Private Depot at Starting Point
    infra_array_poi_type[0] = 1
    # Initialize PoI Choices
    choices = [0, 1, 2, 3, 4, 5]
    # Get Position and Velocity of/before PoI
    i = 0  # Run Variable
    for x in range(1, distance-1):
        if infra_array_poi[x] == 1:
            pos_poi[i] = x
            if i <= 1:
                before = 0
            else:
                before = int(pos_poi[i-1])
            vel_poi[i] = np.mean(route_array_speed[before:x])
            vel_poi_max[i] = np.max(route_array_speed[before:x]) * 3.6  # in km/h
            # Select PoI Type
            distribution = (np.array([scenario['p_type_0'][0], scenario['p_type_1'][0], scenario['p_type_2'][0],
                                      scenario['p_type_3'][0], scenario['p_type_4'][0], scenario['p_type_5'][0]])*100).tolist()
            '''
            # Get distribution over Type
            if vel_poi[i] <= data_array[0, 0] and vel_poi_max[i] <= data_array[1, 0]:
                distribution = data_array[0, 1:7]
            elif vel_poi[i] <= data_array[1, 0] and vel_poi_max[i] <= data_array[2, 0]:
                distribution = data_array[1, 1:7]
            elif vel_poi[i] <= data_array[2, 0] and vel_poi_max[i] <= data_array[3, 0]:
                distribution = data_array[2, 1:7]
            else:
                distribution = data_array[3, 1:7]
            '''
            # Type
            # poi_type = random.choices(choices, weights=(distribution * 100).tolist(), k=1)
            poi_type = random.choices(choices, weights=distribution, k=1)
            infra_array_poi_type[x] = np.array(poi_type)
            # Update Run Variable
            i = i + 1
    # End for

    # Define PoI Type at last PoI
    infra_array_poi_type[-1] = 1

    return infra_array_poi_type
# __________________________________
