import numpy as np
import matplotlib.pyplot as plt

def heun(x0, f, tf, acc):
    ti = 0
    xi = x0
    tlist = [ti]
    xlist = [x0]
    dt = 1
    while ti < tf:
        while True:
            tip1 = ti + dt
            # 前進オイラー法
            xip1_euler = xi + dt*f(ti, xi)
            # ホイン法
            xip1 = xi + dt/2*(f(ti, xi) + f(tip1, xip1_euler))
            if np.max(np.abs((xip1_euler - xip1) / xip1))< acc:
                dt *= 4
                break
            dt /= 4
            
        tlist.append(tip1)
        xlist.append(xip1)
        ti, xi = tip1, xip1
        
    return tlist, xlist

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

'''
初期値
x(0) = 1
y(0) = 0.5
z(0) = 0.5
'''
x0 = np.zeros(3)
x0[0] = 1
x0[1] = 0.5
x0[2] = 0.5

t, x = heun(x0, lorenz, 20, 10**(-5))
fig = plt.figure()
plt.plot(x[1], x[2])
plt.xlabel("Y")
plt.ylabel("Z")
plt.title("heun lorenz")
plt.show()
fig.savefig("lorenz_YZ.png")