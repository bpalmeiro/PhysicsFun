# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 18:15:32 2014

@author: Brais Palmeiro Pazos
"""


import numpy as np
import matplotlib.pylab as plt
import scipy.integrate as inte
from matplotlib import animation
from mpl_toolkits.mplot3d.axes3d import Axes3D



def fun(var,t):
    x,y,z = var
    dxdt = 10*(y-x)
    dydt = 28*x - y - x*z
    dzdt = x*y - 8./3.*z
    return [dxdt,dydt,dzdt]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.azim = 45
ax.elev = 45
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_xticklabels('')
ax.set_yticklabels('')
ax.set_zticklabels('')
linea, = ax.plot([], [], [],lw = 0.5)
ax.set_xlim(-10,10)
ax.set_ylim(-20,20)
ax.set_zlim(0,50)


def anima(i):
    t = np.arange(0, (i + 1) / 10., 0.01) 
    sol = inte.odeint(fun,[5.,5.,5.],t,full_output=True)
    x = sol[0][:,0]
    y = sol[0][:,1]
    z = sol[0][:,2]                       
    ax.elev = 45 + i / 2.                 
    ax.azim = 45 + i / 2.                
    linea.set_data(x, y)                  
    linea.set_3d_properties(z)
    return linea,
anim = animation.FuncAnimation(fig, anima, frames = 500,interval = 1, blit = True,repeat=True)
plt.show()
