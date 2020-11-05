#RLC回路
#Ld^2q/dt^2+Rdq/dt+1/C*q=e(t)
#x1=q,x2=dq/dt=i
#=> dx1/dt=x2, dx2/dt=1/L(-1/C*x1-R*x2+e(t))

import numpy as np
import matplotlib.pyplot as plt

def f(t, x):
    R = 1000
    L = 100
    C = 0.001
    E = 100*np.sin(t)
    f = np.zeros_like(x)
    f[0] = x[1]
    f[1] = -1/(L*C)*x[0] - R/L*x[1] + 1/L*E
    return f

def euler(x0, f, t_start, t_end, dt):
    x = x0
    x_list = [x0]
    t = t_start
    t_list = [t_start]
    while t < t_end:
        x = x + dt*f(t, x)
        t += dt
        x_list.append(x)
        t_list.append(t)
        
    return (t_list, x_list)

t_start = 0
t_end = 20
dt = 0.01        #dt = t_i+1 - t_i

x0 = np.zeros(2)
x0[0] = -5
x0[1] = 0
        
t, x = euler(x0, f, t_start, t_end, dt)
#q = x[0]
#i = x[1]
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("q,i")
plt.title("euler")
plt.show()
fig.savefig("RLC2-2.png")