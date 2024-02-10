# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-08-23
#
# Function Description
# Part of the Dynamic Environment M7
# Prediction of dynamic infrastructure properties according to arrival time prediciton
# _________________________________


# Import Functions:
from Modules.M2_Environment_Properties.CS_model import cs_dynamic_model


# Main Function
def dynamic_env_model(sim, env, vehicle):
    # Information about CS at current position: Type, Daytime:
    # CS Type
    env.cs_type = int(env.infra_array_poi_type[sim.step_dis])
    # Current Time: Start Time + Sum of Timesteps in Time based Time Vector
    # sim.daytime = env.freight_mission_start + (sum(sim.time_time) / 3600)  # in hours
    # For test only
    env.cs_prediction_time_arrive = sim.daytime
    # Get Properties at Current PoI
    env = dynamic_cs_properties(sim, env)

    return env


# Get Charging Station Properties
def dynamic_cs_properties(sim, env):
    # Call function in CS Model File
    env = cs_dynamic_model(sim, env)
    # Return variables
    return env

