# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-08-29
#
# Function Description
# Part of the Dynamic Vehicle Modul M6
# Main File of the dynamic vehicle modul for calculation of energy consumption out of necessary acceleration
# _________________________________


# Import functions
import numpy as np


# Used sources in this file


# Main Function
def dynamic_vehicle_model(sim, env, vehicle):
    # Direction: From Wheel to Battery
    sim.pt_direction = 0
    # Run
    sim, vehicle = vehicle_fde(sim, vehicle, env)
    sim, vehicle = vehicle_wheel(sim, vehicle)
    sim, vehicle = vehicle_gear(sim, vehicle)
    sim, vehicle = vehicle_em(sim, vehicle)
    sim, vehicle = vehicle_pe(sim, vehicle)
    sim, vehicle = vehicle_battery(sim, vehicle, env)

    # Direction: From Battery to Wheel
    sim.pt_direction = 1
    # Run
    sim, vehicle = vehicle_pe(sim, vehicle)
    sim, vehicle = vehicle_em(sim, vehicle)
    sim, vehicle = vehicle_gear(sim, vehicle)
    sim, vehicle = vehicle_wheel(sim, vehicle)
    # Brake if necessary
    if vehicle.wheel_torque_request < 0:
        sim, vehicle = vehicle_brake(sim, vehicle)
    else:
        vehicle.brake_limit = 0
    # FDE
    sim, vehicle = vehicle_fde(sim, vehicle, env)

    return sim, vehicle


# Fundamental Equations of motion
def vehicle_fde(sim, vehicle, env):
    # Current Speed sim.vel_dis[sim.step_dis]
    # Get required acceleration due to cycle speed: sim.acc_target_dis[sim.step_dis]

    # Air Resistance
    F_a = 0.5 * vehicle.cw * vehicle.af * vehicle.roh_air * (sim.vel_dis[sim.step_dis] ** 2)  # in N
    # Rolling Resistance
    F_r = vehicle.mass_total * vehicle.g_force * vehicle.c_rr * np.cos(np.arctan(env.route_array_slope[sim.step_dis])
                                                                                / 100)
    # Gradient Resistance
    F_g = vehicle.mass_total * vehicle.g_force * np.sin(np.arctan(env.route_array_slope[sim.step_dis]) / 100)
    # Total Resistance without acceleration
    F_tot = F_a + F_r + F_g
    # From Acceration to wheel force
    if sim.pt_direction == 0:
        vehicle.wheel_force_request = F_tot + (vehicle.mass_total * vehicle.gear_lambda * sim.acc_target_dis[sim.step_dis])
    # From Wheel force to acceleration
    else:
        sim.acc_dis[sim.step_dis] = (1 / (vehicle.mass_total * vehicle.gear_lambda)) * (vehicle.wheel_force_delivered - F_tot)
        if F_tot - vehicle.wheel_force_delivered == 0:
            sim.acc_dis[sim.step_dis] = 0

    return sim, vehicle


# Wheel Function: Required Torque and Delivered Force
def vehicle_wheel(sim, vehicle):
    # From Force to Torque:
    if sim.pt_direction == 0:
        # Calculate Torque Request
        vehicle.wheel_torque_request = vehicle.r_dyn * vehicle.wheel_force_request
        # Calculate Speed of wheels at current velocity
        vehicle.wheel_speed_request = sim.vel_dis[sim.step_dis] * (60 / (2 * np.pi * vehicle.r_dyn))
        # Check for zero speed to avoid NaN in Power Calculation
        if vehicle.wheel_speed_request == 0:
            vehicle.wheel_speed_request = 0.1
    # From Torque to Force
    else:
        vehicle.wheel_force_delivered = vehicle.wheel_torque_delivered / vehicle.r_dyn

    return sim, vehicle


# Brake
def vehicle_brake(sim, vehicle):
    # Calculate needed brake force
    force_brake_request = vehicle.wheel_force_request - vehicle.wheel_force_delivered
    # If requested brake force is grater than providable force: Max brake force
    if 0.999 * abs(force_brake_request) > vehicle.brake_force:
        brake_force_deliver = vehicle.brake_force
        vehicle.brake_limit = 1
    # Else: Requested Brake Force
    else:
        brake_force_deliver = force_brake_request
        vehicle.brake_limit = 0
    # Calculate Total Wheel Force
    vehicle.wheel_force_delivered = vehicle.wheel_force_delivered - abs(brake_force_deliver)
    return sim, vehicle


