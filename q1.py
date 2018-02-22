# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:51:04 2017

@author: Matthew
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

def nsphere(samples, d):
    """
    Calculates volume of a d dimensional sphere
    """
    n = 0 #inside sphere
    xs = [0]*d #dimensional array
    for i in range(samples):
        Rsum = 0 
        dxs = [rand.uniform(-1,1) for j in range(d)] #incremental lengths
        for j in range(d):
            if abs(xs[j] + dxs[j]) < 1:
                xs[j] = xs[j] + dxs[j]
            Rsum += np.power(xs[j], 2)
            R = np.sqrt(Rsum)
        
        if R <= 1:
            n += 1

    a = (np.power(2, d)*n)/samples
    return a

        
def main():
    d = 7
    sampleSet = [500, 1000, 10000, 20000, 35000, 50000, 75000, 90000]
    avgA = []
    for sample in sampleSet:
        sumA = 0
        for i in range(10):
            sumA += nsphere(sample, d)
        sumA = sumA/10
        avgA.append(sumA)
        
    exp = (16/105.)*np.power(np.pi, 3)
    residuals = []
    for i in range(len(sampleSet)):
        residuals.append(avgA[i] - exp)
    
    fig1 = plt.figure(1)
    frame1=fig1.add_axes((0.05,.3,0.9,.6))
    expected, =  plt.plot((0,100000), (exp, exp), '-k')
    data, = plt.plot(sampleSet, avgA, '*b')
    plt.grid()

    frame1.set_xticklabels([])
    plt.title("Estimation of Volume of 7 Dimensional Unit Sphere",fontsize=24)
    plt.ylabel("Volume",fontsize=24)
    plt.legend([expected,data],["Expected Volume","Monte Carlo Volume"],
               loc=4,fontsize=24)
    
    
    frame2=fig1.add_axes((0.05,.1,0.9,.17))
    plt.plot(sampleSet, residuals, '-k')
    plt.grid()
    plt.ylabel("Residuals",fontsize=24)
    plt.show()
    
main()

    
    