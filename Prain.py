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


def DragForce(sperm, fluid):
    #Drag Force, duh.
    return -1/(6*math.pi*fluid.viscocity*sperm.length)

def SpinDragForce(sperm, fluid):
    #Rotational Drag Force, duh.
    return -1/(8*math.pi*fluid.viscocity*(sperm.lenth)**3)



def main():

    # Read name of output file from command line

    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + "param.firstinput" + "traj.xyz")
        quit()
    else:
        infile_name = sys.argv[1]
        output_file = sys.argv[2]

    infile = open(infile_name,"r")
    infile = np.loadtxt(infile)

    visc = float(infile[0])
    leg = float(infile[1])
    den = int(infile[2])
    speed = int(infile[3])

    #Initialising Sperm and Fluid Objects

    sperm = Spermatozoon(np.array([0,0,0]),np.array([random.randint(0,50),random.randint(0,50),random.randint(0,50)]), 1, leg, np.array([0]), 0)
    fluid = Fluid(visc, speed, den)

    # Set up simulation parameters
    dt = 0.01
    numstep = 2000
    time = 0.0

    #Initial Force Value
    Force = DragForce(sperm, fluid)

    #Initial Time List
    time_list = [0.0]

    #Hopefully I can visulise it with this
    f = open(output_file,'w') #Whatever Programme I use to model this

    


main()
