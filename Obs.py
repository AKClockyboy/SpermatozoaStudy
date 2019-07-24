"""
Code to plot PDF of vector_sum
"""


import sys
import math
import numpy as np
import random
from numpy import linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats
from scipy.linalg import norm #WHO KNOWS HOW MANY OF THESE I WILL NEED?

def translation(vector, vector_list):

    for vector in vector_list:
        for i in range(3):
            vector[i] = vector[i] + vector[i]

    return(vector_list)

def fullrotation(t_v):

    theta =  np.arccos(np.random.uniform(-1, 1))

    alpha = (np.random.uniform(0, 2*np.pi)) #rotation angles

    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],[0 ,1 ,0],[-np.sin(theta), 0, np.cos(theta)]])

    Rz =  np.array([[np.cos(alpha), -np.sin(alpha),0],[np.sin(alpha), np.cos(alpha),0],[0,0,1]]) #rotation matrices

    return(Ry@Rz@t_v, theta)

def torque(final_force_list, initial_force_list, N, torque_list):


    for i in range(N):

        X = final_force_list[i][1]*initial_force_list[i][2] - final_force_list[i][2]*initial_force_list[i][1]
        Y = final_force_list[i][0]*initial_force_list[i][2] - final_force_list[i][2]*initial_force_list[i][0]
        Z = final_force_list[i][0]*initial_force_list[i][1] - final_force_list[i][1]*initial_force_list[i][0]

        torque_list.append(np.array([X,Y,Z]))

    torque = sum(torque_list)

    return(torque)

def forces(n_tr):

    x = sum(n_tr)

    return(x)

def rotation(t_v):

    if t_v[0] > 0 and t_v[2] > 0:
        phi  = -np.arctan((t_v[0])/(t_v[2]))
    elif t_v[0] > 0 and t_v[2] < 0:
        phi = np.arctan((t_v[0])/(t_v[2])) - np.pi/2
    elif t_v[0] < 0 and t_v[2] < 0:
        phi = np.arctan((t_v[0])/(t_v[2])) + np.pi/2
    elif t_v[0] < 0 and t_v[2] > 0:
        phi = -np.arctan((t_v[0])/(t_v[2]))
    elif t_v[0] > 0 and t_v[2] == 0:
        phi = -np.pi/2
    elif t_v[0] == 0 and t_v[2] < 0:
        phi = np.pi
    elif t_v[0] < 0 and t_v[2] ==0:
        phi = -np.pi/2
    elif t_v[0] == 0 and t_v[2] == 0:
        phi = 0

    theta = np.arctan((t_v[1])/np.sqrt(t_v[0]**2+t_v[2]**2)) #rotating in y

    alpha = np.pi/2 - (np.cos(phi)*np.cos(theta))

    Zalpha =  np.arccos(np.random.uniform(-1, 1))
    Yalpha = np.arccos(np.random.uniform(0, 1))
    Xalpha = np.arccos(np.random.uniform(0, 1)) #Random params for rotation

    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],[0 ,1 ,0],[-np.sin(theta), 0, np.cos(theta)]]) #rotating y

    Rx = np.array([[1,0,0],[0,np.cos(phi), -np.sin(phi)],[0, np.sin(phi), np.cos(phi)]]) #rotating x

    RandRz =  np.array([[np.cos(Zalpha), -np.sin(Zalpha),0],[np.sin(Zalpha), np.cos(Zalpha),0],[0,0,1]])

    RandRy = np.array([[np.cos(Yalpha),0,np.sin(Yalpha)],[0,1,0],[-np.sin(Yalpha), 0, np.cos(Yalpha)]])

    RandRx = np.array([[1,0,0],[0,np.cos(Xalpha),-np.sin(Xalpha)],[0, np.sin(Xalpha), np.cos(Xalpha)]])

    Rxi = np.array([[1, 0, 0],[0, np.cos(phi), np.sin(phi)],[0, -np.sin(phi), np.cos(phi)]]) #inversing x rot.

    Ryi = np.array([[np.cos(theta), 0, -np.sin(theta)],[0,1,0],[np.sin(theta), 0, np.cos(theta)]]) #inversing y rot.

    return (Ryi@Rxi@RandRz@RandRx@RandRy@Rx@Ry@t_v, alpha) #my old rotation function for memory's sake

def mean_value(vector_magnitude_list, n_bins):

    counts, edges, patches = plt.hist(vector_magnitude_list, bins = n_bins, color = "w") # takes histogram information

    centres = 0.5*(edges[:-1] + edges[1:]) # calculates centres

    products = np.sum(np.multiply(counts, centres))/len(vector_magnitude_list) # This gives a final value for mean

    return(products)

