import numpy as np

#Aggrigation Function:
a = np.array([[10,20,30],
              [40,50,60]])
print(f"Sum: {np.sum(a)}") #Sum of all Elemenets
print(f"Min: {np.min(a)}")
print(f"Max: {np.max(a)}")
print(f"Var: {np.var(a)}") # 2X of STD
print(f"average: {np.average(a)}")
print(f"Standard Daviation: {np.std(a)}")
print(f"Middle Value: {np.mean(a)}")
print(f"median: {np.median(a)}") # calculate average of all Element
