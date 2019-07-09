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
iterations_of_postitions = 1 #How many ways we arrange the sperm
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0]
N = 20

vector_list = []

for i in range(N): #This loop generates a sphere
    magnitude, vector = obs.RandSphere(N)
    vector_list.append(vector)

transformed_v = obs.translation(vector, vector_list)

for i in range(N):
    transformed_v[i] = transformed_v[i] / np.linalg.norm(transformed_v[i])

obs.MagnitudeSum(vector, vector_list, transformed_v, origin)

print(transformed_v)
new_translation = []
for i in range(len(transformed_v)):
    new_translation.append(obs.rotationZ(transformed_v[i]))


obs.MagnitudeSum(vector, vector_list, new_translation, origin)
