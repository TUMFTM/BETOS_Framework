# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-02
#
# Function Description
# Part of the Operation Simulation Module M8
# Implementation of all possible actions in M83
# Driving, Charging and Resting
# _________________________________


# import functions:
import numpy as np
from Modules.M6_Dynamic_Vehicle import M6_Veh_Dyn

# Used sources in this file:


# Action = Driving
def action_driving(sim, env, vehicle):
    # Decide whether acceleration or deceleration
    select = action_driving_select(sim, vehicle, env)
    # Chose right action
    # Action Acceleration
    if select == 0:
        sim, vehicle = action_acceleration(sim, vehicle, env)
    # Action Deceleration
    else:
        sim, vehicle = action_deceleration(sim, vehicle, env)
    return sim


# Action = Charging and Resting
def action_charge_rest(sim, env, vehicle):
    # Check for Charging
    select_charge = action_charge_select(sim, vehicle, env)
    # Brake down vehicle to velocity = 0 if necessary:

    # Check for Waiting (only in advanced simulation)
    select_wait = action_wait_select(sim, vehicle, env)
    if select_wait == 1:
        sim = action_waiting(sim, vehicle, env)

    # Execute Charging Event
    if select_charge == 1:
        sim = action_charging(sim, vehicle, env)

    # Check for (additional) rest
    select_rest = action_rest_select(sim, vehicle, env)
    # Execute Rest Event
    if select_rest == 1:
        sim = action_rest(sim, vehicle, env)

    return sim


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# SUBFUNCTIONS DRIVING
# Check acceleration or deceleration considering wheel force:
def action_driving_select(sim, vehicle, env):
    # Current velocity
    vel = sim.vel_dis[sim.step_dis]
    # Wanted Velocity
    vel_next = env.route_array_speed[sim.step_dis + 1]
    # Resulting target acceleration
    sim.acc_target_dis[sim.step_dis] = ((vel * (vel_next - vel)) + (0.5 * (vel_next - vel) ** 2)) / 1
    # Resulting time step
    if vel_next-vel == 0:
        sim.time_dis[sim.step_dis] = 1/vel  # in Case of constant speed: t=s/v

    else:
        sim.time_dis[sim.step_dis] = (vel_next - vel) / sim.acc_target_dis[sim.step_dis]

    # Time Based Time
    sim.time_time[sim.step_time] = sim.time_dis[sim.step_dis]
    # Resulting wheel force
    sim.pt_direction = 0
    sim, vehicle = M6_Veh_Dyn.vehicle_fde(sim, vehicle, env)
    wheel_force = vehicle.wheel_force_request
    # Select
    if wheel_force >= 0:
        select = 0
    else:
        select = 1

    return select


# Action = Acceleration
def action_acceleration(sim, vehicle, env):
    # Call Dynamic Vehicle Model. Input: Target Acceleration, Output: Driveable Acceleration
    # Loop over limiting components necessary
    limit = 1
    while limit > 0:
        sim, vehicle = M6_Veh_Dyn.dynamic_vehicle_model(sim, env, vehicle)
        if vehicle.em_limit == 0 and vehicle.bat_limit == 0:
            limit = 0
        else:
            # Set new target acceleration value due to limits
            sim.acc_target_dis[sim.step_dis] = sim.acc_dis[sim.step_dis]
            # Update Duration for distance step
            coeff = [sim.acc_target_dis[sim.step_dis] / 2, sim.vel_dis[sim.step_dis], -1]
            delta_t_raw = np.roots(coeff)
            delta_t = np.real(delta_t_raw)
            number_sol = len(delta_t)
            if number_sol > 1:
                if delta_t[0] > 0 and sim.acc_target_dis[sim.step_dis] >= 0:
                    delta_t = delta_t[0]
                else:
                    delta_t = delta_t[1]
            sim.time_dis[sim.step_dis] = delta_t
            sim.time_time[sim.step_time] = delta_t
    # Calculate velocity in next distance step
    sim.vel_dis[sim.step_dis+1] = sim.vel_dis[sim.step_dis] + (sim.time_dis[sim.step_dis] * sim.acc_dis[sim.step_dis])
    sim.vel_time[sim.step_time + 1] = sim.vel_dis[sim.step_dis+1]
    # Update daytime
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time]/3600)

    return sim, vehicle


