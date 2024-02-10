# _________________________________
# BET.OS Function #
# Operation Scenario Block #
# Designed by MX-2022-05-27
# Function Description
# Definition of Charging Station models according to type
# Definition of Availability, Price, Power of one Charging Station
# Part of the dynamic Environment Module
# _________________________________

# Import
import numpy as np
import pandas
from scipy.interpolate import interp1d
import random


# Main Function for DYNAMIC CS Model
def cs_dynamic_model(sim, env):

    # Static Power according to cs type
    env.cs_power = env.cs_data_power[env.cs_type]
    # Current TimeStamp
    # Get Probability for Availability
    cs_prediction_availability_current, env.cs_price = cs_stochastic_distribution_func(env.cs_type, sim.daytime,
                                                                                           env.cs_data_availability,
                                                                                           env.cs_data_price)
    # Get Availability from Probability and Price at current timestamp
    env.cs_availability = cs_availability_func(cs_prediction_availability_current)

    # Get Probability for Availability and Price Prediction
    env.cs_prediction_availability, env.cs_prediction_price = cs_stochastic_distribution_func(env.cs_type,
                                                                                      env.cs_prediction_time_arrive,
                                                                                      env.cs_data_availability,
                                                                                      env.cs_data_price)

    return env


# ________________________________
# Parametric Stochastic Distribution over Day for availability
def cs_stochastic_distribution_func(cs_type, sim_prediction_time_arrive, cs_data_availability, cs_data_price):

    cs_prediction_availability = cs_data_availability(sim_prediction_time_arrive)[cs_type]
    cs_prediction_price = cs_data_price(sim_prediction_time_arrive)[cs_type]
    
    return cs_prediction_availability, cs_prediction_price


# ________________________________
# Get current availability from probability
def cs_availability_func(cs_prediction_availability):

    choices = [0, 1]
    cs_availability_raw = random.choices(choices, weights=(cs_prediction_availability*100,
                                                           (1-cs_prediction_availability)*100), k=1)
    cs_availability = np.array(cs_availability_raw)

    return cs_availability


# ________________________________
# Read CS Data from Excel file
def cs_data_read_func(scenario):
    # Read Excel File
    #data_raw = pandas.read_excel('BET.OS.Plan.xlsx', sheet_name='ReadData', index_col=None, header=None)
    # Preprocess data
    #data_array = data_raw.to_numpy()
    # Daytime Vector
    daytime = np.linspace(1, 24, num=24, endpoint=True)
    # Read Power
    #cs_data_power = data_array[0, 12:18]
    cs_data_power = np.array([scenario['charging_power_type_0'][0], scenario['charging_power_type_1'][0], scenario['charging_power_type_2'][0],
                              scenario['charging_power_type_3'][0], scenario['charging_power_type_4'][0], scenario['charging_power_type_5'][0]])
    # Read Availability
    #cs_data_availability_raw = data_array[:, 0:6]
    cs_data_availability_raw = np.array([scenario['ava_type_0'], scenario['ava_type_1'], scenario['ava_type_2'],
                                         scenario['ava_type_3'], scenario['ava_type_4'], scenario['ava_type_5']])
    #cs_data_availability = interp1d(daytime, np.transpose(cs_data_availability_raw), kind='linear')
    cs_data_availability = interp1d(daytime, cs_data_availability_raw, kind='linear')
    # Read Price
    #cs_data_price_raw = data_array[:, 6:12]
    cs_data_price_raw = np.array([scenario['price_type_0'], scenario['price_type_1'], scenario['price_type_2'],
                                  scenario['price_type_3'], scenario['price_type_4'], scenario['price_type_5']])
    # cs_data_price = interp1d(daytime, np.transpose(cs_data_price_raw), kind='linear')
    cs_data_price = interp1d(daytime, cs_data_price_raw, kind='linear')
    # Read Waiting time
    # cs_data_waiting_time_raw = data_array[:, 18:19]
    cs_data_waiting_time_raw = np.array([scenario['waiting_time']])
    # cs_data_waiting_time = interp1d(daytime, np.transpose(cs_data_waiting_time_raw), kind='linear')
    cs_data_waiting_time = interp1d(daytime, cs_data_waiting_time_raw, kind='linear')

    return cs_data_availability, cs_data_price, cs_data_power, cs_data_waiting_time
