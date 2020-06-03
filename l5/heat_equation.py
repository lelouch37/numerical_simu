# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 09:31:18 2020

@author: Owner
"""


import numpy as np
from scipy import linalg

n = 20

A = np.zeros([n, n])
A_diag = np.full(n, -2)
A_diag[0] = A_diag[n-1] = 1
A = np.diag(A_diag)
A_diag_1 = np.full(n-1, 1)
A_diag_1[0] = 0
A += np.diag(A_diag_1, k = 1)
A_diag_1[0] = 1
A_diag_1[n-2] = 0
A += np.diag(A_diag_1, k = -1)

b = np.zeros([n, 1])
b[0] = 10

x = linalg.solve(A, b)