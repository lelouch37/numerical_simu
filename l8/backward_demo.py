import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

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

def cond(i, x, DFinv_Fx):
    # Callback function
    return np.max(np.abs(DFinv_Fx)) <= 10**(-14)

# Dfを追加!
def backward_euler(x0, tau, tf, f, Df):
    ti = 0
    xi = x0
    tlist = [ ti ]
    xlist = [ x0 ]
    I = np.eye(len(x0))
    while ti < tf:
        tip1 = ti + tau
        xip1 = newton( xi, (lambda x: x - (xi + tau*f(tip1,x))), (lambda x :I - tau*Df(tip1, x)), cond )
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
    
    return (tlist, xlist)

a = 4
b = -8
c = 10
d = -5

def strogatz( t, x ):
    fx = np.zeros_like(x)
    fx[0] = a*x[0]+b*x[1]
    fx[1] = c*x[0]+d*x[1]
    return fx

def strogatzDf( t, p ):
    Dfp = np.zeros((len(p), len(p)))
    Dfp[0][0] = a
    Dfp[0][1] = b
    Dfp[1][0] = c
    Dfp[1][1] = d
    return Dfp

x0 = np.zeros(2)
x0[0] = -7
x0[1] = 5

t, x = backward_euler(x0, 0.1, 10, strogatz, strogatzDf)
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("X,Y")
plt.title("backward euler")
plt.show()
fig.savefig("strogatz_demo.png")