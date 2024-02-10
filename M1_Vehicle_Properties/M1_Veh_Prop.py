# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-06-14
#
# Function Description
# Part of the Vehicle Properties M1
# Definition of Vehicle Concept Properties
# _________________________________


# import functions:
import numpy as np
import pandas
from scipy.interpolate import interp1d
from scipy.interpolate import interp2d

# Used sources in this file:
# Earl et al.: Vehicle Parameters
# Wolff et al.: Vehicle Parameters
# Kalt et al.: Electric Maschine Parameters
# Wassiliadis et al.: Charging Profile
# Schmalstieg et al.: Battery Data


def vehicle_properties(vehicle, scenario):
    # Driver Properties
    # Mandatory Rest Time
    veh_mandatory_rest_time = 45  # in min
    # Time to connect vehicle to charging station (counts for rest)
    veh_connecting_time = 3*60  # in sec
    # Time to search for parking space (counts not for rest)
    veh_rest_space_time = 3*60  # in sec
    # Total allowed driving time per day
    veh_driving_time_max = 9*60*60  # in sec
    # Maximum daily driving distance
    veh_max_distance_day = scenario['max_daily_distance'][0] * 1000 # in m

    # Vehicle Concept Properties
    # Drag Coefficient Earl et al. 0.6, Discussion with MAN according to aerodynamic potential 0.55
    veh_cw = 0.55
    # Front Area (Earl et al.) in m^2
    veh_af = 10
    # Air density (Earl et al.)
    veh_roh_air = 1.2
    # Gravimetric acceleration
    veh_g_force = 9.81
    # Rolling resistance (Earl et al.) 0.0055, Discussion with MAN 0.0050
    veh_c_rr = 0.0050
    # Tire radius (Wolff et al.)
    veh_r_dyn = 0.47 * 0.95
    # Auxiliary Consumption in kW
    veh_aux_cons = 4  # kW  # Internal Discussion MAN Truck and Bus SE
    # __________
    # Battery Data
    # Battery Capacity in kWh
    veh_battery_capacity = scenario['battery_capacity'][0]  # in kWh
    # Battery Cell Type
    veh_battery_cell_type = scenario['cell_chemistry'][0]
    # Maximum (Dis)Charging Rate
    veh_battery_c_rate_max = scenario['c_rate'][0]
    # Get Cell Data from Cell Properties Function in this File
    veh_cell_r_i_func, veh_cell_ocv_func, veh_cell_c_rate_func = cell_properties(veh_battery_cell_type,
                                                                                 veh_battery_c_rate_max)
    # Maximum Discharge Level
    veh_battery_soc_min = scenario['min_soc'][0]
    # Maximum Charge Level
    veh_battery_soc_max = scenario['max_soc'][0]
    # Battery Buffer
    veh_battery_soc_buffer = 0.05
    # Charging Loss
    veh_battery_charging_loss = 0.9
    # __________
    # Powertrain Data
    # Power Electronics Efficiency
    veh_pe_efficiency = 0.98
    # Motor Efficiency (Alternative Efficiency Map to be defined, yet the Calculation is done with fixed value)
    veh_em_efficiency = 0.95
    # Motor Max Torque in Nm
    veh_em_t_max = 2018
    # Motor Max Torque over Speed
    veh_em_torque_func = electric_maschine_propteries()
    # Motor Max Power in kW
    veh_em_p_max = 1906
    # Gear Ratio
    veh_gear_ratio = 17
    # Gear Efficiency (Mareev et al.)
    veh_gear_efficiency = 0.94
    # Gear Lambda
    veh_gear_lambda = 1.0
    # Maximum Brake Force in N
    veh_brake_force = 225000  # N (22.5 t of axleload (truck), friction = 1-->max. pos. brake force 22.500*1*9.81m/s^2)
    # Maximum Deceleration
    veh_acc_maximum = -2.0  # m/s^2
    # __________
    # Store all Properties in one Veh Object from Veh class
    vehicle.mandatory_rest_time = veh_mandatory_rest_time
    vehicle.connecting_time = veh_connecting_time
    vehicle.rest_space_time = veh_rest_space_time
    vehicle.driving_time_max = veh_driving_time_max
    vehicle.max_day_distance = veh_max_distance_day
    vehicle.cw = veh_cw
    vehicle.af = veh_af
    vehicle.roh_air = veh_roh_air
    vehicle.g_force = veh_g_force
    vehicle.c_rr = veh_c_rr
    vehicle.r_dyn = veh_r_dyn
    vehicle.aux_cons = veh_aux_cons
    vehicle.battery_capacity = veh_battery_capacity
    vehicle.cell_type = veh_battery_cell_type
    vehicle.battery_c_rate_max = veh_battery_c_rate_max
    vehicle.cell_r_i_func = veh_cell_r_i_func
    vehicle.cell_ocv_func = veh_cell_ocv_func
    vehicle.cell_c_rate_func = veh_cell_c_rate_func
    vehicle.battery_soc_min = veh_battery_soc_min
    vehicle.battery_soc_max = veh_battery_soc_max
    vehicle.battery_soc_buffer = veh_battery_soc_buffer
    vehicle.battery_charge_loss = veh_battery_charging_loss
    vehicle.pe_efficiency = veh_pe_efficiency
    vehicle.em_efficiency = veh_em_efficiency
    vehicle.em_t_max = veh_em_t_max
    vehicle.em_torque_func = veh_em_torque_func
    vehicle.em_p_max = veh_em_p_max
    vehicle.gear_ratio = veh_gear_ratio
    vehicle.gear_efficiency = veh_gear_efficiency
    vehicle.gear_lambda = veh_gear_lambda
    vehicle.brake_force = veh_brake_force
    vehicle.acc_max = veh_acc_maximum

    return vehicle


