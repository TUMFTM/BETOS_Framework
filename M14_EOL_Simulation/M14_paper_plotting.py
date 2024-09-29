# _________________________________
# BET.OS Function #
#
# Designed by MX-2024-05-05
#
# Function Description
# Part of the EOL Simulation Module M14
# Analysis of EOL Simulation Results: Plotting Script for the research article: Fast track to a million
#
# _________________________________

from Modules.M14_EOL_Simulation.M14_EOL_Analysis import read_eol_data
from Modules.M14_EOL_Simulation.M14_EOL_Analysis import eol_visualization_cell_chemistry_comparision
from Modules.M14_EOL_Simulation.M14_EOL_Analysis import eol_visualization_million_drive

# Read EOL Results Datasets
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

# Plotting Functions
eol_visualization_million_drive(milage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7, soh_trace_7,
                                milage_trace_7, dod_trace_7, event_id_trace_7, avg_crate_values_7,
                                q_loss_cyclic_trace_7, q_loss_calendaric_trace_7, avg_soc_values_7,
                                milage_macro_trace_122, soh_drop_week_122, time_loss_per_week_day_122, soh_trace_122,
                                milage_trace_122, dod_trace_122, event_id_trace_122, avg_crate_values_122,
                                q_loss_cyclic_trace_122, q_loss_calendaric_trace_122, avg_soc_values_122,
                                milage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8, soh_trace_8,
                                milage_trace_8, dod_trace_8, event_id_trace_8, avg_crate_values_8,
                                q_loss_cyclic_trace_8, q_loss_calendaric_trace_8, avg_soc_values_8,
                                milage_macro_trace_222, soh_drop_week_222, time_loss_per_week_day_222, soh_trace_222,
                                milage_trace_222, dod_trace_222, event_id_trace_222, avg_crate_values_222,
                                q_loss_cyclic_trace_222, q_loss_calendaric_trace_222, avg_soc_values_222,
                                milage_macro_trace_114, soh_drop_week_114, time_loss_per_week_day_114, soh_trace_114,
                                milage_trace_114, dod_trace_114, event_id_trace_114, avg_crate_values_114,
                                q_loss_cyclic_trace_114, q_loss_calendaric_trace_114, avg_soc_values_114,
                                milage_macro_trace_116, soh_drop_week_116, time_loss_per_week_day_116, soh_trace_116,
                                milage_trace_116, dod_trace_116, event_id_trace_116, avg_crate_values_116,
                                q_loss_cyclic_trace_116, q_loss_calendaric_trace_116, avg_soc_values_116,
                                milage_macro_trace_1000, soh_drop_week_1000, time_loss_per_week_day_1000,
                                soh_trace_1000, milage_trace_1000, dod_trace_1000, event_id_trace_1000,
                                avg_crate_values_1000, q_loss_cyclic_trace_1000, q_loss_calendaric_trace_1000,
                                avg_soc_values_1000,
                                milage_macro_trace_1002, soh_drop_week_1002, time_loss_per_week_day_1002,
                                soh_trace_1002, milage_trace_1002, dod_trace_1002, event_id_trace_1002,
                                avg_crate_values_1002, q_loss_cyclic_trace_1002, q_loss_calendaric_trace_1002,
                                avg_soc_values_1002,
                                milage_macro_trace_1003, soh_drop_week_1003, time_loss_per_week_day_1003,
                                soh_trace_1003, milage_trace_1003, dod_trace_1003, event_id_trace_1003,
                                avg_crate_values_1003, q_loss_cyclic_trace_1003, q_loss_calendaric_trace_1003,
                                avg_soc_values_1003,
                                milage_macro_trace_1004, soh_drop_week_1004, time_loss_per_week_day_1004,
                                soh_trace_1004, milage_trace_1004, dod_trace_1004, event_id_trace_1004,
                                avg_crate_values_1004, q_loss_cyclic_trace_1004, q_loss_calendaric_trace_1004,
                                avg_soc_values_1004,
                                milage_macro_trace_1100, soh_drop_week_1100, time_loss_per_week_day_1100,
                                soh_trace_1100, milage_trace_1100, dod_trace_1100, event_id_trace_1100,
                                avg_crate_values_1100, q_loss_cyclic_trace_1100, q_loss_calendaric_trace_1100,
                                avg_soc_values_1100,
                                milage_macro_trace_1050, soh_drop_week_1050, time_loss_per_week_day_1050,
                                soh_trace_1050, milage_trace_1050, dod_trace_1050, event_id_trace_1050,
                                avg_crate_values_1050, q_loss_cyclic_trace_1050, q_loss_calendaric_trace_1050,
                                avg_soc_values_1050)

