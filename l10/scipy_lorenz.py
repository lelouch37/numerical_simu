import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def lorenz(t, x): 
    '''
    ローレンツ方程式:
    dx/dt = -10x + 10y	
    dy/dt = 28x - y - xz
    dz/dt = -8/3z + xy
    '''
    f = np.zeros_like(x)
    f[0] = -10*x[0] + 10*x[1]
    f[1] = 28*x[0] - x[1] - x[0]*x[2]
    f[2] = -8/3*x[2] + x[0]*x[1]
    return f

x0 = np.zeros(3)
x0[0] = 1
x0[1] = 0.5
x0[2] = 0.5

ts = 0
tf = 100
n = 3000

methods = ['RK23','RK45','LSODA','BDF','Radau']

for s in methods:
    sol = integrate.solve_ivp(lorenz, [ts, tf], x0, method=s, dense_output=True)
    t = np.linspace(ts, tf, n)
    z = sol.sol(t)
    plt.subplot(3, 2, methods.index(s)+1)
    plt.plot(t, z.T)
    plt.legend(['x', 'y', 'z'])
    plt.title(s)
    
plt.savefig("lorenz.png")