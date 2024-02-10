# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-02
#
# Function Description
# Part of the Operation Strategy Module M9
# Final Decision using different methods for decision finding
# _________________________________


# import functions:
from Modules.M9_Operation_Strategy.M9_1_Prediction import M91_Prediction
from Modules.M9_Operation_Strategy.M9_2_Filtering import M92_Poi_Filter
from Modules.M9_Operation_Strategy.M9_7_DP import M97_Dyanmic_Programming_OS
from Modules.M9_Operation_Strategy.M9_3_Rulebased import M93_RuleBased_OS
from Modules.M9_Operation_Strategy.M9_7_DP import M97_DP_advanced_OS
from Modules.M9_Operation_Strategy.M9_0_Charging_Management_Multiday.M9_0_1_En_Route import M901_En_Route_CM
import time
# Used sources in this file


# Definition of final decision (betos_action, betos_soc_target, betos_rest_time)
def betos_decision(sim, env, vehicle):

    # Prediction _______________________________________________________________________________________________________
    if env.infra_array_poi[sim.step_dis] == 1:
        sim, env = M91_Prediction.betos_prediction_env_data(sim, env, vehicle)
        # Filtering ____________________________________________________________________________________________________
        sim, env = M92_Poi_Filter.betos_poi_filter(sim, env, vehicle)

        # Decision Making Algorithm ________________________________________________________________________________________
        if sim.betos_version == 0:
        # Rule Based
            sim = M93_RuleBased_OS.betos_rule_based(sim, env, vehicle)
        elif sim.betos_version == 1:
        # Dynamic Programming
            sim = M97_Dyanmic_Programming_OS.betos_dynamic_programming(sim, env, vehicle)
        elif sim.betos_version == 2:
        # Dynamic Programming Real World Env Properties
            sim = M97_DP_advanced_OS.betos_dynamic_programming_ad(sim, env, vehicle)
        # Multi Day Implementation
        elif sim.betos_version == 3:
            sim = M901_En_Route_CM.betos_dynamic_programming_multi(sim, env, vehicle)

    return sim

