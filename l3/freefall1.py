# -*- coding: utf-8 -*-
"""
Created on Tue May  5 23:58:39 2020

@author: Owner
"""

from decimal import Decimal

skytree_height = Decimal('634.0')
g = Decimal('-9.8')
time = Decimal('0')
time_step = Decimal('0.1')

height = skytree_height

while height > 0:
    velocity = Decimal(str(g*time))
    height = Decimal(str(skytree_height + g*time**2/2))
    print("t = " + str(time) + " [s], h = " + str(height) + " [m], v = " + str(abs(velocity)) + " [m/s]")
    time += time_step