"""
Main Code to simulate sperm-like object in a fluid
"""

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

def angular_torque_tings(dt, torque, mass, length):

    angle = torque*dt*5/(2*mass*length*length)

    return(angle)

def PHAT_rot_matrix(torque, x):

    torque = torque/scipy.linalg.norm(torque)

    U1 = torque[0]
    U2 = torque[1]
    U3 = torque[2]

    PHAT = np.array([[np.cos(x)+(1-np.cos(x))*U1*U1, U1*U2*(1-np.cos(x))-U3*(np.sin(x)), U1*U3*(1-np.cos(x))+U2*np.sin(x)], [U2*U1*(1-np.cos(x))+U3*np.sin(x), np.cos(x) + U2*U2*(1-np.cos(x)), U2*U3*(1-np.cos(x)) - U1*np.sin(x)], [U3*U1*(1-np.cos(x))-U2*np.sin(x), U3*U2*(1-np.cos(x))+U1*np.sin(x), np.cos(x)+U3*U3*(1-np.cos(x))]])

    print(PHAT)

    return(PHAT)

def DragForce(sperm, fluid):

    DragForce = -((6*math.pi*fluid.viscocity*sperm.length))*(sperm.velocity)

    return -((6*math.pi*fluid.viscocity*sperm.length))*(sperm.velocity)

def SpinDragForce(sperm, fluid):
    #Rotational Drag Force, duh.

    return -1/(8*math.pi*fluid.viscocity*(sperm.lenth)**3)

def prain(N):

    # Read name of output file from command line

    """
    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " param.firstinput " + "traj.xyz")
        quit()
    else:
        infile_name = sys.argv[1]
        output_file = sys.argv[2]

    infile = open(infile_name,"r")
    infile = np.loadtxt(infile)
    """

    visc = 8
    leg = 0.00005
    den = 1
    speed = 0


    #Initialising Sperm and Fluid Objects

    mean_force, mean_torque, summed_force_list, summed_torque_list = VectGen.FandTGen(N)
    #print(summed_torque_list)

    sperm = Spermatozoon(np.array([0.0001,1,0]), np.array([0,0,0]), 0.1, leg, np.array([0,0,0]), 0, 1)

    fluid = Fluid(visc, speed, den)

    sperm_position_list = []


    # Set up simulation parameters
    dt = 0.01
    numstep = 10000
    time = 0.0

    #Initial Force Value
    force = summed_force_list

    #Torque set-up
    alpha = angular_torque_tings(dt, mean_torque, sperm.mass, sperm.length)
    rot = PHAT_rot_matrix(summed_torque_list, alpha)

    #Initial Time and Position List
    time_list = [0.0]
    pos_list = [sperm.position]



    #Hopefully I can visulise it with this
    #f = open(output_file,'w') #Whatever Programme I use to model this

    # Start the time integration loop
    for t in range(numstep):

        #Position Update
        sperm.leap_pos2nd(dt, rot@force)

        #Re-calculating Force
        force_new = rot@(summed_force_list + DragForce(sperm, fluid))

        #Velocity and Torque/Angle Update
        sperm.leap_velocity(dt, rot@(force + force_new))

        # Increase time and reset force value
        time += dt
        pos_list.append(sperm.position)
        time_list.append(time)
        force = force_new

        #Write a VMD file
        #f.write(str(1)+"\n")
        #f.write("Point = " + str(t+1) +"\n")
        #f.write("s"+ str(1) + " " + str(sperm.position[0]) + " " + str(sperm.position[1]) + " " + str(sperm.position[2]) + "\n")


    #print(scipy.linalg.norm(pos_list[numstep]))

    return(scipy.linalg.norm(pos_list[numstep]) - scipy.linalg.norm(pos_list[0]))
