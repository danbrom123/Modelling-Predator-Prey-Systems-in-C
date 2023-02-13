#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:15:25 2016

@author: danielbromley
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

filename = "output5.txt" 
print filename

def datacollector(filename):
    if filename.endswith('.txt'): # this checks the file is a tx file, as the c code only produces
                                  # .txt files
        pass
    else:
        sys.exit('filetype not txt')
    try:
        with open(filename, 'r') as datafile:
            
            data = np.genfromtxt(datafile,delimiter=' ',skip_header=5,filling_values="nan")
        
    except IOError:
        sys.exit("There has been an issue locating the file - '{}' - please check file is in correct location".format(filename))

    return data

def constantfinder(filename): #finds the constants from the preamble of the txt file
    with open(filename, 'r') as file:
        lines = [line.split() for line in file]
        consts = lines[3]

    alpha = float(consts[2])
    beta = float(consts[5])
    delta = float(consts[8])
    gamma = float(consts[11])
    kappa = 0.0
    lambd = 0.0
    for i in consts: #This part was added later as the old code didnt encorporate kappa or lambda values
        if i == "kappa" or i == "lambda":
            kappa = float(consts[14])
            lambd = float(consts[17])
        
    
    return alpha, beta, delta, gamma, kappa, lambd

def initialpop(filename): #find the initial population values from the preamble of the txt file
    with open(filename, 'r') as file:
        lines = [line.split() for line in file]
        initpop = lines[2]

    prey = initpop[3]
    pred = initpop[7]

    return prey, pred

def timeint(filename): #finds the time step and iteration amount from the preamble of the txt file
    with open(filename, 'r') as file:
        lines = [line.split() for line in file]
        timeint = lines[1]
        nint = lines[0]

        n = nint[4]
        dt = float(timeint[3])

    return dt, n

xpop = datacollector(filename)[:,0]
ypop = datacollector(filename)[:,1]
print "Final prey pop = {}\nFinal predator pop = {}".format(xpop[-1],ypop[-1])
t = datacollector(filename)[:,2]
alpha, beta, delta, gamma, kappa, lambd = constantfinder(filename)
dt, n = timeint(filename)
prey, pred = initialpop(filename)
txt = 'initial prey population = {}\ninitial predator population = {}\nalpha = {}\nbeta = {}\ndelta = {}\ngamma = {}\nkappa = {}\nlambda = {}\nn = {}\ndt = {}'.format(prey,pred,alpha,beta,delta,gamma,kappa,lambd,n,dt)

if float(kappa) == float(0.0) and float(lambd) == float(0.0):
    txt = 'initial prey population = {}\ninitial predator population = {}\nalpha = {}\nbeta = {}\ndelta = {}\ngamma = {}\nn = {}\ndt = {}'.format(prey,pred,alpha,beta,delta,gamma,n,dt)


#plots the graphs 
plt.plot(t, xpop, label = "Prey population")
plt.plot(t, ypop, label = "Preditor population")
plt.legend(loc='upper right')
plt.xlim(0,t[len(t)-1]+1)
a = plt.ylim(0)
plt.text(((t[len(t)-1]+1)*1.02),a[1]/2.1,txt,bbox=dict(facecolor='none', edgecolor='black'))
plt.ylabel("population number")
plt.xlabel("time")
plt.show()

plt.plot(xpop,ypop)
plt.ylabel("Preditor")
plt.xlabel("Prey")
plt.ylim(0)
plt.xlim(0)
plt.show()