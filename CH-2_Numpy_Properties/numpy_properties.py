import numpy as np

# # shape, size, type
arr = np.array([[1,2,3],
                      [4,5,6.1]])

print(f"Shape of 2D array: {arr.shape}") # (2,3) 2=rows, 3=columns
print(f"Size of 2D array-(Total Elements in Array): {arr.size}") #6 Elements in Array
print(f"Type of Array : {tuple(arr)}") 
print(f"Check No. of Dimentions: {arr.ndim}")# 2-Dimention array
print(f"Data Type fo array: {arr.dtype}")

# Change Data Type :
int_arry = arr.astype(int)
# print(f"Change Data Type: {int_arry.astype(int)}")
print(f"Data Type fo array: {int_arry.dtype}")

# Mathamatics:
arr = np.array([10,20,30])

print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr ** 5)
print(arr / 5)
print(arr % 5)

#Aggrigation Function:
a = np.array([[10,20,30],
              [40,50,60]])
print(f"Sum: {np.sum(a)}") #Sum of all Elemenets
print(f"Min: {np.min(a)}")
print(f"Max: {np.max(a)}")
print(f"Var: {np.var(a)}")
print(f"average: {np.average(a)}")
print(f"Standard Daviation: {np.std(a)}")
print(f"Middle Value: {np.mean(a)}")
print(f"median: {np.median(a)}")
