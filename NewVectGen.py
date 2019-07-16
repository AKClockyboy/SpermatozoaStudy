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

#Opening a file to write
f = open('Sphere_Sperm_Data.txt',"w")

#Constants and Parametres
iterations_of_number_increase = 400 #How many ways we arrange the sperm
iterations_of_postitions = 25
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0]
N = 20

#Empty lists to fill later
number_list = []
mean_force_list = []

for i in range(iterations_of_number_increase):

    initial_force_list = []
    final_force_list = []


    for i in range(iterations_of_postitions):

        for i in range(N): #This loop generates a sphere
            magnitude, vector = obs.RandSphere(N)
            initial_force_list.append(vector)

        transformed_v = obs.translation(vector, initial_force_list)

        for i in range(N):
            transformed_v[i] = transformed_v[i] / np.linalg.norm(transformed_v[i])

        alpha_list = [] #list for angles to the sphere

        for i in range(N):
            mtx,alpha = obs.fullrotation(transformed_v[i])
            final_force_list.append(mtx)
            alpha_list.append(alpha)
        x = sum(final_force_list)/len(final_force_list)

    N += 3
    mean_force_list.append(obs.forces(x))
    number_list.append(N)

#Writing to a file
for a,b in zip(mean_force_list,number_list):
    f.write("%s,%s\n" % (a,b))
f.close()

#Plotting it all
obs.mean_length_plotter()
obs.log_length_plotter(N)
