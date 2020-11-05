import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def backward_euler(x0, f, t_start, t_end, dt):
    x = x0
    x_list = [x0]
    t = t_start
    t_list = [t_start]
    while t <= t_end:
        #newton法でF(x)=0を満たすxを求める
        #初期値はxi
        x = newton(x, F, dF, cond)
        t += dt
        x_list.append(x)
        t_list.append(t)
        
    return (t_list, x_list)

def newton(x, F, dF, cond):
    i = 0
    x_i = x
    while True:
        # Newton method
        DFinv_Fx = linalg.solve(dF(x), F(x, x_i))
        x = x - DFinv_Fx 
        
        if cond(i, x, DFinv_Fx):
            break
        i += 1
    return x

#F(x) = x - xt_i - dt*f(t_i+1, x)
def F(x, x_i):
    return x - x_i - dt*f(x)    


a = 4
b = -8
c = 10
d = -5
def dF(p):
    DFp = np.zeros((len(p), len(p)))
    DFp[0][0] = 1 - a*dt
    DFp[0][1] = -b*dt
    DFp[1][0] = -c*dt
    DFp[1][1] = 1 - d*dt
    return DFp
    
#Strogatz
#dx1/dt = ax1 + bx2
#dx2/dt = cx1 + dx2
#f = dx/dt = [[dx1/dt], [dx2/dt]]
def f(x):
    f = np.zeros_like(x)
    f[0] = a*x[0] + b*x[1]
    f[1] = c*x[0] + d*x[1]
    return f

def cond(i, x, DFinv_Fx):
    # Callback function
    return np.max(np.abs(DFinv_Fx)) < 10**(-14)

t_start = 0
t_end = 10
dt = 0.1        #dt = t_i+1 - t_i

x0 = np.zeros(2)
x0[0] = -7
x0[1] = 5

t, x = backward_euler(x0, f, t_start, t_end, dt)
fig = plt.figure()
plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("X,Y")
plt.title("backward euler")
plt.show()
fig.savefig("strogatz.png")