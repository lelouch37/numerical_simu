# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:58:39 2020

@author: Owner
"""

import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

skytree_height = Decimal('634.0')
g = Decimal('-9.8')
time = Decimal('0')
time_step = Decimal('0.1')

time_list = []
height_list = []

height = skytree_height

while height > 0:
    velocity = Decimal(str(g*time))
    height = Decimal(str(skytree_height + g*time**2/2))
    print("t = " + str(time) + " [s], h = " + str(height) + " [m], v = " + str(abs(velocity)) + " [m/s]")
    
    time_list.append(time)
    height_list.append(height)

    time += time_step
    
x = np.array(time_list)
y = np.array(height_list)
t = plt.plot(x, y, 'o')
plt.xlabel("Time [s]")
plt.ylabel("height [m]")