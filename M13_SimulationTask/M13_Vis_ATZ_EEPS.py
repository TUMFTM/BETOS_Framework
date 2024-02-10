# Visualization of Simulation Task for ATZ, EEPS and V2X Plots

# TUM Colors '#005293' (Blau) '#e37222' (Orange) '#a2ad00' (Grün)
# MAN Colors '#44546A' (hellgrau) '#8497B0' (Dunkelgrau) '#DB2960' (Rot)

# Green Colormap 5 ['#1F363D', '#40798C', '#70A9A1', '#9EC1A3', '#CFE0C3]
# Blue Colormap 5 ['#331E36', '#41337A', '#6EA4BF', '#C2EFEB', '#ECFEE8']

# BETOS Green Map ['#0a100f#, '#1d302d', '#30504b', '#43706a', '#568f88', '#70a9a1', '#8fbcb6', '#afcfcb']
# Driver Blue Map ['#003866', '#005293', '#0062b3', '#007ee6', '#1a98ff', '#4dafff', '#80c6ff', '#99d1ff']
# Black Map       ['#1a1a1a', '#333333', '#4d4d4d', '#666666', '#808080', '#999999', '#b3b3b3', '#cccccc']

# color scenario 1 #6c969d
# color scenario 2 #34435e
# color scenario 3 #aa4465

# Import Libraries______________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
import pandas
import scipy.stats as st
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


