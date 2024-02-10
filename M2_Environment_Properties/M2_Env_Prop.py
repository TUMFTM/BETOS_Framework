# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-06-14
#
# Function Description
# Part of the Environment Properties M2
# Definition of Environment Properties of one Charging Station
# _________________________________


# Import Functions:
from Modules.M2_Environment_Properties import CS_model

# Used sources in this file:


def environment_properties(env, scenario):
    # Get Properties
    cs_data_availability, cs_data_price, cs_data_power, cs_data_waiting_time = CS_model.cs_data_read_func(scenario)
    # Store all variables in env object
    env.cs_data_availability = cs_data_availability
    env.cs_data_price = cs_data_price
    env.cs_data_power = cs_data_power
    env.cs_data_waiting_time = cs_data_waiting_time

    return env
