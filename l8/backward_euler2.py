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

R = 1000
L = 100
C = 0.001

def f( t, x ):
    E = 100*np.sin(t)
    f = np.zeros_like(x)
    f[0] = x[1]
    f[1] = -1/(L*C)*x[0] - R/L*x[1] + 1/L*E
    return f

def Df( t, p ):
    Dfp = np.zeros((len(p), len(p)))
    Dfp[0][0] = 0
    Dfp[0][1] = 1
    Dfp[1][0] = -1/(L*C)
    Dfp[1][1] = -R/L
    return Dfp

x0 = np.zeros(2)
x0[0] = -5
x0[1] = 0

t, x = backward_euler(x0, 0.1, 10, f, Df)
#q = x[0]
#i = x[1]
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("q,i")
plt.title("backward euler")
plt.show()
fig.savefig("RLC.png")