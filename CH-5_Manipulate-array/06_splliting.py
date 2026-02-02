import numpy as np

"""
np.split(array, sections, axis = 0) = equal part split

np.vsplit() = vartical split (row wise)
np.hsplit(array, sections) = horizontal split (column wise)
"""

# np.split():
# 1D array:
arr = np.array([10,20,40,50,30,60,70,80])
print(arr)
print( np.split(arr, 2))

# 2D array:
arr_2 =np.array([ 
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(f"axis 0 ={np.split(arr_2, 2, axis=0)}") #Row wize split = 1234, 5678

# np.hsplit(): Column-wise Split -> inside axis = 1
arr_3 =np.array([ 
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(np.hsplit(arr_3, 2))
print(np.hsplit(arr_3, 4))

# np.vsplit() — Vertical split (row-wise) -> inside axis = 0
arr_4 = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])
print(np.vsplit(arr_4, 2))
print(np.vsplit(arr_4, 4))