# 1️⃣ NumPy Fundamentals (NON-NEGOTIABLE):

import numpy as np

# np.array
arr_0d = np.array(10)
arr_1d = np.array([1200,4500.01,4520,3200])
print(type(arr_1d))

# np.ndim = for dimention count
arr_2d = np.array([["1200",4500],[4520,3200]])
arr_3d = np.array([[
                    [1200,4500],
                    [4520,3200]]])
print(f"0D Array: {arr_0d}")
print(f"1D Array: {arr_1d}")
print(f"2D Array: {arr_2d}")
print(f"3D Array: {arr_3d}")

print(f"Dimention: {arr_0d.ndim}") # Scaler 0-Dimention Array
print(f"Dimention: {arr_1d.ndim}") # Vector 1-Dimention Array
print(f"Dimention: {arr_2d.ndim}") # Matrix 2-Dimention Array
print(f"Dimention: {arr_3d.ndim}") # Tensor 3 to more Dimention Array

# np.shape = for know howmany rows and columns 
print(f"Shape of 0D Array: {arr_0d.shape}")
print(f"Shape of 1D Array: {arr_1d.shape}")
print(f"Shape of 2D Array: {arr_2d.shape}")
print(f"Shape of 3D Array: {arr_3d.shape}")

# np.shape = for know Totl elemnt in Array:
print(f"Size of 0D Array: {arr_0d.size}")
print(f"Size of 1D Array: {arr_1d.size}")
print(f"Size of 2D Array: {arr_2d.size}")
print(f"Size of 3D Array: {arr_3d.size}")

# np.dtype = Know array el;ement Data type:

print(f"Data Type of 0D Array:  {arr_0d.dtype}")
print(f"Data Type of 1D Array: {arr_1d.dtype}")
print(f"Data Type of 2D Array: {arr_2d.dtype}")
print(f"Data Type of 3D Array: {arr_3d.dtype}")

# array.astype(datatype) = for change data type of array:
print(f"Change Data type of 1D float64 to int = {arr_1d.astype(int, )},data Type: {arr_1d.dtype}")

# MCreating Arrays:
# np.zeros((rows,cols))

zero = np.zeros((3,5))
print(zero)

# np.ones((rows,cols))
ones = np.ones((3,5))
print(ones)

# np.full((size), value) = for custome value array creation
n = np.full((3,5), 10)
print(n)

# np.arange(start, stop, step) = for sequance generated array
range = np.arange(2, 50, 2)
print(range)

# np.random.rand(size)
random_1= np.random.random((2,3))
print(random_1)

random_2 = np.random.rand(3, 2)
print(random_2)

b = np.random.randn(3, 2)
print(b)

c = np.random.randint(1, 10, size=(2, 3, 5)) #cretae a 3D array np.random.randint(dimention, rows, columns)
print(c.ndim)
print(c)