import numpy as np
import matplotlib.pyplot as plt
array_1x3 = np.arange(0,3)
#AVD-C1 I can change the shape of an array
array_4x3 = np.arange(0,12).reshape(4,3)
print(array_4x3)
#AVD-C2: print the data type
print(array_1x3.dtype)
#AVD-C3: add a 1x3 and 4x3 matrix to make a new 4x3 matrix
array_C3 = array_1x3 + array_4x3
print(array_C3)
#AVD-C5: apply a mask to an array
mask = np.zeros(array_4x3.shape, dtype=bool)
mask[2,1] = True
masked_array = np.ma.masked_array(array_4x3, mask)
print(masked_array)
#AVD-C7: calculate the mean of an array
print(np.mean(array_4x3))
#AVD-C8: append an array on an array
new_array = np.arange(3,10)
appended_array = np.append(array_1x3, new_array)
print(appended_array)
#AVD-C4: fancy indexing to pull the fourth, last and second elements of a numpy
#array
array_4_last_2 = np.array([appended_array[3],appended_array[-1],
                          appended_array[1]])
print(array_4_last_2)
#AVD-B3: Plot a sine function
angles = np.arange(0,2*np.pi,0.1)
sine_func = np.sin(angles)
plt.plot(angles,sine_func)
plt.savefig('AVD:B3')