# Action = Deceleration
def action_deceleration(sim, vehicle, env):
    # Call Dynamic Vehicle model. Input: Target Acceleration. Output: Driveable Acceleration
    sim, vehicle = M6_Veh_Dyn.dynamic_vehicle_model(sim, env, vehicle)
    # Check Brake Limit
    if vehicle.brake_limit == 0:
        # Calculate velocity in next distance step
        sim.vel_dis[sim.step_dis + 1] = sim.vel_dis[sim.step_dis] + (sim.acc_dis[sim.step_dis] * sim.time_dis[sim.step_dis])
        sim.vel_time[sim.step_time + 1] = sim.vel_dis[sim.step_dis + 1]
    # If Brake is at its Limit
    else:
        # Calculation of earlier brakepoint
        # Target Velocity in next distance step
        vel_wanted = env.route_array_speed[sim.step_dis + 1]
        # Save Current Position
        current_step_dis = sim.step_dis
        # Recursive calculation of resulting velocity by maximum deceleration till velocity in brakepoint
        # is higher than driven velocity in cycle: Start in current position = sim.step_dis
        sim.acc_target_dis[sim.step_dis] = vehicle.acc_max
        v_brakepoint = ((vel_wanted ** 2) - (2*sim.acc_target_dis[sim.step_dis] * 1))**0.5
        sim.step_dis = sim.step_dis - 1
        sim.step_time = sim.step_time - 1
        while v_brakepoint < sim.vel_dis[sim.step_dis]:
            # Overwrite driven velocity for forward propagation
            sim.vel_dis[sim.step_dis + 1] = v_brakepoint
            sim.vel_time[sim.step_time + 1] = sim.vel_dis[sim.step_dis + 1]
            # Set target acceleration to maximum deceleration
            sim.acc_target_dis[sim.step_dis] = vehicle.acc_max
            # Calculate resulting velocity in new brake point
            v_brakepoint = ((sim.vel_dis[sim.step_dis + 1] ** 2)-(2*sim.acc_target_dis[sim.step_dis] * 1))**0.5
            # Set brakepoint
            sim.step_dis = sim.step_dis - 1
            sim.step_time = sim.step_time - 1
        # Brakepoint found in sim.step_dis + 1
        sim.step_dis = sim.step_dis + 1
        sim.step_time = sim.step_time + 1
        # Begin braking at new brakepoint
        # First step with individual deceleration
        sim.acc_target_dis[sim.step_dis] = ((sim.vel_dis[sim.step_dis] * (sim.vel_dis[sim.step_dis+1] -
                                                                          sim.vel_dis[sim.step_dis])) +
                                            (0.5 * (sim.vel_dis[sim.step_dis+1] - sim.vel_dis[sim.step_dis]) ** 2)) / 1
        # Time Step
        sim.time_dis[sim.step_dis] = (sim.vel_dis[sim.step_dis+1] - sim.vel_dis[sim.step_dis]) / \
                                     sim.acc_target_dis[sim.step_dis]
        sim.time_time[sim.step_time] = sim.time_dis[sim.step_dis]

        # Run through Dynamic Vehicle Model
        sim, vehicle = M6_Veh_Dyn.dynamic_vehicle_model(sim, env, vehicle)
        # Update distance step
        sim.step_dis = sim.step_dis + 1
        sim.step_time = sim.step_time + 1
        while sim.step_dis < current_step_dis:
            # Target acceleration and velocity already set through backpropagation
            # Time step
            sim.time_dis[sim.step_dis] = (sim.vel_dis[sim.step_dis + 1] - sim.vel_dis[sim.step_dis]) / sim.acc_target_dis[sim.step_dis]
            sim.time_time[sim.step_time] = sim.time_dis[sim.step_dis]
            # Run through Dynamic Vehicle Model for SOC, Temp, SoH
            sim, vehicle = M6_Veh_Dyn.dynamic_vehicle_model(sim, env, vehicle)
            # Update distance
            sim.step_dis = sim.step_dis + 1
            sim.step_time = sim.step_time + 1
        # Last distance towards vel_wanted
        sim.time_dis[sim.step_dis] = (vel_wanted - sim.vel_dis[sim.step_dis]) / sim.acc_target_dis[sim.step_dis]
        sim.time_time[sim.step_time] = sim.time_dis[sim.step_dis]
        # Run through Powertrain
        sim, vehicle = M6_Veh_Dyn.dynamic_vehicle_model(sim, env, vehicle)
        # Velocity
        sim.vel_dis[sim.step_dis + 1] = sim.vel_dis[sim.step_dis] + (sim.acc_dis[sim.step_dis] * sim.time_dis[sim.step_dis])
        sim.vel_time[sim.step_time + 1] = sim.vel_dis[sim.step_dis + 1]

    # Update Daytime
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)

    # Final Check of Velocity nearly at Zero:
    if sim.vel_dis[sim.step_dis + 1] < 1/100:
        sim.vel_dis[sim.step_dis + 1] = 0.0
        sim.vel_time[sim.step_time + 1] = 0.0
            
    return sim, vehicle


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# SUBFUNCTIONS Fast DRIVING
def action_fast_driving(sim, env, vehicle):
    # Battery SoC is calculated from Energy Consumption from prediction
    sim.bat_soc_dis[sim.step_dis + 1] = sim.bat_soc_dis[sim.step_dis] - sim.betos_energy_cons_dis_prediction[sim.step_dis] / \
                                        (vehicle.battery_capacity * 1000 * 3600)
    sim.bat_soc_time[sim.step_time + 1] = sim.bat_soc_dis[sim.step_dis + 1]

    # Energy Consumption from Prediction Module
    sim.energy_cons_dis[sim.step_dis] = sim.betos_energy_cons_dis_prediction[sim.step_dis]

    # Velocity is cycle speed
    sim.vel_dis[sim.step_dis + 1] = env.route_array_speed[sim.step_dis + 1]
    sim.vel_time[sim.step_time + 1] = sim.vel_dis[sim.step_dis + 1]

    # Time steps
    sim.time_dis[sim.step_dis] = sim.betos_time_dis_prediction[sim.step_dis]
    sim.time_time[sim.step_time] = sim.time_dis[sim.step_dis]

    # Update Daytime
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)

    return sim

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# SUBFUNCTIONS CHARGING / RESTING / WAITING
# Select Functions: Waiting, Charging, Resting
# Select Waiting if charging is selected and charging stations is occupied
def action_wait_select(sim, vehicle, env):
    # Check for charging and occupied PoI
    if sim.betos_charge_time[sim.step_dis] > 0 and env.cs_availability > 0:
        select_wait = 1
    else:
        select_wait = 0

    return select_wait


