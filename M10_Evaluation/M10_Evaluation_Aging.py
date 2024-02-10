# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-08-23
# Last update:
#
# Function Description
# Script for aging evaluation after one scenario run
#
# _________________________________

# import libraries
import numpy as np
from scipy.interpolate import interp1d
from Modules.M10_Evaluation.M10_0_Aging_Model import aging_main


# Main Function for Aging Evaluation
def aging_evaluation(sim, env, vehicle):
    # Only if scenario specifies aging evaluation
    if sim.aging_eval > 0:
        # Get Power Profile
        sim = power_profile(sim, env, vehicle)
        # Call Electric and Thermal Battery Model (Schneider et al.)
        if max(abs(sim.betos_aging_power_profile)) > 0:
            # Evaluate Aging (Schneider et al., Schmalstieg et al., Naumann et al.)
            sim = aging_main.aging_function(sim, env, vehicle)

            # Safe position and time step
            sim.eol_battery_aging_pos[sim.eol_aging_evaluation_event] = sim.step_dis / 1000                          # in km
            sim.eol_battery_aging_time_step[sim.eol_aging_evaluation_event] = sim.step_time
            sim.eol_battery_aging_time[sim.eol_aging_evaluation_event] = sum(sim.time_time[0:sim.step_time]) / 3600  # in h

            # Count eol aging evaluation events
            sim.eol_aging_evaluation_event = sim.eol_aging_evaluation_event + 1

    return sim, env, vehicle


## _____________________________________________________________________________________________________________________
## Helpfunctions
# Power Profile Generation
def power_profile(sim, env, vehicle):
    # Use SOC Profile of considered aging time horizon over time to extract power profile
    # Interpolate SOC Profile for equidistant time steps
    time_cum = np.floor(np.concatenate((np.array([0]), np.cumsum(sim.time_time[int(sim.eol_battery_aging_time_step[sim.eol_aging_evaluation_event - 1]):sim.step_time]))))       # cumulated time series
    soc = sim.bat_soc_time[int(sim.eol_battery_aging_time_step[sim.eol_aging_evaluation_event - 1]):sim.step_time + 1]                                                 # soc profile
    max_time = int(time_cum[-1])                                                                # total time in sec
    time_vector = np.linspace(0, max_time, max_time+1)                                          # equidistant time series

    soc_interpol_func = interp1d(time_cum, soc, kind='linear')                                  # Interpolation function for soc
    # Save in sim object
    sim.betos_aging_soc_profile = soc_interpol_func(time_vector)
    sim.betos_aging_time_profile = time_vector

    # Calculate Power Profile from SoC Profile
    energy = vehicle.battery_capacity * sim.betos_aging_soc_profile * 3600 * 1000   # in Ws
    delta_energy = energy[0:len(energy)-1] - energy[1:]                             # energy change per second in Ws
    power = delta_energy                                                            # in case that time step is one second in W

    # Handle interpolation errors in soc trace in charging cases
    if sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] == 1:
        # Search for no changing in original soc trace
        time_zero_first = time_cum[1:]
        time_zero_second = time_cum[0:int(len(soc)-1)]
        zero_values_first = time_zero_first[(soc[0:len(soc)-1] - soc[1:]) == 0]
        zero_values_second = time_zero_second[(soc[0:len(soc) - 1] - soc[1:]) == 0]
        # Power should be zero during no changing in SOC
        power[0:int(zero_values_first[1]+1)] = 0
        power[int(zero_values_second[2]):] = 0

    # Limit power Profile to max 1500 kW (3C)
    power = np.minimum(power, 1000 * 1000)
    # Limit power Profile to min - 1000 kW (Driving)
    power = np.maximum(power, -1500 * 1000)

    # Check if on route charging for charging losses
    if sim.eol_battery_aging_event_id[sim.eol_aging_evaluation_event] == 1:
        power = power/vehicle.battery_charge_loss

    # Save in sim object
    sim.betos_aging_power_profile = power

    return sim



## Aging and V2G Helpfunctions:
def evaluate_aging_v2g(extracted_data, soc, vehicle_battery_capacity_kWh, vehicle_initial_soh):
    C_N = 2.05
    IDA = extracted_data[:, 2]
    scaling_factor = 0.43  # Teichert et al. ID3 NMC Cell

    f1 = 1 - vehicle_initial_soh
    f2 = 0
    g1 = []
    g2 = []
    Q = 0
    Q_virtual = 0
    for i in range(1, len(soc)):
        SoC_start_i = soc[i]
        SoC_start_i_1 = soc[i - 1]
        # Q_virtual = Q_virtual + Q
        Q = abs(SoC_start_i - SoC_start_i_1) * C_N

        # Mean Voltage
        mean_v = (-3.46 * pow(((SoC_start_i_1 + SoC_start_i) / 2), 4) + 8.033 *
                  pow(((SoC_start_i_1 + SoC_start_i) / 2), 3) - 5.849 *
                  pow(((SoC_start_i_1 + SoC_start_i) / 2), 2) + 2.102 * (((SoC_start_i_1 + SoC_start_i) / 2)) + 3.332)

        #term = (np.sqrt((Q + Q_virtual) * C_N) - np.sqrt(Q_virtual * C_N))

        # Belastungsfaktor beta
        beta = (7.348 * pow(10, -3) * pow((mean_v-3.667), 2) + (7.600 * pow(10, -4)) + (4.081 * pow(10, -3)) * abs(
            SoC_start_i - SoC_start_i_1))

        # Bisheriger Ladungsdurchsatz: Annahme Beta konstant
        Q_virtual = (f1/scaling_factor/beta)**2

        # Ladungsdurchsatz
        sr_q = np.sqrt(Q + Q_virtual)

        # Aging
        f1 = beta * scaling_factor * sr_q

        # Zielfunktion f2 -> Generierte Einnahmen; IDA für DA 15 min in EUR/MWh
        if i == 1:
            price = IDA[0]
        else:
            price = IDA[i-1]
        f2 += (price * (SoC_start_i - SoC_start_i_1) * vehicle_battery_capacity_kWh / 1000)  # Gesamte Batteriekapazität Fahrzeug z.B. 500 kWh = 0.5 MWh


    # Constraint for maximum 1 C Chareg/Discharge
    x_i_1 = soc[0:len(soc)-1]
    x_i = soc[1:]
    delta = abs(x_i-x_i_1)

    g1 = max(delta) - 0.25

    return f1, f2, g1

