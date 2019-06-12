"""
Fluid-like object.. this might not be necessary
"""

import numpy as np
import scipy
import math

class Fluid(object):

    def __init__(self, Kvisc, Dvisc, vel, den):

        self.kinematic_viscocity = Kvisc
        self.dynamic_viscocity = Dvisc
        self.velocity = vel
        self.density = den

    def __str__(self):

        return str(self.kinematic_viscocity) + " " + str(self.dynamic_viscocity) + " " + str(self.velocity) + " " + str(self.density)
