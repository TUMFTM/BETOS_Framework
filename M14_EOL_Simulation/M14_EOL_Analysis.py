# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-09-05
#
# Function Description
# Part of the EOL Simulation Module M14
# Analysis of EOL Simulation Results
#
# _________________________________


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy import stats
import plotly.express as px
import matplotlib
from matplotlib.image import NonUniformImage
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.gridspec import GridSpec

# import own functions

# Read data from EOL Simulation
def read_eol_data(scneario_number):
    # which scenario:
    scenario_id = scneario_number
    str_summary = 'Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_' + str(scenario_id) + '_summary.csv'
    # Read Summary File:::
    summary_file = pd.read_csv(str_summary, delimiter=None, header=None).to_numpy()
    soh_macro_trace = summary_file[:, 1]        # SOH Trace on weekly base
    milage_macro_trace = summary_file[:, 0]     #  Milage Trace on weekly base
    number_weeks_eol = len(soh_macro_trace)     # Number of weeks till EOL
    time_loss_per_week_day = np.zeros(len(soh_macro_trace))     # Time loss per week in days
    mandatory_rest_time_per_week = np.zeros(len(soh_macro_trace))

    # Read detail weekly files:::
    # Read first file
    str_week_1 = 'Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_' + str(scenario_id) + '_week_1.csv'
    week_1 = pd.read_csv(str_week_1, delimiter=None, header=None).to_numpy()
    # Initialize traces
    # SOC
    soc_trace = week_1[:, 0]
    # SOH
    soh_trace = week_1[:, 1]
    # DOD
    dod_trace = week_1[:, 4]
    # AVG SOC
    avg_soc_values = week_1[:, 5]
    # AVG CRate
    avg_crate_values = week_1[:, 6]
    # AVG Cell Temperature
    avg_temp_cell_values = week_1[:, 8]
    # Milage Trace
    milage_trace = week_1[:, 3]
    # Event ID trace
    event_id_trace = week_1[:, 11]

    # Driving Time per day
    driving_time_per_day_h = week_1[:, 9][week_1[:, 9] > 0]
    mandatory_rest_time_per_week[0] = np.cumsum(np.floor(driving_time_per_day_h / 4.5))[-1] * 0.75  # in h

    # Time loss per week
    time_loss_per_week_day[0] = (week_1[0, 10] - mandatory_rest_time_per_week[0]) / 24  # in day

    # SOH drop per week
    soh_drop_week = np.zeros((number_weeks_eol, 4))  #0: Driving, 1: On Route, 2: Overnight, 3: Weekend
    soh_drop = week_1[0:len(week_1) - 1, 1] - week_1[1:, 1]
    soh_drop_week[0, 0] = sum(soh_drop[event_id_trace[1:] < 1])
    soh_drop_week[0, 1] = sum(soh_drop[event_id_trace[1:] == 1])
    soh_drop_week[0, 2] = sum(soh_drop[event_id_trace[1:] == 2])
    soh_drop_week[0, 3] = sum(soh_drop[event_id_trace[1:] == 3])

    # Cyclic SOH Drop per week
    soh_drop_cyclic = np.zeros((number_weeks_eol, 4))
    q_loss_cyclic = week_1[1:, 13] - week_1[0:int(len(week_1))-1, 13]
    soh_drop_cyclic[0, 0] = sum(q_loss_cyclic[event_id_trace[1:] < 1])
    soh_drop_cyclic[0, 1] = sum(q_loss_cyclic[event_id_trace[1:] == 1])
    soh_drop_cyclic[0, 2] = sum(q_loss_cyclic[event_id_trace[1:] == 2])
    soh_drop_cyclic[0, 3] = sum(q_loss_cyclic[event_id_trace[1:] == 3])
    last_cyclic_value = week_1[-1, 13]

    # Calendaric SOH Drop per week
    soh_drop_calendaric = np.zeros((number_weeks_eol, 4))
    q_loss_calendaric = week_1[1:, 12] - week_1[0:int(len(week_1))-1, 12]
    soh_drop_calendaric[0, 0] = sum(q_loss_calendaric[event_id_trace[1:] < 1])
    soh_drop_calendaric[0, 1] = sum(q_loss_calendaric[event_id_trace[1:] == 1])
    soh_drop_calendaric[0, 2] = sum(q_loss_calendaric[event_id_trace[1:] == 2])
    soh_drop_calendaric[0, 3] = sum(q_loss_calendaric[event_id_trace[1:] == 3])
    last_calendaric_value = week_1[-1, 14]

    # Read data files
    for i in range(2, number_weeks_eol):
        # Built_string:
        str_1 = 'Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_'
        str_2 = '_week_'
        str_end = '.csv'
        str_read = str_1 + str(int(scenario_id)) + str_2 + str(i) + str_end
        # Read week
        week_data = pd.read_csv(str_read, delimiter=None, header=None).to_numpy()
        # Concatenate arrays
        soc_trace = np.concatenate((soc_trace, week_data[:, 0]))
        soh_trace = np.concatenate((soh_trace, week_data[:, 1]))
        dod_trace = np.concatenate((dod_trace, week_data[:, 4]))
        avg_soc_values = np.concatenate((avg_soc_values, week_data[:, 5]))
        avg_crate_values = np.concatenate((avg_crate_values, week_data[:, 6]))
        avg_temp_cell_values = np.concatenate((avg_temp_cell_values, week_data[:, 8]))
        milage_trace = np.concatenate((milage_trace, week_data[:, 3] + milage_trace[-1]))
        event_id_trace = np.concatenate((event_id_trace, week_data[:, 11]))
        driving_time_per_day_h = week_data[:, 9][week_data[:, 9] > 0]
        mandatory_rest_time_per_week[i-1] = np.cumsum(np.floor(driving_time_per_day_h / 4.5))[-1] * 0.75
        # Time loss
        time_loss_per_week_day[i-1] = time_loss_per_week_day[0] = (week_data[0, 10] - mandatory_rest_time_per_week[i-1]) / 24  # in days
        # SOH Drop according to different events
        soh_drop = week_data[0:len(week_data) - 1, 1] - week_data[1:, 1]
        soh_drop_week[i-1, 0] = sum(soh_drop[week_data[1:, 11] < 1])
        soh_drop_week[i-1, 1] = sum(soh_drop[week_data[1:, 11] == 1])
        soh_drop_week[i-1, 2] = sum(soh_drop[week_data[1:, 11] == 2])
        soh_drop_week[i-1, 3] = sum(soh_drop[week_data[1:, 11] == 3])
        # SOH Drop Cyclic
        week_data[0, 13] = last_cyclic_value
        q_loss_cyclic = week_data[1:, 13] - week_data[0:len(week_data) - 1, 13]
        soh_drop_cyclic[i-1, 0] = sum(q_loss_cyclic[week_data[1:, 11] < 1])
        soh_drop_cyclic[i-1, 1] = sum(q_loss_cyclic[week_data[1:, 11] == 1])
        soh_drop_cyclic[i-1, 2] = sum(q_loss_cyclic[week_data[1:, 11] == 2])
        soh_drop_cyclic[i-1, 3] = sum(q_loss_cyclic[week_data[1:, 11] == 3])
        last_cyclic_value = week_data[-1, 13]
        # SOH Drop Calendaric
        week_data[0, 14] = last_calendaric_value
        q_loss_calendaric = week_data[1:, 12] - week_data[0:len(week_data) - 1, 12]
        soh_drop_calendaric[i-1, 0] = sum(q_loss_calendaric[week_data[1:, 11] < 1])
        soh_drop_calendaric[i-1, 1] = sum(q_loss_calendaric[week_data[1:, 11] == 1])
        soh_drop_calendaric[i-1, 2] = sum(q_loss_calendaric[week_data[1:, 11] == 2])
        soh_drop_calendaric[i-1, 3] = sum(q_loss_calendaric[week_data[1:, 11] == 3])
        last_calendaric_value = week_data[-1, 14]

    # Return dataset:::
    soh_trace = np.concatenate((np.array([1]), soh_trace[dod_trace > 0]))
    avg_soc_values = avg_soc_values[dod_trace > 0]
    avg_crate_values = avg_crate_values[dod_trace > 0]
    avg_temp_cell_values = avg_temp_cell_values[dod_trace > 0]
    milage_trace = np.concatenate((np.array([0]), milage_trace[dod_trace > 0]))
    event_id_trace = event_id_trace[dod_trace > 0]

    dod_trace = dod_trace[dod_trace > 0]

    return soc_trace, soh_trace, dod_trace, avg_soc_values, avg_crate_values, avg_temp_cell_values, milage_trace, \
           event_id_trace, milage_macro_trace, time_loss_per_week_day, soh_drop_week, soh_drop_cyclic, soh_drop_calendaric


