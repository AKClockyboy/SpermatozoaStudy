"""
Sperm-like object... ew
"""

import numpy as np
import scipy
import math

class Sperm(object):

    def __init__(self, pos, vel, mass, len, rotor):

        self.position = pos
        self.velocity = vel
        self.mass = mass
        self.length = len #For now, length will be diametre of sperm-like sphere
        self.rotation_rate = rotor

    def __str__(self):

        return str(self.position) + " " + str(self.velocity) + " " + str(self.mass) + " " + str(self.length) + " " + str(self.rotation_rate)

    def kinetic_energy(self):

        return 0.5*self.mass*(np.linalg.norm(self.velocity))**2

    # Time integration methods

    def leap_velocity(self, dt, force):

        self.velocity = self.velocity + dt*force/self.mass

    def leap_pos1st(self, dt):

        self.position = self.position + dt*(self.velocity)

    def leap_pos2nd(self, dt, force):

        self.position = self.position + dt*(self.velocity) + 0.5*dt**2*force/self.mass
