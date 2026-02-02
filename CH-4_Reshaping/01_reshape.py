"""
converting array dimention without modify the Data

array.reshape(rows, cols) for new shape 

BUT
if Dimentions are same then array re shape
"""
import numpy as np

arr = np.array([1,2,3,4,5,6])
re_arr = arr.reshape(2,3)
print(re_arr)