eol_visualization_cell_chemistry_comparision(milage_macro_trace_1, soh_drop_week_1, time_loss_per_week_day_1,
                                             soh_trace_1, milage_trace_1, dod_trace_1, event_id_trace_1,
                                             avg_crate_values_1, q_loss_cyclic_trace_1, q_loss_calendaric_trace_1,
                                             avg_soc_values_1,
                                             milage_macro_trace_2, soh_drop_week_2, time_loss_per_week_day_2,
                                             soh_trace_2, milage_trace_2, dod_trace_2, event_id_trace_2,
                                             avg_crate_values_2, q_loss_cyclic_trace_2, q_loss_calendaric_trace_2,
                                             avg_soc_values_2,
                                             milage_macro_trace_7, soh_drop_week_7, time_loss_per_week_day_7,
                                             soh_trace_7, milage_trace_7, dod_trace_7, event_id_trace_7,
                                             avg_crate_values_7, q_loss_cyclic_trace_7, q_loss_calendaric_trace_7,
                                             avg_soc_values_7,
                                             milage_macro_trace_8, soh_drop_week_8, time_loss_per_week_day_8,
                                             soh_trace_8, milage_trace_8, dod_trace_8, event_id_trace_8,
                                             avg_crate_values_8, q_loss_cyclic_trace_8, q_loss_calendaric_trace_8,
                                             avg_soc_values_8,
                                             milage_macro_trace_9, soh_drop_week_9, time_loss_per_week_day_9,
                                             soh_trace_9, milage_trace_9, dod_trace_9, event_id_trace_9,
                                             avg_crate_values_9, q_loss_cyclic_trace_9, q_loss_calendaric_trace_9,
                                             avg_soc_values_9,
                                             milage_macro_trace_10, soh_drop_week_10, time_loss_per_week_day_10,
                                             soh_trace_10, milage_trace_10, dod_trace_10, event_id_trace_10,
                                             avg_crate_values_10, q_loss_cyclic_trace_10, q_loss_calendaric_trace_10,
                                             avg_soc_values_10,
                                             milage_macro_trace_32, soh_drop_week_32, time_loss_per_week_day_32,
                                             soh_trace_32, milage_trace_32, dod_trace_32, event_id_trace_32,
                                             avg_crate_values_32, q_loss_cyclic_trace_32, q_loss_calendaric_trace_32,
                                             avg_soc_values_32,
                                             milage_macro_trace_42, soh_drop_week_42, time_loss_per_week_day_42,
                                             soh_trace_42, milage_trace_42, dod_trace_42, event_id_trace_42,
                                             avg_crate_values_42, q_loss_cyclic_trace_42, q_loss_calendaric_trace_42,
                                             avg_soc_values_42,
                                             milage_macro_trace_33, soh_drop_week_33, time_loss_per_week_day_33,
                                             soh_trace_33, milage_trace_33, dod_trace_33, event_id_trace_33,
                                             avg_crate_values_33, q_loss_cyclic_trace_33, q_loss_calendaric_trace_33,
                                             avg_soc_values_33,
                                             milage_macro_trace_332, soh_drop_week_332, time_loss_per_week_day_332,
                                             soh_trace_332, milage_trace_332, dod_trace_332, event_id_trace_332,
                                             avg_crate_values_332, q_loss_cyclic_trace_332, q_loss_calendaric_trace_332,
                                             avg_soc_values_332,
                                             milage_macro_trace_43, soh_drop_week_43, time_loss_per_week_day_43,
                                             soh_trace_43, milage_trace_43, dod_trace_43, event_id_trace_43,
                                             avg_crate_values_43, q_loss_cyclic_trace_43, q_loss_calendaric_trace_43,
                                             avg_soc_values_43,
                                             milage_macro_trace_92, soh_drop_week_92, time_loss_per_week_day_92,
                                             soh_trace_92, milage_trace_92, dod_trace_92, event_id_trace_92,
                                             avg_crate_values_92, q_loss_cyclic_trace_92, q_loss_calendaric_trace_92,
                                             avg_soc_values_92,
                                             milage_macro_trace_102, soh_drop_week_102, time_loss_per_week_day_102,
                                             soh_trace_102, milage_trace_102, dod_trace_102, event_id_trace_102,
                                             avg_crate_values_102, q_loss_cyclic_trace_102, q_loss_calendaric_trace_102,
                                             avg_soc_values_102)


