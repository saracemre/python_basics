import numpy as np

np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(type(np_array))

np_multi = np_array.reshape(3, 3)
# print(np_multi)

# print(np_array.shape)
# print(np_multi.shape)

# print(np_array.ndim)
# print(np_multi.ndim)

# print(np_multi[0][2])
# print(np_multi[0, 2])
# print(np_multi[:, 2])

arr1 = np.arange(0, 10)
# arr2 = arr1 # referans
arr2 = arr1.copy()
arr2[0] = 20
# print(arr1)
# print(arr2)
