"""
Modelling flagella forces on a randomly distributed unit sphere
"""


import sys
import math
import numpy as np
import random
import Obs as obs
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import timeit
import scipy

def FandTGen():
    #Constants and Parametres
    iterations_of_positions = 10000
    mean_length_list = [] #Empty List to be filled later
    origin = [0,0,0]
    N = 20


    #Empty lists to fill later
    number_list = []
    mean_mag_force_list = []
    mean_mag_torque_list = []
    summed_force_list = []
    summed_torque_list = []

    for i in range(iterations_of_positions):

        #more empty lists innit
        initial_force_list = []
        final_force_list = []
        torque_list = []

        for i in range(N): #This loop generates a sphere
            magnitude, vector = obs.RandSphere(N)
            initial_force_list.append(vector)

            #print(initial_force_list)

        transformed_v = obs.translation(vector, initial_force_list) #transforiming to get a nice graph

        for i in range(N):
            transformed_v[i] = transformed_v[i] / np.linalg.norm(transformed_v[i]) #literally for getting a nice graph


        alpha_list = [] #list for angles to the sphere

        for i in range(N):
            mtx,alpha = obs.fullrotation(transformed_v[i])
            final_force_list.append(mtx)
            alpha_list.append(alpha)


        summed_force_list.append(obs.forces(final_force_list))
        summed_torque_list.append(obs.torque(final_force_list, initial_force_list, N, torque_list))

        mean_mag_force_list.append(scipy.linalg.norm(obs.forces(final_force_list)))
        mean_mag_torque_list.append(scipy.linalg.norm(obs.torque(final_force_list, initial_force_list, N, torque_list)))


    mean_force = sum(mean_mag_force_list)/(iterations_of_positions)
    mean_torque = sum(mean_mag_torque_list)/(iterations_of_positions)

    return(mean_force, mean_torque, sum(summed_force_list)/iterations_of_positions, sum(summed_torque_list)/iterations_of_positions)
