import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as plt
import scipy
from Sperm import Spermatozoon
from Fluid import Fluid
import SingleNewVectorGen as VectGen
import Obs as obs
import Prain as Prain

number_of_iterations = 50

N = 1

mean_sperm_displacement = []
sperm_number_list = []

for i in range(number_of_iterations):

    sperm_displacement_list = []

    for i in range(700):

        sperm_displacement_list.append(Prain.prain(N))

    mean_sperm_displacement.append(sum(sperm_displacement_list)/number_of_iterations)

    N += 1
    sperm_number_list.append(N)


y = mean_sperm_displacement
x = sperm_number_list

plt.xlabel('N')
plt.ylabel('Displacement of Sphere')
plt.plot(x, y, c = 'k')
plt.show()
