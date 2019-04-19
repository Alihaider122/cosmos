# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:21:07 2018

@author: ah459
"""
import parameters as p
import myPso
import de

count = 0
de_obj = de.DE(pop=None)
pso_obj = myPso.PSO()
for i in range(p.RUNS):
    count += 1
    print("RUN # ", i + 1)
    de_obj.process()
