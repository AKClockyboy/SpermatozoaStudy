"""
Test for distribution of my random function thing
"""

import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vector = [0,0,1]
vector_list = []

for i in range(50):

    Zalpha =  np.random.uniform(0, 2*np.pi)
    Yalpha = np.arccos(np.random.uniform(0, 1))
    Xalpha = np.arccos(np.random.uniform(0, 1)) #Random params for rotation

    RandRz =  np.array([[np.cos(Zalpha), -np.sin(Zalpha),0],[np.sin(Zalpha), np.cos(Zalpha),0],[0,0,1]])
    RandRy = np.array([[np.cos(Yalpha),0,np.sin(Yalpha)],[0,1,0],[-np.sin(Yalpha), 0, np.cos(Yalpha)]])
    RandRx = np.array([[1,0,0],[0,np.cos(Xalpha),-np.sin(Xalpha)],[0, np.sin(Xalpha), np.cos(Xalpha)]])

    x = (RandRz@RandRx@vector)[0]
    y = (RandRz@RandRx@vector)[1]
    z = (RandRz@RandRx@vector)[2]

    ax.scatter(x, y, z, c='b', marker = '.')

    x = vector[0]
    y = vector[1]
    z = vector[2]

    ax.scatter(x, y, z, c='r', marker = '.')
plt.show()
"""

x,y = np.loadtxt('AverageTorque.txt', delimiter = ' ', unpack=True)
plt.title('Mean Magnitude of Force Vector\nVS\nNumber of Flagella')
plt.xlabel('N')
plt.ylabel('|L|')

lines = plt.plot(x, y, label = None)

plt.setp(lines, 'color', 'm', linewidth = 2.0)
plt.show()
