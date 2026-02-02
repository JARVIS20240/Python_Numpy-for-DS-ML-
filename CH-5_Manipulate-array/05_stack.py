import numpy as np

"""
np.vstack(array1,array2) = row wise stack
np.hstack(array1,array2) = column wise stack
"""

arr1 = np.array([[10,20,30],[40,50,60]])
arr2 = np.array([[40,50,60],[10,20,30]])

print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))