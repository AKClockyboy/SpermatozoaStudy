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


#Opening a file to write
f = open('Sphere_Sperm_Data.txt',"w")

#Constants and Parametres
iterations_of_postitions = 4 #How many ways we arrange the sperm
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0]
N = 1

time1 = timeit.default_timer() #Timing The Loop
vector_list = []

for i in range(N): #This loop generates a sphere
    magnitude, vector = obs.RandSphere(N)
    vector_list.append(vector)


time2 = timeit.default_timer()

transformed_v = obs.translation(vector, vector_list)
new_transformed_v = []

R = obs.rotation(transformed_v, N)
obs.MagnitudeSum(vector, vector_list, R, origin)


print("Time taken for code to run... in seconds :-  " + str(time2 - time1)) #Finish Timing The Loop
