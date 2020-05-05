# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:58:39 2020

@author: Owner
"""

skytree_height = 634.0
g = -9.8
time = 0
time_step = 0.1

height = skytree_height

while height > 0:
    velocity = g*time
    height = skytree_height + g*time**2/2
    print("t = " + str(time) + " [s], h = " + str(height) + " [m], v = " + str(abs(velocity)) + " [m/s]")
    time += time_step