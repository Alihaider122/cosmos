# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:03:58 2018

@author: ah459
"""

import math
import numpy as np

# ------------------- HYPER PARAMETERS -----------------------

pi = math.pi

# ------------- Common in both D.E and PSO -------------------
gbestArray = np.zeros(30)  # array for storing gFitess after every run
RUNS = 30
generations = 1000  # number of iterations
dims = 10  # number of dimensions in each particle
lower_bound = -5.12  # for sphere function
upper_bound = 5.12  # for sphere function
k = 100
# -------------------------------------------------------------

# ----------- for Differential Evolution ----------------------
weighted_factor = 0.4  # weighted factor for mutation
CR = 0.6  # Cross of constant
NP = 40  # number of population
# -------------------------------------------------------------

# ------------ for Particle Swarm Optimization-----------------
swarm = 40  # population size
vmax = 6  # velocity's upper_bound
vmin = -6  # velocity's lower_bound

# -------------------------------------------------------------
