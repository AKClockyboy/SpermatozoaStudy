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
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.title("Randomly distributed flagella vectors on a sphere", fontdict=None, loc='center', pad=None)

#Constants and Parametres
iterations = 100
vector_magnitude_list = []
origin = [0,0,0]
N = 5
n_bins = 50

for i in range(iterations):
    vector_list = []
    #Loop for number of vectors we want
    for i in range(N):
        #Setting up parametres
        phi = np.random.uniform(0,np.pi*2)
        theta = np.arccos(np.random.uniform(-1,1))

        #Creating x, y and z coordinates of the vectors
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)

        #Actualises vector as an array then appends to list --- factor of 1/N ot factorise
        vector = [-x/N, -y/N, -z/N]
        vector_list.append(vector)

        #Plot every vector individually
        ax.scatter(x, y, z, c='b', marker = '3')

    #Now adding N vectors together to obtain magnitude
    vector_sum = (list(map(sum, zip(*vector_list))))
    vector_magnitude = (vector_sum[0]*vector_sum[0] + vector_sum[1]*vector_sum[1] + vector_sum[2]*vector_sum[2])**1/2
    vector_magnitude_list.append(vector_magnitude)


    #Plotting for displaying the line of force
    X, Y, Z = zip(origin)
    U, V, W = zip(vector_sum)
    ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio = 0.01)
plt.show()

print("vector mag list is " + str(vector_magnitude_list))

pdff.PDF2(n_bins, vector_magnitude_list)
plt.show()
