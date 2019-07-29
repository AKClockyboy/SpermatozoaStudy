import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as pyplot
import scipy
from Sperm import Spermatozoon
from Fluid import Fluid
import SingleNewVectorGen as VectGen
import Obs as obs
import Prain as Prain

number_of_iterations = 100
N = 2
sperm_displacement_list = []
sperm_number_list = [2]

for i in range(number_of_iterations):

    displacement = Prain.prain(N)
    sperm_displacement_list.append(displacement)

    N += 1
    sperm_number_list.append(N)


y = sperm_displacement_list
x = sperm_number_list

plt.xlabel('N')
plt.ylabel('Displacement of Sphere')
plt.plot(x, y, c = 'k')
plt.show()
