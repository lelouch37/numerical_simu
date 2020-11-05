import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def strogatz(t, x):
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

ts = 0
tf = 50
n = 3000

sol = integrate.solve_ivp(strogatz, [ts, tf], x0, method="RK45", dense_output=True)
fig = plt.figure()
t = np.linspace(ts, tf, n)
z = sol.sol(t)
plt.plot(t, z.T)
plt.xlabel('t')
plt.legend(['x', 'y'])
plt.title('Runge–Kutta')
plt.show()
fig.savefig("strogatz.png")