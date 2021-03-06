import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def population(t, x): 
    '''
    マルサスモデル
    dx/dt = gamma*x
    '''
    f = np.zeros_like(x)
    gamma = 0.03
    f[0] = gamma*x[0]
    return f

x0 = np.zeros(1)
x0[0] = 5500

syear = 1920
eyear = 2008
n = 3000

methods = ['RK45','Radau']

for s in methods:
    sol = integrate.solve_ivp(population, [syear, eyear], x0, method=s, dense_output=True)
    t = np.linspace(syear, eyear, n)
    z = sol.sol(t)
    plt.subplot(2, 1, methods.index(s)+1)
    plt.plot(t, z.T)
    plt.legend(['N'])
    plt.title(s)
    
plt.savefig("malthusian.png")