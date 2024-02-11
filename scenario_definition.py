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


# Scenario Building Paper No 2: Essential for battery electric long-haul trucks (eTransportation)
def scenario_betos_sec42():
    ## Section 4.1
    # Variation of charging power and battery capacity has to be hard coded or in iterations over both variables
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


# Scenario_definition for etransportation paper section 4.1 (System design comparision)
def scenario_etransportation_sec41(battery_capacity):
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


# Scenario Generation for Aging Paper
def scenario_aging(index):
    # Built dict: S1 (1C LFP)
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S2 (1C NMC)
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S3 (2C LFP)
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S4 (2C NMC)
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S5 (3C LFP)
    scenario_5 = {
        # Scenario ID
        'scenario_id': 5,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0.0,
        'p_type_5': 1.0,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S6 (3C NMC)
    scenario_6 = {
        # Scenario ID
        'scenario_id': 6,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 0,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 3,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S7 (1C LFP Rule based strategy)
    scenario_7 = {
        # Scenario ID
        'scenario_id': 7,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S8 (1C NMC Rule based strategy)
    scenario_8 = {
        # Scenario ID
        'scenario_id': 8,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S9 (2C LFP) Driver Scale Cmean
    scenario_9 = {
        # Scenario ID
        'scenario_id': 9,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S92 (2C LFP) Driver Scale Cmax
    scenario_92 = {
        # Scenario ID
        'scenario_id': 92,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S10 (2C NMC Rule based strategy) Scale Cmean
    scenario_10 = {
        # Scenario ID
        'scenario_id': 10,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S102 (2C NMC Rule based strategy) Scale Cmax
    scenario_102 = {
        # Scenario ID
        'scenario_id': 102,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 0,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # BETOS Scale Scenarios
    # Built dict: S32 (2C LFP BETOS Scale Cmean)
    scenario_32 = {
        # Scenario ID
        'scenario_id': 32,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S33 (2C LFP BETOS Scale Cmax)
    scenario_33 = {
        # Scenario ID
        'scenario_id': 33,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S4 (2C NMC) Scale Cmean
    scenario_42 = {
        # Scenario ID
        'scenario_id': 42,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S4 (2C NMC) Scale Cmax
    scenario_43 = {
        # Scenario ID
        'scenario_id': 43,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # BETOS Scale Scenarios with changes in DOD
    # Built dict: S322 (2C LFP BETOS Scale Cmean and DOD change)
    scenario_322 = {
        # Scenario ID
        'scenario_id': 322,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.2,
        'max_soc': 0.8,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S332 (2C LFP BETOS Scale Cmax and DOD change)
    scenario_332 = {
        # Scenario ID
        'scenario_id': 332,
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
        '1_per_100km': 0,
        '2_per_100km': 0,
        '3_per_100km': 0,
        '4_per_100km': 1,
        # Probability
        'p_type_0': 0,
        'p_type_1': 0,
        'p_type_2': 0,
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,    # in kWh
        'c_rate': 2,
        'min_soc': 0.2,
        'max_soc': 0.8,
        'cell_chemistry': 1,        # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,            # in t
        'trip_length': 3000,        # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S4 (2C NMC) Scale Cmean and DOD Change
    scenario_422 = {
        # Scenario ID
        'scenario_id': 422,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.2,
        'max_soc': 0.8,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S4 (2C NMC) Scale Cmax and DOD Change
    scenario_432 = {
        # Scenario ID
        'scenario_id': 432,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 2,
        'min_soc': 0.2,
        'max_soc': 0.8,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.8,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S12 (1C LFP Heuristic Overnight and Weekend Charging)
    scenario_12 = {
        # Scenario ID
        'scenario_id': 12,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S122 (1C LFP Heuristic Overnight and Weekend Charging, T=25°C, 0.1 End, 0.85 Start)
    scenario_122 = {
        # Scenario ID
        'scenario_id': 122,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.85,
        'end_soc': 0.1,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S222 (1C NMC Heuristic Overnight and Weekend Charging, T=25°C, 0.1 End, 0.85 Start)
    scenario_222 = {
        # Scenario ID
        'scenario_id': 222,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 0,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.85,
        'end_soc': 0.1,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S114 (1C LFP, 400 kWh)
    scenario_114 = {
        # Scenario ID
        'scenario_id': 114,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 400,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.85,
        'end_soc': 0.1,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S114 (1C LFP, 400 kWh)
    scenario_116 = {
        # Scenario ID
        'scenario_id': 116,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 600,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.85,
        'end_soc': 0.1,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }
    # Built dict: S1000 (1C LFP, 1500km per week)
    scenario_1000 = {
        # Scenario ID
        'scenario_id': 1000,
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
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 1500,  # in km
        'max_daily_distance': 350,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S1002 (1C LFP, 2000km per week)
    scenario_1002 = {
        # Scenario ID
        'scenario_id': 1002,
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
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 2000,  # in km
        'max_daily_distance': 450,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S1002 (1C LFP, 2500km per week)
    scenario_1003 = {
        # Scenario ID
        'scenario_id': 1003,
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
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 2500,  # in km
        'max_daily_distance': 550,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S1004 (1C LFP, 1000km per week)
    scenario_1004 = {
        # Scenario ID
        'scenario_id': 1004,
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
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 1000,  # in km
        'max_daily_distance': 225,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S1100 (1C LFP, every 100km CS)
    scenario_1100 = {
        # Scenario ID
        'scenario_id': 1100,
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
        'waiting_time': [900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900,
                         900, 900, 900, 900, 900],
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
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Built dict: S1050 (1C LFP, every 50km CS)
    scenario_1050 = {
        # Scenario ID
        'scenario_id': 1050,
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
        'p_type_3': 0.0,
        'p_type_4': 0,
        'p_type_5': 1,
        # Vehicle properties
        'battery_capacity': 500,  # in kWh
        'c_rate': 1,
        'min_soc': 0.15,
        'max_soc': 1,
        'cell_chemistry': 1,  # (0:NMC, 1:LFP)
        # Mission Properties
        'payload': 19.3,  # in t
        'trip_length': 3000,  # in km
        'max_daily_distance': 650,  # in km
        'start_soc': 0.9,
        'end_soc': 0.2,
        'mission_start': 8.0,
        're_park': 0,
        # BETOS Version (0=Rulebased, 1=Normal DP, 2=Availability Handling, 3=Multiday)
        'version': 3,
        # Driving Sim Version (0=Extend Sim, 1=Fast Sim)
        'driving': 1,
        # Aging Evaluation
        'aging': 1
    }

    # Save as data frame
    s1 = pd.DataFrame(scenario_1)   # 1C LFP
    s2 = pd.DataFrame(scenario_2)   # 1C NMC
    s3 = pd.DataFrame(scenario_3)   # 2C LFP No Scaling
    s4 = pd.DataFrame(scenario_4)   # 2C NMC No Scaling
    s5 = pd.DataFrame(scenario_5)   # 3C LFP No Scaling
    s6 = pd.DataFrame(scenario_6)   # 3C NMC No Scaling
    s32 = pd.DataFrame(scenario_32)  # 2C LFP BETOS Scale Cmean
    s42 = pd.DataFrame(scenario_42)  # 2C NMC BETOS Scale Cmean
    s33 = pd.DataFrame(scenario_33)  # S33 2C LFP Cmax
    s43 = pd.DataFrame(scenario_43)  # S43 2C NMC Cmax
    s322 = pd.DataFrame(scenario_322)  # S322 2C LFP Scale Cmean DOD(0.2,0.80)
    s332 = pd.DataFrame(scenario_332)  # S322 2C LFP Scale Cmax DOD(0.2,0.80)
    s422 = pd.DataFrame(scenario_422)  # S422 2C NMC Scale Cmean DOD(0.2,0.80)
    s432 = pd.DataFrame(scenario_432)  # S432 2C NMC Scale Cmax DOD(0.2,0.80)

    s7 = pd.DataFrame(scenario_7)   # 1C LFP Driver
    s8 = pd.DataFrame(scenario_8)   # 1C NMC Driver
    s9 = pd.DataFrame(scenario_9)   # 2C LFP Driver Scale Cmean
    s10 = pd.DataFrame(scenario_10)   # 2C NMC Driver Scale Cmean
    s92 = pd.DataFrame(scenario_92)   # S92 LFP Driver Scale Cmax
    s102 = pd.DataFrame(scenario_102)  # S102 NMC Driver Scale Cmax
    s12 = pd.DataFrame(scenario_12)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging
    s122 = pd.DataFrame(scenario_122)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C
    s222 = pd.DataFrame(scenario_222)  # 1C NMC BETOS Heuristic Overnight and Weekend Charging, T=25°C

    # Sensitivity Analysis
    s114 = pd.DataFrame(scenario_114)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 400 kWh
    s116 = pd.DataFrame(scenario_116)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 600 kWh

    s1000 = pd.DataFrame(scenario_1000)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 1500km/week
    s1002 = pd.DataFrame(scenario_1002)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 2000km/week
    s1003 = pd.DataFrame(scenario_1003)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 2500km/week
    s1004 = pd.DataFrame(scenario_1004)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 1000km/week

    s1100 = pd.DataFrame(scenario_1100)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 3000km/week, Every 100km CS
    s1050 = pd.DataFrame(scenario_1050)  # 1C LFP BETOS Heuristic Overnight and Weekend Charging, T=25°C, 500 kWh, 3000km/week, Every 50km CS


    # Return index scenario
    if index == 1:
        s_return = s1
    elif index == 2:
        s_return = s2
    elif index == 3:
        s_return = s3
    elif index == 4:
        s_return = s4
    elif index == 5:
        s_return = s5
    elif index == 6:
        s_return = s6
    elif index == 7:
        s_return = s7
    elif index == 8:
        s_return = s8
    elif index == 9:
        s_return = s9
    elif index == 10:
        s_return = s10
    elif index == 32:
        s_return = s32
    elif index == 33:
        s_return = s33
    elif index == 322:
        s_return = s322
    elif index == 42:
        s_return = s42
    elif index == 422:
        s_return = s422
    elif index == 43:
        s_return = s43
    elif index == 12:
        s_return = s12
    elif index == 122:
        s_return = s122
    elif index == 222:
        s_return = s222
    elif index == 92:
        s_return = s92
    elif index == 102:
        s_return = s102
    elif index == 432:
        s_return = s432
    elif index == 332:
        s_return = s332
    elif index == 114:
        s_return = s114
    elif index == 116:
        s_return = s116
    elif index == 1000:
        s_return = s1000
    elif index == 1002:
        s_return = s1002
    elif index == 1003:
        s_return = s1003
    elif index == 1004:
        s_return = s1004
    elif index == 1100:
        s_return = s1100
    elif index == 1050:
        s_return = s1050

    return s_return

