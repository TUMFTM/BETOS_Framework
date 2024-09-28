# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-08-31
#
# Function Description
# Main Function of the EOL Simulation
# for battery electric trucks
# _________________________________


# import libraries
import numpy as np

# import BETOS Functions
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_Multiday_Simulation
from Modules.M9_Operation_Strategy.M9_0_Charging_Management_Multiday.M9_0_3_Weekend import M903_Weekend_CM
import scenario_aging


# Main EOL Simulation
def eol_simulation():
    # <>
    # Get Scenario for one week, 3000km
    scenario_eol = scenario_aging.scenario_aging(1)
    # eol object def for keeping relevant parameters over lifetime

    class EOL:
        pass
    eol = EOL()

    # <>
    # Initialization:
    # EOL not reached
    eol.eol_not_reached = True
    # EOL week count
    eol.week_count = 0  # Start with week 0
    # EOL milage
    eol.milage = 0  # in km
    eol.milage_trace = np.zeros(1000)
    # vehicle battery soh
    eol.battery_soh = 1
    eol.battery_soh_trace = np.zeros(1000)
    eol.battery_soh_trace[0] = 1
    # vehicle battery internal resistance
    eol.battery_internal_resistance_cyclic = 0
    eol.battery_internal_resistance_calendaric = 0
    # vehicle battery capacity loss
    eol.battery_q_loss_cyclic = 0
    eol.battery_q_loss_calendaric = 0
    # initial battery_capacity
    eol.battery_capacity_initial_kWh = scenario_eol['battery_capacity'][0]
    # battery capacity trace
    eol.battery_capacity_trace = np.zeros(10000)

    # <>
    # While loop till EOL is not reached (SOH > 0.8)
    while eol.milage < 1500000 and eol.battery_soh > 0.8:
        # <> Simulation Functions:
        # Start Multiday Simulation (Driving from Monday till Friday)
        sim, env, vehicle, results = M84_Multiday_Simulation.opsim_multiday(scenario_eol, eol)
        # Start Weekend Simulation (Weekend Charging Simulation)
        sim, env, vehicle = M903_Weekend_CM.weekend_charging(sim, env, vehicle)

        # <> Save results:
        # Count Weeks
        eol.week_count = eol.week_count + 1
        # Count milage
        eol.milage = eol.milage + (sim.dis_steps / 1000)  # in km
        eol.milage_trace[eol.week_count] = eol.milage
        # Internal resistance values after one week
        eol.battery_internal_resistance_cyclic = sim.eol_battery_internal_resistance_cyclic[sim.eol_aging_evaluation_event - 1]
        eol.battery_internal_resistance_calendaric = sim.eol_battery_internal_resistance_calendaric[sim.eol_aging_evaluation_event - 1]
        # Capacity loss values after one week
        eol.battery_q_loss_cyclic = sim.eol_battery_q_loss_cyclic[sim.eol_aging_evaluation_event - 1]
        eol.battery_q_loss_calendaric = sim.eol_battery_q_loss_calendaric[sim.eol_aging_evaluation_event - 1]
        # SOH after one week
        eol.battery_soh = sim.eol_battery_soh[sim.eol_aging_evaluation_event - 1]
        eol.battery_soh_trace[eol.week_count] = eol.battery_soh
        # Time loss per week and trip
        # Battery Capacity
        eol.battery_capacity_trace[eol.week_count] = eol.battery_capacity_initial_kWh * eol.battery_soh
        # Save results for one week in M14_EOL_Results
        eol_save_results(sim, env, vehicle, scenario_eol, eol, results)

    return eol


# Save results after one week
def eol_save_results(sim, env, vehicle, scenario, eol, results):
    # Built path: Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_id_week_j.csv
    str_1 = 'Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_'
    str_2 = '_week_'
    str_end = '.csv'

    str_dis = str_1 + str(int(scenario['scenario_id'][0])) + str_2 + str(int(eol.week_count)) + str_end

    # Built dataset
    weekly_results = np.zeros((len(sim.eol_battery_soc_value[0:sim.eol_aging_evaluation_event]), 16))

    weekly_results[:, 0] = sim.eol_battery_soc_value[0:sim.eol_aging_evaluation_event]          # SOC Trace
    weekly_results[:, 1] = sim.eol_battery_soh[0:sim.eol_aging_evaluation_event]                # SOH Trace
    weekly_results[:, 2] = sim.eol_battery_aging_time[0:sim.eol_aging_evaluation_event]         # Time stamp
    weekly_results[:, 3] = sim.eol_battery_aging_pos[0:sim.eol_aging_evaluation_event]          # Position stamp
    weekly_results[:, 4] = sim.eol_battery_dod[0:sim.eol_aging_evaluation_event]                # DOD
    weekly_results[:, 5] = sim.eol_battery_soc_avg[0:sim.eol_aging_evaluation_event]            # Average SOC
    weekly_results[:, 6] = sim.eol_battery_crate_mean[0:sim.eol_aging_evaluation_event]         # Average CRate
    weekly_results[:, 7] = sim.eol_battery_crate_max[0:sim.eol_aging_evaluation_event]          # Max Crate
    weekly_results[:, 8] = sim.eol_battery_temp_mean[0:sim.eol_aging_evaluation_event]          # Average Temperature Cell
    weekly_results[0:len(results['driving_time_day_h']), 9] = results['driving_time_day_h']     # Driving times per Day
    weekly_results[0, 10] = sum(sim.betos_down_time)                                            # Downtime per week
    weekly_results[:, 11] = sim.eol_battery_aging_event_id[0:sim.eol_aging_evaluation_event]    # Event ID (0 Driving, 1 On Route, 2 Overnight, 3 Weekend)
    weekly_results[:, 12] = sim.eol_battery_q_loss_calendaric[0:sim.eol_aging_evaluation_event] # Calendaric Q Loss
    weekly_results[:, 13] = sim.eol_battery_q_loss_cyclic[0:sim.eol_aging_evaluation_event]     # Cyclic Q Loss
    weekly_results[:, 14] = sim.eol_battery_internal_resistance_calendaric[0:sim.eol_aging_evaluation_event]    # Resistance increase calendaric
    weekly_results[:, 15] = sim.eol_battery_internal_resistance_cyclic[0:sim.eol_aging_evaluation_event]        # Resistance increase cyclic

    # Save as csv
    np.savetxt(str_dis, weekly_results, delimiter=",")

    return