# Gear
def vehicle_gear(sim, vehicle):
    # Direction from gear to electric machine
    if sim.pt_direction == 0:
        # Calculate Speed at machine output
        vehicle.em_speed = vehicle.wheel_speed_request * vehicle.gear_ratio
        # Efficiency according to Drive or Recuperate
        efficiency = vehicle.gear_efficiency ** np.sign(vehicle.wheel_torque_request)
        # EM Torque Request
        vehicle.em_torque_request = vehicle.wheel_torque_request / efficiency / vehicle.gear_ratio
    # Direction towards gear output
    else:
        # Efficiency
        efficiency = vehicle.gear_efficiency ** np.sign(vehicle.em_torque_delivered)
        # Torque at gear output
        vehicle.wheel_torque_delivered = vehicle.em_torque_delivered * efficiency * vehicle.gear_ratio

    return sim, vehicle


# EM
def vehicle_em(sim, vehicle):
    # Calculation of needed battery power
    if sim.pt_direction == 0:
        # Calculate max torque at current rotational speed (vehicle.em torque_max_speed)
        em_trq_max_possible = vehicle.em_torque_func(vehicle.em_speed)
        # Recuperation rate according to deceleration
        if sim.acc_target_dis[sim.step_dis] < -1:
            recuperation_rate = 0.5
        else:
            recuperation_rate = 1
        # Using Fixed Efficiency
        efficiency_trq_max = vehicle.em_efficiency
        # Calculate Torque which is delivered by machine by at this load point
        em_trq_deliver_possible = recuperation_rate * em_trq_max_possible * (efficiency_trq_max ** np.sign(vehicle.em_torque_request))
        # Comparison to requested torque
        if np.abs(1.001 * em_trq_deliver_possible) <= np.abs(vehicle.em_torque_request):
            #Set Limit in EM to One
            vehicle.em_limit = 1
            #Calculate Requested Torque/Power from EM
            vehicle.pe_trq_request = np.sign(vehicle.em_torque_request) * em_trq_max_possible * recuperation_rate
        else:
            # Set Limit in EM to Zero
            vehicle.em_limit = 0
            # Efficiency
            efficiency = vehicle.em_efficiency
            vehicle.pe_trq_request = vehicle.em_torque_request / (efficiency ** np.sign(vehicle.em_torque_request))
        # Calculation of Power request on power electronics
        vehicle.em_power_request = 2 * np.pi * vehicle.pe_trq_request * vehicle.em_speed / 60  # in W

    # Calculate delivered torque of em according to power electronics power
    else:
        # Calculate virtual torque of power electronics
        vehicle.pe_trq_delivered = vehicle.pe_power_delivered * 60 / (2 * np.pi * vehicle.em_speed)  # in Nm
        # Fixed Efficiency
        efficiency = vehicle.em_efficiency
        # Calculate torque deliver from electric machine
        vehicle.em_torque_delivered = vehicle.pe_trq_delivered * (efficiency ** np.sign(vehicle.em_torque_request))  # in NM

    return sim, vehicle


# PE
def vehicle_pe(sim, vehicle):
    # Calculate required power from Battery
    if sim.pt_direction == 0:
        # Calculate Power request from PE
        vehicle.pe_power_request = vehicle.em_power_request / vehicle.pe_efficiency
    else:
        # Calculate delivered Power from PE
        vehicle.pe_power_delivered = vehicle.bat_power_delivered * vehicle.pe_efficiency

    return sim, vehicle


# Battery Model only for driving event, for charging see vehicle_battery_charging
def vehicle_battery(sim, vehicle, env):
    # Possible Battery Power at current SoC

    # Requested energy Amount: Discharging --> Energy / Power > 0

    # Check limiting battery power
    vehicle.bat_limit = 0
    # Recuperation near SOC = 1

    # Delivered Power/Energy of Battery
    vehicle_bat_power_demand = vehicle.pe_power_request + (vehicle.aux_cons*1000)
    sim.bat_power_dis[sim.step_dis] = vehicle_bat_power_demand
    sim.energy_cons_dis[sim.step_dis] = sim.bat_power_dis[sim.step_dis] * sim.time_dis[sim.step_dis]  # in Ws
    # SOC, Temp, SOH Update
    sim.bat_soc_dis[sim.step_dis + 1] = sim.bat_soc_dis[sim.step_dis] - sim.energy_cons_dis[sim.step_dis]/\
                                        (vehicle.battery_capacity*1000*3600)

    # Time Based Variables
    sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_dis[sim.step_dis + 1]

    # Reduce Power for Driveline due to auxiliary power
    vehicle.bat_power_delivered = vehicle.pe_power_request

    return sim, vehicle


# Battery Model for Charging and Rest Event
def vehicle_battery_charge(sim, vehicle, env):
    # Time Step

    # Possible Charging Power

    # SOC, Temp, SOH Update

    return sim, vehicle








