import numpy as np

arr1 = np.random.random((5,3))
arr2 = np.random.random((3,2))

dot = np.dot(arr1,arr2)

print(dot, dot.shape)