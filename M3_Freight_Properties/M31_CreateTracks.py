# _________________________________
# BET.OS Function #
# Operation Scenario Block #
# Designed by MX-2023-02-03
# Function Description
# Preparation Truck Tracks from Smart Mobility Database
# Part of the Freight Module
# _________________________________

# import functions

# import libraries
import pandas
import numpy as np
from scipy.signal import savgol_filter
import sqlalchemy
import random as rd

# ______________________________________________________________________________________________________________________
# Read Tracks from SQL Database
def get_tracks():
    # Create SQL Engine
    # JurmMc2Jjj4uCJpckhf
    # create database connection and query data
    engine = sqlalchemy.create_engine('postgresql://{username}:{password}@{url}:{port}/{db_name}'.format(
        username='ftm_asc_zaehringer',
        url='postgres-sm.ftm.mw.tum.de',
        password='JurmMc2Jjj4uCJpckhf',
        db_name='mobtrack',
        port=5432))
    # __________________________________________________________________________________________________________________
    # Get Track ID for one Vehicle ID
    # trips are stored in anon_master (this is just a join of (materialized) views anon_*
    df_trips = pandas.read_sql(
        '''SELECT * from track.track t 
        join track.track_metadata tm on t.id = tm.track_id
        where vehicle_id = 1700000748
        and tm.distance > 100000''', con=engine)
    track_id_array = df_trips.track_id[:].to_numpy()
    array_distance = df_trips.distance[:].to_numpy()

    # Get Single Tracks for each Track ID (For Loop over Track ID)
    track_info = np.zeros((len(track_id_array), 2))
    for id in range(0,len(track_id_array)):
        sql_string_1 = "SELECT _time as time, altitude, speed from ftm_reduced_gps_from_track_id("
        sql_string_2 = str(track_id_array[id])
        sql_string_3 = ", 1)"
        sql = sql_string_1 + sql_string_2 + sql_string_3
        track = pandas.read_sql(sql, con=engine, index_col='time')
        speed_profile = track.speed.to_numpy()
        altitude_profile = track.altitude.to_numpy()
        altitude_profile_filter = savgol_filter(altitude_profile, window_length=1001, polyorder=4)
        track_duration = len(speed_profile)
        # <>
        # Calculate Alpha over Time
        # alpha = asin(h2-h1/(((v2+v1)/2)*t)
        h1= altitude_profile_filter[0:len(altitude_profile)-1]
        h2= altitude_profile_filter[1:len(altitude_profile)]
        v1= speed_profile[0:len(speed_profile)-1]
        v2= speed_profile[1:len(speed_profile)]
        alpha_reduced = ((h2-h1)/(((v2+v1)/2)*1)) * 100  # in %
        alpha_array = np.concatenate([alpha_reduced, np.array([0])])
        alpha_array =np.nan_to_num(alpha_array)
        # <>
        # Calculate Distancebased Track
        # Calculate Distance over time
        i = 0
        array_distance_raw = np.zeros(track_duration)
        while i < track_duration - 1:
            # Set velocity exactly zero in the area of zer0
            if speed_profile[i] <= 1 and speed_profile[i+1] <= 1:
                speed_profile[i] = 0.0
                speed_profile[i+1] = 0.0

            array_distance_raw[i + 1] = array_distance_raw[i] + ((speed_profile[i + 1] + speed_profile[i]) / 2) * 1  # 1Hz Sample
            # Update Variable
            i = i + 1
        # Get Total Distance of Cycle
        distance_cycle = int(np.floor(array_distance_raw[-1]))  # in m
        # Floor array_distance raw
        array_distance_raw = np.floor(array_distance_raw)
        # Initialize distancebased Variables
        array_speed_distancebased_raw = np.zeros(distance_cycle)
        array_distance_distancebased = np.zeros(distance_cycle)
        array_stoptime_distancebaseed = np.zeros(distance_cycle)
        array_slope_distancebased = np.zeros(distance_cycle)

        # Safe Velocity in each Meter Step for distance based Variables
        dis = 0
        k = 0

        while dis < distance_cycle:
            while dis < array_distance_raw[k]:
                array_speed_distancebased_raw[dis] = speed_profile[k]
                if speed_profile[k] <= 3:
                    array_slope_distancebased[dis] = 0
                else:
                    array_slope_distancebased[dis] = alpha_array[k]
                array_distance_distancebased[dis] = dis
                dis = dis + 1
            k = k + 1

        # Distancebased Variable
        route_array_distance = array_distance_distancebased
        route_array_speed = array_speed_distancebased_raw
        route_array_stoptime = array_stoptime_distancebaseed
        route_array_slope = array_slope_distancebased
        # Smooth Speed Profile
        route_array_speed = savgol_filter(route_array_speed, window_length=101, polyorder=3)
        route_array_speed = np.maximum(route_array_speed, 0)  # No negative Speed due to Filter function
        # Check Speed Profile
        route_array_speed[(route_array_speed == 0)] = 1/3.6

        # <>
        # Store Track in TruckMobilityDatabase
        track = np.zeros((len(route_array_distance),4))
        track[:, 0] = route_array_distance
        track[:, 1] = route_array_speed
        track[:, 2] = route_array_slope
        track[:, 3] = route_array_stoptime
        save_string = ["Modules/M3_Freight_Properties/M3_TruckMobility_Database/track_1700000748_",".txt"]
        fill = str(id)
        np.savetxt(fill.join(save_string), track)

        # Additional Information about Tracks like total Distance and Average Speed
        track_info[id, 0] = route_array_distance[-1]  # Distance in m
        track_info[id, 1] = np.mean(route_array_speed)

    # Save Add Info
    np.savetxt("Modules/M3_Freight_Properties/M3_TruckMobility_Database/track_1700000748_Info.txt", track_info)


    return route_array_speed, route_array_distance, route_array_stoptime, route_array_slope


