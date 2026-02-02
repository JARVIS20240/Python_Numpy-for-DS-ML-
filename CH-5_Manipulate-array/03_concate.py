import numpy as np

"""
np.concate((array1, array2), axis =None)
axis = 0 row wise concate
axis = 1 column wise concate
axis = None flatten concate
"""
arr1 = np.array([[10,20],[30,40]])
arr2 = np.array([[60,70],[80,90]])

concate = np.concatenate((arr1,arr2), axis=0)
print(concate)