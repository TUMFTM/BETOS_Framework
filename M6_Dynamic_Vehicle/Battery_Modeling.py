# _________________________________
# BET.OS Function #
#
# Designed by MX-2022-09-06
#
# Function Description
# Part of the Dynamic Vehicle Modul M6
# Battery Modeling functions for power, SOC, Temp, Aging
# _________________________________

# Import functions:
import numpy as np


# Used Sources in this file:


# Calculate deliverable battery power at current SoC
def battery_power(sim, vehicle):
    # Number of cells in Battery Pack
    number_cells = np.ceil((vehicle.battery_capacity / 3600) / (cell.Qnom * cell.Unom))

    return sim, vehicle