def PDF(n_bins, vector_magnitude_list):

    #Method to obtain a probability distribution function
    shape, loc, scale = scipy.stats.lognorm.fit(vector_magnitude_list, floc=0)
    clr = "#EFEFEF"
    counts, edges, patches = plt.hist(vector_magnitude_list, bins = n_bins, color=clr)
    centres = 0.5*(edges[:-1] + edges[1:])
    cdf = scipy.stats.lognorm.cdf(edges, shape, loc=loc, scale=scale)
    prob = np.diff(cdf)

    return(centres, vector_magnitude_list, prob)

def RandSphere(N):

    #Setting up parametres
    phi = np.random.uniform(0, np.pi*2, N)
    theta = np.arccos(np.random.uniform(-1, 1, N))

    #Creating x, y and z coordinates of the vectors
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    #Actualises vector as an array then appends to list --- factor of 1/N ot factorise MAYBE
    for i in range(N):
        vector = [x[i], y[i], z[i]]
    magnitude = norm(np.array([x.sum(), y.sum(), z.sum()]))

    return(magnitude, vector)

def MagnitudeSum(vector_list, transformed_v, origin):
    #Now adding N vectors together to obtain magnitude
    vector_sum = (list(map(sum, zip(*vector_list))))
    #vector_magnitude = (vector_sum[0]*vector_sum[0] + vector_sum[1]*vector_sum[1] + vector_sum[2]*vector_sum[2])**1/2
    #vector_magnitude_list.append(vector_magnitude)

    #Plotting for displaying the line of force
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    for i in range(len(vector_list)):

        X, Y, Z = zip(vector_list[i])
        U, V, W = zip(transformed_v[i])

        ax.quiver(X,Y,Z,U,V,W, arrow_length_ratio = 0.1)

    plt.show()

def PDF_plotter(centres, vector_magnitude_list, prob):

    plt.xlabel("Magnitude of Vector")
    plt.ylabel("Probability")
    plt.plot(centers, len(vector_magnitude_list)*prob,'k-',linewidth=2)
    plt.show()

def mean_length_plotter():

    y,x = np.loadtxt('Sphere_Force_Data.txt', delimiter = ',', unpack=True)

    plt.title('Mean Magnitude of Force Vector\nVS\nNumber of Flagella')
    plt.xlabel('N')
    plt.ylabel('|L|')
                        #Polyfit lies here ):
    lines = plt.plot(x, y, label = None)

    plt.setp(lines, 'color', 'm', linewidth = 2.0)
    plt.show()

def mean_torque_plotter():

    y,x = np.loadtxt('Sphere_Torque_Data.txt', delimiter = ',', unpack=True)

    plt.title('Mean Magnitude of Torque Vector\nVS\nNumber of Flagella')
    plt.xlabel('N')
    plt.ylabel('|L|')

    lines = plt.plot(x, y, label = None)

    plt.setp(lines, 'color', 'm', linewidth = 2.0)
    plt.show()

def sphere_plotter(vector):

    #Establishing the 3D plot of the flagella sphere
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    plt.title("Randomly distributed flagella vectors on a sphere", fontdict=None, loc='center', pad=None)
    ax.scatter(x, y, z, c='b', marker = '3')

def log_length_plotter(N):

    from numpy.polynomial.polynomial import polyfit

    y,x = np.loadtxt('Sphere_Force_Data.txt', delimiter = ',', unpack=True)

    y = np.log(y)
    x = -np.log(np.sqrt(x))

    results = sm.OLS(y,sm.add_constant(x)).fit()
    print(results.summary())

    plt.scatter(x,y, c = 'r', s = 1, marker = '.' )

    X_plot = np.linspace(0, -np.log(N)*1.25,5.5)
    plt.plot(X_plot, X_plot*results.params[1] + results.params[0], c = 'k')
    plt.title('Mean Magnitude of Force Vector\nVS\nNumber of Flagella')
    plt.show()

    """
    OLD LINE FIT CODE RIP
    # Fit with polyfit
    b, m = polyfit(np.log(x), np.log(y), 1)
    plt.title('Log of Mean Magnitude of Force Vector\nVS\n log of Number of Flagella')
    plt.xlabel('Log(N)')
    plt.ylabel('Log(|L|)')
    plt.scatter(-np.log(x), np.log(y), c = 'k', s = 900, marker = '$FUCK$', label = None, linewidths = 0.1)
    #plt.setp(lines, 'color', 'm', linewidth = 2.0)
    plt.plot(np.log(x), b + m * np.log(x), 'c')
    plt.show()
    """
