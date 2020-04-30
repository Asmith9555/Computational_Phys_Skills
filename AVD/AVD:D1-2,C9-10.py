#AVD-D2: Import pylab
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
#AVD-D1: Load data from a csv file with numpy
data = np.genfromtxt('Data.csv', delimiter=',', skip_header=1)
Angles = data[0:19,0]
coin_15m = data[0:19,1]
coin_30m = data[0:19,2]
#AVD-C10: 2D Scatter plot made from data read from a file
plt.scatter(Angles, coin_15m)
#AVD-C9: Add axis labels
plt.xlabel('Angles')
plt.ylabel('Coincidence at 15m')
plt.savefig('AVD:C10.png')
