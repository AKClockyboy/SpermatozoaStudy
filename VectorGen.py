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

#Establish Axis
fig = plt.figure()
ax = plt.axes(projection='3d')


#Uh, loop over polar coords
for i in range(800):
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta ) * np.tan(phi)

    ax.scatter(x, y, z, c='r', marker = '2')

plt.show()
