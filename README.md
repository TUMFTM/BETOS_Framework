# BETOS Framework (Battery-electric Truck Operation Simulation)
This repository provides the open-source code for the operation simulation of battery-electric trucks (BET) in long-haul applications.  
The simulation framework belongs to the following research articles:  
Optimizing the Journey: Dynamic Charging Strategies for Battery-Electric Trucks in Long-Haul Transport  
Authors: M.Zaehringer, O.Teichert, G.Balke, J.Schneider, M.Lienkamp  
DOI: https://doi.org/10.3390/en17040973


Fast track to a million - A simulative case study on the influence of charging management on the lifetime of battery electric trucks
Authors: M. Zaehringer, J. Schneider, G. Balke, K. Abo Gamra, N. Klein, M. Lienkamp
DOI: https://doi.org/10.1016/j.prime.2024.100731

## Necessary Python Packages and Libraries:
We recommend Python 3.7 to 3.10 to run the code.
The following libraries are used: numpy, scipy, matplotlib, multiprocessing, pandas
## Attention: Important first step:
Before the code can be used, you have to unpack the used driving profiles to create an underlying driving cycle. These are stored in M3_Freight_Properties/M3_TruckMobility_Database. Otherwise, the simulation is not able to build the driving cycles. 

## Model Structure and Parameters:
The simulation has a modular structure. The first modules, "M1_Vehicle_Properties", "M2_Environment_Properties", and "M3Freight_Properties", define the basic parameters of the vehicle, the charging infrastructure, and the driving cycle.   
While the essential parameters of the charging infrastructure and the transport profile are defined within a scenario (see input), vehicle parameters such as driving resistance coefficients or efficiencies can be defined within the corresponding script of the first module.  
The modules 5-7 contain the actual models of the vehicle (drivetrain, mass) and the charging infrastructure. The Operation Simulation with the sub-modules Simulation, Action, and Driving offers all the functions required for driving and charging the vehicle. 
The Operation Strategy module contains the various charging management functions. 
The remaining modules are used for visualization or specific investigations and are not required for the essential operation simulation of BET.   
## Perform a single operation simulation:
### Input:
The input is defined through a scenario using a DataFrame. This is done in the script scenario_definition.py.  
To create one single scenario, you can change every property of the battery electric truck, the charging infrastructure, and the underlying transport scenario within the function: scenario_gen()  
The first properties belong to the charging infrastructure model. You can specify the availability of the charging points, the charging power of 5 different types of chargers, and the waiting time of an occupied charger.  
Next, the vehicle parameters are defined. These are the battery capacity, the maximum charging rate, and the battery SOC limits. 
In addition, the transport mission is described by the payload, the trip length, the start and the end SOC, and the starting time of the mission.   
Finally, the used Charging Management can be selected. We implement three different functions. Next to the rule-based NGS strategy, we implement two time-optimal strategies, where one can handle occupied charging stations.   
All information of one scenario is stored as a DataFrame. 

### Simulation results:
Based on the exemplary defined scenario s1, one simulation run is performed by running the main.py script.
All simulation results are accessible in the DataFrame "results". These are:
- scenario_id: Your scenario ID you specified in the scenario definition  
- trip_length_km: the exact trip length in km  
- operation_duration_h: the total operation time of the truck, incl. downtimes  
- arrival_time_h: the daytime on arrival at the destination  
- charging_time_h: the total charging time in h  
- down_time_h: the total downtime due to charging and resting  
- driving_time_h: the pure driving time in h  
- time_loss_min: the total time loss in minutes compared to a diesel truck operating the same scenario  
- energy_consumption_kWhkm: the average energy consumption in kWh/km  
- energy_recharged_kWh: the amount of recharged energy in kWh  
- poi_down_time_h:  the downtimes at each POI  
- number_stops: the number of stops  
- soc_destination: the SOC when reached the destination  
- power_chosen_avg_kw: the average chosen charging power  
- number_wait_events: the total number of waiting events due to occupied charging stations  

### Visualization of a single run:
We provide one visualization script (M12_Visualization/...), which shows the SOC trajectory of the truck's battery over time and distance. 
The execution of the script is, by default, hidden.

## Perform multiple simulation runs using multiprocessing for the article: Optimizing the Journey:
Addressing the research article "Optimizing the Journey: Dynamic Charging Strategies for Battery-Electric Trucks in Long-Haul Transport", we show the simulation of the scenarios shown in this paper.  
All results and plotting scripts for this paper can be found in M13_Simulation_Task.   
### Input:
The input has to be analogous to a single simulation run as a Scenario DataFrame.
For every considered scenario in the research article, we provide the  scenario definition within the scenario_definition.py script.
### Simulation:
For the simulation of several runs of a single scenario, we use the multiprocessing library.  
If you want to recalculate the results from Section 4.1, activate the line: result = pool.map(M13_SimulationTask.sim_section_4_1_sd, iter)  
If you want to recalculate the results from Section 4.2 or 4.3, activate the line: result = pool.map(M13_SimulationTask.sim_section_4_2_3, iter)  
The number of runs is defined by the length of the vector "iter".  
If you want to store the simulation results as CSV, you can activate the line: M13-SimulationTask.postprocess_multi_sx(result)  

### Visualization used in the research article: Optimizing the Journey:
We provide a plotting script within Modules/M13_Simulation_Task/M13_Plotting_Script_Research_Article. If you call the function plotting() all Figures of the paper are generated.  The results used in the research article are located in M13_Simulation_Task/Results/Paper_no2/.

## End-of-life simulation for lifetime prediction of battery-electric long-haul-trucks:
The framework provides a lifetime prediction simulation for two different cell chemistries (NMC and LFP). The investigations based on this Module are published under:
Zaehringer et al.: Fast track to a million - A simulative case studay on the influence of charging management on the lifetime of battery electric trucks

### How to simulate the lifetime
The lifetime simualtion could be stared via the main script. The correspondig function is M14_EOL_Simualtion.eol_simualtion. This gives a object eol back with the main results of the lifetime prediction. All detailed results are automatically stored as single .csv files after simualted operation week. 

### Implementation of the lifetime simulation

### Access the results of the research article

## Contributing and Support
We encourage everybody to contribute to this work. If you have any feedback, don't hesitate to get in touch with me at maximilian.zaehringer@tum.de

## License
Apache License, Version 2.0
