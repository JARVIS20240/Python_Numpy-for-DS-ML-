import numpy as np
#Scaler = a single no OR [0D Array]
sc = 10 #or

scale = np.array([10])

print("Shape of Scaler: 0D =",scale.shape)
print("Size of Scaler:",scale.ndim)

sclae = np.array(10)

print("Shape of Scaler: 0D =",sclae.shape)
print("Size of Scaler:",sclae.ndim)


#Vactor = 1D Array (list)
vact = [10,20,30]
vactor = np.array([10,20,30])

print(f"Shape of Vactor: 1D = {vactor.shape}")
print("Size of Vactors: ",vactor.ndim)


# #Matrix = 2D Array (rows, cols)
mat = [[10,20,30],
       [40,50,60]]
matrix = np.array([[10,20,30],
                   [40,50,60]])

print(f"Shape of Matrix: 2D = {matrix.shape}")
print("Size of Matrix: ",matrix.ndim)

# #Tensor = 3D + Array 
tensor = np.array([[
    [1,2], [3,4],
    [5,6], [7,8]
]])
print(f"Shape of Tensor : nD = {tensor.shape}")
print("Size of Tensor: ",tensor.ndim)