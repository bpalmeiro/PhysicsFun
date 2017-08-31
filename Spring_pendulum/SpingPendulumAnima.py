# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:24:38 2015

@author: brais
"""

import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as inte
from matplotlib import animation

N = 1000
t = np.linspace(0.,25.,N)

L0 = 1.
k = 3.5
m = 0.2
g = 9.8

def fun(var,t):
    theta,X,L,Y = var
    dthetadt = X
    dXdt = -1./(L+L0)*(g*np.sin(theta)+2*Y*X)
    dLdt = Y
    dYdt =(L+L0)*X**2-k/m*L+g*np.cos(theta)
    return [dthetadt,dXdt,dLdt,dYdt]
    

    
sol = inte.odeint(fun,[0.3,0.,1.,0.],t,full_output=True)

theta = sol[0][:,0]
X = sol[0][:,1]
L = sol[0][:,2]
Y = sol[0][:,2]


x = (L+L0)*np.sin(theta)
y = - (L+L0)*np.cos(theta)



fig, ax = plt.subplots(figsize=(5,5))

ax.set_ylim([-2, -1])
ax.set_xlim([1, -1])

animax, = ax.plot([], [])
xa,ya = [],[]

def data_gen():
    cnt = -1
    while cnt < N-1:
        cnt += 1
        yield x[cnt],y[cnt]
    
        

def update(data): 
    xa.append(data[0])
    ya.append(data[1])
    animax.set_data(xa, ya)
    return animax,

anim = animation.FuncAnimation(fig, update, data_gen,repeat=False,interval = 5, blit = True)

plt.show()




