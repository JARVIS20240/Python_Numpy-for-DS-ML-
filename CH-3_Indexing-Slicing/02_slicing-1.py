# slicing: 
""" 
array[start:stop:step]
"""

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[1:5])
print(arr[:3])
print(arr[::2])
print(arr[::-1])
print(arr[[0,2,3]])