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
iterations = 1000
vector_magnitude_list = []
origin = [0,0,0]
N = 7
n_bins = 100

for i in range(iterations):

    magnitude, vector = (pdff.RandSphere(N, ax))
    vector_magnitude_list.append(magnitude)
print("Magnitudes are: " + str(vector_magnitude_list))

plt.show()
pdff.PDF(n_bins, vector_magnitude_list)
plt.show()
