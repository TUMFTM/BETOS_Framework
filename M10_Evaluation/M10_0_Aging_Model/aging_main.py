# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-09-01 (first Implementation by J.S.)
#
# Function Description
# Part of the Evaluation Module for Aging Analysis
# Main Function of the Aging Evaluation
# _________________________________

from Modules.M10_Evaluation.M10_0_Aging_Model.init_battery_data import load_cell_data
from Modules.M10_Evaluation.M10_0_Aging_Model.batteryElectricTruck import BatteryElectricTruck
from Modules.M10_Evaluation.M10_0_Aging_Model.ElectroThermalSingle import calcElectroThermalValuesSingle
from Modules.M10_Evaluation.M10_0_Aging_Model.Aging_Model import calc_aging_routing
import numpy as np


def aging_function(sim, env, vehicle):

    # Chemistry 0:Schmalstieg et. al.  1:Naumann et.al.
    cell_chemistry = vehicle.cell_type
    bet = BatteryElectricTruck()
    battery_capacity = vehicle.battery_capacity          # in kWh
    p_profile = -1 * sim.betos_aging_power_profile       # in W
    dt = 1                                               # in sec

    # Get Cell data from data sheet
    cell = load_cell_data(cell_chemistry, bet)           # Initialize Cell Data + Gravimetric Density / C2P
    # Number of Cells
    n_cells = (battery_capacity * 1000) / (cell.Qnom * cell.Unom)

    # Single Cell Aging Evaluation
    # Initialize variables for clectrothermal Cell Model
    p_value_control = np.zeros((len(p_profile)))
    SOC = np.zeros((len(p_profile)+1))
    Crate = np.zeros((len(p_profile)))
    P_Loss = np.zeros((len(p_profile)))
    T_Cell = np.zeros((len(p_profile)+1))
    T_Housing= np.zeros((len(p_profile)+1))
    P_Cool = np.zeros((len(p_profile)))
    P_Heat = np.zeros((len(p_profile)))

    # Initialize Start Values
    T_Cell[0] = sim.eol_battery_temperature_cell[sim.eol_aging_evaluation_event - 1]                         # Start Temperature of cells
    T_Housing[0] = sim.eol_battery_temperature_housing[sim.eol_aging_evaluation_event - 1]                   # Start Temperature of Housing
    SOC[0] = sim.bat_soc_time[int(sim.eol_battery_aging_time_step[sim.eol_aging_evaluation_event - 1])]      # Start SOC of cells
    T_amb = 20                                                                                               # Ambient Temperature in Grad Celius

    # Run electrothermal model along power vector to receive soc, c-rate, T for aging evaluation
    for idx_p_profile, P_Value_Vehicle in enumerate(p_profile):

        SOC[idx_p_profile+1], Crate[idx_p_profile], P_Value_control, P_Cool[idx_p_profile], T_Cell[idx_p_profile+1], T_Housing[idx_p_profile+1] = calcElectroThermalValuesSingle(cell, bet,
                                        n_cells, T_Cell[idx_p_profile], SOC[idx_p_profile], Crate[idx_p_profile], P_Value_Vehicle, P_Cool[idx_p_profile-1], T_Housing[idx_p_profile], T_amb, dt)

    # Aging Evaluation for given power profile
    # Input from previous calculated aging results
    Q_loss_cal_prev = sim.eol_battery_q_loss_calendaric[sim.eol_aging_evaluation_event - 1]
    Q_loss_cyc_prev = sim.eol_battery_q_loss_cyclic[sim.eol_aging_evaluation_event - 1]
    R_inc_cal_prev = sim.eol_battery_internal_resistance_calendaric[sim.eol_aging_evaluation_event - 1]
    R_inc_cyc_prev = sim.eol_battery_internal_resistance_cyclic[sim.eol_aging_evaluation_event - 1]
    # Get new aging varaibles: res = [Qloss_ges, Rinc_ges, Qloss_new_cal, Rinc_new_cal, Qloss_new_cyc, Rinc_new_cyc, DODs, SOCavgs]
    res_aging = calc_aging_routing(cell_chemistry, cell, SOC, T_Cell, Crate, Q_loss_cal_prev, Q_loss_cyc_prev, R_inc_cal_prev, R_inc_cyc_prev, dt, sim)

    # Scaling Aging effects through higher C rates than 1:
    if sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] == 1:
        scaling_factor = max(1, np.max(Crate[np.abs(sim.betos_aging_power_profile) > 0]))     # C max scaling
        # scaling_factor = max(1, np.mean(Crate[np.abs(sim.betos_aging_power_profile) > 0]))  # C mean scaling
    else:
        scaling_factor = 1

    # Scale Cyclic aging parameters (Only scale the increase!!!):
    res_aging[4] = Q_loss_cyc_prev + (scaling_factor * (res_aging[4] - Q_loss_cyc_prev))   # Q Loss cyclic
    res_aging[5] = R_inc_cyc_prev + (scaling_factor * (res_aging[5] - R_inc_cyc_prev))    # R inc cyclic
    res_aging[0] = res_aging[2] + res_aging[4]                                          # Q loss total
    res_aging[1] = res_aging[3] + res_aging[5]                                          # R inc total

    # Calculation of battery SOH
    sim.eol_battery_soh[sim.eol_aging_evaluation_event] = (vehicle.battery_capacity - (vehicle.battery_capacity * res_aging[0])) / vehicle.battery_capacity

    # Save other aging parameters in sim object
    sim.eol_battery_internal_resistance_cyclic[sim.eol_aging_evaluation_event] = res_aging[5]
    sim.eol_battery_internal_resistance_calendaric[sim.eol_aging_evaluation_event] = res_aging[3]
    sim.eol_battery_q_loss_cyclic[sim.eol_aging_evaluation_event] = 1-((vehicle.battery_capacity - (vehicle.battery_capacity * res_aging[4])) / vehicle.battery_capacity)
    sim.eol_battery_q_loss_calendaric[sim.eol_aging_evaluation_event] = 1-((vehicle.battery_capacity - (vehicle.battery_capacity * res_aging[2])) / vehicle.battery_capacity)
    sim.eol_battery_temperature_cell[sim.eol_aging_evaluation_event] = T_Cell[-1]
    sim.eol_battery_temperature_housing[sim.eol_aging_evaluation_event] = T_Housing[-1]
    sim.eol_battery_soc_value[sim.eol_aging_evaluation_event] = SOC[-1]
    sim.eol_battery_dod[sim.eol_aging_evaluation_event] = res_aging[6][0]
    sim.eol_battery_soc_avg[sim.eol_aging_evaluation_event] = res_aging[7][0]
    sim.eol_battery_crate_mean[sim.eol_aging_evaluation_event] = np.mean(Crate[np.abs(sim.betos_aging_power_profile) > 0])
    sim.eol_battery_crate_max[sim.eol_aging_evaluation_event] = np.max(Crate)
    sim.eol_battery_temp_mean[sim.eol_aging_evaluation_event] = np.mean(T_Cell)

    return sim

