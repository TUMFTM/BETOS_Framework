# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-09
#
# Function Description
# Part of the Visualization Module M12
# Main file of the visualization module
# _________________________________


# import functions:
import matplotlib.pyplot as plt
import numpy as np

# Used sources in this file


# Visualization of one freight simulation task
def visualizsation_single_task(sim, vehicle, env):
    # Set general plot parameters
    plt.rcParams.update({'font.family':'Times New Roman'})
    csfont = {'fontname': 'Times New Roman'}
    docwidth = 16.5  # word doc width in cm
    width_in =docwidth / 2.54
    height_in = width_in * 6 / 16
    FIGSIZE = (width_in, height_in)
    # Plot Vehicle and Infrastructure related properties
    plt.figure(figsize=FIGSIZE)
    # Speed Profile
    plt.plot(env.route_array_distance/1000, sim.vel_dis*3.6, linewidth=1.0, color='#1a1a1a')
    plt.ylim((0, 100))
    plt.xlim((0, (env.route_array_distance[-1]+5000)/1000))
    # Infrastructure
    for i in range(sim.dis_steps):
        # Plot POI:
        if env.infra_array_poi[i] == 1 and env.infra_array_poi_type[i] == 0:
            plt.vlines(x=i/1000, ymin=0, ymax=90, color='#E37222')
        elif env.infra_array_poi[i] == 1 and env.infra_array_poi_type[i] <= 3:
            plt.vlines(x=i/1000, ymin=0, ymax=100, color='#e37222', linewidth=0.5)
        elif env.infra_array_poi[i] == 1 and env.infra_array_poi_type[i] <= 4:
            plt.vlines(x=i / 1000, ymin=0, ymax=100, color='#005293', linestyles='dashed', linewidth=0.5)
        elif env.infra_array_poi[i] == 1 and env.infra_array_poi_type[i] == 5:
            plt.vlines(x=i / 1000, ymin=0, ymax=100, color='#005293', linewidth=0.5)
        # Plot Stop POI:
        if env.route_array_stoptime[i] > 0:
            plt.vlines(x=i/1000, ymin=0, ymax=env.route_array_stoptime[i]/60, color='#E37222', linewidth=0.5)

    # Labeling
    plt.xlabel('Distance in km', **csfont, fontsize=9)
    plt.xticks(**csfont, fontsize=9)
    plt.ylabel('Velocity in km/h', **csfont, fontsize=9)
    plt.yticks(**csfont, fontsize=9)
    plt.title('Transport scenario as distance based driving cycle', **csfont, fontsize=9)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/Paper_no2/Parameters/transport_scenario_infrastructure.png', dpi=400, bbox_inches='tight')
    #Show Plot
    plt.show()

    ## Plot Powertrain Data:
    # Distance based:
    plt.figure(figsize=FIGSIZE)
    plt.ylim((0, 100))
    plt.xlim((0, (env.route_array_distance[-1] + 1000) / 1000))
    # SoC Profile
    plt.plot(env.route_array_distance/1000, sim.bat_soc_dis*100, linewidth=1.0, color='#005293')
    plt.hlines(y=vehicle.battery_soc_min*100, xmin=0, xmax=(env.route_array_distance[-1]) / 1000, color='red')
    plt.plot((env.route_array_distance[-1] + 1000) / 1000, env.freight_destination_soc*100, '+', color='green', markersize=10)
    # Labeling
    plt.xlabel('Distance in km', **csfont, fontsize=9)
    plt.xticks(**csfont, fontsize=9)
    plt.ylabel('SOC in %', **csfont, fontsize=9)
    plt.yticks(**csfont, fontsize=9)
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/Paper_no2/Parameters/transport_scenario_soc.png', dpi=400, bbox_inches='tight')
    # Show Plot
    plt.show()

    # Time Based:
    plt.figure(figsize=FIGSIZE)
    plt.ylim((0, 100))
    plt.xlim((0, sum(sim.time_time[0:sim.step_time])/3600))
    # SoC Profile
    plt.plot(np.cumsum(sim.time_time[0:sim.step_time])/3600, sim.bat_soc_time[0:sim.step_time]*100, linewidth=1.0, color='#005293')
    plt.hlines(y=15, xmin=0, xmax=sum(sim.time_time[0:sim.step_time])/3600, color='red')
    plt.plot(sum(sim.time_time[0:sim.step_time])/3600, env.freight_destination_soc*100, '+', color='green', markersize=10)

    # Labeling
    plt.xlabel('Operation time in h', **csfont, fontsize='9')
    plt.xticks(**csfont, fontsize=9)
    plt.ylabel('SOC in %', **csfont, fontsize='9')
    plt.yticks(**csfont, fontsize=9)
    # Ticks
    # Show Plot
    # plt.savefig('Modules/M13_SimulationTask/M13_Results/Paper_no2/Parameters/transport_scenario_soc_2.png', dpi=400, bbox_inches='tight')
    plt.show()

    return
