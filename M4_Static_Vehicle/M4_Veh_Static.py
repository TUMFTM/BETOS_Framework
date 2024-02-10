# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-08-29
#
# Function Description
# Part of the Static Vehicle Modul M4
# Main file of the Static vehicle modul: Definition if vehicle mass and powertrain properties
# _________________________________

# import functions
import numpy as np
import pandas

# Used sources in this file
# Verbruggen et al.:
# Fries et al.:
# Naunheimer, Fahrzeuggetriebe, 2019, 3.Edition
# König et al.:

def static_vehicle_model(sim, vehicle, env):
    # <>
    # Definition of Vehicle Mass
    # Trailer
    mass_trailer = 7500  # kg Verbruggen et al.
    # Tractor without powertrain
    mass_tractor_no_pt = 5400  # kg Verbruggen et al.
    # Allowed Gross vehicle weight
    mass_GVW_max = 42000  # kg CO2 Option +2t here considered
    # Powertrain Density Properties_____________________________________________________________________________________
    # EM
    mass_den_em = 0.5  # kg/kW Fries et al.
    # Gear total mass
    mass_gear = 0.18 * ((vehicle.gear_ratio * vehicle.em_t_max) ** 0.684) * (1 ** 0.342)  # kg/Nm Naunheimer.
    # Power Electronics
    mass_den_pe = 1 / 12.8  # kg/kW Fries et al.
    # Battery
    mass_den_bat_pack = 165  # Wh/kg Audi Etron --> König et al.
    # vehicle_mass.den_bat_pack = 202  # Wh/kg Mercedes EQXX
    # __________________________________________________________________________________________________________________
    # Calcualtion of Powertrain mass
    # Battery Pack
    mass_battery_pack = vehicle.battery_capacity * 1000 / mass_den_bat_pack
    # Electric Machine
    mass_em = mass_den_em * vehicle.em_p_max
    # HV Path from Motor to Battery
    mass_pe = mass_den_pe * vehicle.em_p_max
    # __________________________________________________________________________________________________________________
    # Calcualtion of BET Tractor Mass
    mass_tractor = mass_tractor_no_pt + mass_gear + mass_em + mass_battery_pack + mass_pe
    # Calcualtion of Whole vehicle
    vehicle.mass_total = mass_trailer + (env.freight_payload*1000) + mass_tractor  # in kg
    #___________________________________________________________________________________________________________________
    # <>
    # Vehicle Charging Map
    vehicle = vehicle_charging_time_map(vehicle, env)
    vehicle = charging_map_calc(sim, vehicle, env)

    return vehicle


# Calculation of Vehicle Charging Time Map
# Save time for Charging from 0% SoC to 100% SoC in Percent steps for each charging station type
# vehicle.charging_time[0,0] = time for charging from 0 to 1 % SoC for PoI Type 1
def vehicle_charging_time_map(vehicle, env):
    # Initialize Charging Time Map Vector
    vehicle.charging_time_map = np.zeros((100, len(env.cs_data_power)-1))
    # Index
    i = 0
    # Iteration over charging amount
    while i < 100:
        for type in range(1, len(env.cs_data_power)):
            # Charging Power from Station
            charging_power_poi = env.cs_data_power[type]
            # Possible Charging Rate Vehicle
            c_rate = vehicle.cell_c_rate_func(i)
            # Possible Charging Power Vehicle
            charging_power_veh = c_rate * vehicle.battery_capacity
            # Charging Power
            charging_power = min(charging_power_veh, charging_power_poi)
            # Charging time for one Percent step
            vehicle.charging_time_map[i, type-1] = ((vehicle.battery_capacity / 100) / charging_power) * 3600  # in sec

        # Index Update
        i = i + 1

    return vehicle

