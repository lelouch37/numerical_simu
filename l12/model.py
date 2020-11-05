import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def model(t, x): 
    '''
    dx1/dt = a1x1 - b1x1y
    dx2/dt = a2x2 - b2x2y
    dy/dt = c1x1y + c2x2y - dy
    x1: 被食者1(食べられる側)の個体数
    x2: 被食者2(食べられる側)の個体数
    y: 捕食者(食べる側)の個体数
    a1: x1増える割合
    a2: x2が増える割合
    b1: x1が食べられて減る割合
    b2: x2が食べられて減る割合
    c1: x1を食べてyが増える割合
    c2: x2を食べてyが増える割合
    d: x1もx2も食べられずにyが減る割合
    '''
    a1 = 0.9
    a2 = 0.8
    b1 = 0.03
    b2 = 0.025
    c1 = 0.01
    c2 = 0.01
    d = 0.25
    f = np.zeros_like(x)
    f[0] = a1*x[0] - b1*x[0]*x[2]
    f[1] = a2*x[1] - b2*x[1]*x[2]
    f[2] = c1*x[0]*x[2] + c2*x[1]*x[2] - d*x[2]
    return f

x0 = np.zeros(3)
x0[0] = 200
x0[1] = 100
x0[2] = 10

stime = 0
etime = 100
n = 3000

methods = ['RK45','Radau']

for s in methods:
    sol = integrate.solve_ivp(model, [stime, etime], x0, method=s, dense_output=True)
    t = np.linspace(stime, etime, n)
    z = sol.sol(t)
    plt.plot(t, z.T)
    plt.legend(['x1', 'x2', 'y'])
    plt.title(s)
    plt.xlabel("time")
    plt.ylabel("number")
    plt.show()
    plt.savefig(s + ".png")