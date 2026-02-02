# array.astype(new dtype) = change array data type
import numpy as np

arr_1d = np.array([[1,2,3], [4,5,6]])
arr_2d = np.array([1.0,2.0,3.0])

int_arr = arr_2d.astype(int)
float_arr = arr_1d.astype(float)
str_arr = arr_1d.astype(str)

print(int_arr,arr_2d.dtype, int_arr.dtype)
print(float_arr,arr_1d.dtype, float_arr.dtype)
print(str_arr,arr_1d.dtype, str_arr.dtype)

