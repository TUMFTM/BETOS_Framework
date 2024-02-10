# _________________________________
# BET.OS Function #
# Operation Scenario Block #
# Designed by MX-2022-05-20
# Function Description
# Preparation of Synthetic Operation Scenario (Velocity profile over time) for Usage in Simulation Environment
# Part of the Freight Module
# _________________________________

import pandas
import numpy as np
from scipy.signal import savgol_filter
from Modules.M3_Freight_Properties import M31_CreateTracks

# Sources:
# Data for Cycle Generation from NEFTON Research Project
# Driving Cycle Generation: Zaehringer et al.: "Compressed Driving Cycles using Markov Chains for
# Vehicle Powertrain Design"


# Main Function of ROUTE Model____
def freight_model(env, scenario):
    # Load Freight Cycle
    #route_array_speed, route_array_distance, route_array_stoptime, route_array_slope = M31_CreateTracks.get_tracks()
    route_array_distance, route_array_speed, route_array_stoptime, route_array_slope = M31_CreateTracks.build_route_from_tracks(env, scenario)
    #route_array_distance, route_array_speed, route_array_stoptime = route_read_cycle()

    return route_array_distance, route_array_speed, route_array_stoptime, route_array_slope
# _________________________________


# Function for Reading Driving Cycle from CSV Profile and transformation in Distance based Profile
def route_read_cycle():
    # Read Data from Driving cycle
    raw_data = pandas.read_csv("OperationScenario/Scenario_Library/Cycle5.csv", header=None)
    array_raw_data = raw_data.to_numpy()
    array_time_raw = array_raw_data[:, 0]               # in sec
    array_speed_raw = array_raw_data[:, 1]/3.6          # in m/s
    duration_cycle = int(array_time_raw[-1])            # Get last element in array
    array_stoptime_raw = array_raw_data[:, 4]           # in sec
    # __________________________________________________________________________________________________________________
    # Read Data from Track Database
    #raw_data = pandas.read_pickle("Modules/M3_Freight_Properties/M3_TruckMobility_Database/track_1500000410194.pkl")
    # speed = raw_data[4][speed].to_numpy()
    # __________________________________________________________________________________________________________________
    # Get alpha profile over time


    # Calculate distance profile over time
    i = 0
    array_distance_raw = np.zeros(duration_cycle)
    while i < duration_cycle-1:
        # Set velocity exactly zero in the area of zer0
        if array_speed_raw[i] <= 0.01:
            array_speed_raw[i] = 0.0

        array_distance_raw[i+1] = array_distance_raw[i] + ((array_speed_raw[i+1] + array_speed_raw[i])/2) * \
                                  (array_time_raw[i+1] - array_time_raw[i])
        # Update Variable
        i = i+1

    # Get Total Distance of Cycle
    distance_cycle = int(round(array_distance_raw[-1], 0))   # in m

    # Initialize distancebased Variables
    array_speed_distancebased_raw = np.zeros(distance_cycle)
    array_distance_distancebased = np.zeros(distance_cycle)
    array_stoptime_distancebaseed = np.zeros(distance_cycle)

    # Safe Velocity in each Meter Step for distance based Variables
    dis = 0
    k = 0

    while dis < distance_cycle:
        while dis < round(array_distance_raw[k], 0):
            array_speed_distancebased_raw[dis] = array_speed_raw[k]
            array_distance_distancebased[dis] = dis
            dis = dis + 1
        k = k + 1

    # Stoptime Extraction
    r = 0
    while r < duration_cycle:
        if array_stoptime_raw[r] > 0:
            dis = int(round(array_distance_raw[r], 0))
            # Safe Stoptime
            if dis == distance_cycle:
                dis = dis-1
            array_stoptime_distancebaseed[dis-1] = array_stoptime_raw[r]
            # Set Velocity to Zero while Stop
        r = r+1

    # Distancebased Variable
    route_array_distance = array_distance_distancebased
    route_array_speed = array_speed_distancebased_raw
    route_array_stoptime = array_stoptime_distancebaseed
    # Smooth Driving Profile due to high frequency in original driving cycle. Using 5th order, moving window with
    # window size of 100 (Savitzky-Golay Filtering)
    route_array_speed = savgol_filter(route_array_speed, window_length=201, polyorder=3)
    # Check Velocity in Stoppoints
    for i in range(distance_cycle):
        if route_array_stoptime[i] > 0:
            route_array_speed[i] = 0

    return route_array_distance, route_array_speed, route_array_stoptime
