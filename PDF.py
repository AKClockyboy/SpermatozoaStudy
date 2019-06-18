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

def PDF2(n_bins, vector_magnitude_list):
    shape,loc,scale=scipy.stats.lognorm.fit(vector_magnitude_list,floc=0)
    clr="#EFEFEF"
    counts,edges,patches=plt.hist(vector_magnitude_list,bins=n_bins,color=clr)
    centers=0.5*(edges[:-1]+edges[1:])
    cdf=scipy.stats.lognorm.cdf(edges,shape,loc=loc,scale=scale)
    prob=np.diff(cdf)
    plt.xlabel("Magnitude of Vector")
    plt.ylabel("Probability")
    plt.plot(centers, len(vector_magnitude_list)*prob,'k-',linewidth=2)
