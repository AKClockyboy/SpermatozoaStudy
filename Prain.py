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
import SingleNewVectorGen as VectGen
import Obs as obs

def linforce():

    return()

def torqueconsid()

    return()

def DragForce(sperm, fluid):
    #Drag Force, duh.

    DragForce = -((6*math.pi*fluid.viscocity*sperm.length))*(sperm.velocity)

    print(DragForce)

    return -((6*math.pi*fluid.viscocity*sperm.length))*(sperm.velocity)

def SpinDragForce(sperm, fluid):
    #Rotational Drag Force, duh.

    return -1/(8*math.pi*fluid.viscocity*(sperm.lenth)**3)

def main():

    # Read name of output file from command line

    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " param.firstinput " + "traj.xyz")
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

    mean_force, mean_torque, summed_force_list, summed_torque_list = VectGen.FandTGen()



    sperm = Spermatozoon(np.array([0.0001,1,0]),np.array([0,0,0]), 80, leg, np.array([0,0,0]), 1)

    fluid = Fluid(visc, speed, den)

    sperm_position_list = []

    # Set up simulation parameters
    dt = 0.1
    numstep = 20000
    time = 0.0

    #Initial Force Value
    force = summed_force_list + DragForce(sperm, fluid)

    #Initial Time and Position List
    time_list = [0.0]
    pos_list = [sperm.position]


    #Hopefully I can visulise it with this
    f = open(output_file,'w') #Whatever Programme I use to model this

    # Start the time integration loop
    for t in range(numstep):

        #Position Update
        sperm.leap_pos2nd(dt, force)

        #Re-calculating Force
        force_new = summed_force_list + DragForce(sperm, fluid)

        #Velocity Update
        sperm.leap_velocity(dt, force + force_new)

        # Increase time and reset force value
        time += dt
        pos_list.append(sperm.position)
        time_list.append(time)
        force = force_new

        #Write a VMD file
        f.write(str(1)+"\n")
        f.write("Point = " + str(t+1) +"\n")
        f.write("s"+ str(1) + " " + str(sperm.position[0]) + " " + str(sperm.position[1]) + " " + str(sperm.position[2]) + "\n")

main()
