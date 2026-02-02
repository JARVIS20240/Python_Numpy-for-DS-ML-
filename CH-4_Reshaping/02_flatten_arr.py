import numpy as np

"""
.ravel()-> Gives View of array [changes effact to original array]
-> ravel() link to original array, changes are effect to real array
just view of original array but in 1D

.flatten()-> gives Copy of array [not effact the changes to original array]
->alwas create a new-copy of original array. changes are not effect to original 
"""
import numpy as np

arr = np.array([[1, 2],
                [3, 4]])
r = arr.ravel()
f = arr.flatten()

r[0] = 123


print(arr.ndim)
print(arr)
print(r)
print(f)