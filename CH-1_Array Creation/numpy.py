import numpy as np

#Scaler = a single no OR [0D Array]
sc = 10 #or
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


# #Array With Default Values:
# # np.zeros((shape))
print("array of 0s:",np.zeros(3))

# # Create array with 1s
print("array of 1s:",np.ones((2,5)))

# # full(shape, values)
print("array of Custom Numbers:",np.full((5,2), (2, 3)))

# # Create a sequance of numbers:
# #arange(start, stop, step)
print("range of np array:",np.arange(2,10,2))

# # Identiti Matrix : [1,0,0],[0,1,0][0,0,1]
print(f"Identiti Matrix: \n{np.eye(5)}")