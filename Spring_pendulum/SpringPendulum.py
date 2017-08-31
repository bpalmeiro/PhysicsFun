# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 18:32:06 2014

@author: Brais Palmeiro Pazos
"""

import numpy as np
import matplotlib.pylab as plt
#import scipy.optimize as sop
import scipy.integrate as inte


t = np.linspace(0.,25.,10000)

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

#print sol[1]['message']

theta = sol[0][:,0]
X = sol[0][:,1]
L = sol[0][:,2]
Y = sol[0][:,2]


x = (L+L0)*np.sin(theta)
y = - (L+L0)*np.cos(theta)


plt.plot(x,y)
plt.show()
