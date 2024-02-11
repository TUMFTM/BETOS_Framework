#_________________________________
# BET.OS Function #
#
# Designed by MX-2023-07-05
#
# Function Description
# Definition of mission scenario for the useage in the main simulation
# _________________________________


# import functions:
import numpy as np
import pandas as pd


# Function
def scenario_gen():
    # Built dict
    scenario_1 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 1,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 250,        # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }

    # Save as data frame
    s1 = pd.DataFrame(scenario_1)

    return s1


# Scenario Article Optimizing the Journey - Section 4.2 and Section 4.3
def scenario_betos_sec42():
    ## Section 4.2
    # S1
    scenario_1 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.8,
        '2_per_100km': 0.2,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.5,
        'p_type_2': 0.5,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 0,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s1 = pd.DataFrame(scenario_1)

    # S2
    scenario_2 = {
        # Scenario ID
        'scenario_id': 2,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.2,
        '2_per_100km': 0.8,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.2,
        'p_type_2': 0.3,
        'p_type_3': 0.3,
        'p_type_4': 0.2,
        'p_type_5': 0,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s2 = pd.DataFrame(scenario_2)

    # S3
    scenario_3 = {
        # Scenario ID
        'scenario_id': 3,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.1,
        '2_per_100km': 0.4,
        '3_per_100km': 0,
        '4_per_100km': 0.5,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.1,
        'p_type_2': 0.2,
        'p_type_3': 0.3,
        'p_type_4': 0.3,
        'p_type_5': 0.1,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0

    }
    s3 = pd.DataFrame(scenario_3)

    # S4
    scenario_4 = {
        # Scenario ID
        'scenario_id': 4,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s4 = pd.DataFrame(scenario_4)

    ## Section 4.3
    # S31
    scenario_31 = {
        # Scenario ID
        'scenario_id': 31,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        'ava_type_3': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        'ava_type_4': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        'ava_type_5': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.1,
        '2_per_100km': 0.4,
        '3_per_100km': 0,
        '4_per_100km': 0.5,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.1,
        'p_type_2': 0.2,
        'p_type_3': 0.3,
        'p_type_4': 0.3,
        'p_type_5': 0.1,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0

    }
    s31 = pd.DataFrame(scenario_31)
    # S32
    scenario_32 = {
        # Scenario ID
        'scenario_id': 32,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        'ava_type_3': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        'ava_type_4': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        'ava_type_5': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.1,
        '2_per_100km': 0.4,
        '3_per_100km': 0,
        '4_per_100km': 0.5,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.1,
        'p_type_2': 0.2,
        'p_type_3': 0.3,
        'p_type_4': 0.3,
        'p_type_5': 0.1,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0

    }
    s32 = pd.DataFrame(scenario_32)
    # S33
    scenario_33 = {
        # Scenario ID
        'scenario_id': 33,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        'ava_type_3': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        'ava_type_4': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        'ava_type_5': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.1,
        '2_per_100km': 0.4,
        '3_per_100km': 0,
        '4_per_100km': 0.5,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.1,
        'p_type_2': 0.2,
        'p_type_3': 0.3,
        'p_type_4': 0.3,
        'p_type_5': 0.1,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0

    }
    s33 = pd.DataFrame(scenario_33)
    # S34
    scenario_34 = {
        # Scenario ID
        'scenario_id': 34,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
        'ava_type_4': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        'ava_type_5': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0.1,
        '2_per_100km': 0.4,
        '3_per_100km': 0,
        '4_per_100km': 0.5,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0.1,
        'p_type_2': 0.2,
        'p_type_3': 0.3,
        'p_type_4': 0.3,
        'p_type_5': 0.1,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0

    }
    s34 = pd.DataFrame(scenario_34)

    # S41
    scenario_41 = {
        # Scenario ID
        'scenario_id': 41,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        'ava_type_3': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        'ava_type_4': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        'ava_type_5': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s41 = pd.DataFrame(scenario_41)
    # S42
    scenario_42 = {
        # Scenario ID
        'scenario_id': 42,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        'ava_type_3': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        'ava_type_4': [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        'ava_type_5': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s42 = pd.DataFrame(scenario_42)
    # S43
    scenario_43 = {
        # Scenario ID
        'scenario_id': 43,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        'ava_type_3': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        'ava_type_4': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        'ava_type_5': [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s43 = pd.DataFrame(scenario_43)
    # S44
    scenario_44 = {
        # Scenario ID
        'scenario_id': 44,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
        'ava_type_4': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        'ava_type_5': [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s44 = pd.DataFrame(scenario_44)

    ## Section 5.1
    # S45
    scenario_45 = {
        # Scenario ID
        'scenario_id': 45,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s45 = pd.DataFrame(scenario_45)
    # S46
    scenario_46 = {
        # Scenario ID
        'scenario_id': 46,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s46 = pd.DataFrame(scenario_46)
    # S47
    scenario_47 = {
        # Scenario ID
        'scenario_id': 47,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1500,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0.5,
        'p_type_5': 0.5,
        # Vehicle properties
        'battery_capacity': 500,
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,
        'trip_length': 675,
        'max_daily_distance': 750,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 2,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 0,
        # Aging
        'aging': 0
    }
    s47 = pd.DataFrame(scenario_47)

    return s1, s2, s3, s4, s31, s32, s33, s34, s41, s42, s43, s44, s45, s46, s47


# Scenario_definition for article: Optimizing the Journey - Section 4.1
def scenario_betos_sec41(battery_capacity):
    # 400 kW
    scenario_1 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 400,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s1 = pd.DataFrame(scenario_1)

    # 600 kW
    scenario_2 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 600,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s2 = pd.DataFrame(scenario_2)

    # 800 kW
    scenario_3 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 800,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s3 = pd.DataFrame(scenario_3)

    # 1000 kW
    scenario_4 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1000,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s4 = pd.DataFrame(scenario_4)

    # 1200 kW
    scenario_5 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1200,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s5 = pd.DataFrame(scenario_5)

    # 1400 kW
    scenario_6 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1400,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s6 = pd.DataFrame(scenario_6)

    # 1600 kW
    scenario_7 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1600,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s7 = pd.DataFrame(scenario_7)

    # 1800 kW
    scenario_8 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 1800,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s8 = pd.DataFrame(scenario_8)

    # 2000 kW
    scenario_9 = {
        # Scenario ID
        'scenario_id': 1,
        # Charging Station properties
        # Availability of cs types
        'ava_type_0': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_1': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_2': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_3': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_4': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'ava_type_5': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # charging prices of cs types
        'price_type_0': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_2': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_4': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'price_type_5': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Charging Power in kW
        'charging_power_type_0': 0,
        'charging_power_type_1': 150,
        'charging_power_type_2': 350,
        'charging_power_type_3': 700,
        'charging_power_type_4': 1000,
        'charging_power_type_5': 2000,
        # Waiting time
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
        # Charging Network properties
        # Density parameter
        '1_per_100km': 0,
        '2_per_100km': 1,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': battery_capacity,  # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 675,  # in km
        'max_daily_distance': 750,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 1,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 0
    }
    # Save as data frame
    s9 = pd.DataFrame(scenario_9)

    return s1, s2, s3, s4, s5, s6, s7, s8, s9

