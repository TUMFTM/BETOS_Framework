# _________________________________
# BET.OS Function #
#
# Designed by MX-2023-08-18
#
# Function Description
# Part of the Operation Strategy Module M9
# Operation strategy using global optimization pipeline with pymoo package
# _________________________________


# import functions:
import numpy as np
from Modules.M8_Operation_Simulation.M8_4_Simulation import M84_DrivingSim

# import pymoo package and its used functions:
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2, RankAndCrowdingSurvival
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_problem, get_reference_directions, get_termination
from pymoo.optimize import minimize
from pymoo.core.mixed import MixedVariableGA, MixedVariableMating, MixedVariableSampling, MixedVariableDuplicateElimination
from pymoo.core.variable import Real, Integer


# Building the problem and run global optimization for one scenario
def evaluation_global_optimization(sim, env, vehicle, scenario):

    # Optimization variables
    number_var = optimization_variables(sim, env, vehicle, scenario)
    # Built optimization problem
    class MyProblem(ElementwiseProblem, number_var, vehicle):
        def __init__(self, **kwargs):
            variables = dict()

            for k in range(1, (number_var/2) + 1):
                variables[f"x{k:02}"] = Real(bounds=(vehicle.battery_soc_min, 1.0))

            for k in range(number_var/2 + 1, number_var + 1):
                variables[f"x{k:02}"] = Integer(bounds=(0, 3))

            super().__init__(vars=variables,  # Number of optimization variables
                             n_obj=2,           # Number of objective functions
                             n_ieq_constr=2,        # Number of contrains
                             elementwise=True)

        def _evaluate(self, x, out, *args, **kwargs):
            x = np.array([x[f"x{k:02}"] for k in range(1, 11)])     # Design Vector

            f1 = objective_1        # time loss function
            f2 = objective_2        # aging function
            c1 = contrain_1 - 0     # HoS regulations constrain
            c2 = constrain_2        #

            out["F"] = [f1, f2]
            out["G"] = [c1, c2]


    # Define algorithm
    algorithm = NSGA2(pop_size=20,
                      sampling=MixedVariableSampling(),
                      mating=MixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination()),
                      eliminate_duplicates=MixedVariableDuplicateElimination(),
                      )
    # Get problem
    problem = MyProblem()
    # Run optimization
    result = minimize(problem,
                      algorithm,
                      ('n_gen', 200),
                      seed=1,
                      verbose=True)
    # Process results

    return sim


# Optimization Variables
def optimization_variables(sim, env, vehicle, scenario):

    number_variables = 2 * int(env.infra_number_poi)

    return number_variables


# Test one Solution loop
def sim_loop(x, sim, env, vehicle, scenario):

    # Extract Strategy from design variable

    # Driving Simulation
    sim = M84_DrivingSim.driving_sim(sim, vehicle, env)
    # Process Simulation Result
    results = M84_DrivingSim.processing_results(sim, vehicle, env, scenario)
    # result[0]: Time Loss
    # result[1]: Aging / SoH Loss
    result = np.array([results['time_loss_min'], results['soh_loss']])

    return result


# Extract BETOS Variables from Design Variable
def extract_betos_var(x, sim, env):

    # Set target rest time at every POI

    # Set target SOC at every POI

    return sim