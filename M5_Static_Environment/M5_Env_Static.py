# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-06-14
#
# Function Description
# Part of the Static Environment M5
# Definition of static environment properties like PoI Position and Type
# _________________________________


# Import Functions:
from Modules.M5_Static_Environment import INFRA_model


# Used Sources in this file:


# Function
def static_env(env, scenario):
    # Get Position and Type of PoI along Route
    env.infra_array_poi, env.infra_array_poi_id, env.infra_array_poi_pos, env.infra_array_poi_type, env.infra_number_poi = \
        INFRA_model.infra_static_model(env, scenario)

    return env

