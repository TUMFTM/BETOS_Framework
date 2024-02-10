# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-11-11
#
# Function Description
# Evaluation of Simulation Tasks

# Import Libraries
import numpy as np
import pandas
import matplotlib.pyplot as plt


def eval_sim_task():
    # Read Input data
    result_time_sparse_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_sparse.csv',
                                             delimiter=None, header=None)
    result_time_sparse = result_time_sparse_raw.to_numpy()

    result_time_mid_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_mid.csv',
                                             delimiter=None, header=None)
    result_time_mid = result_time_mid_raw.to_numpy()

    result_time_dense_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_dense.csv',
                                             delimiter=None, header=None)
    result_time_dense = result_time_dense_raw.to_numpy()

    result_time_sparse_ct_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_sparse_chargetime.csv',
                                             delimiter=None, header=None)
    result_time_sparse_chargetime = result_time_sparse_ct_raw.to_numpy()

    result_time_mid_ct_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_mid_chargetime.csv',
                                          delimiter=None, header=None)
    result_time_mid_chargetime = result_time_mid_ct_raw.to_numpy()

    result_time_dense_chargetime_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_time_dense_chargetime.csv',
                                            delimiter=None, header=None)
    result_time_dense_chargetime = result_time_dense_chargetime_raw.to_numpy()
    # <>
    result_stops_sparse_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_sparse.csv',
                                             delimiter=None, header=None)
    result_stops_sparse = result_stops_sparse_raw.to_numpy()

    result_stops_mid_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_mid.csv',
                                          delimiter=None, header=None)
    result_stops_mid = result_stops_mid_raw.to_numpy()

    result_stops_dense_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_dense.csv',
                                            delimiter=None, header=None)
    result_stops_dense = result_stops_dense_raw.to_numpy()


    result_stops_sparse_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_sparse_chargetime.csv',
                                              delimiter=None, header=None)
    result_stops_sparse_chargetime = result_stops_sparse_raw_ct.to_numpy()

    result_stops_mid_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_mid_chargetime.csv',
                                           delimiter=None, header=None)
    result_stops_mid_chargetime = result_stops_mid_raw_ct.to_numpy()

    result_stops_dense_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_stops_dense_chargetime.csv',
                                             delimiter=None, header=None)
    result_stops_dense_chargetime = result_stops_dense_raw_ct.to_numpy()

    # <>
    result_discharge_sparse_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_sparse.csv',
                                             delimiter=None, header=None)
    result_discharge_sparse = result_discharge_sparse_raw.to_numpy()

    result_discharge_mid_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_mid.csv',
                                          delimiter=None, header=None)
    result_discharge_mid = result_discharge_mid_raw.to_numpy()

    result_discharge_dense_raw = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_dense.csv',
                                            delimiter=None, header=None)
    result_discharge_dense = result_discharge_dense_raw.to_numpy()


    result_discharge_sparse_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_sparse_chargetime.csv',
                                                  delimiter=None, header=None)
    result_discharge_sparse_chargetime = result_discharge_sparse_raw_ct.to_numpy()

    result_discharge_mid_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_mid_chargetime.csv',
                                               delimiter=None, header=None)
    result_discharge_mid_chargetime = result_discharge_mid_raw_ct.to_numpy()

    result_discharge_dense_raw_ct = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/result_discharge_dense_chargetime.csv',
                                                 delimiter=None, header=None)
    result_discharge_dense_chargetime = result_discharge_dense_raw_ct.to_numpy()

    # Process Simulation Results
    # Operation Time Impact_____________________________________________________________________________________________
    # SoC Prediction Error
    soc_error_time_sparse = (result_time_sparse[:, 1] - result_time_sparse[:, 0]) / result_time_sparse[:, 0]
    soc_error_time_mid = (result_time_mid[:, 1] - result_time_mid[:, 0]) / result_time_mid[:, 0]
    soc_error_time_dense = (result_time_dense[:, 1] - result_time_dense[:, 0]) / result_time_dense[:, 0]
    soc_error_time_sparse_chargetime = (result_time_sparse_chargetime[:, 1] - result_time_sparse_chargetime[:, 0]) / \
                                      result_time_sparse_chargetime[:, 0]
    soc_error_time_mid_chargetime = (result_time_mid_chargetime[:, 1] - result_time_mid_chargetime[:,0]) / \
                                      result_time_mid_chargetime[:, 0]
    soc_error_time_dense_chargetime = (result_time_dense_chargetime[:, 1] - result_time_dense_chargetime[:,0]) / \
                                      result_time_dense_chargetime[:, 0]
    # Time Prediction Error
    time_error_time_sparse = (result_time_sparse[:, 2] - result_time_sparse[:, 0]) / result_time_sparse[:, 0]
    time_error_time_mid = (result_time_mid[:, 2] - result_time_mid[:, 0]) / result_time_mid[:, 0]
    time_error_time_dense = (result_time_dense[:, 2] - result_time_dense[:, 0]) / result_time_dense[:, 0]

    time_error_time_sparse_chargetime = (result_time_sparse_chargetime[:, 2] - result_time_sparse_chargetime[:, 0]) / result_time_sparse_chargetime[:, 0]
    time_error_time_mid_chargetime = (result_time_mid_chargetime[:, 2] - result_time_mid_chargetime[:, 0]) / result_time_mid_chargetime[:, 0]
    time_error_time_dense_chargetime = (result_time_dense_chargetime[:, 2] - result_time_dense_chargetime[:, 0]) / result_time_dense_chargetime[:, 0]

    # Charging Profile Error
    crate_error_time_sparse = (result_time_sparse[:, 3] - result_time_sparse[:, 0]) / result_time_sparse[:, 0]
    crate_error_time_mid = (result_time_mid[:, 3] - result_time_mid[:, 0]) / result_time_mid[:, 0]
    crate_error_time_dense = (result_time_dense[:, 3] - result_time_dense[:, 0]) / result_time_dense[:, 0]

    crate_error_time_sparse_chargetime = (result_time_sparse_chargetime[:, 3] - result_time_sparse_chargetime[:, 0]) / result_time_sparse_chargetime[:, 0]
    crate_error_time_mid_chargetime = (result_time_mid_chargetime[:, 3] - result_time_mid_chargetime[:, 0]) / result_time_mid_chargetime[:, 0]
    crate_error_time_dense_chargetime = (result_time_dense_chargetime[:, 3] - result_time_dense_chargetime[:, 0]) / result_time_dense_chargetime[:, 0]

    # Number Stops Impact_______________________________________________________________________________________________
    # SoC Prediction Error
    soc_error_stops_sparse = (result_stops_sparse[:, 1] - result_stops_sparse[:, 0])
    soc_error_stops_mid = (result_stops_mid[:, 1] - result_stops_mid[:, 0])
    soc_error_stops_dense = (result_stops_dense[:, 1] - result_stops_dense[:, 0])

    soc_error_stops_sparse_chargetime = (result_stops_sparse_chargetime[:, 1] - result_stops_sparse_chargetime[:, 0])
    soc_error_stops_mid_chargetime = (result_stops_mid_chargetime[:, 1] - result_stops_mid_chargetime[:, 0])
    soc_error_stops_dense_chargetime = (result_stops_dense_chargetime[:, 1] - result_stops_dense_chargetime[:, 0])

    # Time Prediction Error
    time_error_stops_sparse = (result_stops_sparse[:, 2] - result_stops_sparse[:, 0])
    time_error_stops_mid = (result_stops_mid[:, 2] - result_stops_mid[:, 0])
    time_error_stops_dense = (result_stops_dense[:, 2] - result_stops_dense[:, 0])

    time_error_stops_sparse_chargetime = (result_stops_sparse_chargetime[:, 2] - result_stops_sparse_chargetime[:, 0])
    time_error_stops_mid_chargetime = (result_stops_mid_chargetime[:, 2] - result_stops_mid_chargetime[:, 0])
    time_error_stops_dense_chargetime = (result_stops_dense_chargetime[:, 2] - result_stops_dense_chargetime[:, 0])

    # Charging Profile Error
    crate_error_stops_sparse = (result_stops_sparse[:, 3] - result_stops_sparse[:, 0])
    crate_error_stops_mid = (result_stops_mid[:, 3] - result_stops_mid[:, 0])
    crate_error_stops_dense = (result_stops_dense[:, 3] - result_stops_dense[:, 0])

    crate_error_stops_sparse_chargetime = (result_stops_sparse_chargetime[:, 3] - result_stops_sparse_chargetime[:, 0])
    crate_error_stops_mid_chargetime = (result_stops_mid_chargetime[:, 3] - result_stops_mid_chargetime[:, 0])
    crate_error_stops_dense_chargetime = (result_stops_dense_chargetime[:, 3] - result_stops_dense_chargetime[:, 0])

    # Number Deep Discharge Events Impact_______________________________________________________________________________
    # SoC Prediction Error
    soc_error_discharge_sparse = result_discharge_sparse[:, 1]
    soc_error_discharge_mid = result_discharge_mid[:, 1]
    soc_error_discharge_dense = result_discharge_dense[:, 1]

    soc_error_discharge_sparse_chargetime = result_discharge_sparse_chargetime[:, 1]
    soc_error_discharge_mid_chargetime = result_discharge_mid_chargetime[:, 1]
    soc_error_discharge_dense_chargetime = result_discharge_dense_chargetime[:, 1]

    # Time Prediction Error
    time_error_discharge_sparse = result_discharge_sparse[:, 2]
    time_error_discharge_mid = result_discharge_mid[:, 2]
    time_error_discharge_dense = result_discharge_dense[:, 2]

    time_error_discharge_sparse_chargetime = result_discharge_sparse_chargetime[:, 2]
    time_error_discharge_mid_chargetime = result_discharge_mid_chargetime[:, 2]
    time_error_discharge_dense_chargetime = result_discharge_dense_chargetime[:, 2]

    # Charging Profile Error
    crate_error_discharge_sparse = result_discharge_sparse[:, 3]
    crate_error_discharge_mid = result_discharge_mid[:, 3]
    crate_error_discharge_dense = result_discharge_dense[:, 3]

    crate_error_discharge_sparse_chargetime = result_discharge_sparse_chargetime[:, 3]
    crate_error_discharge_mid_chargetime = result_discharge_mid_chargetime[:, 3]
    crate_error_discharge_dense_chargetime = result_discharge_dense_chargetime[:, 3]

    # Plot Simulation Evaluation Results________________________________________________________________________________
    # Soc Prediction, Impact on Time
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_time_sparse*100, label='SoC Prediction Error Sparse', color='#005293')
    #plt.plot(soc_error_time_mid * 100, label='SoC Prediction Error Mid', color='#E37222')
    #plt.plot(soc_error_time_dense * 100, label='SoC Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Prediction Error in Energy Consumption')
    #plt.show()
    # Time based charging
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_time_sparse_chargetime * 100, label='SoC Prediction Error Sparse CT', color='#005293')
    #plt.plot(soc_error_time_mid_chargetime * 100, label='SoC Prediction Error Mid CT', color='#E37222')
    #plt.plot(soc_error_time_dense_chargetime * 100, label='SoC Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Prediction Error in Energy Consumption')
    #plt.show()
    #___________________________________________________________________________________________________________________
    # Time Prediction, Impact on Time
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_time_sparse * 100, label='Time Prediction Error Sparse', color='#005293')
    #plt.plot(time_error_time_mid * 100, label='Time Prediction Error Mid', color='#E37222')
    #plt.plot(time_error_time_dense * 100, label='Time Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Error in Time')
    #plt.show()
    # Time bases Charging
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_time_sparse_chargetime * 100, label='Time Prediction Error Sparse CT', color='#005293')
    #plt.plot(time_error_time_mid_chargetime * 100, label='Time Prediction Error Mid CT', color='#E37222')
    #plt.plot(time_error_time_dense_chargetime * 100, label='Time Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Prediction Error in Time')
    #plt.show()
    #___________________________________________________________________________________________________________________
    # CRate Prediction, Impact on Time
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(crate_error_time_sparse * 100, label='CRate Prediction Error Sparse', color='#005293')
    #plt.plot(crate_error_time_mid * 100, label='CRate Prediction Error Mid', color='#E37222')
    #plt.plot(crate_error_time_dense * 100, label='CRate Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Prediction Error in Charging Profile')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(crate_error_time_sparse_chargetime * 100, label='CRate Prediction Error Sparse CT', color='#005293')
    #plt.plot(crate_error_time_mid_chargetime * 100, label='CRate Prediction Error Mid CT', color='#E37222')
    #plt.plot(crate_error_time_dense_chargetime * 100, label='CRate Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Impact on Operation Time in %')
    #plt.title('Impact of 10 % Prediction Error in Charging Profile')
    #plt.show()
    #___________________________________________________________________________________________________________________
    # Soc Prediction, Impact on Stops
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_stops_sparse, label='SoC Prediction Error Sparse', color='#005293')
    #plt.plot(soc_error_stops_mid, label='SoC Prediction Error Mid', color='#E37222')
    #plt.plot(soc_error_stops_dense, label='SoC Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Energy Consumption')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_stops_sparse_chargetime, label='SoC Prediction Error Sparse CT', color='#005293')
    #plt.plot(soc_error_stops_mid_chargetime, label='SoC Prediction Error Mid CT', color='#E37222')
    #plt.plot(soc_error_stops_dense_chargetime, label='SoC Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Energy Consumption')
    #plt.show()

    # Time Prediction, Impact on Stops
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_stops_sparse, label='Time Prediction Error Sparse', color='#005293')
    #plt.plot(time_error_stops_mid, label='Time Prediction Error Mid', color='#E37222')
    #plt.plot(time_error_stops_dense, label='Time Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Time')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_stops_sparse_chargetime, label='Time Prediction Error Sparse CT', color='#005293')
    #plt.plot(time_error_stops_mid_chargetime, label='Time Prediction Error Mid CT', color='#E37222')
    #plt.plot(time_error_stops_dense_chargetime, label='Time Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
   #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Time')
    #plt.show()

    # C Rate Prediction, Impact on Stops
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(crate_error_stops_sparse, label='Crate Prediction Error Sparse', color='#005293')
    #plt.plot(crate_error_stops_mid, label='Crate Prediction Error Mid', color='#E37222')
    #plt.plot(crate_error_stops_dense, label='Crate Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Charging Profile')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((-5, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(crate_error_stops_sparse_chargetime, label='Crate Prediction Error Sparse CT', color='#005293')
    #plt.plot(crate_error_stops_mid_chargetime, label='Crate Prediction Error Mid CT', color='#E37222')
    #plt.plot(crate_error_stops_dense_chargetime, label='Crate Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Additional Stops')
    #plt.title('Impact of 10 % Prediction Error in Charging Profile')
    #plt.show()

    # <>
    # Soc Prediction, Impact on Discharge Events
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((0, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_discharge_sparse, label='SoC Prediction Error Sparse', color='#005293')
    #plt.plot(soc_error_discharge_mid, label='SoC Prediction Error Mid', color='#E37222')
    #plt.plot(soc_error_discharge_dense, label='SoC Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Number of deep discharge events')
    #plt.title('Impact of 10 % Error in Energy Consumption')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((0, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(soc_error_discharge_sparse_chargetime, label='SoC Prediction Error Sparse CT', color='#005293')
    #plt.plot(soc_error_discharge_mid_chargetime, label='SoC Prediction Error Mid CT', color='#E37222')
    #plt.plot(soc_error_discharge_dense_chargetime, label='SoC Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Number of deep discharge events')
    #plt.title('Impact of 10 % Error in Energy Consumption')
    #plt.show()

    # Time Prediction, Impact on Discharge Events
    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((0, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_discharge_sparse, label='Time Prediction Error Sparse', color='#005293')
    #plt.plot(time_error_discharge_mid, label='Time Prediction Error Mid', color='#E37222')
    #plt.plot(time_error_discharge_dense, label='Time Prediction Error Dense', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Number of deep discharge events')
    #plt.title('Impact of 10 % Error in Time')
    #plt.show()

    #plt.figure(figsize=(10, 6), dpi=200)
    #plt.ylim((0, 5))
    #plt.xlim((1, 50))
    #plt.hlines(y=0, xmin=1, xmax=50, color='green')
    #plt.plot(time_error_discharge_sparse_chargetime, label='Time Prediction Error Sparse CT', color='#005293')
    #plt.plot(time_error_discharge_mid_chargetime, label='Time Prediction Error Mid CT', color='#E37222')
    #plt.plot(time_error_discharge_dense_chargetime, label='Time Prediction Error Dense CT', color='#A2AD00')
    #plt.legend()
    #plt.xlabel('Simulation Runs')
    #plt.ylabel('Number of deep discharge events')
    #plt.title('Impact of 10 % Error in Time')
    #plt.show()

    # Crate Prediction, Impact on Discharge Events
    plt.figure(figsize=(10, 6), dpi=200)
    plt.ylim((0, 5))
    plt.xlim((1, 50))
    plt.hlines(y=0, xmin=1, xmax=50, color='green')
    plt.plot(crate_error_discharge_sparse, label='Crate Prediction Error Sparse', color='#005293')
    plt.plot(crate_error_discharge_mid, label='Crate Prediction Error Mid', color='#E37222')
    plt.plot(crate_error_discharge_dense, label='Crate Prediction Error Dense', color='#A2AD00')
    plt.legend()
    plt.xlabel('Simulation Runs')
    plt.ylabel('Number of deep discharge events')
    plt.title('Impact of 10 % Error in Charging Profile')
    plt.show()

    plt.figure(figsize=(10, 6), dpi=200)
    plt.ylim((0, 5))
    plt.xlim((1, 50))
    plt.hlines(y=0, xmin=1, xmax=50, color='green')
    plt.plot(crate_error_discharge_sparse_chargetime, label='Crate Prediction Error Sparse CT', color='#005293')
    plt.plot(crate_error_discharge_mid_chargetime, label='Crate Prediction Error Mid CT', color='#E37222')
    plt.plot(crate_error_discharge_dense_chargetime, label='Crate Prediction Error Dense CT', color='#A2AD00')
    plt.legend()
    plt.xlabel('Simulation Runs')
    plt.ylabel('Number of deep discharge events')
    plt.title('Impact of 10 % Error in Charging Profile')
    plt.show()

    return
