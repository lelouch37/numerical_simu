import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def lotka_volterra(t, x):
    '''
    dx/dt = ax - bxy
    dy/dt = cxy - dy
    x: 被食者(食べられる側)の個体数
    y: 捕食者(食べる側)の個体数
    a: xが増える割合
    b: xが食べられて減る割合
    c: xを食べてyが増える割合
    d: xを食べられずにyが減る割合
    '''
    a = 0.9
    b = 0.05
    c = 0.02
    d = 0.3
    f = np.zeros_like(x)
    f[0] = a*x[0] - b*x[0]*x[1]
    f[1] = c*x[0]*x[1] - d*x[1]
    return f

x0 = np.zeros(2)
x0[0] = 100
x0[1] = 15

ts = 0
tf = 100
n = 3000

sol = integrate.solve_ivp(lotka_volterra, [ts, tf], x0, method="RK45", dense_output=True)
fig = plt.figure()
t = np.linspace(ts, tf, n)
z = sol.sol(t)
plt.plot(t, z.T)
plt.xlabel('x')
plt.legend(['x', 'y'])
plt.title('Runge–Kutta lotka-volterra')
plt.show()
fig.savefig("lotka_volterra1.png")