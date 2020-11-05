import numpy as np
import matplotlib.pyplot as plt

def heun(x0, f, dt, tf):
    ti = 0
    xi = x0
    tlist = [ti]
    xlist = [x0]
    while ti < tf:
        tip1 = ti + dt
        # 前進オイラー法
        xip1 = xi + dt*f(ti, xi)
        xip1 = xi + dt/2*(f(ti, xi) + f(tip1, xip1))
        
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
        
    return tlist, xlist

def f(t, x):
    a = 4
    b = -8
    c = 10
    d = -5
    f = np.zeros_like(x)
    f[0] = a*x[0] + b*x[1]
    f[1] = c*x[0] + d*x[1]
    return f

x0 = np.zeros(2)
x0[0] = -7
x0[1] = 5

t, x = heun(x0, f, 0.1, 10)
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("X,Y")
plt.title("heun")
plt.show()
fig.savefig("strogatz1.png")