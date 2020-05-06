# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:40:23 2020

@author: Owner
"""


import numpy as np
import matplotlib.pyplot as plt

skytree_height = 634.0
g = -9.8
time = 0
time_step = 0.1

time_list = []
height_list = []

height = skytree_height

while height > 0:
    velocity = g*time
    height = skytree_height + g*time**2/2
    print("t = " + str(time) + " [s], h = " + str(height) + " [m], v = " + str(abs(velocity)) + " [m/s]")
    
    time_list.append(time)
    height_list.append(height)

    time += time_step
    
x = np.array(time_list)
y = np.array(height_list)
t = plt.plot(x, y, 'o')
plt.xlabel("Time [s]")
plt.ylabel("height [m]")