# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:28:31 2017

@author: Matthew
"""

import random as rand
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

def init(array, length):
    for i in range(0, length): #rows
        for j in range(0, length): #cells in rows
            array[i,j] = rand.choice([1,-1])
            
def neighbors(i, j, array, length):
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
    
    return [top, bottom, left, right]
    
def others(i, j, array, length, r):
    if i+r > length-1:
        rowOther = array[i-r,j]
    else:
        rowOther = array[i+r,j]
        
    if j+r > length-1:
        colOther = array[i,j-r]
    else:
        colOther = array[i,j+r]
    
    return [rowOther,colOther]
    
def dU(i, j, array, length):
    nbs = neighbors(i, j, array, length)    
    return 2.*array[i,j]*(sum(nbs)) #local magnetization
    
  
def pairs(array, length, r):
    total = 0
    for i in range(0, length):
        for j in range(0, length):
            row = array[i,j]*others(i, j, array, length, r)[0]
            col = array[i,j]*others(i, j, array, length, r)[1]
            total = total + row + col
    return total/(2*length**2) #factor of 2 to remove double counting
            
def avgMag(array, length):
    total = 0
    for i in range(0, length):
        for j in range(0, length):
            total += array[i,j]
    return total/(length**2)
    
    
             
def plot(array):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    cmap = colors.ListedColormap(['white','black'])
    bounds = [-1,0,1]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    img = plt.imshow(array, interpolation='nearest',cmap=cmap,norm=norm)
    plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[-1,0,1])
    plt.show()
   


def main():
    T = 1
    length = 10
    array = np.zeros((length,length),dtype=int)
    init(array, length)

    #index = []
    cor = []
    for r in range(1, 3): #int(length/2)+1
        corTmp = 0
        count = 0
        #indexTmp=[]
        for z in range(300*length**2):
            '''
            if z%1000 == 0:
                corTmp.append(pairs(array, length, r) - (avgMag(array, length))**2)
                indexTmp.append(z)
            '''
            if z > 10000 and z%100 == 0:
                corTmp += pairs(array, length, r) - (avgMag(array, length))**2
                count += 1
            
            i = rand.randint(0,length-1)
            j = rand.randint(0,length-1)
        
            deltaU = dU(i, j, array, length)
        
            if deltaU <= 0:
                array[i,j] = -array[i,j]
            else:
                if rand.uniform(0,1) < np.exp(-deltaU/T):
                    array[i,j] = -array[i,j]
        
        corTmp = corTmp/count
        cor.append(corTmp)
        #index.append(indexTmp)
    '''
    r1, = plt.plot(index[0], cor[0])
    r2, = plt.plot(index[1], cor[1])
    r3, = plt.plot(index[2], cor[2])
    r8, = plt.plot(index[7], cor[7])
    r9, = plt.plot(index[8], cor[8])
    r14, = plt.plot(index[13], cor[13])
    r15, = plt.plot(index[14], cor[14])
    string = str(length)+"x"+str(length)+" array. T = "+str(T)
    plt.title(string,fontsize=28)
    plt.xlabel("Monte Carlo Time (iterations)",fontsize=24)
    plt.ylabel("Value of the Correlation Function",fontsize=24)
    plt.legend([r1,r2,r3,r8,r9,r14,r15],
               ["R=1","R=2","R=3","R=8","R=9","R=14","R=15"],
               loc=1,fontsize=20)
    plt.show()
    '''
    slope = (cor[1]-cor[0])
    it = cor[0] - slope*1
    corL = ((cor[0]/np.e)-it)/slope
    print(corL)

main()   

    
    
