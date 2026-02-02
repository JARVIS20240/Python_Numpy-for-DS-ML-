import numpy as np

# np.linspace()
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
"""
start → first number
start→ last number
num → how many numbers you want (default 50)
endpoint → True includes stop in the list
retstep → True also returns the step size between numbers
"""
arr = np.linspace(0, 10, 5)
print(arr)