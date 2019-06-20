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
import scipy.stats
from scipy.linalg import norm

def mean_plotter(vector_magnitude_list):
    shape, loc, scale = scipy.stats.lognorm.fit(vector_magnitude_list, floc=0)
    mean = scipy.stats.lognorm.mean(shape, loc = loc, scale = 100)
    return(mean)

def mean_plotter_2(mean_length_list, flagella_number_list):
    scipy.stats.binned_statistic(mean_length_list, flagella_number_list,)

def PDF(n_bins, vector_magnitude_list):

    shape, loc, scale = scipy.stats.lognorm.fit(vector_magnitude_list, floc=0)
    clr = "#EFEFEF"
    counts, edges, patches = plt.hist(vector_magnitude_list, bins = n_bins, color=clr)
    centers = 0.5*(edges[:-1] + edges[1:])
    cdf = scipy.stats.lognorm.cdf(edges, shape, loc=loc, scale=scale)
    prob = np.diff(cdf)

    mean = scipy.stats.lognorm.mean(shape, loc = loc, scale = scale)

    plt.xlabel("Magnitude of Vector")
    plt.ylabel("Probability")
    plt.plot(centers, len(vector_magnitude_list)*prob,'k-',linewidth=2)
    plt.show()

    return(mean)

def RandSphere(N):
    #Setting up parametres
    phi = np.random.uniform(0, np.pi*2, N)
    theta = np.arccos(np.random.uniform(-1, 1, N))

    #Creating x, y and z coordinates of the vectors
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    #Actualises vector as an array then appends to list --- factor of 1/N ot factorise
    vector = [x/N, y/N, z/N]
    magnitude = norm(np.array([x.sum(),y.sum(),z.sum()]))

    #Plot every vector individually
    #ax.scatter(x, y, z, c='b', marker = '3')

    return(magnitude, vector)

def MagnitudeSum(vector_list, vector_magnitude_list, ax, origin):
    #Now adding N vectors together to obtain magnitude
    vector_sum = (list(map(sum, zip(*vector_list))))
    vector_magnitude = (vector_sum[0]*vector_sum[0] + vector_sum[1]*vector_sum[1] + vector_sum[2]*vector_sum[2])**1/2
    vector_magnitude_list.append(vector_magnitude)

    #Plotting for displaying the line of force
    X, Y, Z = zip(origin)
    U, V, W = zip(vector_sum)
    ax.quiver(X,Y,Z,U,V,W,arrow_length_ratio = 0.1)
