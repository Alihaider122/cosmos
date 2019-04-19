# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:32:58 2018

@author: ah459
"""

import math
import parameters as p


# ---------------------- sphere ----------------------
def sphere(particle):
    fitness = float()
    for i in range(len(particle)):
        fitness = fitness + particle[i] ** 2
    return fitness


# ---------------------- alpine ----------------------
def alpine(vector):
    fitness = float()
    for i in range(len(vector)):
        fitness = fitness + abs((vector[i] * math.sin(vector[i])) + (0.1 * vector[i]))
    return fitness


# ---------------------- ackly ----------------------
def ackly(vector):
    sum1 = 0.0
    sum2 = 0.0
    a = 20
    b = 0.2
    c = 2 * math.pi
    for i in range(len(vector)):
        sum1 = sum1 + vector[i] ** 2
        sum2 = sum2 + math.cos(vector[i] * c)
    fitness = -a * math.exp(-b * math.sqrt(1 / p.dims * sum1)) - math.exp(1 / p.dims * sum2) + a + math.exp(1)
    return fitness


# ---------------------- Rosenberg ----------------------
def rosenberg(vector):
    fitness = float()
    for i in range(len(vector) - 1):
        fitness = fitness + 100 * (((vector[i + 1] - vector[i] ** 2) ** 2) + ((vector[i] - 1) ** 2))
    return fitness


# ---------------------- Rastrigin ----------------------
def rastrigin(vector):
    sum = float()
    for i in range(len(vector)):
        sum = sum + (vector[i] ** 2) - 10 * (math.cos(2 * p.pi * vector[i]))
    fitness = (10 * p.dims) + sum
    return fitness
