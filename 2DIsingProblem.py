# -*- coding: utf-8 -*-
"""
Code to do compute some variables of a ferromagnetic system based on a finite 2D Ising model for different
temperatures, sampling amount of events and system size. The final output are these variables (Energy,
Magnetization and Specific Heat) plots

There may be some buggs in magnitude computation

@author: Brais Palmeiro Pazos
@date: 13/10/2016
"""


####### IMPORTS

import matplotlib.pyplot as plt
import numpy as np



###### SYSTEM PARAMETERS


# Constants
N_VALUES = [10, 50, 100] # Values for N
N_WAIT_VALUES = [10000, 100000] # Steps to let the system ''relax'' to the important states
N_SAMPLES_VALUES = [1000, 10000] # This is every how many steps we keep the values of the energy and magnetization

# Temperature (units:)
T = np.linspace(0.2,4.0,20,endpoint=True)


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

Energy = {}
Magnetization = {}
pos_energies = np.array([-8, -4, -6, -2, 0, 2, 6, 4, 8])
probability = {}
MeanVariables = {}

for N in N_VALUES:
    print '='*70
    print 'N',N
    print '='*70

    Energy[N] = {}
    Magnetization[N] = {}
    MeanVariables[N] = {}
    for Ti in T:
        print '*'*70
        print 'T',Ti
        print '*'*70
        for energy in pos_energies:
            probability[energy] = np.exp(-energy/float(Ti))
        Energy[N][Ti] = {}
        Magnetization[N][Ti] = {}
        MeanVariables[N][Ti] = {}
        system = np.random.choice([1,-1],[N,N])

        for i in np.arange(2):
            print 'NSamples = ',N_SAMPLES_VALUES[i]
            Energy[N][Ti][N_SAMPLES_VALUES[i]] = np.array([])
            Magnetization[N][Ti][N_SAMPLES_VALUES[i]] = np.array([])
            MeanVariables[N][Ti][N_SAMPLES_VALUES[i]] = {}

            print 'Stabilizing...'
            for wait in np.arange(0*N_WAIT_VALUES[i]):
                column = np.random.randint(0,N-1)
                row = np.random.randint(0,N-1)
                deltaE = change_energy(row,column,system)
                if deltaE>0:
                    if probability[energy]>np.random.random():
                        system[row][column] *= -1
                else:
                    system[row][column] *= -1

            print 'Sampling...'

            total_energy = compute_energy(system)
            for sample in np.arange(N_SAMPLES_VALUES[i]):
                column = np.random.randint(0,N-1)
                row = np.random.randint(0,N-1)
                deltaE = change_energy(row,column,system)
                if deltaE>0:
                    if probability[energy]>np.random.random():
                        system[row][column] *= -1
                        total_energy += deltaE
                else:
                    system[row][column] *= -1
                    total_energy += deltaE
                Energy[N][Ti][N_SAMPLES_VALUES[i]] = np.concatenate((Energy[N][Ti][N_SAMPLES_VALUES[i]],[total_energy]))
                Magnetization[N][Ti][N_SAMPLES_VALUES[i]] = np.concatenate((Magnetization[N][Ti][N_SAMPLES_VALUES[i]],[system.sum()]))


            MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['E'] = np.mean(Energy[N][Ti][N_SAMPLES_VALUES[i]])/(N*N)
            MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['E2'] = np.mean(np.power(Energy[N][Ti][N_SAMPLES_VALUES[i]],2))
            MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['M'] = np.mean(Magnetization[N][Ti][N_SAMPLES_VALUES[i]])/(N*N)
            MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['Cv'] = (MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['E']**2+MeanVariables[N][Ti][N_SAMPLES_VALUES[i]]['E2'])/(Ti*2)/(N*N)


# Energy
E = {}
M = {}
Cv = {}
for Ns in N_SAMPLES_VALUES:
    E[Ns] = {}
    M[Ns] = {}
    Cv[Ns] = {}
    for N in N_VALUES:
        E[Ns][N] = np.array([])
        M[Ns][N] = np.array([])
        Cv[Ns][N] = np.array([])
        for Ti in T:
            E[Ns][N] = np.concatenate([E[Ns][N],[ MeanVariables[N][Ti][Ns]['E']]])
            M[Ns][N] = np.concatenate([M[Ns][N],[ MeanVariables[N][Ti][Ns]['M']]])
            Cv[Ns][N] = np.concatenate([Cv[Ns][N],[ MeanVariables[N][Ti][Ns]['Cv']]])

plt.figure(1)
plt.subplot(311)
plt.plot(T,E[1000][10])
plt.plot(T,E[1000][50])
plt.plot(T,E[1000][100])
plt.subplot(312)
plt.plot(T,M[1000][10])
plt.plot(T,M[1000][50])
plt.plot(T,M[1000][100])
plt.subplot(313)
plt.plot(T,Cv[1000][10])
plt.plot(T,Cv[1000][50])
plt.plot(T,Cv[1000][100])

plt.figure(2)
plt.subplot(311)
plt.plot(T,E[10000][10])
plt.plot(T,E[10000][50])
plt.plot(T,E[10000][100])
plt.subplot(312)
plt.plot(T,M[10000][10])
plt.plot(T,M[10000][50])
plt.plot(T,M[10000][100])
plt.subplot(313)
plt.plot(T,Cv[10000][10])
plt.plot(T,Cv[10000][50])
plt.plot(T,Cv[10000][100])

plt.show()