# Select if Charging Event is necessary according to target SOC
def action_charge_select(sim, vehicle, env):
    # Check for Target SOC
    if sim.betos_charge_time[sim.step_dis] > 0:
        select_charge = 1
    else:
        select_charge = 0

    return select_charge


# Select if Rest Event is necessary
def action_rest_select(sim, vehicle, env):
    # Check for Target Rest Time
    if sim.rest_time_dis[sim.step_dis] < sim.betos_rest_time[sim.step_dis]:
        select_rest = 1
    else:
        select_rest = 0

    return select_rest


# ______________________________________________________________________________________________________________________
# Execution Functions: Waiting, Charging, Resting
# Charging Function
def action_charging(sim, vehicle, env):
    # Initialize Charging time
    charging_time = 0
    pure_charge_time = 0
    sum_charge_amount_kwh = 0
    # Current SOC Level
    soc = sim.bat_soc_dis[sim.step_dis]
    # Safe current soc level
    soc_before = soc

    # Track Deep Discharging Event
    if soc < 0.15:
        sim.betos_deep_discharge = sim.betos_deep_discharge + 1

    # Searching for parking space
    sim.time_time[sim.step_time] = vehicle.rest_space_time/2  # in sec
    sim.bat_soc_time[sim.step_time+1] = soc
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
    sim.step_time = sim.step_time + 1

    # Connecting vehicle to Charging Plug
    charging_time = charging_time + vehicle.connecting_time/2  # in sec
    sim.bat_soc_time[sim.step_time + 1] = soc
    sim.time_time[sim.step_time] = charging_time
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
    sim.step_time = sim.step_time + 1

    # Charging to target SOC
    # while soc < min(1, sim.betos_soc_target[sim.step_dis]):
    while pure_charge_time < sim.betos_charge_time[sim.step_dis] and soc < min(1, sim.betos_soc_target[sim.step_dis]):
        # C-Rate
        c_rate = vehicle.cell_c_rate_func(min(100, soc*100))
        # Charging Power
        charging_power = min(c_rate*vehicle.battery_capacity, env.cs_power) * vehicle.battery_charge_loss
        # Charging half Percent
        #time_charging_step = ((vehicle.battery_capacity/200) / charging_power) * 3600  # in sec
        time_charging_step = 30  # use same discretization as in DP approach
        charge_amount_kwh = (charging_power * time_charging_step/3600)   # in kWh
        sum_charge_amount_kwh = sum_charge_amount_kwh + charge_amount_kwh  # in kWh
        # Update Battery Parameters (Temperature, SOH, etc)
        #soc = soc + 0.005  # half Percent Charging Amount pro Step
        soc = soc + (charge_amount_kwh/vehicle.battery_capacity)
        charging_time = charging_time + time_charging_step
        pure_charge_time = pure_charge_time + time_charging_step

        # Time Based Variables Update
        sim.bat_soc_time[sim.step_time + 1] = min(soc, 1.0)  # Maximum SoC = 100 %
        sim.time_time[sim.step_time] = time_charging_step
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update time step variable
        sim.step_time = sim.step_time + 1

    # Disconnect and Paying
    charging_time = charging_time + vehicle.connecting_time/2  # in sec
    # sim.bat_soc_time[sim.step_time] = min(soc, 1.0)
    sim.bat_soc_time[sim.step_time + 1] = min(soc, 1.0)
    sim.time_time[sim.step_time] = vehicle.connecting_time/2
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
    sim.step_time = sim.step_time + 1

    # Driving to highway
    sim.bat_soc_time[sim.step_time + 1] = min(soc, 1.0)
    sim.time_time[sim.step_time] = vehicle.rest_space_time/2
    sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
    sim.step_time = sim.step_time + 1

    # Update distance based variables
    sim.charge_time_dis[sim.step_dis] = pure_charge_time  # pure charging time, excluding connecting time
    sim.rest_time_dis[sim.step_dis] = sim.rest_time_dis[sim.step_dis] + charging_time
    # Safe position if rest is done
    if sum(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis+1]) >= vehicle.mandatory_rest_time * 60:
        sim.pos_rest_done = sim.step_dis
    # Limit SoC
    sim.bat_soc_dis[sim.step_dis] = min(soc, 1.0)

    # Save recharged energy in kWh
    sim.betos_charge_amount[int(env.infra_array_poi_id[sim.step_dis])] = (soc-soc_before)*vehicle.battery_capacity
    # Save rest time at POI in h
    sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] = (sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] + sim.rest_time_dis[sim.step_dis]) / 3600

    return sim

