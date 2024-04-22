import numpy as np

arr1 = np.array([1, 3, 4, 3])
arr2 = np.array([3, 1, 2, 1])

result = np.intersect1d(arr1, arr2)

print("The common elements are:", result)