# Build Route from Tracks from Mobility Database
def build_route_from_tracks(env, scenario):
    # Define Minimum length of tour  # in km
    env.trip_length = scenario['trip_length'][0]
    route_length = (env.trip_length-25)*1000  # in Meter
    route_length_max = (env.trip_length+25)*1000  # in Meter
    # Initialize Tour Length
    tour = 0
    # Get random tracks from database while minimum length isn't reached
    while tour < route_length:
        new = 0
        # Get random track id
        id = rd.randint(0, 180)
        # Read Track
        whichtxt = str(id)
        string = ["Modules/M3_Freight_Properties/M3_TruckMobility_Database/track_1700000748_",".txt"]
        track = np.loadtxt(whichtxt.join(string))
        track[-1, 1] = 0.5  # Set speed in last point of microtrip to near zero
        # Stack Track on tour
        if tour == 0:
            tour_distance = track[:, 0]
            tour_speed = track[:, 1]
            tour_slope = track[:, 2]
            tour_stoptime = track[:, 3]
        else:
            stack = np.array(track[1:-1, 0]+int(tour_distance[-1]))
            tour_distance_test = np.concatenate([tour_distance, stack])
            # Check for max Length ouf tour
            if tour_distance_test[-1] < route_length_max:
                tour_distance = np.concatenate([tour_distance, stack])
                tour_speed = np.concatenate([tour_speed, track[1:-1, 1]])
                tour_slope = np.concatenate([tour_slope, track[1:-1, 2]])
                tour_stoptime = np.concatenate([tour_stoptime, track[1:-1, 3]])
            else:
                new = 1
        # Get total tour length
        tour = tour_distance[-1]
        if new == 1:
            tour = 0

    # Return Variables
    route_array_distance = tour_distance
    route_array_speed = tour_speed
    route_array_stoptime = tour_stoptime
    route_array_slope = tour_slope

    return route_array_distance, route_array_speed, route_array_stoptime, route_array_slope