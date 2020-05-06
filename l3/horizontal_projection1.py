# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:59:21 2020

@author: Owner
"""


skytree_height = 634.0
g = -9.8
time = 0
time_step = 0.1

y = skytree_height
v0_x = 30

while y > 0:
    v_x = v0_x
    v_y = g*time
    x = v_x*time
    y = skytree_height + g*time**2/2
    print("t = " + str(time) + " , ( " + str(x) + " , " + str(y) + " )")
    
    time += time_step