# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:25:53 2020

@author: Owner
"""


import numpy as np
import matplotlib.pyplot as plt

skytree_height = 634.0
g = -9.8
time = 0
time_step = 0.1

x_list = []
y_list = []

y = skytree_height
v0_x = 30

while y > 0:
    v_x = v0_x
    v_y = g*time
    x = v_x*time
    y = skytree_height + g*time**2/2
    print("t = " + str(time) + " , ( " + str(x) + " , " + str(y) + " )")
    
    x_list.append(x)
    y_list.append(y)
    
    time += time_step
    
x_array = np.array(x_list)
y_array = np.array(y_list)
t = plt.plot(x_array, y_array, 'o')
plt.xlabel("x [m]")
plt.ylabel("y [m]")