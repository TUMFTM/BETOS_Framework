# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-11-11
#
# Function Description
# Simulation Task for different papers and articles

# Import Libraries______________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
import pandas
import scipy.stats as st
# Import Functions______________________________________________________________________________________________________
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_Oneday_Simulation
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_Multiday_Simulation
from Modules.M1_Vehicle_Properties import M1_Veh_Prop
from Modules.M2_Environment_Properties import M2_Env_Prop
from Modules.M3_Freight_Properties import M3_Freight_Prop
from Modules.M4_Static_Vehicle import M4_Veh_Static
from Modules.M5_Static_Environment import M5_Env_Static
from Modules.M8_Operation_Simulation.M8_2_Driving import M82_DrivingSim
from Modules.M9_Operation_Strategy.M9_1_Prediction import M91_Prediction
from Modules.M9_Operation_Strategy.M9_9_BiDi_Integration import M_99_BiDi_Integration
from Modules.M12_Visualization import M12_Visualization
import scenario_definition
# ______________________________________________________________________________________________________________________

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Paper No 2 Simulation Task____________________________________________________________________________________________
# Evaluation of different prediction errors
def prediction_task(a):
    # Result Variable Initialization
    #result_time = np.zeros((3))
    #result_stops = np.zeros((3))
    #result_discharge = np.zeros((3))
    #result_time_loss = np.zeros((3))
    #result_mean_power = np.zeros((3))

    # Get Scenario
    scenario = scenario_definition.scenario_gen()

    # Object Def
    vehicle, env, sim = M84_Oneday_Simulation.object_def()
    # Module M1: Vehicle Properties
    vehicle = M1_Veh_Prop.vehicle_properties(vehicle, scenario)
    # Module M2: Environment Properties
    env = M2_Env_Prop.environment_properties(env, scenario)
    # Module M3: Freight Properties
    sim, env = M3_Freight_Prop.freight_properties(sim, env, scenario)
    # Module M4: Vehicle Building
    vehicle = M4_Veh_Static.static_vehicle_model(sim, vehicle, env)
    # Module M5: Building Environment
    env = M5_Env_Static.static_env(env, scenario)
    # <>
    # No Manipulation # Benchmark
    sim.betos_manipulation_cons = 0
    sim.betos_manipulation_time = 0
    sim.betos_manipulation_charge = 0
    # Initialization
    sim = M84_Multiday_Simulation.initialization(env, sim, scenario)
    sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
    sim = M82_DrivingSim.driving_sim(sim, vehicle, env)
    #result_time = np.zeros(3)
    #result_stops = np.zeros(3)
    #result_discharge = np.zeros(3)
    #result_time_loss = np.zeros(3)
    #result_mean_power = np.zeros(3)
    # Save in results variables
    if sim.betos_run_empty == 0:
        result_time = sum(sim.time_time)/3600  # in h
        result_stops = sim.betos_stops
        result_discharge = sim.betos_deep_discharge
        pure_driving_time = sum(sim.time_dis) / 3600
        if pure_driving_time > 9:
            result_time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600) - 1.5  # in h
        elif pure_driving_time <= 9:
            result_time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600) - 0.75
        else:
            result_time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600)

        result_mean_power = np.mean(sim.betos_power[sim.betos_power > 0])
    else:
        result_time = np.nan  # in h
        result_stops = np.nan
        result_discharge = np.nan
        result_time_loss = np.nan  # in h
        result_mean_power = np.nan

    '''
    # <>
    # Manipulation in Consumption "SoC"
    sim.betos_manipulation_cons = -0.15
    sim.betos_manipulation_time = 0
    sim.betos_manipulation_charge = 0
    # Initialization
    sim = M84_OpSim_Main.initialization(env, sim)
    sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
    sim = M84_DrivingSim.driving_sim(sim, vehicle, env)
    # Save in results variables
    if sim.betos_run_empty == 0:
        result_time[1] = sum(sim.time_time) / 3600  # in h
        result_stops[1] = sim.betos_stops
        result_discharge[1] = sim.betos_deep_discharge
        pure_driving_time = sum(sim.time_dis) / 3600
        if pure_driving_time > 9:
            result_time_loss[1] = (((sum(sim.rest_time_dis)) + (1 - sim.betos_re_park) * (
                sum(sim.wait_time_dis))) / 3600) - 1.5  # in h
        else:
            result_time_loss[1] = (((sum(sim.rest_time_dis)) + (1 - sim.betos_re_park) * (
                sum(sim.wait_time_dis))) / 3600) - 0.75

        result_mean_power[1] = np.mean(sim.betos_power[sim.betos_power > 0])
    else:
        result_time[1] = np.nan  # in h
        result_stops[1] = np.nan
        result_discharge[1] = np.nan
        result_time_loss[1] = np.nan  # in h
        result_mean_power[1] = np.nan

    # <>
    # Manipulation in Time "Time"
    sim.betos_manipulation_cons = 0
    sim.betos_manipulation_time = -0.15
    sim.betos_manipulation_charge = 0
    # Initialization
    sim = M84_OpSim_Main.initialization(env, sim)
    sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
    sim = M84_DrivingSim.driving_sim(sim, vehicle, env)
    # Save in results variables
    if sim.betos_run_empty == 0:
        result_time[2] = sum(sim.time_time) / 3600  # in h
        result_stops[2] = sim.betos_stops
        result_discharge[2] = sim.betos_deep_discharge
        pure_driving_time = sum(sim.time_dis) / 3600
        if pure_driving_time > 9:
            result_time_loss[2] = (((sum(sim.rest_time_dis)) + (1 - sim.betos_re_park) * (
                sum(sim.wait_time_dis))) / 3600) - 1.5  # in h
        else:
            result_time_loss[2] = (((sum(sim.rest_time_dis)) + (1 - sim.betos_re_park) * (
                sum(sim.wait_time_dis))) / 3600) - 0.75

        result_mean_power[2] = np.mean(sim.betos_power[sim.betos_power > 0])
    else:
        result_time[2] = np.nan  # in h
        result_stops[2] = np.nan
        result_discharge[2] = np.nan
        result_time_loss[2] = np.nan  # in h
        result_mean_power[2] = np.nan

    # Save Results
    # np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_stops_s3.csv', result_stops, delimiter=",")
    # np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_discharge_s3.csv', result_discharge, delimiter=",")
    # np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3.csv', result_time_loss, delimiter=",")
    # np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/power_s3.csv', result_mean_power, delimiter=",")
    '''
    return result_time_loss


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# ATZ __________________________________________________________________________________________________________________
# ATZ Simulation Task: Time Loss compared to ICET
def atz_sim_task(size):
    # Runs per Combination
    sim_runs = 100
    # Initialization of result matrix
    result_time_loss = np.zeros(sim_runs)
    result_energy_consumption = np.zeros(sim_runs)
    result_distance = np.zeros(sim_runs)

    for iter in range(0, sim_runs):
        # Object Def
        vehicle, env, sim = M84_Oneday_Simulation.object_def()
        # Module M1: Vehicle Properties
        vehicle = M1_Veh_Prop.vehicle_properties(vehicle)
        # Set Combination
        vehicle.battery_capacity = size
        # Module M2: Environment Properties
        env = M2_Env_Prop.environment_properties(env)
        # Module M3: Freight Properties
        env = M3_Freight_Prop.freight_properties(env)
        # Module M4: Vehicle Building
        vehicle = M4_Veh_Static.static_vehicle_model(sim, vehicle, env)
        # Initialization Simulation parameter
        # Module M2: Environment Properties
        env = M2_Env_Prop.environment_properties(env)
        # Module M3: Freight Properties
        sim, env = M3_Freight_Prop.freight_properties(sim, env)
        # Module M5: Building Environment
        env = M5_Env_Static.static_env(env)

        # <>
        # No Manipulation
        sim.betos_manipulation_cons = 0
        sim.betos_manipulation_time = 0
        sim.betos_manipulation_charge = 0
        # Initialization
        sim = M84_Oneday_Simulation.initialization(env, sim)
        sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
        sim = M82_DrivingSim.driving_sim(sim, vehicle, env)

        # save results
        result_time_loss[iter] = (sum(sim.rest_time_dis)/3600)
        result_distance[iter] = env.route_array_distance[-1]/1000
        result_energy_consumption[iter] = sum(sim.energy_cons_dis)/sim.dis_steps/3600

    return result_time_loss


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# EEPS Simulation Task
# Time loss over distance and charging power for one battery truck equipped with 500 kWh of battery size
def eeps_task():
    # Battery Size definition
    battery_size = 500  # in kWh
    # Range of available charging power
    range_power = np.array([400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
    # Range of transport tasks
    range_trip = np.array([400, 450, 500, 550, 600, 650, 700])
    # Number of Sim runs
    sim_runs = 20
    # Initialize results
    result_time_loss = np.zeros((sim_runs, len(range_trip)))
    i = 0
    for trip in range_trip:
        for iter in range(0, sim_runs):
            # Object Def
            vehicle, env, sim = M84_Oneday_Simulation.object_def()
            # Module M1: Vehicle Properties
            vehicle = M1_Veh_Prop.vehicle_properties(vehicle)
            # Set Combination
            vehicle.battery_capacity = battery_size
            # Module M2: Environment Properties
            env = M2_Env_Prop.environment_properties(env)
            # Module M3: Freight Properties
            env.trip_length = trip
            sim, env = M3_Freight_Prop.freight_properties(sim, env)
            # Module M4: Vehicle Building
            vehicle = M4_Veh_Static.static_vehicle_model(sim, vehicle, env)
            # Initialization Simulation parameter
            # Module M2: Environment Properties
            env = M2_Env_Prop.environment_properties(env)
            # Module M3: Freight Properties
            sim, env = M3_Freight_Prop.freight_properties(sim, env)
            # Module M5: Building Environment
            env = M5_Env_Static.static_env(env)

            # <>
            # No Manipulation
            sim.betos_manipulation_cons = 0
            sim.betos_manipulation_time = 0
            sim.betos_manipulation_charge = 0
            # Initialization
            sim = M84_Oneday_Simulation.initialization(env, sim)
            sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
            sim = M82_DrivingSim.driving_sim(sim, vehicle, env)
            # M12_Visualization.visualizsation_single_task(sim, vehicle, env)

            # save results
            result_time_loss[iter, i] = max(0, (sum(sim.rest_time_dis) / 3600) - 0.75)
        # Update Size
        i = i + 1
    # store results
    np.savetxt('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_600_rb_100.csv', result_time_loss, delimiter=",")

    return


# Simulation Task to evaluate BETOS performance on occupied charging stations
def sim_task_betos_occ_poi(a):

    # Object Def
    vehicle, env, sim = M84_Oneday_Simulation.object_def()
    # Module M1: Vehicle Properties
    vehicle = M1_Veh_Prop.vehicle_properties(vehicle)
    # Module M2: Environment Properties
    env = M2_Env_Prop.environment_properties(env)
    # Module M3: Freight Properties
    sim, env = M3_Freight_Prop.freight_properties(sim, env)
    # Module M4: Vehicle Building
    vehicle = M4_Veh_Static.static_vehicle_model(sim, vehicle, env)
    # Module M5: Building Environment
    env = M5_Env_Static.static_env(env)

    # <>
    # No Manipulation # Benchmark
    sim.betos_manipulation_cons = 0
    sim.betos_manipulation_time = 0
    sim.betos_manipulation_charge = 0
    # Initialization
    sim = M84_Oneday_Simulation.initialization(env, sim)
    sim = M91_Prediction.betos_prediction_energy_consumption(sim, vehicle, env)
    sim = M82_DrivingSim.driving_sim(sim, vehicle, env)
    # M12_Visualization.visualizsation_single_task(sim, vehicle, env)

    # Save in results variables
    if sim.betos_run_empty == 0:
        result_time = sum(sim.time_time) / 3600  # in h
        result_stops = sim.betos_stops
        result_discharge = sim.betos_deep_discharge
        pure_driving_time = sum(sim.time_dis)/3600
        if pure_driving_time > 9:
            result_time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600) - 1.5  # in h
        else:
            result_time_loss = (((sum(sim.rest_time_dis)) + (1-sim.betos_re_park) * (sum(sim.wait_time_dis))) / 3600) - 0.75  # in h
        result_wait_count = sim.betos_wait_count
        result_mean_availability_of_poi = np.mean(sim.betos_poi_availability[sim.betos_poi_availability > 0])
        result_mean_power = np.mean(sim.betos_power[sim.betos_power > 0])
        result_prediction_error_energy = ((sum(sim.energy_cons_dis)/sim.dis_steps/3600)-(sum(sim.betos_energy_cons_dis_prediction)/sim.dis_steps/3600))/(sum(sim.energy_cons_dis)/sim.dis_steps/3600)
    else:
        result_time = np.nan  # in h
        result_stops = np.nan
        result_discharge = np.nan
        result_time_loss = np.nan  # in h
        result_wait_count = np.nan
        result_mean_availability_of_poi = np.nan
        result_mean_power = np.nan
        result_prediction_error_energy = np.nan


    return result_time, result_stops, result_discharge, result_time_loss, result_wait_count, result_mean_availability_of_poi, result_mean_power, result_prediction_error_energy
    # return result_time_loss, result_discharge, result_stops, result_mean_power


# Postprocessing for Multiprocessing
def postprocess_multi(results):
    # Array
    res_array = np.array(results)
    # Extract
    result_time = res_array[:, 0]
    result_stops = res_array[:, 1]
    result_discharge = res_array[:, 2]
    result_time_loss = res_array[:, 3]
    result_wait_count = res_array[:, 4]
    result_mean_availability_of_poi = res_array[:, 5]
    result_mean_power = res_array[:, 6]
    result_prediction_error = res_array[:, 7]

    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_time_s3.csv', result_time, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_stops_s3.csv', result_stops, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_discharge_s3.csv', result_discharge, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_time_loss_s3.csv', result_time_loss, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_wait_count_s3.csv', result_wait_count, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_ava_poi_s3.csv', result_mean_availability_of_poi, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_power_s3.csv', result_mean_power, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/repark/Scenario_3/result_error_energy_s3.csv', result_prediction_error, delimiter=",")

    return


