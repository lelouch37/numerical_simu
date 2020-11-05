import numpy as np
from scipy import linalg

def newton(x, f, Df, cond):
    i = 0
    while True:
        # Newton method
        DFinv_Fx = linalg.solve(Df(x), f(x))
        x = x - DFinv_Fx 
        
        if cond(i, x, DFinv_Fx):
            break
        i += 1
    return x


def f(x):
    fx = np.zeros((len(x), 1))
    fx[0] = 2*(x[0]**2) - np.exp(x[1])
    fx[1] = -3*(x[0]*(x[1]**2)) - x[1]**3 - 3
    return fx

def Df(p):
    Dfp = np.zeros((len(p), len(p)))
    Dfp[0][0] = 4*(p[0])
    Dfp[0][1] = -np.exp(p[1])
    Dfp[1][0] = -3*(p[1]**2)
    Dfp[1][1] = -6*(p[0]*p[1]) - 3*(p[1]**2)
    return Dfp

def cond(i, x, DFinv_Fx):
    # Callback function
    return np.max(np.abs(DFinv_Fx)) <= 10**(-14)