# -*- coding: utf-8 -*-
"""
Code to do a litle toy animation based on a finite 2D Ising model
Next step: buliding an list free (online) animation in order to reduce the RAM
usage

Important: Fix SAVING bug, package missing?

@author: Brais Palmeiro Pazos
@date: 13/10/2016
"""

####### IMPORTS

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

###### SYSTEM PARAMETERS

N = 200
Ti = 0.5

# Number of steps (~time)
N_steps = 10000000


def compute_energy(system):
    row, column = system.shape
    E = 0.
    count = 0
    for i in range(row):
        for j in range(column):
            if i<row-1 and j<column-1:
                E += -system[i][j]*(system[(i+1)%row][j]+system[i][(j+1)%column]+system[(i-1)%row][j]+system[i][(j-1)%column])/2
    return E

def change_energy(row, column,system):
    rows,columns = system.shape
    energy = system[row][column]*(system[(row+1)%rows][column]+system[row][(column+1)%columns]+system[(row-1)%rows][column]+system[row][(column-1)%columns])*2
    return energy

fig = plt.figure()
ims = []
probability = {}
pos_energies = np.array([-8, -4, -6, -2, 0, 2, 6, 4, 8])
for energy in pos_energies:
    probability[energy] = np.exp(-energy/float(Ti))


system = np.random.choice([1,-1],[N,N])
im = plt.imshow(system, interpolation='nearest', animated=True)
ims.append([im])

for step in np.arange(N_steps):
    if not step%(N_steps/1000.):
        im = plt.imshow(system, interpolation='nearest', animated=True)
        ims.append([im])
    if not step%(N_steps/10.):
        print 100.*step/N_steps,'%'
    column=np.random.randint(0,N-1)
    row=np.random.randint(0,N-1)
    deltaE = change_energy(row,column,system)
    if deltaE>0:
        if probability[energy]>np.random.random():
            system[row][column] *= -1
    else:
        system[row][column] *= -1

ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True,
                                repeat_delay=1000)


#mywriter = animation.FFMpegWriter()
#ani.save('2D_Ising.mp4')#,writer=mywriter,fps=30)
#ani.save('2D_Ising.mp4')


plt.show()
