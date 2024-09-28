# Framework Main Function
# Designed by MX-2024-12-02
# Function description
# Main Function: Operation Simulation and Evaluation of Battery Electric Trucks

# Import Libraries______________________________________________________________________________________________________
import numpy as np
import multiprocessing as mp

# Import Functions______________________________________________________________________________________________________
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_Oneday_Simulation
from Modules.M13_SimulationTask import M13_SimulationTask
from Modules.M13_SimulationTask.M13_Results import M13_Result_Evaluation
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_Multiday_Simulation
from Modules.M13_SimulationTask import M13_Plotting_Script_Research_Article
from Modules.M14_EOL_Simulation import M14_EOL_Simulation
import scenario_definition
import scenario_aging
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Single Simulation Function:
# s1 = scenario_definition.scenario_gen()
# Single Day (max 700 km)
# sim, env, results = M84_Oneday_Simulation.oneday_sim(scenario=s1)
# Multi Day Simulation (max 3000 km)
# sim, env, vehicle, results = M84_Multiday_Simulation.single_sim_multiday(scenario=s1)
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Paper: Optimizing the Journey - Dynamic charging strategies for battery electric long-haul trucks, M.Zaehringer et al.
# Single Simulation Run Simulation
# s1, s2, s3, s4, s31, s32, s33, s34, s41, s42, s43, s44, s45, s46, s47 = scenario_definition.scenario_betos_sec42()
# sim, env, results = M84_Oneday_Simulation.oneday_sim(scenario=s1)
# Plotting if article figures:
# M13_Plotting_Script_Research_article.plotting()
# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Calculation for Paper: Optimizing the Journey via Multiprocessing
# Multiprocessing Loop
#def main():
    #pool = mp.Pool(mp.cpu_count()-4)
    #print(mp.cpu_count())
    #iter = np.zeros(100)
    #result = pool.map(M13_SimulationTask.sim_section_4_1_sd, iter)
    #result = pool.map(M13_SimulationTask.sim_section_4_2_3, iter)
    #M13_SimulationTask.postprocess_multi_sx(result)


#if __name__=="__main__":
    #main()

# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# End of Life Simulation Main Function
# Paper: Fast track to a million - Mastering time-optimal on-route and aging focused overnight charging for battery
# electric trucks
# eol = M14_EOL_Simulation.eol_simulation()
#summary = np.zeros((eol.week_count, 3))
#summary[:, 0] = eol.milage_trace[0:eol.week_count]
#summary[:, 1] = eol.battery_soh_trace[0:eol.week_count]
#summary[:, 2] = eol.battery_capacity_trace[0:eol.week_count]
#np.savetxt('Modules/M14_EOL_Simulation/M14_EOL_Results/scenario_summary.csv', summary, delimiter=',')



