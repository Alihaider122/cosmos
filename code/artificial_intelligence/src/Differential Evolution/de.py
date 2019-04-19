# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:36:48 2018

@author: ah459
"""

import random
import copy
import math
import parameters as p
import functions as f


class DE:

    def __init__(self, pop):
        self.population = list()
        self.mutants = list()
        self.new_generation = list()
        for i in range(p.NP):
            if pop is None:
                vector = list()
                for params in range(p.dims):
                    temp = random.uniform(p.lower_bound, p.upper_bound)
                    vector.append(temp)
                self.population.append(vector)
            else:
                for j in range(len(pop)):
                    self.population.append(pop[j].position)
            self.mutants.append(0)
            self.new_generation.append(0)
            # -------------------------- Main differential evolution algorithm ---------------------

    def choose_best(self, number, exception_index):
        bests = tuple()
        list_of = list()
        best = math.inf
        temp_list = copy.deepcopy(self.population)
        for x in temp_list:
            fitness = f.sphere(x)  # Choose best from population
            if fitness <= best:
                best = fitness
                bests = (best, x)
        del (temp_list[exception_index])
        for i in range(number):
            list_of.append(random.choice(temp_list))
        list_of.append(bests[1])
        return list_of
        # -------------------------- Mutation ---------------------

    def mutation(self, randoms):
        temp1 = randoms[0]
        temp2 = randoms[1]
        temp3 = randoms[2]
        temp4 = randoms[3]
        temp5 = randoms[4]
        temp_list = []
        temp_list2 = []
        mutant_child = []
        for i in range(len(temp1)):
            x = temp1[i] - temp2[i]
            y = temp3[i] - temp4[i]
            temp_list.append(x)
            temp_list2.append(y)
        for j in range(len(temp_list)):
            s = p.weighted_factor * temp_list[j]
            t = p.weighted_factor * temp_list2[j]
            z = s + t + temp5[j]
            mutant_child.append(z)
        return mutant_child

        # -------------------------- Cross over ---------------------

    def crossOver(self, mutant, target_vector_index):
        tar_vec = self.population[target_vector_index]
        trail_vector = list()
        for i in range(len(mutant)):
            rand = random.uniform(0, 1)
            if rand > p.CR:
                trail_vector.append(tar_vec[i])
            else:
                trail_vector.append(mutant[i])
        return trail_vector

        # -------------------------- Main differential evolution algorithm ---------------------

    def process(self):
        for gen in range(p.generations):
            trails = []
            temp_list1 = []
            temp_list2 = []
            for childs in range(len(self.population)):
                randoms = self.choose_best(4, childs)
                temp = self.mutation(randoms)
                temp_list1.append(temp)
            self.mutants = copy.deepcopy(temp_list1)
            for mutant in range(len(self.mutants)):
                x = self.crossOver(self.mutants[mutant], mutant)
                trails.append(x)
            for i in range(len(self.population)):
                x = f.sphere(self.population[i])
                y = f.sphere(trails[i])
                if y < x:
                    temp_list2.append(trails[i])
                else:
                    temp_list2.append(self.population[i])
            self.new_generation = copy.deepcopy(temp_list2)
            self.population = copy.deepcopy(self.new_generation)
            if (gen % p.k) == 0:
                best = math.inf
                for i in range(p.NP):
                    temp_best = f.sphere(self.new_generation[i])
                    if temp_best < best:
                        best = temp_best
                print("The Most fit value of the generation ", gen, "th is ", '{:.2e}'.format(best))
        best = math.inf
        for i in range(p.NP):
            temp_best = f.sphere(self.new_generation[i])
            if temp_best < best:
                best = temp_best
        return best
