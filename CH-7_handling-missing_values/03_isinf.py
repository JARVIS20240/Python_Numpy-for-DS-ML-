import numpy as np
arr = np.array([1,2, np.inf, 4, -np.inf, 6])
print (np.isinf(arr))

clear_array = np.nan_to_num(arr, neginf=-100, posinf=200)
print(clear_array)