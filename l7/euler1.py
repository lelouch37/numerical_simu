#Strogatz
#dx1/dt = ax1 + bx2
#dx2/dt = cx1 + dx2
#x1(0) = x1_0, x2(0) = x2_0

import numpy as np
import matplotlib.pyplot as plt

#f = dx/dt = [[dx1/dt], [dx2/dt]]
def f(x):
    a = 4
    b = -8
    c = 10
    d = -5
    f = np.zeros_like(x)
    f[0] = a*x[0] + b*x[1]
    f[1] = c*x[0] + d*x[1]
    return f

def euler(x0, f, t_start, t_end, dt):
    x = x0
    x_list = [x0]
    t = t_start
    t_list = [t_start]
    while t < t_end:
        x = x + dt*f(x)
        t += dt
        x_list.append(x)
        t_list.append(t)
        
    return (t_list, x_list)

t_start = 0
t_end = 10
dt = 0.1        #dt = t_i+1 - t_i

x0 = np.zeros(2)
x0[0] = -7
x0[1] = 5
        
t, x = euler(x0, f, t_start, t_end, dt)
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("X,Y")
plt.title("euler")
plt.show()
fig.savefig("strogatz.png")