# Definition of cell properties:
def cell_properties(veh_battery_cell_type, veh_battery_c_rate_max):
    # In case if Schmalstieg Cell (NMC)
    if veh_battery_cell_type <= 1:
        # Nominal cell capacity in Ah
        cell_Qnom = 2.05
        # Nominal cell voltage in V
        cell_Unom = 3.6
        # Minimal cell voltage in V
        cell_Umin = 3.0
        # Maximum cell voltage in V
        cell_Umax = 4.2
        # Maximum charging current in A
        cell_Imax_cont = 2.05
        # Maximum discharge current in A
        cell_Imin_cont = -6.15
        # Heat Capacity Cell Forgez et al.
        cell_T_cap_cell = 76.27
        # Thermal resistance between cell and Housing
        cell_R_th_in = 3.3
        # Cell Start Temperature
        cell_start_temp = 25
        # Internal Resistance Function
        R_i_table = [[0.0985033420000000, 0.0673441220000000, 0.0552824880000000, 0.0472413990000000, 0.0412105820000000,
                  0.0381951740000000],
                 [0.0934776620000000, 0.0673441220000000, 0.0552824880000000, 0.0462362630000000, 0.0412105820000000,
                  0.0392003100000000],
                 [0.0924725250000000, 0.0673441220000000, 0.0542773520000000, 0.0472413990000000, 0.0412105820000000,
                  0.0392003100000000],
                 [0.0914673890000000, 0.0663389860000000, 0.0552824880000000, 0.0472413990000000, 0.0402054460000000,
                  0.0361849010000000],
                 [0.0924725250000000, 0.0693543940000000, 0.0522670800000000, 0.0442259900000000, 0.0422157180000000,
                  0.0381951740000000],
                 [0.0914673890000000, 0.0683492580000000, 0.0532722160000000, 0.0452311270000000, 0.0392003100000000,
                  0.0361849010000000],
                 [0.0934776620000000, 0.0673441220000000, 0.0522670800000000, 0.0432208540000000, 0.0402054460000000,
                  0.0361849010000000],
                 [0.0894571170000000, 0.0683492580000000, 0.0542773520000000, 0.0452311270000000, 0.0392003100000000,
                  0.0381951740000000],
                 [0.0864417090000000, 0.0653338490000000, 0.0492516710000000, 0.0432208540000000, 0.0392003100000000,
                  0.0341746290000000]]
        x_value = [-10, 0, 10, 20, 30, 40]
        y_value = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        cell_r_i_func = interp2d(x_value, y_value, R_i_table, kind='linear')
        # Open Circuit Voltage Function
        points = [0, 0.00696136400000000, 0.0139227290000000, 0.0208840930000000, 0.0278454580000000, 0.0348068220000000,
              0.0417681870000000, 0.0487295510000000, 0.0556909150000000, 0.0626522800000000, 0.0696136440000000,
              0.0765750090000000, 0.0835363730000000, 0.0904977380000000, 0.0974591020000000, 0.104420466000000,
              0.111381831000000, 0.118343195000000, 0.125304560000000, 0.132265924000000, 0.139227289000000,
              0.146188653000000, 0.153150017000000, 0.160111382000000, 0.167072746000000, 0.174034111000000,
              0.180995475000000, 0.187956840000000, 0.194918204000000, 0.201879568000000, 0.208840933000000,
              0.215802297000000, 0.222763662000000, 0.229725026000000, 0.236686391000000, 0.243647755000000,
              0.250609119000000, 0.257570484000000, 0.264531848000000, 0.271493213000000, 0.278454577000000,
              0.285415942000000, 0.292377306000000, 0.299338670000000, 0.306300035000000, 0.313261399000000,
              0.320222764000000, 0.327184128000000, 0.334145493000000, 0.341106857000000, 0.348068221000000,
              0.355029586000000, 0.361990950000000, 0.368952315000000, 0.375913679000000, 0.382875044000000,
              0.389836408000000, 0.396797772000000, 0.403759137000000, 0.410720501000000, 0.417681866000000,
              0.424643230000000, 0.431604595000000, 0.438565959000000, 0.445527323000000, 0.452488688000000,
              0.459450052000000, 0.466411417000000, 0.473372781000000, 0.480334145000000, 0.487295510000000,
              0.494256874000000, 0.501218239000000, 0.508179603000000, 0.515140968000000, 0.522102332000000,
              0.529063696000000, 0.536025061000000, 0.542986425000000, 0.549947790000000, 0.556909154000000,
              0.563870519000000, 0.570831883000000, 0.577793247000000, 0.584754612000000, 0.591715976000000,
              0.598677341000000, 0.605638705000000, 0.612600070000000, 0.619561434000000, 0.626522798000000,
              0.633484163000000, 0.640445527000000, 0.647406892000000, 0.654368256000000, 0.661329621000000,
              0.668290985000000, 0.675252349000000, 0.682213714000000, 0.689175078000000, 0.696136443000000,
              0.703097807000000, 0.710059172000000, 0.717020536000000, 0.723981900000000, 0.730943265000000,
              0.737904629000000, 0.744865994000000, 0.751827358000000, 0.758788723000000, 0.765750087000000,
              0.772711451000000, 0.779672816000000, 0.786634180000000, 0.793595545000000, 0.800556909000000,
              0.807518274000000, 0.814479638000000, 0.821441002000000, 0.828402367000000, 0.835363731000000,
              0.842325096000000, 0.849286460000000, 0.856247825000000, 0.863209189000000, 0.870170553000000,
              0.877131918000000, 0.884093282000000, 0.891054647000000, 0.898016011000000, 0.904977376000000,
              0.911938740000000, 0.918900104000000, 0.925861469000000, 0.932822833000000, 0.939784198000000,
              0.946745562000000, 0.953706927000000, 0.960668291000000, 0.967629655000000, 0.974591020000000,
              0.981552384000000, 0.988513749000000, 0.995475113000000]
        u_ocv = [3.00077868000000, 3.14184953800000, 3.22649205300000, 3.28896629000000, 3.33934874000000, 3.37965469900000,
                3.41290711600000, 3.43709069100000, 3.45019012800000, 3.45925896900000, 3.46732016100000, 3.47235840600000,
                3.47739665100000, 3.48344254500000, 3.48747314100000, 3.49150373600000, 3.49654198100000, 3.50158022600000,
                3.50561082200000, 3.50964141800000, 3.51568731200000, 3.51871025900000, 3.52576380200000, 3.53080204700000,
                3.53684794100000, 3.54289383500000, 3.54793208000000, 3.55397797400000, 3.56002386800000, 3.56506211200000,
                3.57110800600000, 3.57513860200000, 3.58118449600000, 3.58420744300000, 3.58924568800000, 3.59327628400000,
                3.59529158200000, 3.59932217800000, 3.60133747600000, 3.60436042300000, 3.60738337000000, 3.61040631700000,
                3.61342926400000, 3.61645221100000, 3.61947515800000, 3.62149045600000, 3.62451340300000, 3.62652870100000,
                3.62955164800000, 3.63156694600000, 3.63458989300000, 3.63660519000000, 3.63962813700000, 3.64265108400000,
                3.64668168000000, 3.64970462700000, 3.65272757400000, 3.65474287200000, 3.65675817000000, 3.66078876600000,
                3.66381171300000, 3.66683466000000, 3.66985760700000, 3.67388820300000, 3.67791879900000, 3.67993409700000,
                3.68396469300000, 3.68799528900000, 3.69101823600000, 3.69504883200000, 3.69907942800000, 3.70311002400000,
                3.70814826800000, 3.71217886400000, 3.71620946000000, 3.72124770500000, 3.72527830100000, 3.73031654600000,
                3.73535479100000, 3.74140068500000, 3.74543128100000, 3.75046952600000, 3.75550777100000, 3.76155366500000,
                3.76759955900000, 3.77263780400000, 3.77767604900000, 3.78372194200000, 3.78976783600000, 3.79581373000000,
                3.80185962400000, 3.80790551800000, 3.81395141200000, 3.81999730600000, 3.82705084900000, 3.83309674300000,
                3.83914263700000, 3.84518853100000, 3.85224207300000, 3.85929561600000, 3.86634915900000, 3.87239505300000,
                3.87944859600000, 3.88750978800000, 3.89557098000000, 3.90161687400000, 3.90967806600000, 3.91673160900000,
                3.92277750300000, 3.93184634300000, 3.93789223700000, 3.94595342900000, 3.95401462100000, 3.96106816400000,
                3.96912935600000, 3.97618289900000, 3.98525174000000, 3.99230528300000, 4.00036647400000, 4.00641236800000,
                4.01548120900000, 4.02354240100000, 4.03361889100000, 4.03966478500000, 4.04873362600000, 4.05679481800000,
                4.06485601000000, 4.07392485000000, 4.08198604200000, 4.09206253200000, 4.09911607500000, 4.10616961800000,
                4.11020021400000, 4.11523845900000, 4.11826140600000, 4.12329965100000, 4.12733024700000, 4.13236849200000,
                4.13639908800000, 4.14042968300000, 4.14647557700000, 4.15050617300000, 4.15755971600000, 4.16562090800000]
        cell_ocv_func = interp1d(points, u_ocv, kind="linear")
        # Charging Rate function according to veh_battery_c_rate_max NMC (Wassiliadis et al. ID3 Tear Down)
        soc_values = [0, 10,
                      15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                      31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                      41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                      61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                      71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                      81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                      91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
        if veh_battery_c_rate_max == 1:
            charging_rate_values = [0.1, 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 1., 1., 1., 1., 1., 1., 1.,
                                    1., 1., 0.99, 0.932, 0.869, 0.803, 0.733, 0.667, 0.604,
                                    0.546, 0.489, 0.426, 0.357, 0.296, 0.25, 0.20, 0.17, 0.15,
                                    0.1]
        elif veh_battery_c_rate_max == 2:
            charging_rate_values = [0.1, 2., 2., 2., 2., 2.,
                                    2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                    2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                    2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                    2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                    2., 2., 2., 2., 2., 2., 2., 2., 2.,
                                    2., 2., 2., 1.976, 1.92, 1.864, 1.808, 1.75, 1.694,
                                    1.644, 1.588, 1.526, 1.468, 1.41, 1.354, 1.302, 1.242, 1.178,
                                    1.116, 1.052, 0.99, 0.932, 0.868, 0.802, 0.732, 0.666, 0.604,
                                    0.546, 0.488, 0.426, 0.356, 0.296, 0.25, 0.20, 0.17, 0.15,
                                    0.1]
        elif veh_battery_c_rate_max == 3:
            charging_rate_values = [0.1, 3., 3., 3., 3., 3.,
                                    3., 3., 3., 3., 3., 3., 3., 3., 3.,
                                    3., 3., 3., 3., 3., 3., 3., 3., 3.,
                                    3., 3., 3., 3., 3., 3., 3., 3., 3.,
                                    3., 2.976, 2.952, 2.922, 2.889, 2.856, 2.82, 2.784, 2.748,
                                    2.703, 2.652, 2.595, 2.526, 2.457, 2.385, 2.316, 2.256, 2.196,
                                    2.136, 2.082, 2.031, 1.977, 1.92, 1.863, 1.806, 1.749, 1.695,
                                    1.644, 1.587, 1.527, 1.467, 1.41, 1.353, 1.302, 1.242, 1.176,
                                    1.116, 1.05, 0.99, 0.93, 0.867, 0.801, 0.732, 0.666, 0.603,
                                    0.546, 0.489, 0.426, 0.357, 0.25, 0.22, 0.20, 0.17, 0.15,
                                    0.1]
        # charging_param = np.zeros((len(soc_values), 2))
        # charging_param[:, 0] = soc_values
        # charging_param[:, 1] = charging_rate_values
        # np.savetxt('Modules/M13_SimulationTask/M13_Results/Paper_no2/Parameters/charging_param_1_c.csv',
                   # charging_param, delimiter=",")
        # Linear Interpolation function
        cell_c_rate_func = interp1d(soc_values, charging_rate_values, kind="linear")

    return cell_r_i_func, cell_ocv_func, cell_c_rate_func


# Electric maschine properties
def electric_maschine_propteries():
    # Read Torque Curve over Speed
    trq_raw = pandas.read_csv("Modules/M1_Vehicle_Properties/EM_Map/trq.csv", header=None)
    trq_max = trq_raw.to_numpy()
    # Read Speed
    speed_raw = pandas.read_csv("Modules/M1_Vehicle_Properties/EM_Map/speed.csv", header=None)
    speed_max = speed_raw.to_numpy()
    # Interpolate Function
    em_torque_func = interp1d(speed_max[:, 0], trq_max[:, 0], kind="linear")

    return em_torque_func

