import numpy as np
array = np.arange(20).reshape(4,5)
#AVD-B1: using a mask to pull out elements less than 5 and greater than or equal
#to 7
new_array = np.append(array[array < 5],array[array >= 7])
print(new_array)
#AVD-C6: create structured array with dtype "fluid"
fluid = np.dtype([
 ('x', int),
 ('y', np.int64),
 ('rho', 'f8'),
 ('vel', 'f8'),
 ])
 #AVD-B2: Index a structured array with dtype fluid using a string matching the
 #name of a column
structured_array = np.array([(10, 10, 3.0, 1.2),
                              (20, 20, 9.0, 2.2),
                              (30, 30, 27, 3.2)],
                             dtype=fluid)
print(structured_array)
