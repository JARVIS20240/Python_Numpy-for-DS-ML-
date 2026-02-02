import numpy as np 
"""
Fill Misiinsg values with nan_to_num() function
np.nan_to_num(array, nan=Value)
"""
arr = np.array([1,2,np.nan,3,4,np.nan,6])

print(np.nan_to_num(arr, nan=1))