import numpy as np

"""
np.insert(array, index, value, asix=None)
array = original array
index = insert data index
asix = None (data add in Flatten array)
2D array:-
asix = 0 (row wise data insert)
asix = 1 (columns wise data insert)
"""
import numpy as np 

# For 1D array
# arr = np.array([10,20,30,40,50])
# print(arr)
# new_arr = np.insert(arr, 3, 4000)
# print(new_arr)

# For 2D array
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2dr = np.insert(arr_2d, 1, [9, 10], axis=0) #row wise insert
new_arr_2dc = np.insert(arr_2d, 1, [9, 10], axis=1) #row wise insert
new_arr_2dn = np.insert(arr_2d, 1, [9, 10], axis=None) #Retur Flatten array

print(new_arr_2dr)
print(new_arr_2dc)
print(new_arr_2dn)