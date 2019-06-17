"""

Generating Random 3D Unit Vectors

"""

import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.title("Randomly distributed vectors on a sphere", fontdict=None, loc='center', pad=None)
vector_list = []
origin = [0,0,0]
N = 100
n_bins = 50

#Loop for number of vectors we want
for i in range(N):

    #Setting up parametres
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)
    theta = np.arccos(costheta)

    #Creating x, y and z coordinates of the vectors
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    #Actualises vector as an array then appends to list --- factor of 1/N ot factorise
    vector = [-x/N, -y/N, -z/N]
    vector_list.append(vector)


    #Plot...
    ax.scatter(x, y, z, c='b', marker = '3')

#Now adding all vectors together
vector_sum = (list(map(sum, zip(*vector_list))))
vector_magnitude = (vector_sum[0]*vector_sum[0] + vector_sum[1]*vector_sum[1] + vector_sum[2]*vector_sum[2])**1/2
print(vector_magnitude)

ax.scatter(x, y, z, c='b', marker = '3')


#Optional plotting for displaying the line of force
X, Y, Z = zip(origin)
U, V, W = zip(vector_sum)

ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio = 0.5)

np.histogram(vector_list, bins=n_bins)

#...and show
plt.show()
