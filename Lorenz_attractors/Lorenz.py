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


t = np.linspace(0.,20.,10000)

def fun(var,t):
    x,y,z = var
    dxdt = 10*(y-x)
    dydt = 28*x - y - x*z
    dzdt = x*y - 8./3.*z
    return [dxdt,dydt,dzdt]
    

    
sol = inte.odeint(fun,[5.,5.,5.],t,full_output=True)

print sol[1]['message']

x = sol[0][:,0]
y = sol[0][:,1]
z = sol[0][:,2]


fig=plt.figure( )
fig.subplots_adjust(bottom=0.05 , left=0.06 , top =0.975 , right =0.97)

plt.subplot(2,1,1)
plt.suptitle('y vs x',fontsize=18)
plt.plot(x,y)

plt.subplot(2,1,2)
plt.plot(x,z)
plt.suptitle('z vs x',fontsize=18)

plt.show()