# ______________________________________________________________________________________________________________________
# [3] ATZ article plot: Time Loss over battery capacity and charging power
# Visualization of ATZ Simulation Task
def vis_atz():
    # Initialize total result matrix____________________________________________________________________________________
    result_time_loss = np.zeros((100, 5, 9))     # Parameter Set 1
    result_time_loss_p2 = np.zeros((20, 5, 9))  # Parameter Set 2
    result_time_loss_rb = np.zeros((100, 5, 9))
    # Read Data Time Loss_______________________________________________________________________________________________
    # <> BETOS
    # Parameter: Start with 80% SoC, discharge to 15% allowed

    result_time_loss[:, 0, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 0] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_400.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 0] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_400.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 1] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_600.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 1] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_600.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 2] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_800.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 2] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_800.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 3] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1000.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 3] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1000.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1200.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1200.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1200.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 4] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1200.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 4] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1200.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1400.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 5] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1400.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 5] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1400.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1600.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 6] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1600.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 6] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1600.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1800.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 7] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1800.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 7] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1800.csv', delimiter=None, header=None).to_numpy()).reshape(100,))

    result_time_loss[:, 0, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_2000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 1, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_2000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 2, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_2000.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss[:, 3, 8] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_2000.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    result_time_loss[:, 4, 8] = np.maximum(0, np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_2000.csv', delimiter=None, header=None).to_numpy()).reshape(100,))
    '''
    # Parameter: Start with 90% SoC, discharge to 10% allowed
    result_time_loss_p2[:, :, 0] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_400.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 1] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_600.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 2] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_800.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 3] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_1000.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 4] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_1200.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 5] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_1400.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 6] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_1600.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 7] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_1800.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_p2[:, :, 8] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ_90_10/result_time_loss_2000.csv', delimiter=None, header=None).to_numpy()
    '''
    # <> Driver
    result_time_loss_rb[:, 0, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 0] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 1] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 2] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 3] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1200_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1200_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1200_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1200_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 4] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1200_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 5] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1400_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 6] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1600_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_1800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_1800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_1800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_1800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 7] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_1800_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    result_time_loss_rb[:, 0, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_400_2000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 1, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_500_2000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 2, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_600_2000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 3, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_700_2000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)
    result_time_loss_rb[:, 4, 8] = np.array(pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figure_1/result_time_loss_800_2000_rb.csv', delimiter=None, header=None).to_numpy()).reshape(100,)

    # Data Energy Consumption___________________________________________________________________________________________
    # result_energy_consumption_400 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/ATZ/result_energy_consumption_400.csv', delimiter=None, header=None).to_numpy()

    # Plotting _________________________________________________________________________________________________________
    # Comparison Driver to BETOS (P1 Set)
    # Plot Time Loss over Battery Capacity and Charging Power as Contourf Plot
    # BETOS
    battery_capacity = np.array([400, 500, 600, 700, 800])
    charging_power = np.array([400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
    time_loss = np.transpose(np.mean(result_time_loss, axis=0)*60)  # in min
    time_loss_rb = np.transpose(np.mean(result_time_loss_rb, axis=0)*60)  # in min
    # Plot Parameters:
    plt.rc('font', family='Times New Roman')
    color_1 = ['#4d74a8', '#7192BE', '#ABBFD8', '#D5DFEC', '#C4D9BE', '#88B380']
    color_2 = ['#88B380', '#C4D9BE', '#D5DFEC', '#ABBFD8', '#7192BE', '#4d74a8']
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 6 / 16
    FIGSIZE = (width_in, height_in)
    csfont = {'fontname': 'Times New Roman'}
    # Figure
    #color_2 = ['#334E70', '#4d74a8', '#7192BE', '#ABBFD8', '#D5DFEC', '#E7F0e6', '#C4D9BE', '#95BA8C', '#88B380','#70A366']
    fig, ax = plt.subplots(1, 3, figsize=FIGSIZE, gridspec_kw={'width_ratios': [1.7, 2, 1]})
    fig.suptitle('Time loss of BET in long-haul application ', **csfont, fontsize=9, y=1.05)
    cs = ax[1].contourf(battery_capacity, charging_power, time_loss, levels=[0, 10, 20, 30, 40, 60, 80],
                      colors=color_2, extend=None)
    # colors = ['#1d302d', '#30504b', '#43706a', '#568f88', '#70a9a1', '#8fbcb6']
    cmap = plt.colorbar(cs, ax=ax[1])
    # Axis Labeling
    cmap.set_label('Time loss in min', fontsize=9)
    cmap.ax.tick_params(labelsize=9)
    ax[1].set_xlabel('Installed battery capacity in kWh', **csfont, fontsize=9)
    # ax[1].set_ylabel('Installed charging power every 50km in kW', **csfont, fontsize=14)
    ax[1].yaxis.set_major_locator(MultipleLocator(200))
    ax[1].yaxis.set_minor_locator(MultipleLocator(100))
    ax[1].tick_params(labelsize=9, labelleft=False)
    ax[1].set_title('BETOS', **csfont, fontsize=9)

    # DRIVER
    cs1 = ax[0].contourf(battery_capacity, charging_power, time_loss_rb, levels=[0, 10, 20, 30, 40, 60, 80],
                        colors=color_2, extend='both')
    # cmap1 = plt.colorbar(cs1, ax=ax[0])
    # Axis Labeling
    # cmap1.set_label('Time loss in min', fontsize=10)
    # cmap1.ax.tick_params(labelsize=9)
    ax[0].set_xlabel('Installed battery capacity in kWh', **csfont, fontsize=9)
    ax[0].set_ylabel('Installed charging power every 50km in kW', **csfont, fontsize=9)
    ax[0].tick_params(labelsize=9)
    ax[0].set_title('NGS', **csfont, fontsize=9)
    ax[0].yaxis.set_major_locator(MultipleLocator(200))
    ax[0].yaxis.set_minor_locator(MultipleLocator(100))

    # Range of time loss in one combination of installed capacity and power for Driver and BETOS
    # Set up data
    range_fixed_parameter = np.zeros((len(result_time_loss), 2))
    range_fixed_parameter[:, 0] = result_time_loss_rb[:, 1, 3] * 60       # in min
    range_fixed_parameter[:, 1] = result_time_loss[:, 1, 3] * 60    # in min
    medianprops = dict(linewidth=0, color='#1a1a1a')
    meanprops = dict(linestyle='-', color='black', linewidth=1)
    bplot = ax[2].boxplot(range_fixed_parameter, labels=["NGS", "BETOS"], showfliers=True, patch_artist=True,
                          medianprops=medianprops, widths=(0.5, 0.5), showmeans=True, meanprops=meanprops, meanline=True)
    colors = ['#7192BE', '#C4D9BE']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    ax[2].tick_params(labelsize=9)
    ax[2].yaxis.set_label_position("right")
    ax[2].yaxis.tick_right()
    ax[2].set_ylim((0, 90))
    ax[2].set_ylabel('Time loss in min', **csfont, fontsize=9)
    ax[2].set_title('Dispersion (500 kWh/1000kW)', **csfont, fontsize=9)
    # ax[2].grid(zorder=0)
    ax[2].yaxis.set_major_locator(MultipleLocator(20))
    ax[2].yaxis.set_minor_locator(MultipleLocator(10))
    plt.text(0.5, -0.28, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes,fontsize=9, rotation=0)
    plt.text(0.5, -0.28, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=9, rotation=0)
    plt.text(0.5, -0.28, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[2].transAxes, fontsize=9, rotation=0)

    # Save Figure
    #plt.savefig('Modules/M13_SimulationTask/M13_Results/Paper_no2/Figures/Time_Loss_BET_Driver_BETOS_Range_FIG_5_3.svg', dpi=400, bbox_inches='tight')
    plt.show()

    # __________________________________________________________________________________________________________________
    # Comparison BETOS P1 to P2
    time_loss_p2 = np.transpose(np.mean(result_time_loss_p2, axis=0) * 60)  # in min
    time_loss_p1 = np.transpose(np.mean(result_time_loss, axis=0) * 60)  # in min
    # Figure
    fig, ax = plt.subplots(1, 3, figsize=FIGSIZE, gridspec_kw={'width_ratios': [1.7, 2, 1]})
    fig.suptitle('Comparison Parameter Set P1 (80,15) to P2 (90,10)', **csfont, fontsize=11, y=1.05)

    # P2
    cs = ax[1].contourf(battery_capacity, charging_power, time_loss_p2, levels=[0, 10, 20, 30, 40, 50, 60],
                        colors=['#005293', '#0062b3', '#007ee6', '#1a98ff', '#4dafff', '#80c6ff'], extend='both')
    #colors=['#1d302d', '#30504b', '#43706a', '#568f88', '#70a9a1', '#8fbcb6']
    cmap = plt.colorbar(cs, ax=ax[1])
    # Axis Labeling
    cmap.set_label('Time loss in min', fontsize=9)
    cmap.ax.tick_params(labelsize=9)
    ax[1].set_xlabel('Installed battery capacity in kWh', **csfont, fontsize=9)
    # ax[1].set_ylabel('Installed charging power every 50km in kW', **csfont, fontsize=14)
    ax[1].tick_params(labelsize=9, labelleft=False)
    ax[1].set_title('P2 (90,10)', **csfont, fontsize=10)

    # P1
    cs1 = ax[0].contourf(battery_capacity, charging_power, time_loss_p1, levels=[0, 10, 20, 30, 40, 50, 60],
                         colors=['#005293', '#0062b3', '#007ee6', '#1a98ff', '#4dafff', '#80c6ff'], extend='both')
    # cmap1 = plt.colorbar(cs1, ax=ax[0])
    # Axis Labeling
    # cmap1.set_label('Time loss in min', fontsize=10)
    # cmap1.ax.tick_params(labelsize=9)
    ax[0].set_xlabel('Installed battery capacity in kWh', **csfont, fontsize=9)
    ax[0].set_ylabel('Installed charging power every 50km in kW', **csfont, fontsize=9)
    ax[0].tick_params(labelsize=9)
    ax[0].set_title('P1 (80,15)', **csfont, fontsize=10)

    # Range of time loss in one combination
    # Set up data
    range_fixed_parameter = np.zeros((len(result_time_loss), 2))
    range_fixed_parameter[:, 0] = result_time_loss[:, 1, 3] * 60  # in min
    range_fixed_parameter[:, 1] = result_time_loss_p2[:, 1, 3] * 60  # in min
    medianprops = dict(linewidth=1, color='#ECFEE8')
    bplot = ax[2].boxplot(range_fixed_parameter, labels=["P1", "P2"], showfliers=False, patch_artist=True,
                          medianprops=medianprops)
    colors = ['#007ee6', '#43706a']
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    ax[2].tick_params(labelsize=9)
    ax[2].yaxis.set_label_position("right")
    ax[2].yaxis.tick_right()
    ax[2].set_ylabel('Time loss in min', **csfont, fontsize=9)
    ax[2].set_title('Range (500kWh/1000kW)', **csfont, fontsize=10)

    # Save Figure
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/Paper_no2/Time_Loss_BET_P1_P2.png', dpi=400, bbox_inches='tight')
    plt.show()

    # __________________________________________________________________________________________________________________
    # Additional Plot of Energy Consumption
    # Energy Consumption Boxplot for different Battery capacities
    plt.rc('font', family='Times New Roman')
    csfont = {'fontname': 'Times New Roman'}
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    ax4.set_title('Energy consumption in long-haul application', **csfont, fontsize=20,
                  y=1.05)
    plt.ylabel('Energy consumption in kWh/km', **csfont, fontsize=16)
    plt.xlabel('Installed battery capacity in kWh', **csfont, fontsize=16)
    plt.ylim((1, 1.5))
    medianprops = dict(linewidth=2, color='#ECFEE8')
    bplot4 = ax4.boxplot(result_energy_consumption_400, labels=["400", "500", "600", "700", "800"],
                         showfliers=False, patch_artist=True, medianprops=medianprops)
    colors = ['#1F363D', '#40798C', '#70A9A1', '#9EC1A3', '#CFE0C3']
    for patch, color in zip(bplot4['boxes'], colors):
        patch.set_facecolor(color)
    ax4.tick_params(labelsize=16)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/ATZ/Energy_consumption_boxplot.png', dpi=400)
    plt.show()

    return


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# [4] V2X Trading Simulation results
def vis_v2x():
    # Read Results:
    # 200kW 500kWh 1EFC per Weekend:
    trading_events_500_200_1_2019_we = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/V2X/2021_1efc_500kwh_200kw_weekend.csv',
                                         delimiter=None, header=None).to_numpy()
    trading_events_500_200_1_2020_we = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/V2X/2020_1efc_500kwh_200kw_weekend.csv',
                                         delimiter=None, header=None).to_numpy()
    trading_events_500_200_1_2021_we = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/V2X/2021_1efc_500kwh_200kw_weekend.csv',
                                         delimiter=None, header=None).to_numpy()
    trading_events_500_200_1_2022_we = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/V2X/2022_1efc_500kwh_200kw_weekend.csv',
                                         delimiter=None, header=None).to_numpy()

    # <>
    # Revenue and Spread Plots
    # Which year to plot
    year = 2020
    if year == 2019:
        trading_event = trading_events_500_200_1_2019_we
    elif year == 2020:
        trading_event = trading_events_500_200_1_2020_we
    elif year == 2022:
        trading_event = trading_events_500_200_1_2021_we
    else:
        trading_event = trading_events_500_200_1_2022_we
    # Building Regression Model
    # Rev over Max Spread:
    x = trading_event[:, 2][trading_event[:, 2] > 0]
    y = trading_event[:, 0][trading_event[:, 2] > 0]
    res = st.linregress(x, y)

    # Visualization
    # Revenue over EFC
    # Plot Parameters:
    plt.rc('font', family='Times New Roman')
    csfont = {'fontname': 'Times New Roman'}
    # Figure
    plt.figure(figsize=(10, 8))
    plt.scatter(trading_event[:, 1], trading_event[:, 0], marker='*', color='#8497B0', s=80)
    plt.xticks(**csfont, fontsize=16)
    plt.xlim((0, 1))
    plt.yticks(**csfont, fontsize=16)
    plt.ylim(-200, 10)
    plt.xlabel('EFC per weekend using V2X', **csfont, fontsize=16)
    plt.ylabel('Energy Cost for 30% - 90% SoC in Eur using V2X in Eur', **csfont, fontsize=16)
    plt.title('V2X on Weekend (2022 / 500kWh / 200kW/ 1EFC)', **csfont, fontsize=20)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/2022_500kwh_200kw_1efc_rev_efc.png', dpi=400)
    plt.show()
    # Revenue over max spread
    plt.figure(figsize=(10, 8))
    plt.scatter(x, y, marker='*', color='#8497B0', s=80)
    plt.plot(x, res.intercept + res.slope * x, linewidth=2, color='#DB2960', label='linear regression')
    plt.xticks(**csfont, fontsize=16)
    plt.xlim((0, 150))
    plt.yticks(**csfont, fontsize=16)
    plt.ylim((-200, 10))
    plt.xlabel('Maximum market spread on weekend in ct', **csfont, fontsize=16)
    plt.ylabel('Energy Cost for 30% - 90% SoC in Eur using V2X in Eur', **csfont, fontsize=16)
    plt.title('V2X on Weekend (2022 / 500kWh / 200kW/ 1EFC)', **csfont, fontsize=20)
    plt.legend(fontsize=16)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/2022_500kwh_200kw_1efc_rev_spread.png', dpi=400)
    plt.show()

    # <>
    # Maximum Battery Cost in Eur/kWh if using V2X
    battery_capacity = 500  # kWh
    cycle_life = 2000
    cycles_no_v2x = 52*(60/200)  # 60% Recharge over Weekend, 200% = 1 EFC, 52 Weeks
    additional_efc_2019 = sum(trading_events_500_200_1_2019_we[:, 1]) - cycles_no_v2x
    revenue_2019 = v2x = -sum(trading_events_500_200_1_2019_we[:, 0])
    energy_v2x_2019 = sum(trading_events_500_200_1_2019_we[:, 1]) * battery_capacity
    cost_battery_max_2019 = (revenue_2019/energy_v2x_2019)*cycle_life

    additional_efc_2020 = sum(trading_events_500_200_1_2020_we[:, 1]) - cycles_no_v2x
    revenue_2020 = v2x = -sum(trading_events_500_200_1_2020_we[:, 0])
    energy_v2x_2020 = sum(trading_events_500_200_1_2020_we[:, 1]) * battery_capacity
    cost_battery_max_2020 = (revenue_2020 / energy_v2x_2020) * cycle_life

    additional_efc_2021 = sum(trading_events_500_200_1_2021_we[:, 1]) - cycles_no_v2x
    revenue_2021 = v2x = -sum(trading_events_500_200_1_2021_we[:, 0])
    energy_v2x_2021 = sum(trading_events_500_200_1_2021_we[:, 1]) * battery_capacity
    cost_battery_max_2021 = (revenue_2021 / energy_v2x_2021) * cycle_life

    additional_efc_2022 = sum(trading_events_500_200_1_2022_we[:, 1]) - cycles_no_v2x
    revenue_2022 = v2x = -sum(trading_events_500_200_1_2022_we[:, 0])
    energy_v2x_2022 = sum(trading_events_500_200_1_2022_we[:, 1]) * battery_capacity
    cost_battery_max_2022 = (revenue_2022 / energy_v2x_2022) * cycle_life

    cost_battery_max = np.array([cost_battery_max_2019, cost_battery_max_2020, cost_battery_max_2021, cost_battery_max_2022])

    # Plot Battery Replacement
    plt.rc('font', family='Times New Roman')
    fig, ax = plt.subplots(figsize=(10, 8))
    years = ['2019', '2020', '2021', '2022']
    ax.bar(years, cost_battery_max, color='#41337A', label='Cost parity V2X')
    plt.xlabel('Year', **csfont, fontsize=18)
    plt.xticks(**csfont, fontsize=16)
    plt.ylabel('Max battery replacement costs in Eur/kWh', **csfont, fontsize=18)
    plt.yticks(**csfont, fontsize=16)
    plt.title('Max battery replacement costs when using V2G application on Weekend', **csfont, fontsize=20, y=1.05)
    plt.legend(fontsize=16)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/replacement_500kwh_200kw_1ef_we.png', dpi=400)
    plt.show()

    # Plot Total Revenue
    revenue_array = np.array([revenue_2019, revenue_2020, revenue_2021, revenue_2022])
    plt.rc('font', family='Times New Roman')
    fig, ax = plt.subplots(figsize=(10, 8))
    years = ['2019', '2020', '2021', '2022']
    ax.bar(years, revenue_array, color='#41337A', label='Total revenue')
    plt.xlabel('Year', **csfont, fontsize=18)
    plt.xticks(**csfont, fontsize=16)
    plt.ylabel('Yearly revenue in Eur', **csfont, fontsize=18)
    plt.yticks(**csfont, fontsize=16)
    plt.title('Additional Revenue using V2G application on Weekend', **csfont, fontsize=20, y=1.05)
    plt.legend(fontsize=16)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/revenue_500kwh_200kw_1efc_weekend.png', dpi=400)
    plt.show()

    # Boxplot of revenues
    revenue = np.array([-trading_events_500_200_1_2019_we[:, 0], -trading_events_500_200_1_2020_we[:, 0],
                        -trading_events_500_200_1_2021_we[:, 0], -trading_events_500_200_1_2022_we[:, 0]])

    fig4, ax4 = plt.subplots(figsize=(10, 6))
    ax4.set_title('Revenue per Event in Eur (500 kWh / 200 kW / 30 Additional EFC per Year)', **csfont, fontsize=20, y=1.05)
    plt.ylabel('Revenue in Eur', **csfont, fontsize=16)
    plt.ylim((-10, 200))
    medianprops = dict(linewidth=2, color='#6EA4BF')
    bplot4 = ax4.boxplot(revenue, labels=["2019", "2020", "2021", "2022"],
                         showfliers=False, patch_artist=True, medianprops=medianprops)
    colors = ['#41337A', '#41337A', '#41337A', '#41337A']
    for patch, color in zip(bplot4['boxes'], colors):
        patch.set_facecolor(color)
    ax4.tick_params(labelsize=16)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/V2X/boxplot_revenue_500kwh_200kw_1efc_we.png', dpi=400)
    plt.show()

    return

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
#  [5] Visualization of EEPS
def vis_eeps():
    # Read data
    result_time_loss = np.zeros((20, 7, 7))
    result_time_loss[:,:,0] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_400_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,1] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_600_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,2] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_800_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,3] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_1000_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,4] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_1200_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,5] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_1400_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss[:,:,6] = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/EEPS/result_time_loss_1600_rb.csv', delimiter=None, header=None).to_numpy()

    # Preprocessing
    trip_length = np.array([400, 450, 500, 550, 600, 650, 700])
    charging_power = np.array([400, 600, 800, 1000, 1200, 1400, 1600])
    time_loss = np.transpose(np.mean(result_time_loss, axis=0) * 60)  # in min
    # Plot Parameters:
    plt.rc('font', family='Times New Roman')
    docwidth = 16.4  # word doc width in cm
    width_in = docwidth / 2.54
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    csfont = {'fontname': 'Times New Roman'}
    # Figure
    fig, ax = plt.subplots(1, 2, figsize=FIGSIZE, gridspec_kw={'width_ratios': [1, 0.3]})
    # fig.suptitle('Required additional time of BET in long-haul application ', **csfont, fontsize=9, y=1)
    cs = ax[0].contourf(trip_length, charging_power, time_loss, levels=[0, 10, 20, 30, 40, 50, 60],
                        colors=['#003866', '#0062b3', '#007ee6', '#1a98ff', '#4dafff', '#99d1ff'], extend='both')

    # cmap = plt.colorbar(cs, ax=ax[0])
    # Axis Labeling
    # cmap.set_label('Time loss in min', fontsize=9)
    # cmap.ax.tick_params(labelsize=9)
    ax[0].set_xlabel('Average Trip Length in km', **csfont, fontsize=9)
    ax[0].set_ylabel('Charging Power in kW', **csfont, fontsize=9)
    ax[0].tick_params(labelsize=9)
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)
    # ax.text(0.5, 0.5, '10 min', **csfont, fontsize=9)
    plt.text(0.4, 0.45, '+10 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    plt.text(0.65, 0.35, '+20 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    plt.text(0.77, 0.25, '+30 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    plt.text(0.84, 0.21, '+40 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    plt.text(0.90, 0.16, '+50 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    plt.text(0.96, 0.12, '+60 min', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=9, rotation=55)
    # Plot range of Time Loss for 600kW and 600km
    data_range = result_time_loss[:, 4, 1]*60

    ax[1].set_ylabel('Time in min', **csfont, fontsize=9)
    ax[1].set_ylim((0, 40))
    medianprops = dict(linewidth=1, color='black')
    colors = ['#0062b3']
    bplot = ax[1].boxplot(data_range, showfliers=False,
                            patch_artist=True, medianprops=medianprops, widths=(0.25))
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['left'].set_visible(False)
    #ax[1].spines['bottom'].set_visible(False)
    ax[1].set_xticklabels(labels=["600 km|600 kW"])
    ax[1].yaxis.tick_right()
    ax[1].yaxis.set_label_position("right")
    ax[1].tick_params(labelsize=9)
    ax[1].grid(False)
    plt.savefig('Modules/M13_SimulationTask/M13_Results/EEPS/Time_loss_trip_length_2.svg', dpi=400, bbox_inches='tight')
    plt.show()

    return


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# [6] Visualization of VDI
def vis_vdi():
    result_time_loss_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s2.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s1_1.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s4.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s2_2.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s5 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s6.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s6 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s3_3.csv', delimiter=None, header=None).to_numpy()
    # result_time_loss_s7 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/VDI/result_time_loss_s7.csv', delimiter=None, header=None).to_numpy()
    time_loss_comparision_s1 = (result_time_loss_s1[:, 0] - 0.75) * 60  # S1
    time_loss_comparision_s2 = (result_time_loss_s2[:, 0] - 0.75) * 60  # S2
    time_loss_comparision_s3 = (result_time_loss_s3[:, 0] - 0.75) * 60  # S3
    time_loss_comparision_s4 = (result_time_loss_s4[:, 0] - 0.75) * 60  # S4
    time_loss_comparision_s5 = (result_time_loss_s5[:, 0] - 0.75) * 60  # S5
    time_loss_comparision_s6 = (result_time_loss_s6[:, 0] - 0.75) * 60  # S6
    # time_loss_comparision_s7 = (result_time_loss_s7[:, 0] - 0.75) * 60  # S7
    # Plotting
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    fig4, ax4 = plt.subplots()
    fig4.set_size_inches(FIGSIZE)
    fig4.suptitle('Time loss compared to ICET', **csfont, fontsize=10, y=1.05)
    medianprops = dict(linewidth=1, color='black')
    colors_1 = ['#30504b', '#30504b', '#568f88']
    # S1
    ax4.set_title('for different Charging Networks', **csfont, fontsize=9)
    ax4.set_ylabel('Additional time per trip in min', **csfont, fontsize=9)
    ax4.set_ylim((0, 80))
    bplot4 = ax4.boxplot([time_loss_comparision_s1, time_loss_comparision_s2, time_loss_comparision_s3, time_loss_comparision_s4, time_loss_comparision_s5, time_loss_comparision_s6], showfliers=False, patch_artist=True, medianprops=medianprops,
                         widths=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5))

    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax4.set_xticklabels(labels=["VDI1", "VDI1_100_20", "VDI2", "VDI2_100_20", "VDI3", "VDI3_100_20"])
    ax4.tick_params(labelsize=9)
    ax4.grid(True)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/VDI/Time_loss_2.png', dpi=400, bbox_inches='tight')
    plt.show()

    return


# Visualization of AFIR Analysis
def vis_afir():
    # Read Data
    result_time_loss_350 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_350.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_700 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_700.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_1000 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_1000.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_1500 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_1500.csv', delimiter=None, header=None).to_numpy()

    time_loss_350 = result_time_loss_350[:, 0] * 60
    time_loss_700 = (result_time_loss_700[:, 0]) * 60
    time_loss_1000 = (result_time_loss_1000[:, 0]) * 60
    time_loss_1500 = (result_time_loss_1500[:, 0]) * 60

    result_time_loss_350_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_350_100km.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_700_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_700_100km.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_1000_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_1000_100km.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_1500_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/AFIR/result_time_loss_1500_100km.csv', delimiter=None, header=None).to_numpy()

    time_loss_350_120 = result_time_loss_350_100[:, 0] * 60
    time_loss_700_120 = (result_time_loss_700_100[:, 0]) * 60
    time_loss_1000_120 = (result_time_loss_1000_100[:, 0]) * 60
    time_loss_1500_120 = (result_time_loss_1500_100[:, 0]) * 60

    # Prepare Plot
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9
    # Colors
    medianprops = dict(linewidth=0, color='black')
    meanprop = dict(linewidth=1, color='black', linestyle='-')
    colors_1 = ['#6c969d', '#6c969d', '#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e', '#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465', '#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080', '#808080']

    # Plot
    fig, ax = plt.subplots()
    fig.set_size_inches(FIGSIZE)
    fig.suptitle('AFIR Analysis', **csfont, fontsize=textsize, y=1.0)
    ax.set_ylim((0, 80))
    ax.set_ylabel('Additional time in min', **csfont, fontsize=textsize)
    bplot4 = ax.boxplot([time_loss_350_120, time_loss_700_120, time_loss_1000_120, time_loss_1500_120], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    ax.set_xticklabels(labels=["350 kW", "700 kW", "1000 kW", "1500 kW"], rotation=90)
    ax.tick_params(labelsize=9)
    ax.grid(True)
    ax.yaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_minor_locator(MultipleLocator(10))

    plt.savefig('Modules/M13_SimulationTask/M13_Results/AFIR/Analysis_power_120km.svg', dpi=400, bbox_inches='tight')
    plt.show()

    return
