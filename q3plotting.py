# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:20:46 2017

@author: Matthew
"""

import matplotlib.pyplot as plt


temps = [1, 2, 2.3, 2.5, 3, 4, 6]
A40 = [7.89,5.88,4.52,2.83,2.23,1.93,1.79]
A20 = [5.29,1.98,4.38,2.90,2.14,1.88,1.77]
A10 = [2.82,1.70,2.23,2.31,1.97,1.82,1.68]

p40, = plt.plot(temps, A40)
p20, = plt.plot(temps, A20)
p10, = plt.plot(temps, A10)
plt.title("Correlation Lengths of Monte Carlo 2D Ising Model", fontsize=28)
plt.xlabel("Unitless Temperature Values", fontsize=24)
plt.ylabel("Correlation Length (Grid Units)", fontsize=24)
plt.legend([p40,p20,p10],["40x40","20x20","10x10"], fontsize=24)
plt.show()