# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-02
#
# Function Description
# Part of the Operation Strategy (BET.OS) Module M9
# M91: Prediction Functions of BET.OS such as Energy Consumption and Charging station data
# _________________________________


# import functions:
import math
import numpy as np
from Modules.M7_Dynamic_Environment import M7_Env_dynamic

# Used sources in this file:

# BETOS Prediction:
# First Integration Level: Predict System State (Vehicle and Infrastructure) when reaching next upcoming PoI
def betos_predicition(sim, vehicle, env):
    # Vehicle related data
    sim = betos_prediction_energy_consumption(sim, vehicle, env)
    # Environment related data
    sim, env = betos_prediction_env_data(sim, env, vehicle)

    return sim, env


# Energy Consumption and Driving Time Prediction
def betos_prediction_energy_consumption(sim, vehicle, env):
    # Energy Consumption Prediction through quasi static longitudinal simulation
    # Velocity before acceleration
    v1 = env.route_array_speed[0:sim.dis_steps-1]
    # Velocity after acceleration
    v2 = env.route_array_speed[1:sim.dis_steps]
    # delta v
    delta_v = v2-v1
    # acceleration
    a = 0.5*(delta_v*delta_v) + (v1*delta_v)  # in m/s^2
    # Time step
    t =1/((v2+v1)/2)
    # Resistance
    F_tot = (0.5*vehicle.cw*vehicle.roh_air*vehicle.af*(v1*v1))+\
            (vehicle.mass_total*vehicle.c_rr*vehicle.g_force*np.cos(np.arctan(env.route_array_slope[0:sim.dis_steps-1])/100))+\
            (vehicle.mass_total*a*vehicle.gear_lambda)+\
            (vehicle.mass_total*vehicle.g_force*np.sin(np.arctan(env.route_array_slope[0:sim.dis_steps-1])/100))
    # Torque and Speed
    n = v1/(2*np.pi*vehicle.r_dyn)  #1/s
    torque = F_tot*vehicle.r_dyn
    # Power and Energy at battery
    p = 2 * np.pi * torque * n
    p_bat = p/((vehicle.gear_efficiency * vehicle.em_efficiency * vehicle.pe_efficiency)**np.sign(F_tot))
    e_bat = p_bat*t
    # Safe in sim object and bring in same dimension as other non prediction variables
    sim.betos_energy_cons_dis_prediction = np.concatenate((e_bat, np.array([0])))  # in Ws
    sim.betos_time_dis_prediction = np.concatenate((t, np.array([0])))  # in s
    sim.betos_power_dis_prediction = np.concatenate((p_bat, np.array([0])))  # in W

    # Use dynamic prediction error between zero and sim.betos_manipulation_cons
    dynamic_error_cons = np.random.rand(sim.dis_steps) * sim.betos_manipulation_cons
    dynamic_error_time = np.random.rand(sim.dis_steps) * sim.betos_manipulation_time

    # Error in Prediction Analysis (optional)
    sim.betos_energy_cons_dis_prediction = (1.0 * sim.betos_energy_cons_dis_prediction) + (dynamic_error_cons * np.sign(sim.betos_energy_cons_dis_prediction) * \
                                           sim.betos_energy_cons_dis_prediction)

    sim.betos_time_dis_prediction = sim.betos_time_dis_prediction + dynamic_error_time * sim.betos_time_dis_prediction

    # Use time prediction to get driving time from poi to destination
    for i in range(0, int(env.infra_number_poi)):
        sim.betos_driving_time_destination[i, 0] = i  # (POI ID)
        sim.betos_driving_time_destination[i, 1] = sum(sim.betos_time_dis_prediction[int(env.infra_array_poi_pos[i]):int(env.infra_array_poi_pos[-1])]) / 3600  # in hours

    return sim


# Environment Data Prediction
def betos_prediction_env_data(sim, env, vehicle):
    # Prediction of Environment Properties
    env = M7_Env_dynamic.dynamic_env_model(sim, env, vehicle)

    return sim, env

