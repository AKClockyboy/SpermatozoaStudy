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
f = open('Sphere_Force_Data.txt',"w")
g = open('Sphere_Torque_Data.txt',"w")


#Constants and Parametres
iterations_of_number_increase = 1000 #How many ways we arrange the sperm
iterations_of_postitions = 10
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0]
N = 20

#Empty lists to fill later
number_list = []
mean_force_list = []
mean_torque_list = []

for i in range(iterations_of_number_increase):

    initial_force_list = []
    final_force_list = []
    final_force_list_2 = []

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

        force = obs.forces(final_force_list)

        final_force_list_2.append(force)


    print("Torque is this --> " + str(obs.torque(final_force_list, initial_force_list, N)))
    print("Norm of torque is this --> " + str(scipy.linalg.norm(obs.torque(final_force_list, initial_force_list, N))))

    x = sum(final_force_list_2)/(iterations_of_postitions)
    y = scipy.linalg.norm(obs.torque(final_force_list, initial_force_list, N))
    N += 2
    mean_force_list.append(x)
    mean_torque_list.append(y)
    number_list.append(N)

#Writing to a file
for a,b in zip(mean_torque_list,number_list):
    g.write("%s,%s\n" % (a,b))
g.close()

for a,b in zip(mean_force_list,number_list):
    f.write("%s,%s\n" % (a,b))
f.close()

#Plotting it all
obs.mean_length_plotter()
#obs.mean_torque_plotter()
#obs.log_length_plotter(N)