# Postprocessing for Multiprocessing
def postprocess_multi_sx(results):
    # Array
    res_array = np.array(results)
    # Extract
    result_time_loss_min = res_array[:, 0]
    result_power = res_array[:, 1]
    result_stops = res_array[:, 2]
    result_wait = res_array[:, 3]

    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Review/Section_41/result_time_loss_500_2000.csv', result_time_loss_min, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Review/Section_41/result_power_500_2000.csv', result_power, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Review/Section_41/result_stops_500_2000.csv', result_stops, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Review/Section_41/result_wait_500_2000.csv', result_wait, delimiter=",")


    return


# Post Process Prediction Task
def postprocess_multi_px(results):
    # Array
    res_array = np.array(results)
    # Extract
    result_time_loss = res_array[:, 0, :]
    result_discharge = res_array[:, 1, :]
    result_stops = res_array[:, 2, :]
    result_mean_power = res_array[:, 3, :]

    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_stops_s3.csv', result_stops, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_discharge_s3.csv', result_discharge, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s3.csv', result_time_loss, delimiter=",")
    np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s3.csv', result_mean_power, delimiter=",")

    return


# Optimizing the Journey Section 4.1:
# 1: Comparision BETOS Driver for different systems designs
def sim_section_4_1_sd(a):
    # Define battery capacity in kWh
    battery_capacity = 500
    # Get all scenarios regarding Infrastructure
    s400, s600, s800, s1000, s1200, s1400, s1600, s1800, s2000 = \
        scenario_definition.scenario_sec41(battery_capacity=battery_capacity)
    # Simulate one scenario with multiprocessing
    sim, env, results = M84_Oneday_Simulation.oneday_sim(scenario=s2000)
    time_loss_min = results['time_loss_min']
    power_mean = results['power_chosen_avg_kw']
    stops = results['number_stops']
    wait_count = results['number_wait_events']


    return time_loss_min, power_mean, stops, wait_count


# Optimizing the Journey Section 42/3:
# 1: Comparision BETOS Driver for different systems designs
def sim_section_4_2_3(a):
    # Get all scenarios regarding Infrastructure
    s1, s2, s3, s4, s31, s32, s33, s34, s41, s42, s43, s44, s45, s46, s47 = scenario_definition.scenario_betos_sec42()
    # Simulate one scenario with multiprocessing
    sim, env, results = M84_Oneday_Simulation.oneday_sim(scenario=s1)
    time_loss_min = results['time_loss_min']
    power_mean = results['power_chosen_avg_kw']
    stops = results['number_stops']
    wait_count = results['number_wait_events']


    return time_loss_min, power_mean, stops, wait_count