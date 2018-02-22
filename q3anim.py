# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:38:47 2017

@author: Matthew
"""

import random as rand
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib import animation

            
def dU(i, j, array, length):
    m = length-1
    #print("i, j: ", str(i) + ', ' + str(j))
    #PBC
    if i == 0: #top row
        top = array[m,j]
    else: 
        top = array[i-1,j]
        
    if i == m: #bottom row
        bottom = array[0,j]
    else:
        bottom = array[i+1,j]
        
    if j == 0: #first element in row
        left = array[i,m]
    else:
        left = array[i,j-1]
    
    if j == m: #last element in row
        right = array[i,0]
    else:
        right = array[i,j+1]
        
    return 2.*array[i,j]*(top+bottom+left+right) #local magnetization
    
#-------------

T = 2.2
length = 100
array = np.zeros((length,length),dtype=int)

def init():
    for i in range(0, length): #rows
        for j in range(0, length): #cells in rows
            array[i,j] = rand.choice([1,-1])
init()

plt.ioff()
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Array Size: " + str(length) + ", T = " + str(T))
    
cmap = colors.ListedColormap(['white','black'])
bounds = [-1,0,1]
norm = colors.BoundaryNorm(bounds, cmap.N)
    
img = plt.imshow(array, interpolation='nearest',cmap=cmap,norm=norm, animated=True)

def update(*args):
    for z in range(10*length**2):
        i = rand.randint(0,length-1)
        j = rand.randint(0,length-1)
        
        deltaU = dU(i, j, array, length)
        
        if deltaU <= 0:
            array[i,j] = -array[i,j]
        else:
            if rand.uniform(0,1) < np.exp(-deltaU/T):
                array[i,j] = -array[i,j]
    img.set_array(array)
    return img,

ani = animation.FuncAnimation(fig, update, interval=50, blit=True)
ani.save("attempt_5.mp4", fps=10, extra_args=['-vcodec','libx264'])
       