# Analysis of EOL Dataset
def eol_dataset_analysis():
    # Get results datasets:_____________________________________________________________________________________________
    # Get dataset for scenario 1
    soc_trace_1, soh_trace_1, dod_trace_1, avg_soc_values_1, avg_crate_values_1, avg_temp_cell_values_1,  \
    milage_trace_1, event_id_trace_1,  milage_macro_trace_1, time_loss_per_week_day_1, soh_drop_week_1, \
    q_loss_cyclic_trace_1, q_loss_calendaric_trace_1 = read_eol_data(1)

    # Get dataset for scenario 122
    soc_trace_122, soh_trace_122, dod_trace_122, avg_soc_values_122, avg_crate_values_122, avg_temp_cell_values_122, \
    milage_trace_122, event_id_trace_122, milage_macro_trace_122, time_loss_per_week_day_122, soh_drop_week_122, \
    q_loss_cyclic_trace_122, q_loss_calendaric_trace_122 = read_eol_data(122)

    # Get dataset for scenario 2
    soc_trace_2, soh_trace_2, dod_trace_2, avg_soc_values_2, avg_crate_values_2, avg_temp_cell_values_2, \
    milage_trace_2, event_id_trace_2, milage_macro_trace_2, time_loss_per_week_day_2, soh_drop_week_2, \
    q_loss_cyclic_trace_2, q_loss_calendaric_trace_2 = read_eol_data(2)

    # Get dataset for scenario 222
    soc_trace_222, soh_trace_222, dod_trace_222, avg_soc_values_222, avg_crate_values_222, avg_temp_cell_values_222, \
    milage_trace_222, event_id_trace_222, milage_macro_trace_222, time_loss_per_week_day_222, soh_drop_week_222, \
    q_loss_cyclic_trace_222, q_loss_calendaric_trace_222 = read_eol_data(222)

    # Get dataset for scenario 3
    soc_trace_3, soh_trace_3, dod_trace_3, avg_soc_values_3, avg_crate_values_3, avg_temp_cell_values_3, \
    milage_trace_3, event_id_trace_3, milage_macro_trace_3, time_loss_per_week_day_3, soh_drop_week_3, \
    q_loss_cyclic_trace_3, q_loss_calendaric_trace_3 = read_eol_data(3)

    # Get dataset for scenario 32 (2C LFP Scale)
    soc_trace_32, soh_trace_32, dod_trace_32, avg_soc_values_32, avg_crate_values_32, avg_temp_cell_values_32, \
    milage_trace_32, event_id_trace_32, milage_macro_trace_32, time_loss_per_week_day_32, soh_drop_week_32, \
    q_loss_cyclic_trace_32, q_loss_calendaric_trace_32 = read_eol_data(32)

    # Get dataset for scenario 33 (2C LFP Scale)
    soc_trace_33, soh_trace_33, dod_trace_33, avg_soc_values_33, avg_crate_values_33, avg_temp_cell_values_33, \
    milage_trace_33, event_id_trace_33, milage_macro_trace_33, time_loss_per_week_day_33, soh_drop_week_33, \
    q_loss_cyclic_trace_33, q_loss_calendaric_trace_33 = read_eol_data(33)

    # Get dataset for scenario 332 (2C LFP Scale, DOD change)
    soc_trace_332, soh_trace_332, dod_trace_332, avg_soc_values_332, avg_crate_values_332, avg_temp_cell_values_332, \
    milage_trace_332, event_id_trace_332, milage_macro_trace_332, time_loss_per_week_day_332, soh_drop_week_332, \
    q_loss_cyclic_trace_332, q_loss_calendaric_trace_332 = read_eol_data(332)

    # Get dataset for scenario 42 (2C NMC Scale)
    soc_trace_42, soh_trace_42, dod_trace_42, avg_soc_values_42, avg_crate_values_42, avg_temp_cell_values_42, \
    milage_trace_42, event_id_trace_42, milage_macro_trace_42, time_loss_per_week_day_42, soh_drop_week_42, \
    q_loss_cyclic_trace_42, q_loss_calendaric_trace_42 = read_eol_data(42)

    # Get dataset for scenario 43 (2C NMC Scale)
    soc_trace_43, soh_trace_43, dod_trace_43, avg_soc_values_43, avg_crate_values_43, avg_temp_cell_values_43, \
    milage_trace_43, event_id_trace_43, milage_macro_trace_43, time_loss_per_week_day_43, soh_drop_week_43, \
    q_loss_cyclic_trace_43, q_loss_calendaric_trace_43 = read_eol_data(43)

    # Get dataset for scenario 5
    soc_trace_5, soh_trace_5, dod_trace_5, avg_soc_values_5, avg_crate_values_5, avg_temp_cell_values_5, \
    milage_trace_5, event_id_trace_5, milage_macro_trace_5, time_loss_per_week_day_5, soh_drop_week_5, \
    q_loss_cyclic_trace_5, q_loss_calendaric_trace_5 = read_eol_data(5)

    # NGS Scenarios
    # Get data set from scenario 7
    # NGS 1C LFP
    soc_trace_7, soh_trace_7, dod_trace_7, avg_soc_values_7, avg_crate_values_7, avg_temp_cell_values_7, \
    milage_trace_7, event_id_trace_7, milage_macro_trace_7, time_loss_per_week_day_7, soh_drop_week_7, \
    q_loss_cyclic_trace_7, q_loss_calendaric_trace_7 = read_eol_data(7)
    # NGS 1C NMC
    soc_trace_8, soh_trace_8, dod_trace_8, avg_soc_values_8, avg_crate_values_8, avg_temp_cell_values_8, \
    milage_trace_8, event_id_trace_8, milage_macro_trace_8, time_loss_per_week_day_8, soh_drop_week_8, \
    q_loss_cyclic_trace_8, q_loss_calendaric_trace_8 = read_eol_data(8)

    # NGS 2C LFP Scale
    soc_trace_9, soh_trace_9, dod_trace_9, avg_soc_values_9, avg_crate_values_9, avg_temp_cell_values_9, \
    milage_trace_9, event_id_trace_9, milage_macro_trace_9, time_loss_per_week_day_9, soh_drop_week_9, \
    q_loss_cyclic_trace_9, q_loss_calendaric_trace_9 = read_eol_data(9)

    # NGS 2C LFP Scale
    soc_trace_92, soh_trace_92, dod_trace_92, avg_soc_values_92, avg_crate_values_92, avg_temp_cell_values_92, \
    milage_trace_92, event_id_trace_92, milage_macro_trace_92, time_loss_per_week_day_92, soh_drop_week_92, \
    q_loss_cyclic_trace_92, q_loss_calendaric_trace_92 = read_eol_data(92)

    # NGS 2C NMC Scale
    soc_trace_10, soh_trace_10, dod_trace_10, avg_soc_values_10, avg_crate_values_10, avg_temp_cell_values_10, \
    milage_trace_10, event_id_trace_10, milage_macro_trace_10, time_loss_per_week_day_10, soh_drop_week_10, \
    q_loss_cyclic_trace_10, q_loss_calendaric_trace_10 = read_eol_data(10)

    # NGS 2C NMC Scale
    soc_trace_102, soh_trace_102, dod_trace_102, avg_soc_values_102, avg_crate_values_102, avg_temp_cell_values_102, \
    milage_trace_102, event_id_trace_102, milage_macro_trace_102, time_loss_per_week_day_102, soh_drop_week_102, \
    q_loss_cyclic_trace_102, q_loss_calendaric_trace_102 = read_eol_data(102)

    # Sensitivity Analysis regarding battery capacity
    soc_trace_114, soh_trace_114, dod_trace_114, avg_soc_values_114, avg_crate_values_114, avg_temp_cell_values_114, \
    milage_trace_114, event_id_trace_114, milage_macro_trace_114, time_loss_per_week_day_114, soh_drop_week_114, \
    q_loss_cyclic_trace_114, q_loss_calendaric_trace_114 = read_eol_data(114)

    soc_trace_116, soh_trace_116, dod_trace_116, avg_soc_values_116, avg_crate_values_116, avg_temp_cell_values_116, \
    milage_trace_116, event_id_trace_116, milage_macro_trace_116, time_loss_per_week_day_116, soh_drop_week_116, \
    q_loss_cyclic_trace_116, q_loss_calendaric_trace_116 = read_eol_data(116)

    soc_trace_1000, soh_trace_1000, dod_trace_1000, avg_soc_values_1000, avg_crate_values_1000, avg_temp_cell_values_1000, \
    milage_trace_1000, event_id_trace_1000, milage_macro_trace_1000, time_loss_per_week_day_1000, soh_drop_week_1000, \
    q_loss_cyclic_trace_1000, q_loss_calendaric_trace_1000 = read_eol_data(1000)

    soc_trace_1002, soh_trace_1002, dod_trace_1002, avg_soc_values_1002, avg_crate_values_1002, avg_temp_cell_values_1002, \
    milage_trace_1002, event_id_trace_1002, milage_macro_trace_1002, time_loss_per_week_day_1002, soh_drop_week_1002, \
    q_loss_cyclic_trace_1002, q_loss_calendaric_trace_1002 = read_eol_data(1002)

    soc_trace_1003, soh_trace_1003, dod_trace_1003, avg_soc_values_1003, avg_crate_values_1003, avg_temp_cell_values_1003, \
    milage_trace_1003, event_id_trace_1003, milage_macro_trace_1003, time_loss_per_week_day_1003, soh_drop_week_1003, \
    q_loss_cyclic_trace_1003, q_loss_calendaric_trace_1003 = read_eol_data(1003)

    soc_trace_1004, soh_trace_1004, dod_trace_1004, avg_soc_values_1004, avg_crate_values_1004, avg_temp_cell_values_1004, \
    milage_trace_1004, event_id_trace_1004, milage_macro_trace_1004, time_loss_per_week_day_1004, soh_drop_week_1004, \
    q_loss_cyclic_trace_1004, q_loss_calendaric_trace_1004 = read_eol_data(1004)

    soc_trace_1100, soh_trace_1100, dod_trace_1100, avg_soc_values_1100, avg_crate_values_1100, avg_temp_cell_values_1100, \
    milage_trace_1100, event_id_trace_1100, milage_macro_trace_1100, time_loss_per_week_day_1100, soh_drop_week_1100, \
    q_loss_cyclic_trace_1100, q_loss_calendaric_trace_1100 = read_eol_data(1100)

    soc_trace_1050, soh_trace_1050, dod_trace_1050, avg_soc_values_1050, avg_crate_values_1050, avg_temp_cell_values_1050, \
    milage_trace_1050, event_id_trace_1050, milage_macro_trace_1050, time_loss_per_week_day_1050, soh_drop_week_1050, \
    q_loss_cyclic_trace_1050, q_loss_calendaric_trace_1050 = read_eol_data(1050)

    # Visualization Functions:__________________________________________________________________________________________
    eol_visualization_million_drive(milage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7, soh_trace_7, milage_trace_7, dod_trace_7, event_id_trace_7, avg_crate_values_7, q_loss_cyclic_trace_7, q_loss_calendaric_trace_7, avg_soc_values_7,
                                    milage_macro_trace_122, soh_drop_week_122, time_loss_per_week_day_122, soh_trace_122, milage_trace_122, dod_trace_122, event_id_trace_122, avg_crate_values_122, q_loss_cyclic_trace_122, q_loss_calendaric_trace_122, avg_soc_values_122,
                                    milage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8, soh_trace_8, milage_trace_8, dod_trace_8, event_id_trace_8, avg_crate_values_8, q_loss_cyclic_trace_8, q_loss_calendaric_trace_8, avg_soc_values_8,
                                    milage_macro_trace_222, soh_drop_week_222, time_loss_per_week_day_222, soh_trace_222, milage_trace_222, dod_trace_222, event_id_trace_222, avg_crate_values_222, q_loss_cyclic_trace_222, q_loss_calendaric_trace_222, avg_soc_values_222,
                                    milage_macro_trace_114, soh_drop_week_114, time_loss_per_week_day_114, soh_trace_114, milage_trace_114, dod_trace_114, event_id_trace_114, avg_crate_values_114, q_loss_cyclic_trace_114, q_loss_calendaric_trace_114, avg_soc_values_114,
                                    milage_macro_trace_116, soh_drop_week_116, time_loss_per_week_day_116, soh_trace_116, milage_trace_116, dod_trace_116, event_id_trace_116, avg_crate_values_116, q_loss_cyclic_trace_116, q_loss_calendaric_trace_116, avg_soc_values_116,
                                    milage_macro_trace_1000, soh_drop_week_1000, time_loss_per_week_day_1000, soh_trace_1000, milage_trace_1000, dod_trace_1000, event_id_trace_1000, avg_crate_values_1000, q_loss_cyclic_trace_1000, q_loss_calendaric_trace_1000, avg_soc_values_1000,
                                    milage_macro_trace_1002, soh_drop_week_1002, time_loss_per_week_day_1002, soh_trace_1002, milage_trace_1002, dod_trace_1002, event_id_trace_1002, avg_crate_values_1002, q_loss_cyclic_trace_1002, q_loss_calendaric_trace_1002, avg_soc_values_1002,
                                    milage_macro_trace_1003, soh_drop_week_1003, time_loss_per_week_day_1003, soh_trace_1003, milage_trace_1003, dod_trace_1003, event_id_trace_1003, avg_crate_values_1003, q_loss_cyclic_trace_1003, q_loss_calendaric_trace_1003, avg_soc_values_1003,
                                    milage_macro_trace_1004, soh_drop_week_1004, time_loss_per_week_day_1004, soh_trace_1004, milage_trace_1004, dod_trace_1004, event_id_trace_1004, avg_crate_values_1004, q_loss_cyclic_trace_1004, q_loss_calendaric_trace_1004, avg_soc_values_1004,
                                    milage_macro_trace_1100, soh_drop_week_1100, time_loss_per_week_day_1100, soh_trace_1100, milage_trace_1100, dod_trace_1100, event_id_trace_1100, avg_crate_values_1100, q_loss_cyclic_trace_1100, q_loss_calendaric_trace_1100, avg_soc_values_1100,
                                    milage_macro_trace_1050, soh_drop_week_1050, time_loss_per_week_day_1050, soh_trace_1050, milage_trace_1050, dod_trace_1050, event_id_trace_1050, avg_crate_values_1050, q_loss_cyclic_trace_1050, q_loss_calendaric_trace_1050, avg_soc_values_1050)

    eol_visualization_cell_chemistry_comparision(milage_macro_trace_1, soh_drop_week_1, time_loss_per_week_day_1, soh_trace_1, milage_trace_1, dod_trace_1, event_id_trace_1, avg_crate_values_1, q_loss_cyclic_trace_1, q_loss_calendaric_trace_1, avg_soc_values_1,
                                                 milage_macro_trace_2, soh_drop_week_2, time_loss_per_week_day_2, soh_trace_2, milage_trace_2, dod_trace_2, event_id_trace_2, avg_crate_values_2, q_loss_cyclic_trace_2, q_loss_calendaric_trace_2, avg_soc_values_2,
                                                 milage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7, soh_trace_7, milage_trace_7, dod_trace_7, event_id_trace_7, avg_crate_values_7, q_loss_cyclic_trace_7, q_loss_calendaric_trace_7, avg_soc_values_7,
                                                 milage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8, soh_trace_8, milage_trace_8, dod_trace_8, event_id_trace_8, avg_crate_values_8, q_loss_cyclic_trace_8, q_loss_calendaric_trace_8, avg_soc_values_8,
                                                 milage_macro_trace_9, soh_drop_week_9, time_loss_per_week_day_9, soh_trace_9, milage_trace_9, dod_trace_9, event_id_trace_9, avg_crate_values_9, q_loss_cyclic_trace_9, q_loss_calendaric_trace_9, avg_soc_values_9,
                                                 milage_macro_trace_10, soh_drop_week_10, time_loss_per_week_day_10, soh_trace_10, milage_trace_10, dod_trace_10, event_id_trace_10, avg_crate_values_10, q_loss_cyclic_trace_10, q_loss_calendaric_trace_10, avg_soc_values_10,
                                                 milage_macro_trace_32, soh_drop_week_32, time_loss_per_week_day_32, soh_trace_32, milage_trace_32, dod_trace_32, event_id_trace_32, avg_crate_values_32, q_loss_cyclic_trace_32, q_loss_calendaric_trace_32, avg_soc_values_32,
                                                 milage_macro_trace_42, soh_drop_week_42, time_loss_per_week_day_42, soh_trace_42, milage_trace_42, dod_trace_42, event_id_trace_42, avg_crate_values_42, q_loss_cyclic_trace_42, q_loss_calendaric_trace_42, avg_soc_values_42,
                                                 milage_macro_trace_33, soh_drop_week_33, time_loss_per_week_day_33, soh_trace_33, milage_trace_33, dod_trace_33, event_id_trace_33, avg_crate_values_33, q_loss_cyclic_trace_33, q_loss_calendaric_trace_33, avg_soc_values_33,
                                                 milage_macro_trace_332, soh_drop_week_332, time_loss_per_week_day_332, soh_trace_332, milage_trace_332, dod_trace_332, event_id_trace_332, avg_crate_values_332, q_loss_cyclic_trace_332, q_loss_calendaric_trace_332, avg_soc_values_332,
                                                 milage_macro_trace_43, soh_drop_week_43, time_loss_per_week_day_43, soh_trace_43, milage_trace_43, dod_trace_43, event_id_trace_43, avg_crate_values_43, q_loss_cyclic_trace_43, q_loss_calendaric_trace_43, avg_soc_values_43,
                                                 milage_macro_trace_92, soh_drop_week_92, time_loss_per_week_day_92, soh_trace_92, milage_trace_92, dod_trace_92, event_id_trace_92, avg_crate_values_92, q_loss_cyclic_trace_92, q_loss_calendaric_trace_92, avg_soc_values_92,
                                                 milage_macro_trace_102, soh_drop_week_102, time_loss_per_week_day_102, soh_trace_102, milage_trace_102, dod_trace_102, event_id_trace_102, avg_crate_values_102, q_loss_cyclic_trace_102, q_loss_calendaric_trace_102, avg_soc_values_102)


    return


