# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:24:19 2017

@author: rosen
"""

import numpy as np
import math
import matplotlib.pyplot as plt

delta_x = .5/500
x = np.arange(0,.5+delta_x,delta_x) #array of values of independent variable
psi = np.zeros(len(x)) #array of values for psi
energy = 0 #starting value for energy
theoretical_energy = (np.pi**2) / 2
error = 0.001
psi[0] = math.sqrt(2)
psi[1] = math.sqrt(2)
print(len(x))
print(x[500])
loop_continue = True
while loop_continue:
    for i in range(0,len(x) - 2):
        psi[i+2] = 2*psi[i+1] - psi[i] - 2*(delta_x**2)*energy*psi[i]
    if abs(psi[i+2]) > error:
        energy += 0.001
    else:
        difference = abs(energy - theoretical_energy)
        plt.plot(x, psi, 'b')
        print("""
        The estimated energy is {}. 
        The difference between this estimation of the energy and the theoretical value of the energy is {}
        When the energy is {}, the value of psi when x = 0.5 is {}""".format(energy,difference,energy,psi[i+2]))
        loop_continue = False
plt.plot(x,math.sqrt(2)*np.cos(np.pi * x),'r') 
plt.show()

