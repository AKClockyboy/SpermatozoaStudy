"""
Modelling flagella forces on a randomly distributed unit sphere
"""


import sys
import math
import numpy as np
import random
import Obs as Obs
from numpy import linalg as LA
import timeit


#Opening a file to write
f = open('Sphere_Sperm_Data.txt',"w")

#Constants and Parametres
iterations_of_postitions = 40 #How many ways we arrange the sperm
iterations_of_numbers = 500 #How many times we want to increase number of sperm
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0] #Ditto
N = 2
n_bins = 35 #Bins for the histogram plot

time1 = timeit.default_timer() #Take time 1

for i in range(iterations_of_numbers):
    vector_magnitude_list = []

    for i in range(iterations_of_postitions): #This loop generates the spheres

        magnitude, vector = (Obs.RandSphere(N))
        vector_magnitude_list.append(magnitude)

    N += 3 #How many the number of flagella increases by

    flagella_number_list.append(N)
    mean_length_list.append((Obs.mean_value(vector_magnitude_list, n_bins))) #Now we append the empty lists from before

#Finally, write to a file
for a,b in zip(mean_length_list,flagella_number_list):
    f.write("%s,%s\n" % (a,b))
f.close()

time2 = timeit.default_timer() #Take time 2
print("Time taken for code to run... in seconds :-  " + str(time2 - time1)) #Finish Timing The Loop

Obs.mean_length_plotter() #Finally, send it to be plotted
Obs.log_length_plotter(N)
