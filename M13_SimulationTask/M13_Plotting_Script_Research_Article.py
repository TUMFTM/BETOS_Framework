# _________________________________
# BET.OS Function #
#
# Designed by MX-2024-02-12
#
# Function Description
# Part of the M13 Simulation Task Module
# Plotting Script of the research article: Optimizing the Journey - Dynamic Charging Strategis for Battery Electric Trucks in Long-Haul Transport
# _________________________________

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas
import scipy.stats as st
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Plotting_Function
def plotting():
    # __________________________________________________________________________________________________________________
    # Plotting Section 4.1:
    # Initialize total result matrix
    result_time_loss = np.zeros((100, 5, 9))     # Parameter Set 1
    result_time_loss_p2 = np.zeros((20, 5, 9))  # Parameter Set 2
    result_time_loss_rb = np.zeros((100, 5, 9))
    # Read Data Time Loss
    # <> BETOS
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

    # Plotting
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
    fig, ax = plt.subplots(1, 3, figsize=FIGSIZE, gridspec_kw={'width_ratios': [1.7, 2, 1]})
    fig.suptitle('Time loss of BET in long-haul application ', **csfont, fontsize=9, y=1.05)
    cs = ax[1].contourf(battery_capacity, charging_power, time_loss, levels=[0, 10, 20, 30, 40, 60, 80],
                      colors=color_2, extend=None)
    cmap = plt.colorbar(cs, ax=ax[1])
    # Axis Labeling
    cmap.set_label('Time loss in min', fontsize=9)
    cmap.ax.tick_params(labelsize=9)
    ax[1].set_xlabel('Installed battery capacity in kWh', **csfont, fontsize=9)
    ax[1].yaxis.set_major_locator(MultipleLocator(200))
    ax[1].yaxis.set_minor_locator(MultipleLocator(100))
    ax[1].tick_params(labelsize=9, labelleft=False)
    ax[1].set_title('BETOS', **csfont, fontsize=9)

    # DRIVER
    cs1 = ax[0].contourf(battery_capacity, charging_power, time_loss_rb, levels=[0, 10, 20, 30, 40, 60, 80],
                        colors=color_2, extend='both')
    # cmap1 = plt.colorbar(cs1, ax=ax[0])
    # Axis Labeling
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
    ax[2].yaxis.set_major_locator(MultipleLocator(20))
    ax[2].yaxis.set_minor_locator(MultipleLocator(10))
    plt.text(0.5, -0.28, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes,fontsize=9, rotation=0)
    plt.text(0.5, -0.28, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=9, rotation=0)
    plt.text(0.5, -0.28, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[2].transAxes, fontsize=9, rotation=0)

    plt.show()
    # __________________________________________________________________________________________________________________
    # Section 4.2
    # Read Data
    # <> impact on time
    result_time_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_time_s1.csv', delimiter=None, header=None).to_numpy()
    result_time_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_time_s2.csv', delimiter=None, header=None).to_numpy()
    result_time_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_s3.csv', delimiter=None, header=None).to_numpy()
    result_time_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_s4.csv', delimiter=None, header=None).to_numpy()
    # <> impact on stops
    result_stops_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_stops_s1.csv', delimiter=None, header=None).to_numpy()
    result_stops_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_stops_s2.csv', delimiter=None, header=None).to_numpy()
    result_stops_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_stops_s3.csv', delimiter=None, header=None).to_numpy()
    result_stops_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_stops_s4.csv', delimiter=None, header=None).to_numpy()
    # <> impact on deep discharge events
    result_discharge_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_discharge_s1.csv', delimiter=None, header=None).to_numpy()
    result_discharge_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_discharge_s2.csv', delimiter=None, header=None).to_numpy()
    result_discharge_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_discharge_s3.csv', delimiter=None, header=None).to_numpy()
    result_discharge_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_discharge_s4.csv', delimiter=None, header=None).to_numpy()
    # <> time loss in different scenarios BETOS
    result_time_loss_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_time_loss_s1.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_time_loss_s2.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s4.csv', delimiter=None, header=None).to_numpy()
    # <> time loss in different scenarios RuleBased (Driver)
    result_time_loss_s1_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_time_loss_s1_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s2_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_time_loss_s2_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s3_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s4_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s4_rb.csv', delimiter=None, header=None).to_numpy()
    # <> taken stops using Driver strategy
    result_stops_s1_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_stops_s1_rb.csv', delimiter=None, header=None).to_numpy()
    result_stops_s2_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_stops_s2_rb.csv', delimiter=None, header=None).to_numpy()
    result_stops_s3_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_stops_s3_rb.csv', delimiter=None, header=None).to_numpy()
    result_stops_s4_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_stops_s4_rb.csv', delimiter=None, header=None).to_numpy()
    # <> chosen mean power in different scenarios
    chosen_power_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/power_s1.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s1 = chosen_power_s1[:, 0]
    chosen_power_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/power_s2.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s2 = chosen_power_s2[:, 0]
    chosen_power_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/power_s3.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s3 = chosen_power_s3[:, 0]
    chosen_power_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s4 = chosen_power_s4[:, 0]
    # <> chosen mean power in different scenarios with rulebased strategy
    chosen_power_s1_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/power_s1_rb.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s1_rb = chosen_power_s1_rb[:, 0]
    chosen_power_s2_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/power_s2_rb.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s2_rb = chosen_power_s2_rb[:, 0]
    chosen_power_s3_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/power_s3_rb.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s3_rb = chosen_power_s3_rb[:, 0]
    chosen_power_s4_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4_rb.csv', delimiter=None, header=None).to_numpy()
    chosen_power_s4_rb = chosen_power_s4_rb[:, 0]

    # Global Figure Parameters
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 16 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9

    # Time Loss Compared to ICET for different Strategy implementations (RB, DP) in different scenarios
    time_loss_comparision = np.zeros((len(result_time_loss_s1_rb), 6))
    time_loss_comparision_s1_rb = (result_time_loss_s1_rb[:, 0]) * 60  # S1
    time_loss_comparision_s1_rb = time_loss_comparision_s1_rb[~np.isnan(time_loss_comparision_s1_rb)]
    time_loss_comparision_s1 = (result_time_loss_s1[:, 0]) * 60  # S1
    time_loss_comparision_s2_rb = (result_time_loss_s2_rb[:, 0]) * 60  # S2
    time_loss_comparision_s2_rb = time_loss_comparision_s2_rb[~np.isnan(time_loss_comparision_s2_rb)]
    time_loss_comparision_s2 = (result_time_loss_s2[:, 0]) * 60  # S2
    time_loss_comparision_s3_rb = (result_time_loss_s3_rb[:, 0]) * 60  # S3
    time_loss_comparision_s3_rb = time_loss_comparision_s3_rb[~np.isnan(time_loss_comparision_s3_rb)]
    time_loss_comparision_s3 = (result_time_loss_s3[:, 0]) * 60  # S3
    time_loss_comparision_s4_rb = (result_time_loss_s4_rb[:, 0]) * 60  # S4
    time_loss_comparision_s4_rb = time_loss_comparision_s4_rb[~np.isnan(time_loss_comparision_s4_rb)]
    time_loss_comparision_s4 = (result_time_loss_s4[:, 0]) * 60  # S4
    # Plotting Figure (7)
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    fig4, ax4 = plt.subplots(1, 4)
    fig4.set_size_inches(FIGSIZE)
    fig4.suptitle('CS 2 Charging Network - Additional time per trip', **csfont, fontsize=textsize, y=1.05)
    medianprops = dict(linewidth=0, color='black')
    meanprop = dict(linewidth=1, color='black', linestyle='-')
    flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='black')
    colors_1 = ['#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080']
    # S1
    ax4[0].set_title('Scenario 1', **csfont, fontsize=textsize)
    ax4[0].set_ylabel('Additional time in min', **csfont, fontsize=textsize)
    ax4[0].set_ylim((0, 220))
    bplot4 = ax4[0].boxplot([time_loss_comparision_s1_rb, time_loss_comparision_s1], showfliers=True,
                            flierprops=flierprops,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax4[0].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0].tick_params(labelsize=textsize)
    ax4[0].grid(True)
    ax4[0].yaxis.set_major_locator(MultipleLocator(40))
    ax4[0].yaxis.set_minor_locator(MultipleLocator(20))

    # S2
    ax4[1].set_title('Scenario 2', **csfont, fontsize=textsize)
    ax4[1].set_ylim((0, 220))
    bplot4 = ax4[1].boxplot([time_loss_comparision_s2_rb, time_loss_comparision_s2], showfliers=True,
                            flierprops=flierprops,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_2):
        patch.set_facecolor(color)
    ax4[1].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1].tick_params(labelsize=textsize)
    ax4[1].tick_params(labelleft=False)
    ax4[1].grid(True)
    ax4[1].yaxis.set_major_locator(MultipleLocator(40))
    ax4[1].yaxis.set_minor_locator(MultipleLocator(20))
    # S3
    ax4[2].set_title('Scenario 3', **csfont, fontsize=textsize)
    ax4[2].set_ylim((0, 220))
    bplot4 = ax4[2].boxplot([time_loss_comparision_s3_rb, time_loss_comparision_s3], showfliers=True,
                            flierprops=flierprops,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    ax4[2].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[2].tick_params(labelsize=textsize)
    ax4[2].tick_params(labelleft=False)
    ax4[2].grid(True)
    ax4[2].yaxis.set_major_locator(MultipleLocator(40))
    ax4[2].yaxis.set_minor_locator(MultipleLocator(20))
    # S4
    ax4[3].set_title('Scenario 4', **csfont, fontsize=9)
    ax4[3].set_ylim((0, 220))
    bplot4 = ax4[3].boxplot([time_loss_comparision_s4_rb, time_loss_comparision_s4], showfliers=True,
                            flierprops=flierprops,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax4[3].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[3].tick_params(labelsize=textsize)
    ax4[3].tick_params(labelleft=False)
    ax4[3].grid(True)
    ax4[3].yaxis.set_major_locator(MultipleLocator(40))
    ax4[3].yaxis.set_minor_locator(MultipleLocator(20))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=0.3)
    plt.text(0.5, -0.25, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax4[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax4[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax4[2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax4[3].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # Analyse chosen power
    # Figure (8)
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    fig4, ax4 = plt.subplots(1, 4)
    fig4.set_size_inches(FIGSIZE)
    fig4.suptitle('CS 2 Charging Network - Average chosen charging power', **csfont, fontsize=textsize, y=1.05)
    colors_1 = ['#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080']
    # S1
    ax4[0].set_ylim((0, 1500))
    ax4[0].set_title('Scenario 1', **csfont, fontsize=textsize)
    ax4[0].set_ylabel('Charging power in kW', **csfont, fontsize=textsize)
    bplot4 = ax4[0].boxplot([chosen_power_s1_rb, chosen_power_s1], showfliers=False,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax4[0].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0].tick_params(labelsize=textsize)
    ax4[0].grid(True)
    ax4[0].axhline(250, color='#666666', linewidth=1.0)
    ax4[0].yaxis.set_major_locator(MultipleLocator(500))
    ax4[0].yaxis.set_minor_locator(MultipleLocator(250))
    # S2
    ax4[1].set_ylim((0, 1500))
    ax4[1].set_title('Scenario 2', **csfont, fontsize=textsize)
    bplot4 = ax4[1].boxplot([chosen_power_s2_rb, chosen_power_s2], showfliers=False,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_2):
        patch.set_facecolor(color)
    ax4[1].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1].tick_params(labelsize=textsize)
    ax4[1].tick_params(labelleft=False)
    ax4[1].grid(True)
    ax4[1].axhline(545, color='#666666', linewidth=1.0)
    ax4[1].yaxis.set_major_locator(MultipleLocator(500))
    ax4[1].yaxis.set_minor_locator(MultipleLocator(250))

    # S3
    ax4[2].set_ylim((0, 1500))
    ax4[2].set_title('Scenario 3', **csfont, fontsize=textsize)
    bplot4 = ax4[2].boxplot([chosen_power_s3_rb, chosen_power_s3], showfliers=False,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    ax4[2].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[2].tick_params(labelsize=textsize)
    ax4[2].tick_params(labelleft=False)
    ax4[2].grid(True)
    ax4[2].axhline(745, color='#666666', linewidth=1.0)
    ax4[2].yaxis.set_major_locator(MultipleLocator(500))
    ax4[2].yaxis.set_minor_locator(MultipleLocator(250))

    # S4
    ax4[3].set_ylim((0, 1500))
    ax4[3].set_title('Scenario 4', **csfont, fontsize=textsize)
    bplot4 = ax4[3].boxplot([chosen_power_s4_rb, chosen_power_s4], showfliers=False,
                            patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                            medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax4[3].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[3].tick_params(labelsize=textsize)
    ax4[3].tick_params(labelleft=False)
    ax4[3].grid(True)
    ax4[3].axhline(1250, color='#666666', linewidth=1.0)
    ax4[3].yaxis.set_major_locator(MultipleLocator(500))
    ax4[3].yaxis.set_minor_locator(MultipleLocator(250))
    plt.text(0.5, -0.25, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax4[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax4[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax4[2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.25, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax4[3].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # Analyse chosen power
    # Figure (9)
    height_in = width_in * 8 / 16
    FIGSIZE = (width_in, height_in)
    fig4, ax4 = plt.subplots(2, 4)
    fig4.set_size_inches(FIGSIZE)
    # fig4.tight_layout(h_pad=1)
    fig4.suptitle('CS 2 Charging Network - Charging power and stops', **csfont, fontsize=textsize)
    colors_1 = ['#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080']
    # S1
    ax4[0, 0].set_ylim((0, 1500))
    ax4[0, 0].set_title('Scenario 1', **csfont, fontsize=textsize)
    ax4[0, 0].set_ylabel('Charging power in kW', **csfont, fontsize=textsize)
    bplot4 = ax4[0, 0].boxplot([chosen_power_s1_rb, chosen_power_s1], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    # ax4[0, 0].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0, 0].tick_params(labelsize=textsize)
    ax4[0, 0].tick_params(labelbottom=False)
    ax4[0, 0].grid(True)
    ax4[0, 0].axhline(250, color='#666666', linewidth=1.0)
    ax4[0, 0].yaxis.set_major_locator(MultipleLocator(500))
    ax4[0, 0].yaxis.set_minor_locator(MultipleLocator(250))
    # S2
    ax4[0, 1].set_ylim((0, 1500))
    ax4[0, 1].set_title('Scenario 2', **csfont, fontsize=textsize)
    bplot4 = ax4[0, 1].boxplot([chosen_power_s2_rb, chosen_power_s2], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_2):
        patch.set_facecolor(color)
    # ax4[0, 1].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0, 1].tick_params(labelsize=textsize)
    ax4[0, 1].tick_params(labelleft=False, labelbottom=False)
    ax4[0, 1].grid(True)
    ax4[0, 1].axhline(545, color='#666666', linewidth=1.0)
    ax4[0, 1].yaxis.set_major_locator(MultipleLocator(500))
    ax4[0, 1].yaxis.set_minor_locator(MultipleLocator(250))

    # S3
    ax4[0, 2].set_ylim((0, 1500))
    ax4[0, 2].set_title('Scenario 3', **csfont, fontsize=textsize)
    bplot4 = ax4[0, 2].boxplot([chosen_power_s3_rb, chosen_power_s3], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    # ax4[0, 2].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0, 2].tick_params(labelsize=textsize)
    ax4[0, 2].tick_params(labelleft=False, labelbottom=False)
    ax4[0, 2].grid(True)
    ax4[0, 2].axhline(745, color='#666666', linewidth=1.0)
    ax4[0, 2].yaxis.set_major_locator(MultipleLocator(500))
    ax4[0, 2].yaxis.set_minor_locator(MultipleLocator(250))

    # S4
    ax4[0, 3].set_ylim((0, 1500))
    ax4[0, 3].set_title('Scenario 4', **csfont, fontsize=textsize)
    bplot4 = ax4[0, 3].boxplot([chosen_power_s4_rb, chosen_power_s4], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    # ax4[0, 3].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[0, 3].tick_params(labelsize=textsize)
    ax4[0, 3].tick_params(labelleft=False, labelbottom=False)
    ax4[0, 3].grid(True)
    ax4[0, 3].axhline(1250, color='#666666', linewidth=1.0)
    ax4[0, 3].yaxis.set_major_locator(MultipleLocator(500))
    ax4[0, 3].yaxis.set_minor_locator(MultipleLocator(250))
    plt.text(0.5, -0.1, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax4[0, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax4[0, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax4[0, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax4[0, 3].transAxes, fontsize=textsize, rotation=0)

    # S1
    ax4[1, 0].set_ylim((0, 5))
    # ax4[1, 0].set_title('Scenario 1', **csfont, fontsize=textsize)
    ax4[1, 0].set_ylabel('Number of stops', **csfont, fontsize=textsize)
    bplot4 = ax4[1, 0].boxplot([result_stops_s1_rb[:, 0], result_stops_s1[:, 0]], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax4[1, 0].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1, 0].tick_params(labelsize=textsize)
    ax4[1, 0].grid(True)
    ax4[1, 0].yaxis.set_major_locator(MultipleLocator(1))
    ax4[1, 0].yaxis.set_minor_locator(MultipleLocator(0.5))
    # S2
    ax4[1, 1].set_ylim((0, 5))
    # ax4[1, 1].set_title('Scenario 2', **csfont, fontsize=textsize)
    bplot4 = ax4[1, 1].boxplot([result_stops_s2_rb[:, 0], result_stops_s2[:, 0]], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_2):
        patch.set_facecolor(color)
    ax4[1, 1].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1, 1].tick_params(labelsize=textsize)
    ax4[1, 1].tick_params(labelleft=False)
    ax4[1, 1].grid(True)
    ax4[1, 1].yaxis.set_major_locator(MultipleLocator(1))
    ax4[1, 1].yaxis.set_minor_locator(MultipleLocator(0.5))

    # S3
    ax4[1, 2].set_ylim((0, 5))
    # ax4[1, 2].set_title('Scenario 3', **csfont, fontsize=textsize)
    bplot4 = ax4[1, 2].boxplot([result_stops_s3_rb[:, 0], result_stops_s3[:, 0]], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    ax4[1, 2].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1, 2].tick_params(labelsize=textsize)
    ax4[1, 2].tick_params(labelleft=False)
    ax4[1, 2].grid(True)
    ax4[1, 2].yaxis.set_major_locator(MultipleLocator(1))
    ax4[1, 2].yaxis.set_minor_locator(MultipleLocator(0.5))

    # S4
    ax4[1, 3].set_ylim((0, 5))
    # ax4[1, 3].set_title('Scenario 4', **csfont, fontsize=textsize)
    bplot4 = ax4[1, 3].boxplot([result_stops_s4_rb[:, 0], result_stops_s4[:, 0]], showfliers=False,
                               patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                               medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax4[1, 3].set_xticklabels(labels=["NGS", "BETOS"])
    ax4[1, 3].tick_params(labelsize=textsize)
    ax4[1, 3].tick_params(labelleft=False)
    ax4[1, 3].grid(True)
    ax4[1, 3].yaxis.set_major_locator(MultipleLocator(1))
    ax4[1, 3].yaxis.set_minor_locator(MultipleLocator(0.5))
    plt.text(0.5, -0.3, '(e)', horizontalalignment='center', verticalalignment='center', transform=ax4[1, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.3, '(f)', horizontalalignment='center', verticalalignment='center', transform=ax4[1, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.3, '(g)', horizontalalignment='center', verticalalignment='center', transform=ax4[1, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.3, '(h)', horizontalalignment='center', verticalalignment='center', transform=ax4[1, 3].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # __________________________________________________________________________________________________________________
    # Section 4.3
    # Read Data Time Loss
    # Scenario 4:
    result_time_loss_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s4.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s41 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_time_loss_s41.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s42 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_time_loss_s42.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s43 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_time_loss_s43.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s44 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_time_loss_s44.csv', delimiter=None, header=None).to_numpy()

    result_time_loss_s4_rb = pandas.read_csv( 'Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s4_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s41_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_time_loss_s41_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s42_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_time_loss_s42_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s43_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_time_loss_s43_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s44_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_time_loss_s44_rb.csv', delimiter=None, header=None).to_numpy()

    time_loss_s4 = (result_time_loss_s4[:, 0]) * 60
    time_loss_s41 = result_time_loss_s41[:, 0] * 60
    time_loss_s42 = result_time_loss_s42[:, 0] * 60
    time_loss_s43 = result_time_loss_s43[:, 0] * 60
    time_loss_s44 = result_time_loss_s44[:, 0] * 60

    time_loss_s4_rb = (result_time_loss_s4_rb[:, 0]) * 60
    time_loss_s4_rb = time_loss_s4_rb[~np.isnan(time_loss_s4_rb)]
    time_loss_s41_rb = (result_time_loss_s41_rb[:, 0]) * 60
    time_loss_s41_rb = time_loss_s41_rb[~np.isnan(time_loss_s41_rb)]
    time_loss_s42_rb = (result_time_loss_s42_rb[:, 0]) * 60
    time_loss_s42_rb = time_loss_s42_rb[~np.isnan(time_loss_s42_rb)]
    time_loss_s43_rb = (result_time_loss_s43_rb[:, 0]) * 60
    time_loss_s43_rb = time_loss_s43_rb[~np.isnan(time_loss_s43_rb)]
    time_loss_s44_rb = (result_time_loss_s44_rb[:, 0]) * 60
    time_loss_s44_rb = time_loss_s44_rb[~np.isnan(time_loss_s44_rb)]

    # Read data Waiting events
    events_wait_s41 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_wait_count_s41.csv', delimiter=None, header=None).to_numpy()
    events_wait_s41 = events_wait_s41[:, 0]
    events_wait_s42 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_wait_count_s42.csv', delimiter=None, header=None).to_numpy()
    events_wait_s42 = events_wait_s42[:, 0]
    events_wait_s43 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_wait_count_s43.csv', delimiter=None, header=None).to_numpy()
    events_wait_s43 = events_wait_s43[:, 0]
    events_wait_s44 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_wait_count_s44.csv', delimiter=None, header=None).to_numpy()
    events_wait_s44 = events_wait_s44[:, 0]

    events_wait_s41_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_wait_count_s41_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s41_rb = events_wait_s41_rb[:, 0]
    events_wait_s42_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_wait_count_s42_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s42_rb = events_wait_s42_rb[:, 0]
    events_wait_s43_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_wait_count_s43_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s43_rb = events_wait_s43_rb[:, 0]
    events_wait_s44_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_wait_count_s44_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s44_rb = events_wait_s44_rb[:, 0]

    # Read Data Availabilty
    ava_s41 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_ava_poi_s41.csv', delimiter=None, header=None).to_numpy()
    ava_s41 = ava_s41[:, 0]
    ava_s42 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_ava_poi_s42.csv', delimiter=None, header=None).to_numpy()
    ava_s42 = ava_s42[:, 0]
    ava_s43 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_ava_poi_s43.csv', delimiter=None, header=None).to_numpy()
    ava_s43 = ava_s43[:, 0]
    ava_s44 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_ava_poi_s44.csv', delimiter=None, header=None).to_numpy()
    ava_s44 = ava_s44[:, 0]

    ava_s41_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_ava_poi_s41_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s41_rb = ava_s41_rb[:, 0]
    ava_s42_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_ava_poi_s42_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s42_rb = ava_s42_rb[:, 0]
    ava_s43_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_ava_poi_s43_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s43_rb = ava_s43_rb[:, 0]
    ava_s44_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_ava_poi_s44_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s44_rb = ava_s44_rb[:, 0]

    # Read Data Power
    power_s41 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_power_s41.csv', delimiter=None, header=None).to_numpy()
    power_s41 = power_s41[:, 0]
    power_s42 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_power_s42.csv', delimiter=None, header=None).to_numpy()
    power_s42 = power_s42[:, 0]
    power_s43 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_power_s43.csv', delimiter=None, header=None).to_numpy()
    power_s43 = power_s43[:, 0]
    power_s44 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_power_s44.csv', delimiter=None, header=None).to_numpy()
    power_s44 = power_s44[:, 0]
    power_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4.csv', delimiter=None, header=None).to_numpy()
    power_s4 = power_s4[:, 0]

    power_s41_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_power_s41_rb.csv', delimiter=None, header=None).to_numpy()
    power_s41_rb = power_s41_rb[:, 0]
    power_s42_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_power_s42_rb.csv', delimiter=None,header=None).to_numpy()
    power_s42_rb = power_s42_rb[:, 0]
    power_s43_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_power_s43_rb.csv', delimiter=None, header=None).to_numpy()
    power_s43_rb = power_s43_rb[:, 0]
    power_s44_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_power_s44_rb.csv', delimiter=None, header=None).to_numpy()
    power_s44_rb = power_s44_rb[:, 0]
    power_s4_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4_rb.csv', delimiter=None, header=None).to_numpy()
    power_s4_rb = power_s4_rb[:, 0]

    # Scenario 3:
    result_time_loss_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s31 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_time_loss_s31.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s32 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_time_loss_s32.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s33 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_time_loss_s33.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s34 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_time_loss_s34.csv', delimiter=None,header=None).to_numpy()

    result_time_loss_s3_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s31_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_time_loss_s31_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s32_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_time_loss_s32_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s33_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_time_loss_s33_rb.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s34_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_time_loss_s34_rb.csv', delimiter=None, header=None).to_numpy()

    time_loss_s3 = (result_time_loss_s3[:, 0]) * 60
    time_loss_s31 = result_time_loss_s31[:, 0] * 60
    time_loss_s32 = result_time_loss_s32[:, 0] * 60
    time_loss_s33 = result_time_loss_s33[:, 0] * 60
    time_loss_s34 = result_time_loss_s34[:, 0] * 60

    time_loss_s3_rb = (result_time_loss_s3_rb[:, 0]) * 60
    time_loss_s3_rb = time_loss_s3_rb[~np.isnan(time_loss_s3_rb)]
    time_loss_s31_rb = (result_time_loss_s31_rb[:, 0]) * 60
    time_loss_s31_rb = time_loss_s31_rb[~np.isnan(time_loss_s31_rb)]
    time_loss_s32_rb = (result_time_loss_s32_rb[:, 0]) * 60
    time_loss_s32_rb = time_loss_s32_rb[~np.isnan(time_loss_s32_rb)]
    time_loss_s33_rb = (result_time_loss_s33_rb[:, 0]) * 60
    time_loss_s33_rb = time_loss_s33_rb[~np.isnan(time_loss_s33_rb)]
    time_loss_s34_rb = (result_time_loss_s34_rb[:, 0]) * 60
    time_loss_s34_rb = time_loss_s34_rb[~np.isnan(time_loss_s34_rb)]

    # Read data Waiting events
    events_wait_s31 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_wait_count_s31.csv', delimiter=None, header=None).to_numpy()
    events_wait_s31 = events_wait_s31[:, 0]
    events_wait_s32 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_wait_count_s32.csv', delimiter=None, header=None).to_numpy()
    events_wait_s32 = events_wait_s32[:, 0]
    events_wait_s33 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_wait_count_s33.csv', delimiter=None, header=None).to_numpy()
    events_wait_s33 = events_wait_s33[:, 0]
    events_wait_s34 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_wait_count_s34.csv', delimiter=None, header=None).to_numpy()
    events_wait_s34 = events_wait_s34[:, 0]

    events_wait_s31_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_wait_count_s31_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s31_rb = events_wait_s31_rb[:, 0]
    events_wait_s32_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_wait_count_s32_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s32_rb = events_wait_s32_rb[:, 0]
    events_wait_s33_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_wait_count_s33_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s33_rb = events_wait_s33_rb[:, 0]
    events_wait_s34_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_wait_count_s34_rb.csv', delimiter=None, header=None).to_numpy()
    events_wait_s34_rb = events_wait_s34_rb[:, 0]

    # Read Data Availabilty
    ava_s31 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_ava_poi_s31.csv', delimiter=None, header=None).to_numpy()
    ava_s31 = ava_s31[:, 0]
    ava_s32 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_ava_poi_s32.csv', delimiter=None, header=None).to_numpy()
    ava_s32 = ava_s32[:, 0]
    ava_s33 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_ava_poi_s33.csv', delimiter=None, header=None).to_numpy()
    ava_s33 = ava_s33[:, 0]
    ava_s34 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_ava_poi_s34.csv', delimiter=None, header=None).to_numpy()
    ava_s34 = ava_s34[:, 0]

    ava_s31_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_ava_poi_s31_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s31_rb = ava_s31_rb[:, 0]
    ava_s32_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_ava_poi_s32_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s32_rb = ava_s32_rb[:, 0]
    ava_s33_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_ava_poi_s33_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s33_rb = ava_s33_rb[:, 0]
    ava_s34_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_ava_poi_s34_rb.csv', delimiter=None, header=None).to_numpy()
    ava_s34_rb = ava_s34_rb[:, 0]

    # Read Data Power
    power_s31 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_power_s31.csv', delimiter=None, header=None).to_numpy()
    power_s31 = power_s31[:, 0]
    power_s32 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_power_s32.csv', delimiter=None, header=None).to_numpy()
    power_s32 = power_s32[:, 0]
    power_s33 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_power_s33.csv', delimiter=None, header=None).to_numpy()
    power_s33 = power_s33[:, 0]
    power_s34 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_power_s34.csv', delimiter=None, header=None).to_numpy()
    power_s34 = power_s34[:, 0]
    power_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/power_s3.csv', delimiter=None, header=None).to_numpy()
    power_s3 = power_s3[:, 0]
    power_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4.csv', delimiter=None, header=None).to_numpy()
    power_s4 = power_s4[:, 0]

    power_s31_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1_AD/result_power_s31_rb.csv', delimiter=None, header=None).to_numpy()
    power_s31_rb = power_s31_rb[:, 0]
    power_s32_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2_AD/result_power_s32_rb.csv', delimiter=None, header=None).to_numpy()
    power_s32_rb = power_s32_rb[:, 0]
    power_s33_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3_AD/result_power_s33_rb.csv', delimiter=None, header=None).to_numpy()
    power_s33_rb = power_s33_rb[:, 0]
    power_s34_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_power_s34_rb.csv', delimiter=None, header=None).to_numpy()
    power_s34_rb = power_s34_rb[:, 0]
    power_s3_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/power_s3_rb.csv', delimiter=None, header=None).to_numpy()
    power_s3_rb = power_s3_rb[:, 0]
    power_s4_rb = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/power_s4_rb.csv', delimiter=None, header=None).to_numpy()
    power_s4_rb = power_s4_rb[:, 0]

    # Global Figure Setup
    # Set up Plot Parameter
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 8 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9

    # Additional Time
    fig, ax = plt.subplots(2, 5)
    fig.set_size_inches(FIGSIZE)
    fig.suptitle('CS 3 Real World - Additional time per trip', **csfont, fontsize=textsize, y=1)
    medianprops = dict(linewidth=0, color='black')
    meanprop = dict(linewidth=1, color='black', linestyle='-')
    flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='black')
    colors_1 = ['#aa4465', '#808080']
    # Driver
    ax[0, 0].set_ylabel('Time loss in min', **csfont, fontsize=textsize)
    ax[0, 0].set_ylim((0, 160))
    ax[0, 0].set_title('Real World 1', **csfont, fontsize=textsize)
    bplot4 = ax[0, 0].boxplot([time_loss_s31_rb, time_loss_s41_rb], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 0].tick_params(labelsize=textsize)
    ax[0, 0].grid(True)
    ax[0, 0].set_xticklabels([])
    ax[0, 0].yaxis.set_major_locator(MultipleLocator(40))
    ax[0, 0].yaxis.set_minor_locator(MultipleLocator(20))
    plt.text(-0.65, 0.5, 'NGS', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes,
             fontsize=textsize, rotation=90)

    ax[0, 1].set_ylim((0, 160))
    ax[0, 1].set_title('Real World 2', **csfont, fontsize=textsize)
    bplot4 = ax[0, 1].boxplot([time_loss_s32_rb, time_loss_s42_rb], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 1].tick_params(labelsize=9, labelleft=False)
    ax[0, 1].set_xticklabels([])
    ax[0, 1].yaxis.set_major_locator(MultipleLocator(40))
    ax[0, 1].yaxis.set_minor_locator(MultipleLocator(20))
    ax[0, 1].grid(True)

    ax[0, 2].set_ylim((0, 160))
    ax[0, 2].set_title('Real World 3', **csfont, fontsize=textsize)
    bplot4 = ax[0, 2].boxplot([time_loss_s33_rb, time_loss_s43_rb], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 2].grid(True)
    ax[0, 2].yaxis.set_major_locator(MultipleLocator(40))
    ax[0, 2].yaxis.set_minor_locator(MultipleLocator(20))
    ax[0, 2].set_xticklabels([])

    ax[0, 3].set_ylim((0, 160))
    ax[0, 3].set_title('Real World 4', **csfont, fontsize=textsize)
    bplot4 = ax[0, 3].boxplot([time_loss_s34_rb, time_loss_s44_rb], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 3].grid(True)
    ax[0, 3].yaxis.set_major_locator(MultipleLocator(40))
    ax[0, 3].yaxis.set_minor_locator(MultipleLocator(20))
    ax[0, 3].set_xticklabels([])

    ax[0, 4].set_ylim((0, 160))
    ax[0, 4].set_title('Ideal', **csfont, fontsize=9)
    bplot4 = ax[0, 4].boxplot([time_loss_s3_rb, time_loss_s4_rb], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 4].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 4].grid(True)
    ax[0, 4].yaxis.set_major_locator(MultipleLocator(40))
    ax[0, 4].yaxis.set_minor_locator(MultipleLocator(20))
    ax[0, 4].set_xticklabels([])

    # BETOS
    ax[1, 0].set_ylabel('Time loss in min', **csfont, fontsize=textsize)
    ax[1, 0].set_ylim((0, 160))
    bplot4 = ax[1, 0].boxplot([time_loss_s31, time_loss_s41], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 0].set_xticklabels(labels=["S3-1", "S4-1"], rotation=90)
    ax[1, 0].tick_params(labelsize=textsize)
    ax[1, 0].grid(True)
    ax[1, 0].yaxis.set_minor_locator(MultipleLocator(20))
    ax[1, 0].yaxis.set_major_locator(MultipleLocator(40))
    plt.text(-0.65, 0.5, 'BETOS', horizontalalignment='center', verticalalignment='center',
             transform=ax[1, 0].transAxes, fontsize=textsize, rotation=90)

    ax[1, 1].set_ylim((0, 160))
    bplot4 = ax[1, 1].boxplot([time_loss_s32, time_loss_s42], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 1].set_xticklabels(labels=["S3-2", "S4-2"], rotation=90)
    ax[1, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 1].grid(True)
    ax[1, 1].yaxis.set_minor_locator(MultipleLocator(20))
    ax[1, 1].yaxis.set_major_locator(MultipleLocator(40))

    ax[1, 2].set_ylim((0, 160))
    bplot4 = ax[1, 2].boxplot([time_loss_s33, time_loss_s43], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 2].set_xticklabels(labels=["S3-3", "S4-3"], rotation=90)
    ax[1, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 2].grid(True)
    ax[1, 2].yaxis.set_minor_locator(MultipleLocator(20))
    ax[1, 2].yaxis.set_major_locator(MultipleLocator(40))

    ax[1, 3].set_ylim((0, 160))
    bplot4 = ax[1, 3].boxplot([time_loss_s34, time_loss_s44], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 3].set_xticklabels(labels=["S3-4", "S4-4"], rotation=90)
    ax[1, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 3].grid(True)
    ax[1, 3].yaxis.set_minor_locator(MultipleLocator(20))
    ax[1, 3].yaxis.set_major_locator(MultipleLocator(40))

    ax[1, 4].set_ylim((0, 160))
    bplot4 = ax[1, 4].boxplot([time_loss_s3, time_loss_s4], showfliers=True, flierprops=flierprops,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 4].set_xticklabels(labels=["S3", "S4"], rotation=90)
    ax[1, 4].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 4].grid(True)
    ax[1, 4].yaxis.set_minor_locator(MultipleLocator(20))
    ax[1, 4].yaxis.set_major_locator(MultipleLocator(40))

    plt.text(0.5, -0.1, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 3].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(e)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 4].transAxes, fontsize=textsize, rotation=0)

    plt.text(0.5, -0.35, '(f)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(g)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(h)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(i)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 3].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(j)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 4].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # Mean chosen Power
    fig, ax = plt.subplots(2, 5)
    fig.set_size_inches(FIGSIZE)
    fig.suptitle('CS 3 Real World - Average chosen charging power', **csfont, fontsize=textsize, y=1)
    colors_1 = ['#aa4465', '#808080']
    power = [745, 1250]

    # Driver
    ax[0, 0].set_ylabel('Power in kW', **csfont, fontsize=textsize)
    ax[0, 0].set_ylim((0, 1500))
    ax[0, 0].set_title('Real World 1', **csfont, fontsize=textsize)
    bplot4 = ax[0, 0].boxplot([power_s31_rb, power_s41_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 0].tick_params(labelsize=textsize)
    ax[0, 0].grid(True)
    ax[0, 0].set_xticklabels([])
    ax[0, 0].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[0, 0].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[0, 0].yaxis.set_major_locator(MultipleLocator(500))
    ax[0, 0].yaxis.set_minor_locator(MultipleLocator(250))
    plt.text(-0.7, 0.5, 'NGS', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes,
             fontsize=textsize, rotation=90)

    ax[0, 1].set_ylim((0, 1500))
    ax[0, 1].set_title('Real World 2', **csfont, fontsize=textsize)
    bplot4 = ax[0, 1].boxplot([power_s32_rb, power_s42_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 1].grid(True)
    ax[0, 1].set_xticklabels([])
    ax[0, 1].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[0, 1].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[0, 1].yaxis.set_major_locator(MultipleLocator(500))
    ax[0, 1].yaxis.set_minor_locator(MultipleLocator(250))

    ax[0, 2].set_ylim((0, 1500))
    ax[0, 2].set_title('Real World 3', **csfont, fontsize=textsize)
    bplot4 = ax[0, 2].boxplot([power_s33_rb, power_s43_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 2].grid(True)
    ax[0, 2].set_xticklabels([])
    ax[0, 2].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[0, 2].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[0, 2].yaxis.set_major_locator(MultipleLocator(500))
    ax[0, 2].yaxis.set_minor_locator(MultipleLocator(250))

    ax[0, 3].set_ylim((0, 1500))
    ax[0, 3].set_title('Real World', **csfont, fontsize=textsize)
    bplot4 = ax[0, 3].boxplot([power_s34_rb, power_s44_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 3].grid(True)
    ax[0, 3].set_xticklabels([])
    ax[0, 3].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[0, 3].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[0, 3].yaxis.set_major_locator(MultipleLocator(500))
    ax[0, 3].yaxis.set_minor_locator(MultipleLocator(250))

    ax[0, 4].set_ylim((0, 1500))
    ax[0, 4].set_title('Ideal', **csfont, fontsize=textsize)
    bplot4 = ax[0, 4].boxplot([power_s3_rb, power_s4_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 4].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 4].grid(True)
    ax[0, 4].set_xticklabels([])
    ax[0, 4].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[0, 4].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[0, 4].yaxis.set_major_locator(MultipleLocator(500))
    ax[0, 4].yaxis.set_minor_locator(MultipleLocator(250))

    # BETOS
    ax[1, 0].set_ylabel('Power in kW', **csfont, fontsize=textsize)
    ax[1, 0].set_ylim((0, 1500))
    bplot4 = ax[1, 0].boxplot([power_s31, power_s41], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 0].set_xticklabels(labels=["S3-1", "S4-1"], rotation=90)
    ax[1, 0].tick_params(labelsize=textsize)
    ax[1, 0].grid(True)
    plt.text(-0.7, 0.5, 'BETOS', horizontalalignment='center', verticalalignment='center', transform=ax[1, 0].transAxes,
             fontsize=textsize, rotation=90)
    ax[1, 0].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[1, 0].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[1, 0].yaxis.set_major_locator(MultipleLocator(500))
    ax[1, 0].yaxis.set_minor_locator(MultipleLocator(250))

    ax[1, 1].set_ylim((0, 1500))
    bplot4 = ax[1, 1].boxplot([power_s32, power_s42], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 1].set_xticklabels(labels=["S3-2", "S4-2"], rotation=90)
    ax[1, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 1].grid(True)
    ax[1, 1].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[1, 1].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[1, 1].yaxis.set_major_locator(MultipleLocator(500))
    ax[1, 1].yaxis.set_minor_locator(MultipleLocator(250))

    ax[1, 2].set_ylim((0, 1500))
    bplot4 = ax[1, 2].boxplot([power_s33, power_s43], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 2].set_xticklabels(labels=["S3-3", "S4-3"], rotation=90)
    ax[1, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 2].grid(True)
    ax[1, 2].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[1, 2].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[1, 2].yaxis.set_major_locator(MultipleLocator(500))
    ax[1, 2].yaxis.set_minor_locator(MultipleLocator(250))

    ax[1, 3].set_ylim((0, 1500))
    bplot4 = ax[1, 3].boxplot([power_s34, power_s44], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 3].set_xticklabels(labels=["S3-4", "S4-4"], rotation=90)
    ax[1, 3].tick_params(labelsize=9, labelleft=False)
    ax[1, 3].grid(True)
    ax[1, 3].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[1, 3].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[1, 3].yaxis.set_major_locator(MultipleLocator(500))
    ax[1, 3].yaxis.set_minor_locator(MultipleLocator(250))

    ax[1, 4].set_ylim((0, 1500))
    bplot4 = ax[1, 4].boxplot([power_s3, power_s4], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 4].set_xticklabels(labels=["S3", "S4"], rotation=90)
    ax[1, 4].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 4].grid(True)
    ax[1, 4].axhline(power[1], color=colors_1[1], linewidth=1.0)
    ax[1, 4].axhline(power[0], color=colors_1[0], linewidth=1.0)
    ax[1, 4].yaxis.set_major_locator(MultipleLocator(500))
    ax[1, 4].yaxis.set_minor_locator(MultipleLocator(250))

    plt.text(0.5, -0.1, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 3].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(e)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 4].transAxes, fontsize=textsize, rotation=0)

    plt.text(0.5, -0.35, '(f)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(g)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(h)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(i)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 3].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(j)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 4].transAxes, fontsize=textsize, rotation=0)
    plt.show()

    # Mean availability of chosen POI
    fig, ax = plt.subplots(2, 4)
    fig.set_size_inches(FIGSIZE)
    colors_1 = ['#aa4465', '#808080']
    ava = [0.35, 0.51, 0.74, 0.2, 0.3, 0.65, 0.88, 0.75]
    # Driver
    ax[0, 0].set_ylabel('Average availability', **csfont, fontsize=textsize)
    ax[0, 0].set_ylim((0, 1))
    ax[0, 0].set_title('Real World 1', **csfont, fontsize=textsize)
    bplot4 = ax[0, 0].boxplot([ava_s31_rb, ava_s41_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 0].tick_params(labelsize=textsize)
    ax[0, 0].grid(True)
    ax[0, 0].set_xticklabels([])
    plt.text(-0.52, 0.5, 'NGS', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes,
             fontsize=textsize, rotation=90)
    ax[0, 0].axhline(ava[0], color=colors_1[0], linewidth=1.0)
    ax[0, 0].axhline(ava[3], color=colors_1[1], linewidth=1.0)
    ax[0, 0].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[0, 1].set_ylim((0, 1))
    ax[0, 1].set_title('Real World 2', **csfont, fontsize=textsize)
    bplot4 = ax[0, 1].boxplot([ava_s32_rb, ava_s42_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 1].grid(True)
    ax[0, 1].set_xticklabels([])
    ax[0, 1].axhline(ava[1], color=colors_1[0], linewidth=1.0)
    ax[0, 1].axhline(ava[4], color=colors_1[1], linewidth=1.0)
    ax[0, 1].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[0, 2].set_ylim((0, 1))
    ax[0, 2].set_title('Real World 3', **csfont, fontsize=textsize)
    bplot4 = ax[0, 2].boxplot([ava_s33_rb, ava_s43_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 2].grid(True)
    ax[0, 2].set_xticklabels([])
    ax[0, 2].axhline(ava[2], color=colors_1[0], linewidth=1.0)
    ax[0, 2].axhline(ava[5], color=colors_1[1], linewidth=1.0)
    ax[0, 2].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[0, 3].set_ylim((0, 1))
    ax[0, 3].set_title('Real World 4', **csfont, fontsize=textsize)
    bplot4 = ax[0, 3].boxplot([ava_s34_rb, ava_s44_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 3].grid(True)
    ax[0, 3].set_xticklabels([])
    ax[0, 3].axhline(ava[6], color=colors_1[0], linewidth=1.0)
    ax[0, 3].axhline(ava[7], color=colors_1[1], linewidth=1.0)
    ax[0, 3].yaxis.set_minor_locator(MultipleLocator(0.1))

    # BETOS
    ax[1, 0].set_ylabel('Average availability', **csfont, fontsize=textsize)
    ax[1, 0].set_ylim((0, 1))
    bplot4 = ax[1, 0].boxplot([ava_s31, ava_s41], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 0].set_xticklabels(labels=["S3-1", "S4-1"], rotation=90)
    ax[1, 0].tick_params(labelsize=9)
    ax[1, 0].grid(True)
    plt.text(-0.52, 0.5, 'BETOS', horizontalalignment='center', verticalalignment='center',
             transform=ax[1, 0].transAxes, fontsize=textsize, rotation=90)
    ax[1, 0].axhline(ava[0], color=colors_1[0], linewidth=1.0)
    ax[1, 0].axhline(ava[3], color=colors_1[1], linewidth=1.0)
    ax[1, 0].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[1, 1].set_ylim((0, 1))
    bplot4 = ax[1, 1].boxplot([ava_s32, ava_s42], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 1].set_xticklabels(labels=["S3-2", "S4-2"], rotation=90)
    ax[1, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 1].grid(True)
    ax[1, 1].axhline(ava[1], color=colors_1[0], linewidth=1.0)
    ax[1, 1].axhline(ava[4], color=colors_1[1], linewidth=1.0)
    ax[1, 1].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[1, 2].set_ylim((0, 1))
    bplot4 = ax[1, 2].boxplot([ava_s33, ava_s43], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 2].set_xticklabels(labels=["S3-3", "S4-3"], rotation=90)
    ax[1, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 2].grid(True)
    ax[1, 2].axhline(ava[2], color=colors_1[0], linewidth=1.0)
    ax[1, 2].axhline(ava[5], color=colors_1[1], linewidth=1.0)
    ax[1, 2].yaxis.set_minor_locator(MultipleLocator(0.1))

    ax[1, 3].set_ylim((0, 1))
    bplot4 = ax[1, 3].boxplot([ava_s34, ava_s44], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 3].set_xticklabels(labels=["S3-3", "S4-3"], rotation=90)
    ax[1, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 3].grid(True)
    ax[1, 3].axhline(ava[6], color=colors_1[0], linewidth=1.0)
    ax[1, 3].axhline(ava[7], color=colors_1[1], linewidth=1.0)
    ax[1, 3].yaxis.set_minor_locator(MultipleLocator(0.1))

    plt.text(0.5, -0.1, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 3].transAxes, fontsize=textsize, rotation=0)

    plt.text(0.5, -0.35, '(e)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(f)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(g)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(h)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 3].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # Mean number of waiting events per trip
    fig, ax = plt.subplots(2, 4)
    fig.set_size_inches(FIGSIZE)
    fig.suptitle('CS 3 - Real World - Waiting events per trip', **csfont, fontsize=textsize, y=1.0)
    colors_1 = ['#aa4465', '#808080']
    # Driver
    ax[0, 0].set_ylabel('Number of waiting events', **csfont, fontsize=textsize)
    ax[0, 0].set_ylim((0, 5))
    ax[0, 0].set_title('Real World 1', **csfont, fontsize=textsize)
    bplot4 = ax[0, 0].boxplot([events_wait_s31_rb, events_wait_s41_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 0].tick_params(labelsize=textsize)
    ax[0, 0].grid(True)
    ax[0, 0].set_xticklabels([])
    ax[0, 0].yaxis.set_minor_locator(MultipleLocator(1))
    plt.text(-0.45, 0.5, 'NGS', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes,
             fontsize=textsize, rotation=90)

    ax[0, 1].set_ylim((0, 5))
    ax[0, 1].set_title('Real World 2', **csfont, fontsize=textsize)
    bplot4 = ax[0, 1].boxplot([events_wait_s32_rb, events_wait_s42_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 1].grid(True)
    ax[0, 1].set_xticklabels([])
    ax[0, 1].yaxis.set_minor_locator(MultipleLocator(1))

    ax[0, 2].set_ylim((0, 5))
    ax[0, 2].set_title('Real World 3', **csfont, fontsize=textsize)
    bplot4 = ax[0, 2].boxplot([events_wait_s33_rb, events_wait_s43_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 2].grid(True)
    ax[0, 2].set_xticklabels([])
    ax[0, 2].yaxis.set_minor_locator(MultipleLocator(1))

    ax[0, 3].set_ylim((0, 5))
    ax[0, 3].set_title('Real World 4', **csfont, fontsize=textsize)
    bplot4 = ax[0, 3].boxplot([events_wait_s34_rb, events_wait_s44_rb], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[0, 3].grid(True)
    ax[0, 3].set_xticklabels([])
    ax[0, 3].yaxis.set_minor_locator(MultipleLocator(1))

    # BETOS
    ax[1, 0].set_ylabel('Number of waiting events', **csfont, fontsize=textsize)
    ax[1, 0].set_ylim((0, 5))
    bplot4 = ax[1, 0].boxplot([events_wait_s31, events_wait_s41], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 0].set_xticklabels(labels=["S3-1", "S4-1"], rotation=90)
    ax[1, 0].tick_params(labelsize=textsize)
    ax[1, 0].grid(True)
    ax[1, 0].yaxis.set_minor_locator(MultipleLocator(1))
    plt.text(-0.45, 0.5, 'BETOS', horizontalalignment='center', verticalalignment='center',
             transform=ax[1, 0].transAxes, fontsize=9, rotation=90)

    ax[1, 1].set_ylim((0, 5))
    bplot4 = ax[1, 1].boxplot([events_wait_s32, events_wait_s42], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 1].set_xticklabels(labels=["S3-2", "S4-2"], rotation=90)
    ax[1, 1].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 1].grid(True)
    ax[1, 1].yaxis.set_minor_locator(MultipleLocator(1))

    ax[1, 2].set_ylim((0, 5))
    bplot4 = ax[1, 2].boxplot([events_wait_s33, events_wait_s43], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 2].set_xticklabels(labels=["S3-3", "S4-3"], rotation=90)
    ax[1, 2].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 2].grid(True)
    ax[1, 2].yaxis.set_minor_locator(MultipleLocator(1))

    ax[1, 3].set_ylim((0, 5))
    bplot4 = ax[1, 3].boxplot([events_wait_s34, events_wait_s44], showfliers=False,
                              patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                              medianprops=medianprops, widths=(0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[1, 3].set_xticklabels(labels=["S3-4", "S4-4"], rotation=90)
    ax[1, 3].tick_params(labelsize=textsize, labelleft=False)
    ax[1, 3].grid(True)
    ax[1, 3].yaxis.set_minor_locator(MultipleLocator(1))
    plt.text(0.5, -0.1, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.1, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[0, 3].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(e)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(f)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(g)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(h)', horizontalalignment='center', verticalalignment='center', transform=ax[1, 3].transAxes, fontsize=textsize, rotation=0)

    plt.show()
    # __________________________________________________________________________________________________________________
    # Section 5 Sensitivity Analysis
    # Import Data:
    result_time_loss_s1_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s1_100.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s1 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_1/result_time_loss_s1.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s1_80 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s1_80.csv', delimiter=None, header=None).to_numpy()
    time_loss_s1_100 = (result_time_loss_s1_100[:, 0]) * 60
    time_loss_s1 = (result_time_loss_s1[:, 0]) * 60
    time_loss_s1_80 = (result_time_loss_s1_80[:, 0]) * 60

    result_time_loss_s2_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s2_100.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s2 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_2/result_time_loss_s2.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s2_80 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s2_80.csv', delimiter=None, header=None).to_numpy()
    time_loss_s2_100 = (result_time_loss_s2_100[:, 0]) * 60
    time_loss_s2 = (result_time_loss_s2[:, 0]) * 60
    time_loss_s2_80 = (result_time_loss_s2_80[:, 0]) * 60

    result_time_loss_s3_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s3_100.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s3 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_3/result_time_loss_s3.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s3_80 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s3_80.csv', delimiter=None, header=None).to_numpy()
    time_loss_s3_100 = result_time_loss_s3_100[:, 0] * 60
    time_loss_s3 = (result_time_loss_s3[:, 0]) * 60
    time_loss_s3_80 = (result_time_loss_s3_80[:, 0]) * 60

    result_time_loss_s4_100 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s4_100.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s4 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4/result_time_loss_s4.csv', delimiter=None, header=None).to_numpy()
    result_time_loss_s4_80 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s4_80.csv', delimiter=None, header=None).to_numpy()
    time_loss_s4_100 = (result_time_loss_s4_100[:, 0]) * 60
    time_loss_s4 = (result_time_loss_s4[:, 0]) * 60
    time_loss_s4_80 = (result_time_loss_s4_80[:, 0]) * 60

    result_time_loss_s51_ni = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s51_ni.csv', delimiter=None, header=None).to_numpy()
    time_loss_s51_ni = (result_time_loss_s51_ni[:, 0]) * 60
    result_time_loss_s51 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Scenario_4_AD/result_time_loss_s34.csv', delimiter=None, header=None).to_numpy()
    time_loss_s51 = (result_time_loss_s51[:, 0]) * 60

    result_time_loss_s52_ni = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s52_ni.csv', delimiter=None, header=None).to_numpy()
    time_loss_s52_ni = (result_time_loss_s52_ni[:, 0]) * 60
    result_time_loss_s52 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s52.csv', delimiter=None, header=None).to_numpy()
    time_loss_s52 = (result_time_loss_s52[:, 0]) * 60

    result_time_loss_s53_ni = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s53_ni.csv', delimiter=None, header=None).to_numpy()
    time_loss_s53_ni = (result_time_loss_s53_ni[:, 0]) * 60
    result_time_loss_s53 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s53.csv', delimiter=None, header=None).to_numpy()
    time_loss_s53 = (result_time_loss_s53[:, 0]) * 60

    result_time_loss_s54_ni = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s54_ni.csv', delimiter=None,header=None).to_numpy()
    time_loss_s54_ni = (result_time_loss_s54_ni[:, 0]) * 60
    result_time_loss_s54 = pandas.read_csv('Modules/M13_SimulationTask/M13_Results/Paper_no2/Sensitivity/result_time_loss_s54.csv', delimiter=None, header=None).to_numpy()
    time_loss_s54 = (result_time_loss_s54[:, 0]) * 60

    # Figure Layout
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    width_in = 14 / 2.54
    height_in = width_in * 7 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9
    # Colors
    medianprops = dict(linewidth=0, color='black')
    meanprop = dict(linewidth=1, color='black', linestyle='-')
    colors_1 = ['#6c969d', '#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080', '#808080']

    # 5.1 Information Loss
    fig, ax = plt.subplots(1, 3)
    fig.set_size_inches(FIGSIZE)
    fig.tight_layout()
    fig.suptitle('Sensitivity analysis - Information loss (BETOS)', **csfont, fontsize=textsize, y=1.0)
    ax[0].set_ylim((0, 100))
    ax[0].set_ylabel('Time in min', **csfont, fontsize=textsize)
    bplot4 = ax[0].boxplot([time_loss_s52_ni, time_loss_s52, time_loss_s4], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax[0].set_xticklabels(labels=["S4-5 NI", "S4-5", "S4"], rotation=90)
    ax[0].tick_params(labelsize=textsize)
    ax[0].grid(True)
    ax[0].yaxis.set_major_locator(MultipleLocator(20))
    ax[0].yaxis.set_minor_locator(MultipleLocator(10))

    ax[1].set_ylim((0, 100))
    bplot4 = ax[1].boxplot([time_loss_s53_ni, time_loss_s53, time_loss_s4], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax[1].set_xticklabels(labels=["S4-6 NI", "S4-6", "S4"], rotation=90)
    ax[1].tick_params(labelsize=9, labelleft=False)
    ax[1].grid(True)
    ax[1].yaxis.set_major_locator(MultipleLocator(20))
    ax[1].yaxis.set_minor_locator(MultipleLocator(10))

    ax[2].set_ylim((0, 100))
    bplot4 = ax[2].boxplot([time_loss_s54_ni, time_loss_s54, time_loss_s4], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax[2].set_xticklabels(labels=["S4-7 NI", "S4-7", "S4"], rotation=90)
    ax[2].tick_params(labelsize=textsize, labelleft=False)
    ax[2].grid(True)
    ax[2].yaxis.set_major_locator(MultipleLocator(20))
    ax[2].yaxis.set_minor_locator(MultipleLocator(10))

    plt.text(0.5, -0.35, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[2].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # 5.2 Prediction Error
    # Time Loss compared to ICET with prediction errors BETOS
    impact_time_loss_s1 = np.zeros((len(result_discharge_s1), 6))
    impact_time_loss_s1[:, 0] = (result_time_loss_s1[:, 0]) * 60
    impact_time_loss_s1[:, 1] = (result_time_loss_s1[:, 1]) * 60
    impact_time_loss_s1[:, 2] = (result_time_loss_s1[:, 2]) * 60

    impact_time_loss_s2 = np.zeros((len(result_discharge_s1), 6))
    impact_time_loss_s2[:, 0] = (result_time_loss_s2[:, 0]) * 60
    impact_time_loss_s2[:, 1] = (result_time_loss_s2[:, 1]) * 60
    impact_time_loss_s2[:, 2] = (result_time_loss_s2[:, 2]) * 60

    impact_time_loss_s3 = np.zeros((len(result_discharge_s1), 6))
    impact_time_loss_s3[:, 0] = (result_time_loss_s3[:, 0]) * 60
    impact_time_loss_s3[:, 1] = (result_time_loss_s3[:, 1]) * 60
    impact_time_loss_s3[:, 2] = (result_time_loss_s3[:, 2]) * 60

    impact_time_loss_s4 = np.zeros((len(result_discharge_s1), 6))
    impact_time_loss_s4[:, 0] = (result_time_loss_s4[:, 0]) * 60
    impact_time_loss_s4[:, 1] = (result_time_loss_s4[:, 1]) * 60
    impact_time_loss_s4[:, 2] = (result_time_loss_s4[:, 2]) * 60

    # Plotting Figure (10)
    fig5, ax = plt.subplots(1, 4, figsize=FIGSIZE)
    fig5.suptitle('Sensitivity analysis - Energy / Time prediction errors', **csfont, fontsize=textsize, y=1.05)

    colors_1 = ['#6c969d', '#6c969d', '#6c969d']
    colors_2 = ['#34435e', '#34435e', '#34435e']
    colors_3 = ['#aa4465', '#aa4465', '#aa4465']
    colors_4 = ['#808080', '#808080', '#808080']
    # S1
    ax[0].set_title('Scenario 1', **csfont, fontsize=textsize)
    ax[0].set_ylabel('Additional Time in min', **csfont, fontsize=textsize)
    ax[0].set_ylim((0, 120))
    bplot5 = ax[0].boxplot(impact_time_loss_s1[:, 0:3], showfliers=False, patch_artist=True, showmeans=True,
                           meanline=True, meanprops=meanprop, medianprops=medianprops, widths=(0.5, 0.5, 0.5,))
    for patch, color in zip(bplot5['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0].tick_params(labelsize=textsize)
    ax[0].set_xticklabels(labels=["Ideal", "Energy", "Time"], rotation=90)
    ax[0].grid(True)
    ax[0].yaxis.set_major_locator(MultipleLocator(20))
    ax[0].yaxis.set_minor_locator(MultipleLocator(10))
    # S2
    ax[1].set_title('Scenario 2', **csfont, fontsize=textsize)
    ax[1].tick_params(labelleft=False)
    ax[1].set_ylim((0, 120))
    bplot5 = ax[1].boxplot(impact_time_loss_s2[:, 0:3], showfliers=False, patch_artist=True, showmeans=True,
                           meanline=True, meanprops=meanprop, medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot5['boxes'], colors_2):
        patch.set_facecolor(color)
    ax[1].tick_params(labelsize=textsize)
    ax[1].set_xticklabels(labels=["Ideal", "Energy", "Time"], rotation=90)
    ax[1].grid(True)
    ax[1].yaxis.set_major_locator(MultipleLocator(20))
    ax[1].yaxis.set_minor_locator(MultipleLocator(10))
    # S3
    ax[2].set_title('Scenario 3', **csfont, fontsize=9)
    ax[2].tick_params(labelleft=False)
    ax[2].set_ylim((0, 120))
    bplot5 = ax[2].boxplot(impact_time_loss_s3[:, 0:3], showfliers=False, patch_artist=True, showmeans=True,
                           meanline=True, meanprops=meanprop, medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot5['boxes'], colors_3):
        patch.set_facecolor(color)
    ax[2].tick_params(labelsize=textsize)
    ax[2].set_xticklabels(labels=["Ideal", "Energy", "Time"], rotation=90)
    ax[2].grid(True)
    ax[2].yaxis.set_major_locator(MultipleLocator(20))
    ax[2].yaxis.set_minor_locator(MultipleLocator(10))
    # S4
    ax[3].set_title('Scenario 4', **csfont, fontsize=textsize)
    ax[3].tick_params(labelleft=False)
    ax[3].set_ylim((0, 120))
    bplot5 = ax[3].boxplot(impact_time_loss_s4[:, 0:3], showfliers=False, patch_artist=True, showmeans=True,
                           meanline=True, meanprops=meanprop, medianprops=medianprops,
                           widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot5['boxes'], colors_4):
        patch.set_facecolor(color)
    ax[3].tick_params(labelsize=textsize)
    ax[3].set_xticklabels(labels=["Ideal", "Energy", "Time"], rotation=90)
    ax[3].grid(True)
    ax[3].yaxis.set_major_locator(MultipleLocator(20))
    ax[3].yaxis.set_minor_locator(MultipleLocator(10))

    plt.text(0.5, -0.4, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[3].transAxes, fontsize=textsize, rotation=0)

    plt.show()

    # 5.3 Starting Conditions
    width_in = 16.5 / 2.54
    height_in = width_in * 5 / 16
    FIGSIZE = (width_in, height_in)
    fig, ax = plt.subplots(1, 4)
    fig.set_size_inches(FIGSIZE)
    fig.suptitle('Sensitivity analysis - Starting SOC (BETOS)', **csfont, fontsize=textsize, y=1.0)
    ax[0].set_ylim((0, 120))
    ax[0].set_ylabel('Additional time in min', **csfont, fontsize=textsize)
    bplot4 = ax[0].boxplot([time_loss_s1_100, time_loss_s1, time_loss_s1_80], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_1):
        patch.set_facecolor(color)
    ax[0].set_xticklabels(labels=["S1 100%", "S1 90%", "S1 80%"], rotation=90)
    ax[0].tick_params(labelsize=9)
    ax[0].grid(True)
    ax[0].yaxis.set_major_locator(MultipleLocator(20))
    ax[0].yaxis.set_minor_locator(MultipleLocator(10))
    # S2
    ax[1].set_ylim((0, 120))
    bplot4 = ax[1].boxplot([time_loss_s2_100, time_loss_s2, time_loss_s2_80], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_2):
        patch.set_facecolor(color)
    ax[1].set_xticklabels(labels=["S2 100%", "S2 90%", "S2 80%"], rotation=90)
    ax[1].tick_params(labelsize=textsize, labelleft=False)
    ax[1].grid(True)
    ax[1].yaxis.set_major_locator(MultipleLocator(20))
    ax[1].yaxis.set_minor_locator(MultipleLocator(10))
    # S3
    ax[2].set_ylim((0, 120))
    bplot4 = ax[2].boxplot([time_loss_s3_100, time_loss_s3, time_loss_s3_80], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_3):
        patch.set_facecolor(color)
    ax[2].set_xticklabels(labels=["S3 100%", "S3 90%", "S3 80%"], rotation=90)
    ax[2].tick_params(labelsize=textsize, labelleft=False)
    ax[2].grid(True)
    ax[2].yaxis.set_major_locator(MultipleLocator(20))
    ax[2].yaxis.set_minor_locator(MultipleLocator(10))
    # S4
    ax[3].set_ylim((0, 120))
    bplot4 = ax[3].boxplot([time_loss_s4_100, time_loss_s4, time_loss_s4_80], showfliers=False,
                           patch_artist=True, showmeans=True, meanline=True, meanprops=meanprop,
                           medianprops=medianprops, widths=(0.5, 0.5, 0.5))
    for patch, color in zip(bplot4['boxes'], colors_4):
        patch.set_facecolor(color)
    ax[3].set_xticklabels(labels=["S4 100%", "S4 90%", "S4 80%"], rotation=90)
    ax[3].tick_params(labelsize=textsize, labelleft=False)
    ax[3].grid(True)
    ax[3].yaxis.set_major_locator(MultipleLocator(20))
    ax[3].yaxis.set_minor_locator(MultipleLocator(10))

    plt.text(0.5, -0.4, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax[2].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.4, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax[3].transAxes, fontsize=textsize, rotation=0)

    plt.show()
    # __________________________________________________________________________________________________________________
    return