# ______________________________________________________________________________________________________________________
# <> Only for Dynamic Programming Strategy Approach
# Calculation of Charging Map: What is the target SOC after charging from given SoC for different charging times
# specified in decision_1_charge. Only Used for Dynamic Programming Approach
def charging_map_calc(sim, vehicle, env):
    '''
    # <>
    # Calculate new map
    # Maximum Charging time in case of 0 to 100 % at slowest charger
    #env.cs_data_power = np.array([0, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
    env.cs_data_power = np.array([0, 150, 350, 700, 1000, 1500])
    #env.cs_data_power = np.array([0, 200, 250, 300, 450, 550, 650, 750, 850, 900, 950, 1050, 1100, 1150, 1250, 1300, 1350, 1450])
    slowest_charger = int(np.argmax(vehicle.charging_time_map[0, :]))
    max_charging_time = sum(vehicle.charging_time_map[:, slowest_charger])
    decision_1_charge = np.ceil(np.linspace(0, 100*60, num=101))  # Use 100 decisions
    # Dimension of map
    n_types = len(env.cs_data_power)
    n_soc = 101  # from 0 to 100% in 1% steps
    n_charging_times = len(decision_1_charge)
    # Initialize Charging Map
    charging_map = np.zeros((n_types, n_soc, n_charging_times))
    # Fill in charging map
    for i in range(0, n_types):
        for j in range(0, n_soc):
            for k in range(0, n_charging_times):
                if k > 0:
                    charging_time = int(decision_1_charge[k]) - int(decision_1_charge[k-1])
                    soc = charging_map[i, j, k-1]
                else:
                    charging_time = int(decision_1_charge[k])
                    soc = j
                # Init soc
                # Iteration over one second time steps
                if charging_time > 0:
                    for l in range(0, charging_time+1):
                        # Charging Power
                        p_charge = (min(env.cs_data_power[i], (vehicle.cell_c_rate_func(min(100, soc)) * vehicle.battery_capacity))) * vehicle.battery_charge_loss
                        # p_charge = env.cs_data_power[i]
                        # New soc
                        if soc < 100:
                            soc = soc + ((((p_charge * 1)/3600) / vehicle.battery_capacity) * 100)  # one second of charge
                        else:
                            soc = 100
                # SOC after charging
                charging_map[i, j, k] = soc  # Use Integer for charging map
    # Safe in vehicle object
    vehicle.charging_map = charging_map
    # <>
    # Save Charging Map
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_0_1.csv', charging_map[0, :, :], delimiter=",")
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_150_1.csv', charging_map[1, :, :], delimiter=",")
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_350_1.csv', charging_map[2, :, :], delimiter=",")
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_700_1.csv', charging_map[3, :, :], delimiter=",")
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_1000_1.csv', charging_map[4, :, :], delimiter=",")
    np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_355_1500_1.csv', charging_map[5, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_850_1400_3.csv', charging_map[6, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_800_1600_3.csv', charging_map[7, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_800_1800_3.csv', charging_map[8, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_800_2000_3.csv', charging_map[9, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_500_1400_2.csv', charging_map[10, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_500_1500_2.csv', charging_map[11,:,:], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_500_1600_2.csv', charging_map[12, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_500_1800_2.csv', charging_map[13, :, :], delimiter=",")
    #np.savetxt('Modules/M1_Vehicle_Properties/Charging_Maps/c_map_500_2000_2.csv', charging_map[14, :, :], delimiter=",")
    # <>
    # Existing Charging Maps
    map_exist_battery = np.array([300, 350, 400, 450, 500, 550, 600, 650, 700])
    map_exist_power = np.array([0, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950,
                                1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350,  1400, 1450, 1500, 1600, 1800, 2000])
    map_exist_crate = np.array([1, 2, 3])
    '''
    # Building string of Map path
    str1 = 'Modules/M1_Vehicle_Properties/Charging_Maps/c_map_'
    str2 = '_'
    str3 = '.csv'
    # How many maps: Number of different chargers along the route
    n_maps = len(env.cs_data_power)
    # Initialize Charging Map
    charging_map = np.zeros((n_maps, 101, 101))
    # Load Maps
    for i in range(0, n_maps):
        # Build string
        string = str1 + str(int(vehicle.battery_capacity) - (int(vehicle.battery_capacity) % 5)) + \
                 str2 + str(int(env.cs_data_power[i])) + str2 + \
                 str(vehicle.battery_c_rate_max) + str3
        c_map = pandas.read_csv(string, delimiter=None, header=None).to_numpy()
        charging_map[i, :, :] = c_map

    # In vehicle object
    vehicle.charging_map = charging_map

    # Read Maps, that are dependent from Temperature:
    #str_1 = 'Modules/M1_Vehicle_Properties/Charging_Maps/c_map_'
    #str_2 = '_'
    #str_3 = '.csv'
    #str_4 = 'winter'
    #str_5 = 'summer'


    return vehicle

