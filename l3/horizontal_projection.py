# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:59:21 2020

@author: Owner
"""


import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

skytree_height = Decimal('634.0')
g = Decimal('-9.8')
time = Decimal('0')
time_step = Decimal('0.1')

x_list = []
y_list = []

y = skytree_height
v0_x = 30

while y > 0:
    v_x = v0_x
    v_y = Decimal(str(g*time))
    x = Decimal(str(v_x*time))
    y = Decimal(str(skytree_height + g*time**2/2))
    print("t = " + str(time) + " , ( " + str(x) + " , " + str(y) + " )")
    
    x_list.append(x)
    y_list.append(y)
    
    time += time_step
    
x_array = np.array(x_list)
y_array = np.array(y_list)
t = plt.plot(x_array, y_array, 'o')
plt.xlabel("x [m]")
plt.ylabel("y [m]")