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
import csv
from scipy.linalg import norm #WHO KNOWS HOW MANY OF THESE I WILL NEED?

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
    vector = [x, y, z]
    magnitude = norm(np.array([x.sum(), y.sum(), z.sum()]))

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

def PDF_plotter(centres, vector_magnitude_list, prob):

    plt.xlabel("Magnitude of Vector")
    plt.ylabel("Probability")
    plt.plot(centers, len(vector_magnitude_list)*prob,'k-',linewidth=2)
    plt.show()

def mean_length_plotter():

    from numpy.polynomial.polynomial import polyfit

    y,x = np.loadtxt('Sphere_Sperm_Data.txt', delimiter = ',', unpack=True)

    C = np.sqrt(8/(3*math.pi))
    plt.title('Mean Magnitude of Force Vector\nVS\nNumber of Flagella')
    plt.xlabel('N')
    plt.ylabel('|L|')
    #b, m = polyfit(-C*np.sqrt(x), y, 0.01)
    #plt.plot(C*(np.sqrt(x)), y,  label = None)
    lines = plt.plot(-C*np.sqrt(x), y, label = None)
    #plt.plot((x), b + m * (x), 'c')
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

    y,x = np.loadtxt('Sphere_Sperm_Data.txt', delimiter = ',', unpack=True)

    y = np.log(y)
    x = -np.log(np.sqrt(x))

    results = sm.OLS(y,sm.add_constant(x)).fit()
    print(results.summary())

    plt.scatter(x,y, c = 'r', s = 1, marker = '.' )

    X_plot = np.linspace(0, -np.log(N)*1.25,5.5)
    plt.plot(X_plot, X_plot*results.params[1] + results.params[0], c = 'k')

    plt.show()

    """
    OLD LINE FIT CODE
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
