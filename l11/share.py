import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def share(t, x): 
    f = np.zeros_like(x)
    gamma = 0.08
    xinf = follower*100
    f[0] = gamma*(1-x[0]/xinf)*x[0]
    return f

x0 = np.zeros(1)
follower = 1000
x0[0] = follower*0.3

syear = 0
eyear = 120
n = 3000

methods = ['RK45','Radau']

for s in methods:
    sol = integrate.solve_ivp(share, [syear, eyear], x0, method=s, dense_output=True)
    t = np.linspace(syear, eyear, n)
    z = sol.sol(t)
    plt.plot(t, z.T)
    plt.legend(['N'])
    plt.title(s)
    plt.xlabel("time[sec]")
    plt.ylabel("share")
    plt.show()
    plt.savefig("share_" + s + ".png")