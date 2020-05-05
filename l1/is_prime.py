# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:40:24 2020

@author: Owner
"""

def is_prime(x) :
    for num in range(2, x):
        if x % num == 0:
            return False
            break
    else:
        return True