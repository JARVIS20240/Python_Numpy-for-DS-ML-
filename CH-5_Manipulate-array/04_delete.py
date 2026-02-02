import numpy as np

"""
np.delete(array, index, axis = None) -> give copy of array
"""
arr1 = np.array([[10,20],[30,40]])
print(arr1)
new = np.delete(arr1, 0, axis=None)
print(new)