# Rest Function
def action_rest(sim, vehicle, env):
    # Check if charging is performed for additional stop time for leaving and reentering the highway
    if sim.rest_time_dis[sim.step_dis] > 0:
        stop_time = 0
    else:
        # Searching for parking space, counts not for rest
        stop_time = vehicle.rest_space_time  # in sec
        sim.bat_soc_time[sim.step_time] = sim.bat_soc_dis[sim.step_dis]
        sim.time_time[sim.step_time] = stop_time
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        sim.step_time = sim.step_time + 1

    # Get required rest time
    rest_required = sim.betos_rest_time[sim.step_dis] - sim.rest_time_dis[sim.step_dis]  # in sec

    # Perform rest
    rest_time = 0
    while rest_time < rest_required:
        # Count rest time
        rest_time = rest_time + 1
        sim.time_time[sim.step_time] = 1  # in 1 sec steps
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update Battery Parameter
        # SoC while resting is not changing
        sim.bat_soc_time[sim.step_time] = sim.bat_soc_time[sim.step_time - 1]
        # Update time step for timebased variables
        sim.step_time = sim.step_time + 1

    # Add additional rest time to total rest time in distancebased vector
    sim.rest_time_dis[sim.step_dis] = sim.rest_time_dis[sim.step_dis] + rest_time
    # Safe position if rest is done
    if sum(sim.rest_time_dis[sim.pos_rest_done+1:sim.step_dis+1]) >= vehicle.mandatory_rest_time * 60:
        sim.pos_rest_done = sim.step_dis
    # Last SoC Point in Array
    sim.bat_soc_time[sim.step_time] = sim.bat_soc_time[sim.step_time - 1]

    # Save rest time at POI in h
    sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] = (sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] + sim.rest_time_dis[sim.step_dis]) / 3600

    return sim

# Waiting Function in case of occupied charging station:
def action_waiting(sim, vehicle, env):
    # Get waiting time
    waiting_time = env.cs_data_waiting_time(sim.daytime)
    # Safe Wait session
    sim.betos_wait_count += 1
    # Perform waiting
    time_wait = 0
    while time_wait < waiting_time:
        # Count wait time
        time_wait += 1
        # Time step
        sim.time_time[sim.step_time] = 1  # in 1 sec steps
        sim.daytime = sim.daytime + (sim.time_time[sim.step_time] / 3600)
        # Update Battery Parameter
        # SoC is not changing, secondary consumers are neglected
        sim.bat_soc_time[sim.step_time] = sim.bat_soc_time[sim.step_time - 1]
        # Update time step in sim
        sim.step_time += 1
    # Add waiting time to total rest time of re-parking is allowed
    sim.rest_time_dis[sim.step_dis] = sim.rest_time_dis[sim.step_dis] + sim.betos_re_park * time_wait
    sim.wait_time_dis[sim.step_dis] = time_wait
    # Last Soc Point in Array
    sim.bat_soc_time[sim.step_time] = sim.bat_soc_time[sim.step_time - 1]

    # Save rest time at POI in h
    sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] = (sim.betos_down_time[int(env.infra_array_poi_id[sim.step_dis])] + time_wait) / 3600

    return sim

