# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:47:12 2017

@author: Matthew
"""

import random as rand
import numpy as np
import matplotlib.pyplot as plt

def func(y):
    return np.power(np.sin(1/y), 2)
    
def integrate(samples, upper):
    n = 0
    xmax = upper
    ymax = 1
    for i in range(samples):
        
        xr = rand.uniform(0,xmax)
        yr = rand.uniform(0,ymax)
        if yr <= func(xr):
            n += 1
    return ymax*xmax*(n/samples)
    
def main():
    
    X = np.linspace(0,1,1000)
    Y = []
    for x in X:
        Y.append(integrate(10000,x))
    
    plt.plot(X,Y)
    plt.title("Monte Carlo Integrated Function", fontsize=24)
    plt.ylabel("f(x)", fontsize=24)
    plt.xlabel("x", fontsize=24)
    
main()
    
    
    
    
    
    



        
        
    