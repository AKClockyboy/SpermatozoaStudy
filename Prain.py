"""
Main Code to simulate sperm-like object in a fluid
"""

import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as pyplot
from Sperm import Spermatozoon
from Fluid import Fluid


def DragForce(radius, velocity, Eta):
    return -(6*pi*Eta*velocity)

def main():
    # Read name of output file from command line
    """
    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + "param.firstinput" )
        quit()
    else:
        infile_name = sys.argv[1]
        output_file = sys.arg[2]
    """
    sperm = []

    print(sperm)

    sperm = sperm.append(Spermatozoon(np.array([0,0,0]),np.array(random.randint(1,101),random.randint(1,101),random.randint(1,101)]), 1, np.array([0]),np.array([0])))

    print(sperm)

main()
