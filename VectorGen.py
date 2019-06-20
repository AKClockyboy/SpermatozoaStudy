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

#Establishing the 3D plot
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#plt.title("Randomly distributed flagella vectors on a sphere", fontdict=None, loc='center', pad=None)


#Constants and Parametres
iterations = 1
vector_magnitude_list = []
mean_length_list = []
flagella_number_list = []
origin = [0,0,0]
N = 2
n_bins = 1000

for i in range(n_bins):
    for i in range(iterations):
        magnitude, vector = (pdff.RandSphere(N)) #re-add 'ax'
        vector_magnitude_list.append(magnitude)

    mean = pdff.mean_plotter(vector_magnitude_list)
    mean_length_list.append(mean)
    N += 1
    flagella_number_list.append(N)

print("Number List :" + str(flagella_number_list))
print("Mean List :" + str(mean_length_list))
plt.xlabel("Number")
plt.ylabel("Mean_Length_List")
plt.plot(flagella_number_list, mean_length_list)
plt.show()