# Visualization for comparision of the two different cell chemistries NMC and LFP
def eol_visualization_cell_chemistry_comparision(mileage_macro_trace_1, soh_drop_week_1, time_loss_per_week_day_1, soh_trace_1, mileage_trace_1, dod_trace_1, event_id_trace_1, avg_crate_values_1, q_loss_cyclic_trace_1, q_loss_calendaric_trace_1, avg_soc_values_1,
                                                 mileage_macro_trace_2, soh_drop_week_2, time_loss_per_week_day_2, soh_trace_2, mileage_trace_2, dod_trace_2, event_id_trace_2, avg_crate_values_2, q_loss_cyclic_trace_2, q_loss_calendaric_trace_2, avg_soc_values_2,
                                                 mileage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7, soh_trace_7, mileage_trace_7, dod_trace_7, event_id_trace_7, avg_crate_values_7, q_loss_cyclic_trace_7, q_loss_calendaric_trace_7, avg_soc_values_7,
                                                 mileage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8, soh_trace_8, mileage_trace_8, dod_trace_8, event_id_trace_8, avg_crate_values_8, q_loss_cyclic_trace_8, q_loss_calendaric_trace_8, avg_soc_values_8,
                                                 mileage_macro_trace_9, soh_drop_week_9, time_loss_per_week_day_9, soh_trace_9, mileage_trace_9, dod_trace_9, event_id_trace_9, avg_crate_values_9, q_loss_cyclic_trace_9, q_loss_calendaric_trace_9, avg_soc_values_9,
                                                 mileage_macro_trace_10, soh_drop_week_10, time_loss_per_week_day_10, soh_trace_10, mileage_trace_10, dod_trace_10, event_id_trace_10, avg_crate_values_10, q_loss_cyclic_trace_10, q_loss_calendaric_trace_10, avg_soc_values_10,
                                                 mileage_macro_trace_32, soh_drop_week_32, time_loss_per_week_day_32, soh_trace_32, mileage_trace_32, dod_trace_32, event_id_trace_32, avg_crate_values_32, q_loss_cyclic_trace_32, q_loss_calendaric_trace_32, avg_soc_values_32,
                                                 mileage_macro_trace_42, soh_drop_week_42, time_loss_per_week_day_42, soh_trace_42, mileage_trace_42, dod_trace_42, event_id_trace_42, avg_crate_values_42, q_loss_cyclic_trace_42, q_loss_calendaric_trace_42, avg_soc_values_42,
                                                 mileage_macro_trace_33, soh_drop_week_33, time_loss_per_week_day_33, soh_trace_33, mileage_trace_33, dod_trace_33, event_id_trace_33, avg_crate_values_33, q_loss_cyclic_trace_33, q_loss_calendaric_trace_33, avg_soc_values_33,
                                                 mileage_macro_trace_332, soh_drop_week_332, time_loss_per_week_day_332, soh_trace_332, mileage_trace_332, dod_trace_332, event_id_trace_332, avg_crate_values_332, q_loss_cyclic_trace_332, q_loss_calendaric_trace_332, avg_soc_values_332,
                                                 mileage_macro_trace_43, soh_drop_week_43, time_loss_per_week_day_43, soh_trace_43, mileage_trace_43, dod_trace_43, event_id_trace_43, avg_crate_values_43, q_loss_cyclic_trace_43, q_loss_calendaric_trace_43, avg_soc_values_43,
                                                 mileage_macro_trace_92, soh_drop_week_92, time_loss_per_week_day_92, soh_trace_92, mileage_trace_92, dod_trace_92, event_id_trace_92, avg_crate_values_92, q_loss_cyclic_trace_92, q_loss_calendaric_trace_92, avg_soc_values_92,
                                                 mileage_macro_trace_102, soh_drop_week_102, time_loss_per_week_day_102, soh_trace_102, mileage_trace_102, dod_trace_102, event_id_trace_102, avg_crate_values_102, q_loss_cyclic_trace_102, q_loss_calendaric_trace_102, avg_soc_values_102):
    # General Figure Settings:
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 9 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9
    color_lfp = '#34435e'
    map_lfp = ['#dbdee2', '#b7bec6', '#959fab', '#748191', '#546477', '#34495e']
    color_lfp_2c ='#aa4465'
    map_lfp_2c = ['#f3dfe4', '#e6c0c9', '#d9a1af', '#ca8395', '#bb647d', '#aa4465']
    color_nmc = '#0e79b2'
    map_nmc = ['#8ed1e6', '#55bb71', '#1da4ed', '#0e79b2', '#094d71', '#052639']
    color_nmc_2c = '#8d3b72'
    map_nmc_2c = ['#e1b7d3', '#cf8cb9', '#bd619f', '#8d3b72', '#652a51', '#3a182e']  #'#1d0c17'
    linestyle_betos = '-'
    linestyle_driver = '-.'

    # __________________________________________________________________________________________________________________
    # Figure 6:
    height_in_1 = width_in * 6 / 16
    FIGSIZE_1 = (width_in, height_in_1)
    fig1, ax1 = plt.subplots(1, 2)
    fig1.set_size_inches(FIGSIZE_1)
    fig1.tight_layout(w_pad=2)

    ax1[0].plot(mileage_trace_1 / 1000, soh_trace_1, label='LFP 1C BETOS', color=color_lfp, zorder=10)
    ax1[0].plot(mileage_trace_2 / 1000, soh_trace_2, label='NMC 1C BETOS', color=color_nmc, zorder=10)
    ax1[0].plot(mileage_trace_7 / 1000, soh_trace_7, label='LFP 1C NGS', color=color_lfp, linestyle=linestyle_driver, zorder=10)
    ax1[0].plot(mileage_trace_8 / 1000, soh_trace_8, label='NMC 1C NGS', color=color_nmc, linestyle=linestyle_driver, zorder=10)

    ax1[0].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax1[0].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax1[0].set_ylim((0.7, 1))
    ax1[0].set_xlim((0, 1000))
    ax1[0].yaxis.set_major_locator(MultipleLocator(0.05))
    ax1[0].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax1[0].xaxis.set_major_locator(MultipleLocator(200))
    ax1[0].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[0].grid(zorder=0)
    plt.text(0.5, -0.26, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax1[0].transAxes, fontsize=textsize, rotation=0)


    ax1[1].plot(mileage_macro_trace_1 / 1000, np.cumsum(time_loss_per_week_day_1), color=color_lfp, linewidth=1.5, label='LFP 1C BETOS', zorder=10)
    ax1[1].plot(mileage_macro_trace_2 / 1000, np.cumsum(time_loss_per_week_day_2), color=color_nmc, linewidth=1.5, label='NMC 1C BETOS', zorder=10)
    ax1[1].plot(mileage_macro_trace_7 / 1000, np.cumsum(time_loss_per_week_day_7), color=color_lfp, linewidth=1.5, label='LFP 1C NGS', linestyle=linestyle_driver, zorder=10)
    ax1[1].plot(mileage_macro_trace_8 / 1000, np.cumsum(time_loss_per_week_day_8), color=color_nmc, linewidth=1.5, label='NMC 1C NGS', linestyle=linestyle_driver, zorder=10)

    ax1[1].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax1[1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax1[1].set_ylim((0, 80))
    ax1[1].set_xlim((0, 1000))
    ax1[1].yaxis.set_major_locator(MultipleLocator(20))
    ax1[1].yaxis.set_minor_locator(MultipleLocator(10))
    ax1[1].xaxis.set_major_locator(MultipleLocator(200))
    ax1[1].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[1].legend(fontsize=textsize, loc='center', bbox_to_anchor=(-0.15, -0.4), ncol=4)
    ax1[1].tick_params(labelsize=textsize)
    ax1[1].grid(zorder=0)
    plt.text(0.5, -0.26, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax1[1].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_6.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # __________________________________________________________________________________________________________________
    # Figure 8:
    # Stressfactors for LFP Chemistry
    height_in = width_in * 12 / 16
    FIGSIZE = (width_in, height_in)
    fig2, ax2 = plt.subplots(2, 2, gridspec_kw={'width_ratios': [1, 1], 'height_ratios': [1, 1.5]})
    fig2.set_size_inches(FIGSIZE)
    fig2.tight_layout(w_pad=1, h_pad=2)
    plt.subplots_adjust(left=0.07, bottom=0.09)


    n, bins, patches = ax2[0, 0].hist(avg_soc_values_1[event_id_trace_1 == 1], 20,
                                      weights=np.zeros_like(avg_soc_values_1[event_id_trace_1 == 1]) + 1. /
                                              avg_soc_values_1[
                                                  event_id_trace_1 == 1].size,
                                      color=color_lfp)

    ax2[0, 0].set_ylabel('Frequency', **csfont, fontsize=textsize)
    ax2[0, 0].set_title('1C LFP On Route BETOS', **csfont, fontsize=textsize)
    ax2[0, 0].set_xlabel('Avg SOC', **csfont, fontsize=textsize)
    ax2[0, 0].set_ylim((0, 0.6))
    ax2[0, 0].set_xlim((0, 1))
    ax2[0, 0].yaxis.set_major_locator(MultipleLocator(0.1))
    ax2[0, 0].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax2[0, 0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[0, 0].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax2[0, 0].transAxes, fontsize=textsize, rotation=0)


    n, bins, patches = ax2[0, 1].hist(avg_soc_values_7[event_id_trace_7 == 1], 30,
                                      weights=np.zeros_like(avg_soc_values_7[event_id_trace_7 == 1]) + 1. /
                                              avg_soc_values_7[
                                                  event_id_trace_7 == 1].size,
                                      color=color_lfp)

    ax2[0, 1].set_xlabel('Avg SOC', **csfont, fontsize=textsize)
    ax2[0, 1].set_title('1C LFP On Route NGS', **csfont, fontsize=textsize)
    ax2[0, 1].set_ylim((0, 0.6))
    ax2[0, 1].set_xlim((0, 1))
    ax2[0, 1].yaxis.set_major_locator(MultipleLocator(0.1))
    ax2[0, 1].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax2[0, 1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[0, 1].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax2[0, 1].transAxes, fontsize=textsize, rotation=0)


    cmap = ListedColormap(map_lfp)
    bounds = [0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24]
    norm = BoundaryNorm(bounds, cmap.N)
    # Bins
    xedge = np.linspace(0, 1, 21)
    yedge = np.linspace(0, 3, 21)
    # Histogramm
    H_2c, x_2c, y_2c = np.histogram2d(dod_trace_1[event_id_trace_1 == 1], avg_crate_values_1[event_id_trace_1 == 1],
                                      bins=(xedge, yedge))
    H_2c = H_2c.T / len(dod_trace_1[event_id_trace_1 == 1])  # relative frequency

    im = NonUniformImage(ax2[1, 0], interpolation='bilinear', cmap=cmap, norm=norm)
    xcenters = (x_2c[:-1] + x_2c[1:]) / 2
    ycenters = (y_2c[:-1] + y_2c[1:]) / 2
    im.set_data(xcenters, ycenters, H_2c)
    ax2[1, 0].add_image(im)
    cbar = plt.colorbar(im, ax=ax2[1, 0], orientation="horizontal", pad=0.2, label='Relative Frequency')
    ax2[1, 0].set_xlim(x_2c[[0, -1]])
    ax2[1, 0].set_ylim(y_2c[[0, -1]])
    ax2[1, 0].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax2[1, 0].set_ylabel('Avg C-Rate', **csfont, fontsize=textsize)
    ax2[1, 0].yaxis.set_major_locator(MultipleLocator(0.5))
    ax2[1, 0].yaxis.set_minor_locator(MultipleLocator(0.25))
    ax2[1, 0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[1, 0].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax2[1, 0].transAxes, fontsize=textsize, rotation=0)


    cmap = ListedColormap(map_lfp)
    bounds = [0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24]
    norm = BoundaryNorm(bounds, cmap.N)
    # Bins
    xedge = np.linspace(0, 1, 11)
    yedge = np.linspace(0, 3, 11)
    # Histogramm
    H_2c, x_2c, y_2c = np.histogram2d(dod_trace_7[event_id_trace_7 == 1], avg_crate_values_7[event_id_trace_7 == 1],
                                      bins=(xedge, yedge))
    H_2c = H_2c.T / len(dod_trace_7[event_id_trace_7 == 1])  # relative frequency

    im = NonUniformImage(ax2[1, 1], interpolation='bilinear', cmap=cmap, norm=norm)
    xcenters = (x_2c[:-1] + x_2c[1:]) / 2
    ycenters = (y_2c[:-1] + y_2c[1:]) / 2
    im.set_data(xcenters, ycenters, H_2c)
    ax2[1, 1].add_image(im)
    cbar = plt.colorbar(im, ax=ax2[1, 1], orientation="horizontal", pad=0.2, label='Relative Frequency')
    ax2[1, 1].set_xlim(x_2c[[0, -1]])
    ax2[1, 1].set_ylim(y_2c[[0, -1]])
    ax2[1, 1].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax2[1, 1].yaxis.set_major_locator(MultipleLocator(0.5))
    ax2[1, 1].yaxis.set_minor_locator(MultipleLocator(0.25))
    ax2[1, 1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[1, 1].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax2[1, 1].transAxes, fontsize=textsize, rotation=0)

    # plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_8.svg', dpi=400)

    plt.show()

    # Figure 10:
    # Stress factors comparision
    height_in = width_in * 12 / 16
    FIGSIZE = (width_in, height_in)
    fig2, ax2 = plt.subplots(2, 2, gridspec_kw={'width_ratios': [1, 1], 'height_ratios': [1, 1.5]})
    fig2.set_size_inches(FIGSIZE)
    fig2.tight_layout(w_pad=1, h_pad=2)
    plt.subplots_adjust(left=0.07, bottom=0.09)

    n, bins, patches = ax2[0, 0].hist(avg_soc_values_1[event_id_trace_1 == 1], 20,
                                      weights=np.zeros_like(avg_soc_values_1[event_id_trace_1 == 1]) + 1. /
                                              avg_soc_values_1[
                                                  event_id_trace_1 == 1].size,
                                      color=color_lfp)

    ax2[0, 0].set_ylabel('Frequency', **csfont, fontsize=textsize)
    ax2[0, 0].set_title('1C LFP On Route BETOS', **csfont, fontsize=textsize)
    ax2[0, 0].set_xlabel('Avg SOC', **csfont, fontsize=textsize)
    ax2[0, 0].set_ylim((0, 0.6))
    ax2[0, 0].set_xlim((0, 1))
    ax2[0, 0].yaxis.set_major_locator(MultipleLocator(0.1))
    ax2[0, 0].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax2[0, 0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[0, 0].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax2[0, 0].transAxes,
             fontsize=textsize, rotation=0)

    n, bins, patches = ax2[0, 1].hist(avg_soc_values_32[event_id_trace_32 == 1], 30,
                                      weights=np.zeros_like(avg_soc_values_32[event_id_trace_32 == 1]) + 1. /
                                              avg_soc_values_32[
                                                  event_id_trace_32 == 1].size,
                                      color=color_lfp_2c)

    ax2[0, 1].set_xlabel('Avg SOC', **csfont, fontsize=textsize)
    ax2[0, 1].set_title('2C LFP On Route BETOS', **csfont, fontsize=textsize)
    ax2[0, 1].set_ylim((0, 0.6))
    ax2[0, 1].set_xlim((0, 1))
    ax2[0, 1].yaxis.set_major_locator(MultipleLocator(0.1))
    ax2[0, 1].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax2[0, 1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[0, 1].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax2[0, 1].transAxes,
             fontsize=textsize, rotation=0)

    cmap = ListedColormap(map_lfp)
    bounds = [0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24]
    norm = BoundaryNorm(bounds, cmap.N)
    # Bins
    xedge = np.linspace(0, 1, 21)
    yedge = np.linspace(0, 3, 21)
    # Histogramm
    H_2c, x_2c, y_2c = np.histogram2d(dod_trace_1[event_id_trace_1 == 1], avg_crate_values_1[event_id_trace_1 == 1],
                                      bins=(xedge, yedge))
    H_2c = H_2c.T / len(dod_trace_1[event_id_trace_1 == 1])  # relative frequency

    im = NonUniformImage(ax2[1, 0], interpolation='bilinear', cmap=cmap, norm=norm)
    xcenters = (x_2c[:-1] + x_2c[1:]) / 2
    ycenters = (y_2c[:-1] + y_2c[1:]) / 2
    im.set_data(xcenters, ycenters, H_2c)
    ax2[1, 0].add_image(im)
    cbar = plt.colorbar(im, ax=ax2[1, 0], orientation="horizontal", pad=0.2, label='Relative Frequency')
    ax2[1, 0].set_xlim(x_2c[[0, -1]])
    ax2[1, 0].set_ylim(y_2c[[0, -1]])
    ax2[1, 0].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax2[1, 0].set_ylabel('Avg C-Rate', **csfont, fontsize=textsize)
    ax2[1, 0].yaxis.set_major_locator(MultipleLocator(0.5))
    ax2[1, 0].yaxis.set_minor_locator(MultipleLocator(0.25))
    ax2[1, 0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[1, 0].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax2[1, 0].transAxes,
             fontsize=textsize, rotation=0)

    cmap = ListedColormap(map_lfp_2c)
    bounds = [0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24]
    norm = BoundaryNorm(bounds, cmap.N)
    # Bins
    xedge = np.linspace(0, 1, 11)
    yedge = np.linspace(0, 3, 11)
    # Histogramm
    H_2c, x_2c, y_2c = np.histogram2d(dod_trace_32[event_id_trace_32 == 1], avg_crate_values_32[event_id_trace_32 == 1],
                                      bins=(xedge, yedge))
    H_2c = H_2c.T / len(dod_trace_32[event_id_trace_32 == 1])  # relative frequency

    im = NonUniformImage(ax2[1, 1], interpolation='bilinear', cmap=cmap, norm=norm)
    xcenters = (x_2c[:-1] + x_2c[1:]) / 2
    ycenters = (y_2c[:-1] + y_2c[1:]) / 2
    im.set_data(xcenters, ycenters, H_2c)
    ax2[1, 1].add_image(im)
    cbar = plt.colorbar(im, ax=ax2[1, 1], orientation="horizontal", pad=0.2, label='Relative Frequency')
    ax2[1, 1].set_xlim(x_2c[[0, -1]])
    ax2[1, 1].set_ylim(y_2c[[0, -1]])
    ax2[1, 1].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax2[1, 1].yaxis.set_major_locator(MultipleLocator(0.5))
    ax2[1, 1].yaxis.set_minor_locator(MultipleLocator(0.25))
    ax2[1, 1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax2[1, 1].xaxis.set_minor_locator(MultipleLocator(0.1))
    plt.text(0.1, 0.9, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax2[1, 1].transAxes,
             fontsize=textsize, rotation=0)

    # plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_10.svg', dpi=400)

    plt.show()

    # Figure 9:
    # Time loss and SOH Loss of LFP Cells over Lifetime BETOS
    height_in_6 = width_in * 9 / 16
    FIGSIZE_6 = (width_in, height_in_6)
    fig6, ax6 = plt.subplots(2, 2)
    fig6.set_size_inches(FIGSIZE_6)
    fig6.tight_layout(h_pad=2, w_pad=2)
    # Scenario 33 und 92
    ax6[0, 0].plot(mileage_trace_1 / 1000, soh_trace_1, label='LFP 1C BETOS', color=color_lfp, zorder=10)
    ax6[0, 0].plot(mileage_trace_32 / 1000, soh_trace_32, label='LFP 2C BETOS Cmean', color=color_lfp_2c, zorder=10)
    ax6[0, 0].plot(mileage_trace_33 / 1000, soh_trace_33, label='LFP 2C BETOS Cmax', color=color_lfp_2c, linestyle=':', zorder=10)

    ax6[0, 0].set_title('LFP cell chemistry - BETOS', **csfont, fontsize=textsize)
    ax6[0, 0].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax6[0, 0].set_ylim((0.7, 1))
    ax6[0, 0].set_xlim((0, 1000))
    ax6[0, 0].yaxis.set_major_locator(MultipleLocator(0.1))
    ax6[0, 0].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax6[0, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax6[0, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[0, 0].grid(zorder=0)
    plt.text(0.5, -0.26, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax6[0, 0].transAxes, fontsize=textsize, rotation=0)

    ax6[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(time_loss_per_week_day_1), color=color_lfp, linewidth=1.5, label='LFP 1C BETOS', zorder=10)
    ax6[1, 0].plot(mileage_macro_trace_32 / 1000, np.cumsum(time_loss_per_week_day_32), color=color_lfp_2c, linewidth=1.5, label='LFP 2C BETOS Cmean', zorder=10)
    ax6[1, 0].plot(mileage_macro_trace_33 / 1000, np.cumsum(time_loss_per_week_day_33), color=color_lfp_2c, linewidth=1.5, linestyle=':', label='LFP 2C BETOS Cmax')

    ax6[1, 0].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax6[1, 0].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax6[1, 0].set_ylim((0, 80))
    ax6[1, 0].set_xlim((0, 1000))
    ax6[1, 0].yaxis.set_major_locator(MultipleLocator(20))
    ax6[1, 0].yaxis.set_minor_locator(MultipleLocator(10))
    ax6[1, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax6[1, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[1, 0].tick_params(labelsize=textsize)
    ax6[1, 0].grid(zorder=0)
    plt.text(0.5, -0.4, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax6[1, 0].transAxes, fontsize=textsize, rotation=0)

    ax6[0, 1].plot(mileage_trace_7 / 1000, soh_trace_7, label='LFP 1C NGS', color=color_lfp, zorder=10)
    ax6[0, 1].plot(mileage_trace_9 / 1000, soh_trace_9, label='LFP 2C NGS Cmean', color=color_lfp_2c, zorder=10)
    ax6[0, 1].plot(mileage_trace_92 / 1000, soh_trace_92, label='LFP 2C NGS Cmax', color=color_lfp_2c, linestyle=':', zorder=10)

    ax6[0, 1].set_title('LFP cell chemistry - NGS', **csfont, fontsize=textsize)
    ax6[0, 1].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax6[0, 1].set_ylim((0.7, 1))
    ax6[0, 1].set_xlim((0, 1000))
    ax6[0, 1].yaxis.set_major_locator(MultipleLocator(0.1))
    ax6[0, 1].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax6[0, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax6[0, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[0, 1].grid(zorder=0)
    plt.text(0.5, -0.26, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax6[0, 1].transAxes, fontsize=textsize, rotation=0)

    ax6[1, 1].plot(mileage_macro_trace_7 / 1000, np.cumsum(time_loss_per_week_day_7), color=color_lfp, linewidth=1.5, label='LFP 1C', zorder=10)
    ax6[1, 1].plot(mileage_macro_trace_9 / 1000, np.cumsum(time_loss_per_week_day_9), color=color_lfp_2c, linewidth=1.5, label='LFP 2C Cmean', zorder=10)
    ax6[1, 1].plot(mileage_macro_trace_92 / 1000, np.cumsum(time_loss_per_week_day_92), color=color_lfp_2c, linewidth=1.5, label='LFP 2C Cmax', linestyle=':', zorder=10)


    ax6[1, 1].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax6[1, 1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax6[1, 1].set_ylim((0, 80))
    ax6[1, 1].set_xlim((0, 1000))
    ax6[1, 1].yaxis.set_major_locator(MultipleLocator(20))
    ax6[1, 1].yaxis.set_minor_locator(MultipleLocator(10))
    ax6[1, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax6[1, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[1, 1].legend(fontsize=textsize, loc='center', bbox_to_anchor=(-0.25, -0.55), ncol=3)
    ax6[1, 1].tick_params(labelsize=textsize)
    ax6[1, 1].grid(zorder=0)
    plt.text(0.5, -0.4, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax6[1, 1].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_9.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure A1
    # Time loss and SOH Loss of NMC Cells over Lifetime
    height_in_7 = width_in * 9 / 16
    FIGSIZE_7 = (width_in, height_in_6)
    fig7, ax7 = plt.subplots(2, 2)
    fig7.set_size_inches(FIGSIZE_7)
    fig7.tight_layout(h_pad=2, w_pad=2)
    # Scenario 43 und 102
    ax7[0, 0].plot(mileage_trace_2 / 1000, soh_trace_2, label='NMC 1C BETOS', color=color_nmc, zorder=10)
    ax7[0, 0].plot(mileage_trace_42 / 1000, soh_trace_42, label='NMC 2C BETOS Cmean', color=color_nmc_2c, zorder=10)
    ax7[0, 0].plot(mileage_trace_43 / 1000, soh_trace_43, label='NMC 2C BETOS Cmax', color=color_nmc_2c, zorder=10, linestyle=':')

    ax7[0, 0].set_title('NMC cell chemistry - BETOS', **csfont, fontsize=textsize)
    ax7[0, 0].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax7[0, 0].set_ylim((0.7, 1))
    ax7[0, 0].set_xlim((0, 1000))
    ax7[0, 0].yaxis.set_major_locator(MultipleLocator(0.1))
    ax7[0, 0].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax7[0, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax7[0, 0].xaxis.set_minor_locator(MultipleLocator(100))
    plt.text(0.5, -0.26, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax7[0, 0].transAxes, fontsize=textsize, rotation=0)
    ax7[0, 0].grid(zorder=0)

    ax7[1, 0].plot(mileage_macro_trace_2 / 1000, np.cumsum(time_loss_per_week_day_2), color=color_nmc, linewidth=1.5, label='NMC 1C BETOS', zorder=10)
    ax7[1, 0].plot(mileage_macro_trace_42 / 1000, np.cumsum(time_loss_per_week_day_42), color=color_nmc_2c, linewidth=1.5, label='NMC 2C BETOS Cmean', zorder=10)
    ax7[1, 0].plot(mileage_macro_trace_43 / 1000, np.cumsum(time_loss_per_week_day_43), color=color_nmc_2c, linewidth=1.5, label='NMC 2C BETOS Cmax', zorder=10, linestyle=':')

    ax7[1, 0].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax7[1, 0].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax7[1, 0].set_ylim((0, 80))
    ax7[1, 0].set_xlim((0, 1000))
    ax7[1, 0].yaxis.set_major_locator(MultipleLocator(20))
    ax7[1, 0].yaxis.set_minor_locator(MultipleLocator(10))
    ax7[1, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax7[1, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax7[1, 0].tick_params(labelsize=textsize)
    ax7[1, 0].grid(zorder=0)
    plt.text(0.5, -0.4, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax7[1, 0].transAxes, fontsize=textsize, rotation=0)

    ax7[0, 1].plot(mileage_trace_8 / 1000, soh_trace_8, label='NMC 1C NGS', color=color_nmc, zorder=10)
    ax7[0, 1].plot(mileage_trace_10 / 1000, soh_trace_10, label='NMC 2C NGS Cmean', color=color_nmc_2c, zorder=10)
    ax7[0, 1].plot(mileage_trace_102 / 1000, soh_trace_102, label='NMC 2C NGS Cmax', color=color_nmc_2c, linestyle=':', zorder=10)


    ax7[0, 1].set_title('NMC cell chemistry - NGS', **csfont, fontsize=textsize)
    ax7[0, 1].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax7[0, 1].set_ylim((0.7, 1))
    ax7[0, 1].set_xlim((0, 1000))
    ax7[0, 1].yaxis.set_major_locator(MultipleLocator(0.1))
    ax7[0, 1].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax7[0, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax7[0, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax7[0, 1].grid(zorder=0)
    plt.text(0.5, -0.26, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax7[0, 1].transAxes, fontsize=textsize, rotation=0)

    ax7[1, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(time_loss_per_week_day_8), color=color_nmc, linewidth=1.5, label='NMC 1C', zorder=10)
    ax7[1, 1].plot(mileage_macro_trace_10 / 1000, np.cumsum(time_loss_per_week_day_10), color=color_nmc_2c, linewidth=1.5, label='NMC 2C Cmean', zorder=10)
    ax7[1, 1].plot(mileage_macro_trace_102 / 1000, np.cumsum(time_loss_per_week_day_102), color=color_nmc_2c, linewidth=1.5, label='NMC 2C Cmax', linestyle=':', zorder=10)


    ax7[1, 1].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax7[1, 1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax7[1, 1].set_ylim((0, 80))
    ax7[1, 1].set_xlim((0, 1000))
    ax7[1, 1].yaxis.set_major_locator(MultipleLocator(20))
    ax7[1, 1].yaxis.set_minor_locator(MultipleLocator(10))
    ax7[1, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax7[1, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax7[1, 1].legend(fontsize=textsize, loc='center', bbox_to_anchor=(-0.3, -0.65), ncol=3)
    ax7[1, 1].tick_params(labelsize=textsize)
    ax7[1, 1].grid(zorder=0)
    plt.text(0.5, -0.4, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax7[1, 1].transAxes, fontsize=textsize, rotation=0)

    # plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_A1_NMC.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure 7:
    # Calendaric and Cyclic loss for LFP and NMC chemistry for 1C
    height_in_9 = width_in * 10 / 16
    FIGSIZE_9 = (width_in, height_in_9)
    fig9, ax9 = plt.subplots(2, 2)
    fig9.set_size_inches(FIGSIZE_9)
    fig9.tight_layout(h_pad=4, w_pad=2)
    # Lines
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Cyclic', linestyle='-.', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Calendaric', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Cyclic', linestyle='-.', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Calendaric', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Cyclic', linestyle='-.', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Calendaric', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]) + np.cumsum(q_loss_cyclic_trace_1[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Cyclic', linestyle='-.', zorder=10)
    ax9[1, 0].plot(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]) + np.cumsum(q_loss_cyclic_trace_1[:, 1]) + np.cumsum(q_loss_calendaric_trace_1[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Calendaric', zorder=10)
    # Filling
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, 0, np.cumsum(q_loss_cyclic_trace_1[:, 0]), color='#6c969d', alpha=0.15, hatch='//', zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]), color='#6c969d', alpha=0.6, zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]), color='#aa4465', alpha=0.15, hatch='//', zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]), color='#aa4465', alpha=0.6, zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]), color='#808080', alpha=0.15, hatch='//', zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]), color='#808080', alpha=0.6, zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]) + np.cumsum(q_loss_cyclic_trace_1[:, 1]), color='#34435e', alpha=0.15, hatch='//', zorder=10)
    ax9[1, 0].fill_between(mileage_macro_trace_1 / 1000, np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]) + np.cumsum(q_loss_cyclic_trace_1[:, 1]), np.cumsum(q_loss_cyclic_trace_1[:, 0]) + np.cumsum(q_loss_calendaric_trace_1[:, 0]) + np.cumsum(q_loss_cyclic_trace_1[:, 2]) + np.cumsum(q_loss_calendaric_trace_1[:, 2]) + np.cumsum(q_loss_cyclic_trace_1[:, 3]) + np.cumsum(q_loss_calendaric_trace_1[:, 3]) + np.cumsum(q_loss_cyclic_trace_1[:, 1]) + np.cumsum(q_loss_calendaric_trace_1[:, 1]), color='#34435e', alpha=0.6, zorder=10)
    ax9[1, 0].vlines(mileage_macro_trace_7[-1]/1000, 0, 0.25, linestyles='dashed', color='black', linewidth=1)
    # Setup
    ax9[1, 0].set_title('LFP BETOS', **csfont, fontsize=textsize)
    ax9[1, 0].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    ax9[1, 0].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax9[1, 0].set_ylim((0, 0.25))
    ax9[1, 0].set_xlim((0, 1000))
    ax9[1, 0].yaxis.set_major_locator(MultipleLocator(0.05))
    ax9[1, 0].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax9[1, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax9[1, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax9[1, 0].grid(zorder=0)
    plt.text(0.5, -0.4, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax9[1, 0].transAxes, fontsize=textsize, rotation=0)


    # Lines
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]), color='#6c969d', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]), color='#6c969d', linewidth=1.5, zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]), color='#aa4465', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]), color='#aa4465', linewidth=1.5, zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]), color='#808080', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]), color='#808080', linewidth=1.5, zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]) + np.cumsum(q_loss_cyclic_trace_2[:, 1]), color='#34435e', linewidth=1.5, linestyle='-.',zorder=10)
    ax9[1, 1].plot(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]) + np.cumsum(q_loss_cyclic_trace_2[:, 1]) + np.cumsum(q_loss_calendaric_trace_2[:, 1]), color='#34435e', linewidth=1.5, zorder=10)
    # Filling
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, 0, np.cumsum(q_loss_cyclic_trace_2[:, 0]), color='#6c969d', alpha=0.15, hatch='//', zorder=5, label='Driving Cyclic')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]), np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]), color='#6c969d', alpha=0.6, zorder=5, label='Driving Calendric')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]), np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]), color='#aa4465', alpha=0.15, hatch='//', zorder=5, label='Overnight Weekday Charging Cyclic')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]),np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]), color='#aa4465', alpha=0.6, zorder=5, label='Overnight Weekday Charging Calendric')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]),np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]), color='#808080', alpha=0.15, hatch='//', zorder=5, label='Weekend Charging Cyclic')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]), np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]), color='#808080', alpha=0.6, zorder=5, label='Weekend Charging Calendric')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]),np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]) + np.cumsum(q_loss_cyclic_trace_2[:, 1]), color='#34435e', alpha=0.15, hatch='//', zorder=5, label='On Route Charging Cyclic')
    ax9[1, 1].fill_between(mileage_macro_trace_2 / 1000, np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]) + np.cumsum(q_loss_cyclic_trace_2[:, 1]),np.cumsum(q_loss_cyclic_trace_2[:, 0]) + np.cumsum(q_loss_calendaric_trace_2[:, 0]) + np.cumsum(q_loss_cyclic_trace_2[:, 2]) + np.cumsum(q_loss_calendaric_trace_2[:, 2]) + np.cumsum(q_loss_cyclic_trace_2[:, 3]) + np.cumsum(q_loss_calendaric_trace_2[:, 3]) + np.cumsum(q_loss_cyclic_trace_2[:, 1]) + np.cumsum(q_loss_calendaric_trace_2[:, 1]), color='#34435e', alpha=0.6, zorder=5, label='On Route Charging Calendric')
    ax9[1, 1].vlines(mileage_macro_trace_8[-1] / 1000, 0, 0.25, linestyles='dashed', color='black', linewidth=1)
    # Setup
    ax9[1, 1].set_title('NMC BETOS', **csfont, fontsize=textsize)
    #ax9[1, 1].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    ax9[1, 1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax9[1, 1].set_ylim((0, 0.25))
    ax9[1, 1].set_xlim((0, 1000))
    ax9[1, 1].yaxis.set_major_locator(MultipleLocator(0.05))
    ax9[1, 1].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax9[1, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax9[1, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax9[1, 1].legend(loc='center', bbox_to_anchor=(-0.2, -0.85), ncol=2)
    ax9[1, 1].grid(zorder=0)
    plt.text(0.5, -0.4, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax9[1, 1].transAxes, fontsize=textsize, rotation=0)


    # Driver
    # Lines
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Cyclic', linestyle='-.', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Calendaric', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Cyclic', linestyle='-.', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Calendaric', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Cyclic', linestyle='-.', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Calendaric', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Cyclic', linestyle='-.', zorder=10)
    ax9[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]) + np.cumsum(q_loss_calendaric_trace_7[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Calendaric', zorder=10)
    # Filling
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, 0, np.cumsum(q_loss_cyclic_trace_7[:, 0]), color='#6c969d', alpha=0.15, hatch='//', zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), color='#6c969d', alpha=0.6, zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), color='#aa4465', alpha=0.15, hatch='//', zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), color='#aa4465', alpha=0.6, zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), color='#808080', alpha=0.15, hatch='//', zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), color='#808080', alpha=0.6, zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), color='#34435e', alpha=0.15, hatch='//', zorder=10)
    ax9[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]) + np.cumsum(q_loss_calendaric_trace_7[:, 1]), color='#34435e', alpha=0.6, zorder=10)
    # Setup
    ax9[0, 0].set_title('LFP NGS', **csfont, fontsize=textsize)
    ax9[0, 0].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    ax9[0, 0].set_ylim((0, 0.25))
    ax9[0, 0].set_xlim((0, 1000))
    ax9[0, 0].yaxis.set_major_locator(MultipleLocator(0.05))
    ax9[0, 0].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax9[0, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax9[0, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax9[0, 0].grid(zorder=0)
    plt.text(0.5, -0.3, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax9[0, 0].transAxes, fontsize=textsize, rotation=0)


    # Lines
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]), color='#6c969d', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), color='#6c969d', linewidth=1.5, zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), color='#aa4465', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), color='#aa4465', linewidth=1.5, zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), color='#808080', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), color='#808080', linewidth=1.5, zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), color='#34435e', linewidth=1.5, linestyle='-.', zorder=10)
    ax9[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]) + np.cumsum(q_loss_calendaric_trace_8[:, 1]), color='#34435e', linewidth=1.5, zorder=10)
    # Filling
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, 0, np.cumsum(q_loss_cyclic_trace_8[:, 0]), color='#6c969d', alpha=0.15, hatch='//', zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), color='#6c969d', alpha=0.6, zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), color='#aa4465', alpha=0.15, hatch='//', zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), color='#aa4465', alpha=0.6, zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), color='#808080', alpha=0.15, hatch='//', zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), color='#808080', alpha=0.6, zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), color='#34435e', alpha=0.15, hatch='//', zorder=5)
    ax9[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]) + np.cumsum(q_loss_calendaric_trace_8[:, 1]), color='#34435e', alpha=0.6, zorder=5)

    # Setup
    ax9[0, 1].set_title('NMC NGS', **csfont, fontsize=textsize)
    #ax9[1, 1].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    #ax9[0, 1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax9[0, 1].set_ylim((0, 0.25))
    ax9[0, 1].set_xlim((0, 1000))
    ax9[0, 1].yaxis.set_major_locator(MultipleLocator(0.05))
    ax9[0, 1].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax9[0, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax9[0, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax9[0, 1].grid(zorder=0)
    plt.text(0.5, -0.3, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax9[0, 1].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_7.png', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure 11:
    # Histogram: SOH Drop over DOD for 1C and 2C
    height_in_9 = width_in * 7 / 16
    FIGSIZE_9 = (width_in, height_in_9)
    fig9, ax9 = plt.subplots(1, 2)
    fig9.set_size_inches(FIGSIZE_9)
    fig9.tight_layout(w_pad=2.5)

    soh_drop_1 = soh_trace_1[0:int(len(soh_trace_1) - 1)] - soh_trace_1[1:]
    hist_dod = np.histogram(dod_trace_1[event_id_trace_1 == 1], bins=50, range=(0, 1))
    average_soh_loss_bin = np.zeros(50)
    ax9[0].scatter(dod_trace_1[event_id_trace_1 == 1], soh_drop_1[event_id_trace_1 == 1] * 500, color=color_lfp, marker='*', zorder=10)
    soh_drop_1_filtered = soh_drop_1[event_id_trace_1 == 1]
    dod_trace_1_filtered = dod_trace_1[event_id_trace_1 == 1]
    for i in range(0, 50):
        con_1 = lambda x: dod_trace_1_filtered[x] < hist_dod[1][i+1]
        con_2 = lambda x: dod_trace_1_filtered[x] >= hist_dod[1][i]
        average_soh_loss_bin[i] = np.sum([soh_drop_1_filtered[i] for i in range(len(dod_trace_1_filtered)) if con_1(i) and con_2(i)])
    ax91 = ax9[0].twinx()
    ax91.plot(np.linspace(0,1,50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax9[0].plot(np.linspace(0,1,50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax9[0].set_title('1C (LFP, BETOS)', **csfont, fontsize=textsize)
    ax9[0].set_ylabel('Qloss in kWh', **csfont, fontsize=textsize)
    ax9[0].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax91.tick_params(labelright=False)
    ax9[0].set_ylim((0, 0.15))
    ax91.set_ylim((0, 0.15))
    ax9[0].set_xlim((0, 1))
    ax9[0].yaxis.set_major_locator(MultipleLocator(0.025))
    ax9[0].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax91.yaxis.set_major_locator(MultipleLocator(0.025))
    ax91.yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax9[0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax9[0].xaxis.set_minor_locator(MultipleLocator(0.1))
    ax9[0].grid(zorder=0)
    ax9[0].legend(fontsize=textsize)
    plt.text(0.5, -0.26, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax9[0].transAxes, fontsize=textsize, rotation=0)

    soh_drop_33 = soh_trace_33[0:int(len(soh_trace_33) - 1)] - soh_trace_33[1:]
    hist_dod = np.histogram(dod_trace_33[event_id_trace_33 == 1], bins=50, range=(0, 1))
    condition_1 = (event_id_trace_33 == 1) & (avg_crate_values_33 <= 1.6)
    condition_2 = (event_id_trace_33 == 1) & (avg_crate_values_33 > 1.6)
    ax9[1].scatter(dod_trace_33[condition_1], soh_drop_33[condition_1] * 500, color='#d9a1af', marker='*', zorder=10, label='≤1.6C')
    ax9[1].scatter(dod_trace_33[condition_2], soh_drop_33[condition_2] * 500, color=color_lfp_2c, marker='*', zorder=10, label='>1.6C')
    average_soh_loss_bin = np.zeros(50)
    soh_drop_33_filtered = soh_drop_33[event_id_trace_33 == 1]
    dod_trace_33_filtered = dod_trace_33[event_id_trace_33 == 1]
    for i in range(0, 50):
        con_1 = lambda x: dod_trace_33_filtered[x] < hist_dod[1][i + 1]
        con_2 = lambda x: dod_trace_33_filtered[x] >= hist_dod[1][i]
        average_soh_loss_bin[i] = np.sum([soh_drop_33_filtered[i] for i in range(len(dod_trace_33_filtered)) if con_1(i) and con_2(i)])
    ax92 = ax9[1].twinx()
    ax92.plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax9[1].plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax9[1].set_title('2C with Cmax scaling (LFP, BETOS)', **csfont, fontsize=textsize)
    ax9[1].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax9[1].tick_params(labelleft=False)
    ax9[1].set_ylim((0, 0.15))
    ax92.set_ylim((0, 0.15))
    ax92.set_ylabel('Summarized capacity loss', **csfont, fontsize=textsize)
    ax9[1].set_xlim((0, 1))
    ax9[1].yaxis.set_major_locator(MultipleLocator(0.025))
    ax9[1].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax92.yaxis.set_major_locator(MultipleLocator(0.025))
    ax92.yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax9[1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax9[1].xaxis.set_minor_locator(MultipleLocator(0.1))
    ax9[1].legend(fontsize=textsize)
    ax9[1].grid(zorder=0)
    plt.text(0.5, -0.26, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax9[1].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_11.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure 12:
    # Time loss and SOH Loss of LFP Cells over Lifetime BETOS
    height_in_6 = width_in * 11 / 16
    FIGSIZE_6 = (width_in, height_in_6)
    fig6, ax6 = plt.subplots(2, 2)
    fig6.set_size_inches(FIGSIZE_6)
    fig6.tight_layout(w_pad=2, h_pad=4)

    # Scenario 33 und 332
    ax6[0, 0].plot(mileage_trace_1 / 1000, soh_trace_1, label='LFP 1C BETOS', color=color_lfp, zorder=10)
    ax6[0, 0].plot(mileage_trace_33 / 1000, soh_trace_33, label='LFP 2C BETOS Cmax', color=color_lfp_2c, linestyle=':', zorder=10)
    ax6[0, 0].plot(mileage_trace_332 / 1000, soh_trace_332, label='LFP 2C BETOS Cmax DOD', color=color_lfp_2c, linestyle='--', zorder=10)

    ax6[0, 0].set_title('LFP 1C/2C (Cmax, BETOS)', **csfont, fontsize=textsize)
    ax6[0, 0].set_ylabel('State of Health', **csfont, fontsize=textsize)
    ax6[0, 0].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax6[0, 0].set_ylim((0.7, 1))
    ax6[0, 0].set_xlim((0, 1000))
    ax6[0, 0].yaxis.set_major_locator(MultipleLocator(0.1))
    ax6[0, 0].yaxis.set_minor_locator(MultipleLocator(0.05))
    ax6[0, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax6[0, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[0, 0].grid(zorder=0)
    plt.text(0.5, -0.36, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax6[0, 0].transAxes, fontsize=textsize, rotation=0)

    ax6[0, 1].plot(mileage_macro_trace_1 / 1000, np.cumsum(time_loss_per_week_day_1), color=color_lfp, linewidth=1.5, label='LFP 1C BETOS', zorder=10)
    ax6[0, 1].plot(mileage_macro_trace_33 / 1000, np.cumsum(time_loss_per_week_day_33), color=color_lfp_2c, linewidth=1.5, linestyle=':', label='LFP 2C BETOS Cmax')
    ax6[0, 1].plot(mileage_macro_trace_332 / 1000, np.cumsum(time_loss_per_week_day_332), color=color_lfp_2c, linewidth=1.5, linestyle='--', label='LFP 2C BETOS Cmax DOD')

    ax6[0, 1].set_ylabel('Time loss in days', **csfont, fontsize=textsize)
    ax6[0, 1].set_title('LFP 1C/2C (Cmax, BETOS)', **csfont, fontsize=textsize)
    ax6[0, 1].set_xlabel('Mileage in tkm', **csfont, fontsize=textsize)
    ax6[0, 1].set_ylim((0, 80))
    ax6[0, 1].set_xlim((0, 1000))
    ax6[0, 1].yaxis.set_major_locator(MultipleLocator(20))
    ax6[0, 1].yaxis.set_minor_locator(MultipleLocator(10))
    ax6[0, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax6[0, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax6[0, 1].tick_params(labelsize=textsize)
    ax6[0, 1].grid(zorder=0)
    ax6[0, 1].legend(loc='center', bbox_to_anchor=(-0.2, -2.1), ncol=3)
    plt.text(0.5, -0.36, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax6[0, 1].transAxes, fontsize=textsize, rotation=0)

    soh_drop_33 = soh_trace_33[0:int(len(soh_trace_33) - 1)] - soh_trace_33[1:]
    hist_dod = np.histogram(dod_trace_33[event_id_trace_33 == 1], bins=50, range=(0, 1))
    condition_1 = (event_id_trace_33 == 1) & (avg_crate_values_33 <= 1.6)
    condition_2 = (event_id_trace_33 == 1) & (avg_crate_values_33 > 1.6)
    ax6[1, 0].scatter(dod_trace_33[condition_1], soh_drop_33[condition_1] * 500, color='#d9a1af', marker='*', zorder=10, label='≤1.6C')
    ax6[1, 0].scatter(dod_trace_33[condition_2], soh_drop_33[condition_2] * 500, color=color_lfp_2c, marker='*', zorder=10, label='>1.6C')
    average_soh_loss_bin = np.zeros(50)
    soh_drop_33_filtered = soh_drop_33[event_id_trace_33 == 1]
    dod_trace_33_filtered = dod_trace_33[event_id_trace_33 == 1]
    for i in range(0, 50):
        con_1 = lambda x: dod_trace_33_filtered[x] < hist_dod[1][i + 1]
        con_2 = lambda x: dod_trace_33_filtered[x] >= hist_dod[1][i]
        average_soh_loss_bin[i] = np.sum([soh_drop_33_filtered[i] for i in range(len(dod_trace_33_filtered)) if con_1(i) and con_2(i)])
    ax61 = ax6[1, 0].twinx()
    ax61.plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax6[1, 0].plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax6[1, 0].set_title('2C | Regular DOD (SOC: 0.15-1)', **csfont, fontsize=textsize)
    ax6[1, 0].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax6[1, 0].set_ylabel('Q loss in kWh')
    ax6[1, 0].set_ylim((0, 0.15))
    ax6[1, 0].set_xlim((0, 1))
    ax61.set_ylim((0, 0.15))
    ax61.tick_params(labelright=False)
    ax6[1, 0].yaxis.set_major_locator(MultipleLocator(0.025))
    ax6[1, 0].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax92.yaxis.set_major_locator(MultipleLocator(0.025))
    ax92.yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax6[1, 0].xaxis.set_major_locator(MultipleLocator(0.2))
    ax6[1, 0].xaxis.set_minor_locator(MultipleLocator(0.1))
    #ax6[1, 0].legend(fontsize=textsize)
    ax6[1, 0].grid(zorder=0)
    plt.text(0.5, -0.36, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax6[1, 0].transAxes, fontsize=textsize, rotation=0)

    soh_drop_332 = soh_trace_332[0:int(len(soh_trace_332) - 1)] - soh_trace_332[1:]
    hist_dod = np.histogram(dod_trace_332[event_id_trace_332 == 1], bins=50, range=(0, 1))
    condition_1 = (event_id_trace_332 == 1) & (avg_crate_values_332 <= 1.6)
    condition_2 = (event_id_trace_332 == 1) & (avg_crate_values_332 > 1.6)
    ax6[1, 1].scatter(dod_trace_332[condition_1], soh_drop_332[condition_1] * 500, color='#d9a1af', marker='*', zorder=10, label='≤1.6C')
    ax6[1, 1].scatter(dod_trace_332[condition_2], soh_drop_332[condition_2] * 500, color=color_lfp_2c, marker='*', zorder=10, label='>1.6C')
    average_soh_loss_bin = np.zeros(50)
    soh_drop_332_filtered = soh_drop_332[event_id_trace_332 == 1]
    dod_trace_332_filtered = dod_trace_332[event_id_trace_332 == 1]
    for i in range(0, 50):
        con_1 = lambda x: dod_trace_332_filtered[x] < hist_dod[1][i + 1]
        con_2 = lambda x: dod_trace_332_filtered[x] >= hist_dod[1][i]
        average_soh_loss_bin[i] = np.sum([soh_drop_332_filtered[i] for i in range(len(dod_trace_332_filtered)) if con_1(i) and con_2(i)])
    ax62 = ax6[1, 1].twinx()
    ax62.plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax6[1, 1].plot(np.linspace(0, 1, 50), np.cumsum(average_soh_loss_bin), label='CumSum Qloss', color='k', zorder=10)
    ax6[1, 1].set_title('2C | DOD Limit (SOC: 0.2-0.8)', **csfont, fontsize=textsize)
    ax6[1, 1].set_xlabel('DOD', **csfont, fontsize=textsize)
    ax6[1, 1].tick_params(labelleft=False)
    ax6[1, 1].set_ylim((0, 0.15))
    ax6[1, 1].set_xlim((0, 1))
    ax62.set_ylim((0, 0.15))
    ax62.set_ylabel('Summarized capacity loss', **csfont, fontsize=textsize)
    ax6[1, 1].yaxis.set_major_locator(MultipleLocator(0.025))
    ax6[1, 1].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax6[1, 1].xaxis.set_major_locator(MultipleLocator(0.2))
    ax6[1, 1].xaxis.set_minor_locator(MultipleLocator(0.1))
    ax6[1, 1].legend(fontsize=textsize, loc='center', bbox_to_anchor=(-0.2, -0.75), ncol=3)
    ax6[1, 1].grid(zorder=0)
    plt.text(0.5, -0.36, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax6[1, 1].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_12.svg', dpi=400, bbox_inches='tight')
    plt.show()

    return


def eol_visualization_million_drive(mileage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7, soh_trace_7, mileage_trace_7, dod_trace_7, event_id_trace_7, avg_crate_values_7, q_loss_cyclic_trace_7, q_loss_calendaric_trace_7, avg_soc_values_7,
                                    mileage_macro_trace_122, soh_drop_week_122, time_loss_per_week_day_122, soh_trace_122, mileage_trace_122, dod_trace_122, event_id_trace_122, avg_crate_values_122, q_loss_cyclic_trace_122, q_loss_calendaric_trace_122, avg_soc_values_122,
                                    mileage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8, soh_trace_8, mileage_trace_8, dod_trace_8, event_id_trace_8, avg_crate_values_8, q_loss_cyclic_trace_8, q_loss_calendaric_trace_8, avg_soc_values_8,
                                    mileage_macro_trace_222, soh_drop_week_222, time_loss_per_week_day_222, soh_trace_222, mileage_trace_222, dod_trace_222, event_id_trace_222, avg_crate_values_222, q_loss_cyclic_trace_222, q_loss_calendaric_trace_222, avg_soc_values_222,
                                    mileage_macro_trace_114, soh_drop_week_114, time_loss_per_week_day_114, soh_trace_114, mileage_trace_114, dod_trace_114, event_id_trace_114, avg_crate_values_114, q_loss_cyclic_trace_114, q_loss_calendaric_trace_114, avg_soc_values_114,
                                    mileage_macro_trace_116, soh_drop_week_116, time_loss_per_week_day_116, soh_trace_116, mileage_trace_116, dod_trace_116, event_id_trace_116, avg_crate_values_116, q_loss_cyclic_trace_116, q_loss_calendaric_trace_116, avg_soc_values_116,
                                    mileage_macro_trace_1000, soh_drop_week_1000, time_loss_per_week_day_1000, soh_trace_1000, mileage_trace_1000, dod_trace_1000, event_id_trace_1000, avg_crate_values_1000, q_loss_cyclic_trace_1000, q_loss_calendaric_trace_1000, avg_soc_values_1000,
                                    mileage_macro_trace_1002, soh_drop_week_1002, time_loss_per_week_day_1002, soh_trace_1002, mileage_trace_1002, dod_trace_1002, event_id_trace_1002, avg_crate_values_1002, q_loss_cyclic_trace_1002, q_loss_calendaric_trace_1002, avg_soc_values_1002,
                                    mileage_macro_trace_1003, soh_drop_week_1003, time_loss_per_week_day_1003, soh_trace_1003, mileage_trace_1003, dod_trace_1003, event_id_trace_1003, avg_crate_values_1003, q_loss_cyclic_trace_1003, q_loss_calendaric_trace_1003, avg_soc_values_1003,
                                    mileage_macro_trace_1004, soh_drop_week_1004, time_loss_per_week_day_1004, soh_trace_1004, mileage_trace_1004, dod_trace_1004, event_id_trace_1004, avg_crate_values_1004, q_loss_cyclic_trace_1004, q_loss_calendaric_trace_1004, avg_soc_values_1004,
                                    mileage_macro_trace_1100, soh_drop_week_1100, time_loss_per_week_day_1100, soh_trace_1100, mileage_trace_1100, dod_trace_1100, event_id_trace_1100, avg_crate_values_1100, q_loss_cyclic_trace_1100, q_loss_calendaric_trace_1100, avg_soc_values_1100,
                                    mileage_macro_trace_1050, soh_drop_week_1050, time_loss_per_week_day_1050, soh_trace_1050, mileage_trace_1050, dod_trace_1050, event_id_trace_1050, avg_crate_values_1050, q_loss_cyclic_trace_1050, q_loss_calendaric_trace_1050, avg_soc_values_1050):
    # General Figure Settings:
    csfont = {'fontname': 'Times New Roman'}
    plt.rc('font', family='Times New Roman')
    docwidth = 16.5  # word doc width in cm
    width_in = 16.5 / 2.54
    height_in = width_in * 9 / 16
    FIGSIZE = (width_in, height_in)
    textsize = 9
    color_lfp = '#34435e'
    map_lfp = ['#dbdee2', '#b7bec6', '#959fab', '#748191', '#546477', '#34495e']
    color_lfp_2c = '#aa4465'
    map_lfp_2c = ['#f3dfe4', '#e6c0c9', '#d9a1af', '#ca8395', '#bb647d', '#aa4465']
    color_nmc = '#0e79b2'
    map_nmc = ['#8ed1e6', '#55bb71', '#1da4ed', '#0e79b2', '#094d71', '#052639']
    color_nmc_2c = '#8d3b72'
    map_nmc_2c = ['#e1b7d3', '#cf8cb9', '#bd619f', '#8d3b72', '#652a51', '#3a182e']  # '#1d0c17'
    linestyle_betos = '-'
    linestyle_driver = '-.'

    # Figure 13:
    # Capaloss over Mileage for Driver 1C LFP versus BETOS informed 1C LFP
    height_in_1 = width_in * 12 / 16
    FIGSIZE_1 = (width_in, height_in_1)
    fig1, ax1 = plt.subplots(2, 2)
    fig1.set_size_inches(FIGSIZE_1)
    fig1.tight_layout(w_pad=0.5, h_pad=4)

    # Driver
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Cyclic', linestyle='-.', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Calendric', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Cyclic', linestyle='-.', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Calendric', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Cyclic', linestyle='-.', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Calendric', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Cyclic',linestyle='-.', zorder=5)
    ax1[0, 0].plot(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]) + np.cumsum(q_loss_calendaric_trace_7[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Calendric', zorder=5)
    # Filling
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, 0, np.cumsum(q_loss_cyclic_trace_7[:, 0]), color='#6c969d', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), color='#6c969d', alpha=0.6, zorder=5)
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), color='#aa4465', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), color='#aa4465', alpha=0.6, zorder=5)
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), color='#808080', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), color='#808080', alpha=0.6, zorder=5)
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), color='#34435e', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 0].fill_between(mileage_macro_trace_7 / 1000, np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]), np.cumsum(q_loss_cyclic_trace_7[:, 0]) + np.cumsum(q_loss_calendaric_trace_7[:, 0]) + np.cumsum(q_loss_cyclic_trace_7[:, 2]) + np.cumsum(q_loss_calendaric_trace_7[:, 2]) + np.cumsum(q_loss_cyclic_trace_7[:, 3]) + np.cumsum(q_loss_calendaric_trace_7[:, 3]) + np.cumsum(q_loss_cyclic_trace_7[:, 1]) + np.cumsum(q_loss_calendaric_trace_7[:, 1]), color='#34435e', alpha=0.6, zorder=5)
    # Setup
    ax1[0, 0].set_title('LFP (1C Peak, NGS)', **csfont, fontsize=textsize)
    ax1[0, 0].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    #ax1[0, 0].set_xlabel('Mileage in thousand km', **csfont, fontsize=textsize)
    ax1[0, 0].set_ylim((0, 0.25))
    ax1[0, 0].set_xlim((0, 1100))
    ax1[0, 0].yaxis.set_major_locator(MultipleLocator(0.05))
    ax1[0, 0].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax1[0, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax1[0, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[0, 0].grid(zorder=0)
    plt.text(0.5, -0.2, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax1[0, 0].transAxes, fontsize=textsize, rotation=0)


    # BETOS informed
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Cyclic', linestyle='-.', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Calendaric', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Cyclic', linestyle='-.', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Calendaric', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Cyclic', linestyle='-.', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Calendaric', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]) + np.cumsum(q_loss_cyclic_trace_122[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Cyclic', linestyle='-.', zorder=5)
    ax1[1, 0].plot(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]) + np.cumsum(q_loss_cyclic_trace_122[:, 1]) + np.cumsum(q_loss_calendaric_trace_122[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Calendaric', zorder=5)
    # Filling
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, 0, np.cumsum(q_loss_cyclic_trace_122[:, 0]), color='#6c969d', alpha=0.15, zorder=5, hatch='//')
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]), color='#6c969d', alpha=0.6, zorder=5)
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]), color='#aa4465', alpha=0.15, zorder=5, hatch='//')
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]), color='#aa4465', alpha=0.6, zorder=5)
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]), color='#808080', alpha=0.15, zorder=5, hatch='//')
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]), color='#808080', alpha=0.6, zorder=5)
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]) + np.cumsum(q_loss_cyclic_trace_122[:, 1]), color='#34435e', alpha=0.15, zorder=5, hatch='//')
    ax1[1, 0].fill_between(mileage_macro_trace_122 / 1000, np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]) + np.cumsum(q_loss_cyclic_trace_122[:, 1]), np.cumsum(q_loss_cyclic_trace_122[:, 0]) + np.cumsum(q_loss_calendaric_trace_122[:, 0]) + np.cumsum(q_loss_cyclic_trace_122[:, 2]) + np.cumsum(q_loss_calendaric_trace_122[:, 2]) + np.cumsum(q_loss_cyclic_trace_122[:, 3]) + np.cumsum(q_loss_calendaric_trace_122[:, 3]) + np.cumsum(q_loss_cyclic_trace_122[:, 1]) + np.cumsum(q_loss_calendaric_trace_122[:, 1]), color='#34435e', alpha=0.6, zorder=5)
    ax1[1, 0].vlines(mileage_macro_trace_7[-1]/1000, 0, 0.25, color='black', linestyles='dashed', linewidth=1)
    # Setup
    ax1[1, 0].set_title('LFP (1C Peak, BETOS informed)', **csfont, fontsize=textsize)
    ax1[1, 0].set_xlabel('Mileage in thousand km', **csfont, fontsize=textsize)
    ax1[1, 0].set_ylabel('Capacity loss', **csfont, fontsize=textsize)
    ax1[1, 0].set_ylim((0, 0.25))
    ax1[1, 0].set_xlim((0, 1100))
    ax1[1, 0].yaxis.set_major_locator(MultipleLocator(0.05))
    ax1[1, 0].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax1[1, 0].xaxis.set_major_locator(MultipleLocator(200))
    ax1[1, 0].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[1, 0].grid(zorder=0)
    plt.text(0.5, -0.31, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax1[1, 0].transAxes, fontsize=textsize, rotation=0)

    # Driver
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Cyclic', linestyle='-.', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), color='#6c969d', linewidth=1.5, label='Driving Calendaric', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Cyclic', linestyle='-.', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), color='#aa4465', linewidth=1.5, label='Overnight Weekday Charging Calendaric', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Cyclic', linestyle='-.', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), color='#808080', linewidth=1.5, label='Weekend Charging Calendaric', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Cyclic',linestyle='-.', zorder=5)
    ax1[0, 1].plot(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]) + np.cumsum(q_loss_calendaric_trace_8[:, 1]), color='#34435e', linewidth=1.5, label='On Route Charging Calendaric', zorder=5)
    # Filling
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, 0, np.cumsum(q_loss_cyclic_trace_8[:, 0]), color='#6c969d', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), color='#6c969d', alpha=0.6, zorder=5)
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), color='#aa4465', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), color='#aa4465', alpha=0.6, zorder=5)
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), color='#808080', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), color='#808080', alpha=0.6, zorder=5)
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), color='#34435e', alpha=0.15, zorder=5, hatch='//')
    ax1[0, 1].fill_between(mileage_macro_trace_8 / 1000, np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]), np.cumsum(q_loss_cyclic_trace_8[:, 0]) + np.cumsum(q_loss_calendaric_trace_8[:, 0]) + np.cumsum(q_loss_cyclic_trace_8[:, 2]) + np.cumsum(q_loss_calendaric_trace_8[:, 2]) + np.cumsum(q_loss_cyclic_trace_8[:, 3]) + np.cumsum(q_loss_calendaric_trace_8[:, 3]) + np.cumsum(q_loss_cyclic_trace_8[:, 1]) + np.cumsum(q_loss_calendaric_trace_8[:, 1]), color='#34435e', alpha=0.6, zorder=5)
    # Setup
    ax1[0, 1].set_title('NMC (1C Peak, NGS)', **csfont, fontsize=textsize)
    # ax1[0, 1].set_xlabel('Mileage in thousand km', **csfont, fontsize=textsize)
    ax1[0, 1].tick_params(labelleft=False)
    ax1[0, 1].set_ylim((0, 0.25))
    ax1[0, 1].set_xlim((0, 1100))
    ax1[0, 1].yaxis.set_major_locator(MultipleLocator(0.05))
    ax1[0, 1].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax1[0, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax1[0, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[0, 1].grid(zorder=0)
    plt.text(0.5, -0.2, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax1[0, 1].transAxes, fontsize=textsize, rotation=0)

    # BETOS informed
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]), color='#6c969d', linewidth=1.5, linestyle='-.', zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]), color='#6c969d', linewidth=1.5, zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]), color='#aa4465', linewidth=1.5, linestyle='-.', zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]), color='#aa4465', linewidth=1.5, zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]), color='#808080', linewidth=1.5, linestyle='-.', zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]), color='#808080', linewidth=1.5, zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]) + np.cumsum(q_loss_cyclic_trace_222[:, 1]), color='#34435e', linewidth=1.5, linestyle='-.', zorder=5)
    ax1[1, 1].plot(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]) + np.cumsum(q_loss_cyclic_trace_222[:, 1]) + np.cumsum(q_loss_calendaric_trace_222[:, 1]), color='#34435e', zorder=5)
    # Filling
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, 0, np.cumsum(q_loss_cyclic_trace_222[:, 0]), color='#6c969d', alpha=0.15, zorder=5, hatch='//', label='Driving Cyclic')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]), color='#6c969d', alpha=0.6, zorder=5, label='Driving Calendaric')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]), color='#aa4465', alpha=0.15, zorder=5, hatch='//', label='Overnight Weekday Charging Cyclic')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]), color='#aa4465', alpha=0.6, zorder=5, label='Overnight Weekday Charging Calendaric')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]), color='#808080', alpha=0.15, zorder=5, hatch='//', label='Weekend Charging Cyclic')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]), color='#808080', alpha=0.6, zorder=5, label='Weekend Charging Calendaric')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]) + np.cumsum(q_loss_cyclic_trace_222[:, 1]), color='#34435e', alpha=0.15, zorder=5, hatch='//', label='On Route Charging Cyclic')
    ax1[1, 1].fill_between(mileage_macro_trace_222 / 1000, np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]) + np.cumsum(q_loss_cyclic_trace_222[:, 1]), np.cumsum(q_loss_cyclic_trace_222[:, 0]) + np.cumsum(q_loss_calendaric_trace_222[:, 0]) + np.cumsum(q_loss_cyclic_trace_222[:, 2]) + np.cumsum(q_loss_calendaric_trace_222[:, 2]) + np.cumsum(q_loss_cyclic_trace_222[:, 3]) + np.cumsum(q_loss_calendaric_trace_222[:, 3]) + np.cumsum(q_loss_cyclic_trace_222[:, 1]) + np.cumsum(q_loss_calendaric_trace_222[:, 1]), color='#34435e', alpha=0.6, zorder=5, label='On Route Charging Calendaric')
    ax1[1, 1].vlines(mileage_macro_trace_8[-1]/1000, 0, 0.25, color='black', linestyles='dashed', linewidth=1)
    # Setup
    ax1[1, 1].set_title('NMC (1C Peak, BETOS informed)', **csfont, fontsize=textsize)
    ax1[1, 1].set_xlabel('Mileage in thousand km', **csfont, fontsize=textsize)
    ax1[1, 1].tick_params(labelleft=False)
    ax1[1, 1].set_ylim((0, 0.25))
    ax1[1, 1].set_xlim((0, 1100))
    ax1[1, 1].yaxis.set_major_locator(MultipleLocator(0.05))
    ax1[1, 1].yaxis.set_minor_locator(MultipleLocator(0.025))
    ax1[1, 1].xaxis.set_major_locator(MultipleLocator(200))
    ax1[1, 1].xaxis.set_minor_locator(MultipleLocator(100))
    ax1[1, 1].grid(zorder=0)
    ax1[1, 1].legend(loc='center', bbox_to_anchor=(-0.15, -0.6), ncol=2, fontsize=textsize)
    plt.text(0.5, -0.31, '(d)', horizontalalignment='center', verticalalignment='center', transform=ax1[1, 1].transAxes, fontsize=textsize, rotation=0)

    #Save Fig
    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_13.png', dpi=400, bbox_inches='tight')
    plt.show()

    # Figure 14
    # Sensitivity analysis - Visulaization as trajectories
    height_in_2 = width_in * 5 / 16
    FIGSIZE_2 = (width_in, height_in_2)
    fig2, ax2 = plt.subplots(1, 3)
    fig2.set_size_inches(FIGSIZE_2)
    fig2.tight_layout(w_pad=2)

    battery_capacity = [400, 500, 600]
    mileage_eol = np.array([mileage_macro_trace_114[-1], mileage_macro_trace_122[-1], mileage_macro_trace_116[-1]]) / 1000  # in tkm
    weeks_eol = np.array([len(mileage_macro_trace_114), len(mileage_macro_trace_122), len(mileage_macro_trace_116)])

    ax2[0].plot(battery_capacity, mileage_eol, color='k', linewidth=1.5, label='LFP', zorder=10)
    ax2[0].set_xlabel('Battery capacity in kWh', **csfont, fontsize=textsize)
    ax2[0].set_ylabel('Mileage EOL in tkm', **csfont, fontsize=textsize)
    ax2[0].set_ylim((0, 1200))
    ax2[0].set_xlim((375, 625))
    ax2[0].yaxis.set_major_locator(MultipleLocator(200))
    ax2[0].yaxis.set_minor_locator(MultipleLocator(100))
    ax2[0].xaxis.set_major_locator(MultipleLocator(50))
    ax2[0].xaxis.set_minor_locator(MultipleLocator(25))
    ax2[0].grid(zorder=0)

    plt.text(0.5, -0.35, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax2[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax2[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax2[2].transAxes, fontsize=textsize, rotation=0)

    # Aging Portions
    a_p_driving_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_114[:, 0])[-1], np.cumsum(q_loss_cyclic_trace_122[:, 0])[-1],
         np.cumsum(q_loss_cyclic_trace_116[:, 0])[-1]])
    a_p_driving_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_114[:, 0])[-1], np.cumsum(q_loss_calendaric_trace_122[:, 0])[-1],
         np.cumsum(q_loss_calendaric_trace_116[:, 0])[-1]])
    a_p_onroute_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_114[:, 1])[-1], np.cumsum(q_loss_cyclic_trace_122[:, 1])[-1],
         np.cumsum(q_loss_cyclic_trace_116[:, 1])[-1]])
    a_p_onroute_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_114[:, 1])[-1], np.cumsum(q_loss_calendaric_trace_122[:, 1])[-1],
         np.cumsum(q_loss_calendaric_trace_116[:, 1])[-1]])

    ax2[1].plot(battery_capacity, a_p_driving_cyc, color='#6c969d', linewidth=1.5, label='LFP DR cyc', zorder=10)
    ax2[1].plot(battery_capacity, a_p_driving_cal, color='#6c969d', linewidth=1.5, label='LFP DR cal', zorder=10, linestyle=':')
    ax2[1].plot(battery_capacity, a_p_onroute_cyc, color='#34435e', linewidth=1.5, label='LFP OR cyc', zorder=10)
    ax2[1].plot(battery_capacity, a_p_onroute_cal, color='#34435e', linewidth=1.5, label='LFP OR cal', zorder=10, linestyle=':')
    ax2[1].set_xlabel('Battery capacity in kWh', **csfont, fontsize=textsize)
    ax2[1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    ax2[1].set_ylim((0, 0.1))
    ax2[1].set_xlim((375, 625))
    ax2[1].yaxis.set_major_locator(MultipleLocator(0.025))
    ax2[1].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax2[1].xaxis.set_major_locator(MultipleLocator(50))
    ax2[1].xaxis.set_minor_locator(MultipleLocator(25))
    ax2[1].grid(zorder=0)
    ax2[1].legend(loc='center', bbox_to_anchor=(0.05, -0.55), ncol=2, fontsize=textsize)

    a_p_overnight_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_114[:, 2])[-1], np.cumsum(q_loss_cyclic_trace_122[:, 2])[-1],
         np.cumsum(q_loss_cyclic_trace_116[:, 2])[-1]])
    a_p_overnight_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_114[:, 2])[-1], np.cumsum(q_loss_calendaric_trace_122[:, 2])[-1],
         np.cumsum(q_loss_calendaric_trace_116[:, 2])[-1]])

    a_p_weekend_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_114[:, 3])[-1], np.cumsum(q_loss_cyclic_trace_122[:, 3])[-1],
         np.cumsum(q_loss_cyclic_trace_116[:, 3])[-1]])
    a_p_weekend_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_114[:, 3])[-1], np.cumsum(q_loss_calendaric_trace_122[:, 3])[-1],
         np.cumsum(q_loss_calendaric_trace_116[:, 3])[-1]])

    ax2[2].plot(battery_capacity, a_p_overnight_cyc, color='#aa4465', linewidth=1.5, label='LFP ON cyc', zorder=10)
    ax2[2].plot(battery_capacity, a_p_overnight_cal, color='#aa4465', linewidth=1.5, label='LFP ON cal', zorder=10, linestyle=':')
    ax2[2].plot(battery_capacity, a_p_weekend_cyc, color='#808080', linewidth=1.5, label='LFP WE cyc', zorder=10)
    ax2[2].plot(battery_capacity, a_p_weekend_cal, color='#808080', linewidth=1.5, label='LFP WE cal', zorder=10, linestyle=':')
    ax2[2].set_xlabel('Battery capacity in kWh', **csfont, fontsize=textsize)
    # ax3[1, 1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    #ax2[2].tick_params(labelleft=False)
    ax2[2].set_ylim((0, 0.1))
    ax2[2].set_xlim((375, 625))
    ax2[2].yaxis.set_major_locator(MultipleLocator(0.025))
    ax2[2].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax2[2].xaxis.set_major_locator(MultipleLocator(50))
    ax2[2].xaxis.set_minor_locator(MultipleLocator(25))
    ax2[2].grid(zorder=0)
    ax2[2].legend(loc='center', bbox_to_anchor=(0.25, -0.55), ncol=2, fontsize=textsize)

    # plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_14.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure 15
    # Visualization of second sensitivity analysis with varying weekly distance driven
    height_in_3 = width_in * 5 / 16
    FIGSIZE_3 = (width_in, height_in_3)
    fig3, ax3 = plt.subplots(1, 3)
    fig3.set_size_inches(FIGSIZE_3)
    fig3.tight_layout(w_pad=2)

    # Mileage EOL over weekly distance
    weekly_dis = [1000, 1500, 2000, 2500, 3000]
    mileage_eol_500 = np.array([mileage_macro_trace_1004[-1], mileage_macro_trace_1000[-1], mileage_macro_trace_1002[-1], mileage_macro_trace_1003[-1], mileage_macro_trace_122[-1]]) /1000
    mileage_eol_400 = np.array([mileage_macro_trace_114[-1], mileage_macro_trace_114[-1], mileage_macro_trace_114[-1], mileage_macro_trace_114[-1], mileage_macro_trace_114[-1]]) /1000
    mileage_eol_600 = np.array([mileage_macro_trace_116[-1], mileage_macro_trace_116[-1], mileage_macro_trace_116[-1], mileage_macro_trace_116[-1], mileage_macro_trace_116[-1]]) /1000

    ax3[0].plot(weekly_dis, mileage_eol_500, color=color_lfp, linewidth=1.5, label='LFP 500kWh', zorder=10)
    ax3[0].set_xlabel('Weekly mileage in km', **csfont, fontsize=textsize)
    ax3[0].set_ylabel('Mileage EOL in tkm', **csfont, fontsize=textsize)
    ax3[0].set_ylim((0, 1200))
    ax3[0].set_xlim((1000, 3100))
    ax3[0].yaxis.set_major_locator(MultipleLocator(200))
    ax3[0].yaxis.set_minor_locator(MultipleLocator(100))
    ax3[0].xaxis.set_major_locator(MultipleLocator(500))
    ax3[0].xaxis.set_minor_locator(MultipleLocator(250))
    ax3[0].grid(zorder=0)

    # Weeks EOL over weekly distance
    weeks_eol_500 = np.array([len(mileage_macro_trace_1004), len(mileage_macro_trace_1000), len(mileage_macro_trace_1002), len(mileage_macro_trace_1003), len(mileage_macro_trace_122)])
    weeks_eol_400 = np.array([len(mileage_macro_trace_114), len(mileage_macro_trace_114), len(mileage_macro_trace_114), len(mileage_macro_trace_114), len(mileage_macro_trace_114)])
    weeks_eol_600 = np.array([len(mileage_macro_trace_116), len(mileage_macro_trace_116), len(mileage_macro_trace_116), len(mileage_macro_trace_116), len(mileage_macro_trace_116)])
    # Aging Portions
    a_p_driving_cyc = np.array([np.cumsum(q_loss_cyclic_trace_1004[:, 0])[-1], np.cumsum(q_loss_cyclic_trace_1000[:, 0])[-1],
                                np.cumsum(q_loss_cyclic_trace_1002[:, 0])[-1], np.cumsum(q_loss_cyclic_trace_1003[:, 0])[-1],
                                np.cumsum(q_loss_cyclic_trace_122[:, 0])[-1]])
    a_p_driving_cal = np.array([np.cumsum(q_loss_calendaric_trace_1004[:, 0])[-1], np.cumsum(q_loss_calendaric_trace_1000[:, 0])[-1],
                                np.cumsum(q_loss_calendaric_trace_1002[:, 0])[-1], np.cumsum(q_loss_calendaric_trace_1003[:, 0])[-1],
                                np.cumsum(q_loss_calendaric_trace_122[:, 0])[-1]])

    a_p_onroute_cyc = np.array([np.cumsum(q_loss_cyclic_trace_1004[:, 1])[-1], np.cumsum(q_loss_cyclic_trace_1000[:, 1])[-1],
                                np.cumsum(q_loss_cyclic_trace_1002[:, 1])[-1], np.cumsum(q_loss_cyclic_trace_1003[:, 1])[-1],
                                np.cumsum(q_loss_cyclic_trace_122[:, 1])[-1]])
    a_p_onroute_cal = np.array([np.cumsum(q_loss_calendaric_trace_1004[:, 1])[-1], np.cumsum(q_loss_calendaric_trace_1000[:, 1])[-1],
                                np.cumsum(q_loss_calendaric_trace_1002[:, 1])[-1], np.cumsum(q_loss_calendaric_trace_1003[:, 1])[-1],
                                np.cumsum(q_loss_calendaric_trace_122[:, 1])[-1]])

    ax3[1].plot(weekly_dis, a_p_driving_cyc, color='#6c969d', linewidth=1.5, label='LFP DR cyc', zorder=10)
    ax3[1].plot(weekly_dis, a_p_driving_cal, color='#6c969d', linewidth=1.5, label='LFP DR cal', zorder=10, linestyle=':')
    ax3[1].plot(weekly_dis, a_p_onroute_cyc, color='#34435e', linewidth=1.5, label='LFP OR cyc', zorder=10)
    ax3[1].plot(weekly_dis, a_p_onroute_cal, color='#34435e', linewidth=1.5, label='LFP OR cal', zorder=10, linestyle=':')
    ax3[1].set_xlabel('Weekly mileage in km', **csfont, fontsize=textsize)
    ax3[1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    ax3[1].set_ylim((0, 0.1))
    ax3[1].set_xlim((1000, 3100))
    ax3[1].yaxis.set_major_locator(MultipleLocator(0.025))
    ax3[1].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax3[1].xaxis.set_major_locator(MultipleLocator(500))
    ax3[1].xaxis.set_minor_locator(MultipleLocator(250))
    ax3[1].grid(zorder=0)
    ax3[1].legend(loc='center', bbox_to_anchor=(0.05, -0.55), ncol=2, fontsize=textsize)

    a_p_overnight_cyc = np.array([np.cumsum(q_loss_cyclic_trace_1004[:, 2])[-1], np.cumsum(q_loss_cyclic_trace_1000[:, 2])[-1],
                                np.cumsum(q_loss_cyclic_trace_1002[:, 2])[-1], np.cumsum(q_loss_cyclic_trace_1003[:, 2])[-1],
                                np.cumsum(q_loss_cyclic_trace_122[:, 2])[-1]])
    a_p_overnight_cal = np.array([np.cumsum(q_loss_calendaric_trace_1004[:, 2])[-1], np.cumsum(q_loss_calendaric_trace_1000[:, 2])[-1],
                                np.cumsum(q_loss_calendaric_trace_1002[:, 2])[-1], np.cumsum(q_loss_calendaric_trace_1003[:, 2])[-1],
                                np.cumsum(q_loss_calendaric_trace_122[:, 2])[-1]])

    a_p_weekend_cyc = np.array([np.cumsum(q_loss_cyclic_trace_1004[:, 3])[-1], np.cumsum(q_loss_cyclic_trace_1000[:, 3])[-1],
                                np.cumsum(q_loss_cyclic_trace_1002[:, 3])[-1], np.cumsum(q_loss_cyclic_trace_1003[:, 3])[-1],
                                np.cumsum(q_loss_cyclic_trace_122[:, 3])[-1]])
    a_p_weekend_cal = np.array([np.cumsum(q_loss_calendaric_trace_1004[:, 3])[-1], np.cumsum(q_loss_calendaric_trace_1000[:, 3])[-1],
                                np.cumsum(q_loss_calendaric_trace_1002[:, 3])[-1], np.cumsum(q_loss_calendaric_trace_1003[:, 3])[-1],
                                np.cumsum(q_loss_calendaric_trace_122[:, 3])[-1]])

    ax3[2].plot(weekly_dis, a_p_overnight_cyc, color='#aa4465', linewidth=1.5, label='LFP ON cyc', zorder=10)
    ax3[2].plot(weekly_dis, a_p_overnight_cal, color='#aa4465', linewidth=1.5, label='LFP ON cal', zorder=10, linestyle=':')
    ax3[2].plot(weekly_dis, a_p_weekend_cyc, color='#808080', linewidth=1.5, label='LFP WE cyc', zorder=10)
    ax3[2].plot(weekly_dis, a_p_weekend_cal, color='#808080', linewidth=1.5, label='LFP WE cal', zorder=10, linestyle=':')
    ax3[2].set_xlabel('Weekly mileage in km', **csfont, fontsize=textsize)
    # ax3[1, 1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    #ax3[1, 1].tick_params(labelleft=False)
    ax3[2].set_ylim((0, 0.1))
    ax3[2].set_xlim((1000, 3100))
    ax3[2].yaxis.set_major_locator(MultipleLocator(0.025))
    ax3[2].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax3[2].xaxis.set_major_locator(MultipleLocator(500))
    ax3[2].xaxis.set_minor_locator(MultipleLocator(250))
    ax3[2].grid(zorder=0)
    ax3[2].legend(loc='center', bbox_to_anchor=(0.25, -0.55), ncol=2, fontsize=textsize)
    plt.text(0.5, -0.35, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax3[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax3[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax3[2].transAxes, fontsize=textsize, rotation=0)

    #plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_15.svg', dpi=400, bbox_inches='tight')

    plt.show()

    # Figure 16:
    # Visualization of second sensitivity analysis with varying weekly distance driven
    height_in_3 = width_in * 5 / 16
    FIGSIZE_3 = (width_in, height_in_3)
    fig3, ax3 = plt.subplots(1, 3)
    fig3.set_size_inches(FIGSIZE_3)
    fig3.tight_layout(w_pad=2)

    # Mileage EOL over weekly distance
    weekly_dis = [25, 50, 100]
    mileage_eol_500 = np.array(
        [mileage_macro_trace_122[-1], mileage_macro_trace_1050[-1], mileage_macro_trace_1100[-1]]) / 1000


    ax3[0].plot(weekly_dis, mileage_eol_500, color=color_lfp, linewidth=1.5, label='LFP 500kWh', zorder=10)
    ax3[0].set_xlabel('Distance between Charger in km', **csfont, fontsize=textsize)
    ax3[0].set_ylabel('Mileage EOL in tkm', **csfont, fontsize=textsize)
    ax3[0].set_ylim((0, 1200))
    ax3[0].set_xlim((25, 125))
    ax3[0].yaxis.set_major_locator(MultipleLocator(200))
    ax3[0].yaxis.set_minor_locator(MultipleLocator(100))
    ax3[0].xaxis.set_major_locator(MultipleLocator(25))
    ax3[0].xaxis.set_minor_locator(MultipleLocator(12.5))
    ax3[0].grid(zorder=0)

    # Aging Portions
    a_p_driving_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_122[:, 0])[-1], np.cumsum(q_loss_cyclic_trace_1050[:, 0])[-1], np.cumsum(q_loss_cyclic_trace_1100[:, 0])[-1]])
    a_p_driving_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_122[:, 0])[-1], np.cumsum(q_loss_calendaric_trace_1050[:, 0])[-1], np.cumsum(q_loss_calendaric_trace_1100[:, 0])[-1]])
    a_p_onroute_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_122[:, 1])[-1], np.cumsum(q_loss_cyclic_trace_1050[:, 1])[-1], np.cumsum(q_loss_cyclic_trace_1100[:, 1])[-1]])
    a_p_onroute_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_122[:, 1])[-1], np.cumsum(q_loss_calendaric_trace_1050[:, 1])[-1], np.cumsum(q_loss_calendaric_trace_1100[:, 1])[-1]])

    ax3[1].plot(weekly_dis, a_p_driving_cyc, color='#6c969d', linewidth=1.5, label='LFP DR cyc', zorder=10)
    ax3[1].plot(weekly_dis, a_p_driving_cal, color='#6c969d', linewidth=1.5, label='LFP DR cal', zorder=10, linestyle=':')
    ax3[1].plot(weekly_dis, a_p_onroute_cyc, color='#34435e', linewidth=1.5, label='LFP OR cyc', zorder=10)
    ax3[1].plot(weekly_dis, a_p_onroute_cal, color='#34435e', linewidth=1.5, label='LFP OR cal', zorder=10, linestyle=':')
    ax3[1].set_xlabel('Distance between Charger in km', **csfont, fontsize=textsize)
    ax3[1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    ax3[1].set_ylim((0, 0.1))
    ax3[1].set_xlim((25, 125))
    ax3[1].yaxis.set_major_locator(MultipleLocator(0.025))
    ax3[1].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax3[1].xaxis.set_major_locator(MultipleLocator(25))
    ax3[1].xaxis.set_minor_locator(MultipleLocator(12.5))
    ax3[1].grid(zorder=0)
    ax3[1].legend(loc='center', bbox_to_anchor=(0.05, -0.55), ncol=2, fontsize=textsize)

    a_p_overnight_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_122[:, 2])[-1], np.cumsum(q_loss_cyclic_trace_1050[:, 2])[-1], np.cumsum(q_loss_cyclic_trace_1100[:, 2])[-1]])
    a_p_overnight_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_122[:, 2])[-1], np.cumsum(q_loss_calendaric_trace_1050[:, 2])[-1], np.cumsum(q_loss_calendaric_trace_1100[:, 2])[-1]])
    a_p_weekend_cyc = np.array(
        [np.cumsum(q_loss_cyclic_trace_122[:, 3])[-1], np.cumsum(q_loss_cyclic_trace_1050[:, 3])[-1], np.cumsum(q_loss_cyclic_trace_1100[:, 3])[-1]])
    a_p_weekend_cal = np.array(
        [np.cumsum(q_loss_calendaric_trace_122[:, 3])[-1], np.cumsum(q_loss_calendaric_trace_1050[:, 3])[-1], np.cumsum(q_loss_calendaric_trace_1100[:, 3])[-1]])

    ax3[2].plot(weekly_dis, a_p_overnight_cyc, color='#aa4465', linewidth=1.5, label='LFP ON cyc', zorder=10)
    ax3[2].plot(weekly_dis, a_p_overnight_cal, color='#aa4465', linewidth=1.5, label='LFP ON cal', zorder=10, linestyle=':')
    ax3[2].plot(weekly_dis, a_p_weekend_cyc, color='#808080', linewidth=1.5, label='LFP WE cyc', zorder=10)
    ax3[2].plot(weekly_dis, a_p_weekend_cal, color='#808080', linewidth=1.5, label='LFP WE cal', zorder=10, linestyle=':')
    ax3[2].set_xlabel('Distance between Charger in km', **csfont, fontsize=textsize)
    # ax3[1, 1].set_ylabel('Capacity loss in %', **csfont, fontsize=textsize)
    # ax3[1, 1].tick_params(labelleft=False)
    ax3[2].set_ylim((0, 0.1))
    ax3[2].set_xlim((25, 125))
    ax3[2].yaxis.set_major_locator(MultipleLocator(0.025))
    ax3[2].yaxis.set_minor_locator(MultipleLocator(0.0125))
    ax3[2].xaxis.set_major_locator(MultipleLocator(25))
    ax3[2].xaxis.set_minor_locator(MultipleLocator(12.5))
    ax3[2].grid(zorder=0)
    ax3[2].legend(loc='center', bbox_to_anchor=(0.25, -0.55), ncol=2, fontsize=textsize)
    plt.text(0.5, -0.35, '(a)', horizontalalignment='center', verticalalignment='center', transform=ax3[0].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(b)', horizontalalignment='center', verticalalignment='center', transform=ax3[1].transAxes, fontsize=textsize, rotation=0)
    plt.text(0.5, -0.35, '(c)', horizontalalignment='center', verticalalignment='center', transform=ax3[2].transAxes, fontsize=textsize, rotation=0)

    # plt.savefig('Modules/M14_EOL_Simulation/M14_Figures/Paper/Paper_Figure_16.svg', dpi=400, bbox_inches='tight')

    plt.show()

    return