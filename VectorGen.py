"""

Generating Random 3D Unit Vectors

"""

import sys
import math
import numpy as np
import random
import PDF as pdff
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import timeit



#Opening a file to write
f = open('Sphere_Sperm_Data.csv',"w")

#Constants and Parametres
iterations_of_postitions = 7 #How many sperm push the sphere
iterations_of_numbers = 150 #How many times we want to increase number of sperm
mean_length_list = [] #Empty List to be filled later
flagella_number_list = [] #Ditto
origin = [0,0,0]
N = 2
n_bins = 50 #Bins for the histogram plot

time1 = timeit.default_timer()

for i in range(iterations_of_numbers):
    vector_magnitude_list = []

    for i in range(iterations_of_postitions):

        magnitude, vector = (pdff.RandSphere(N)) #remember to re-add 'ax'

        vector_magnitude_list.append(magnitude)

    #f.write("%s \n" % vector_magnitude_list)

    N += 1

    flagella_number_list.append(N)

    mean_length_list.append(pdff.mean_value_2(vector_magnitude_list, n_bins))

#Finally, write to a file
for a,b in zip(mean_length_list,flagella_number_list):
    f.write("%s, %s \n" % (a,b))
f.close()

time2 = timeit.default_timer()
print("Time taken for code to run... in seconds :-  " + str(time2 - time1))

pdff.mean_length_plotter()
