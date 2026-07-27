import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)#searchsorted returns the index where the value should be inserted to maintain sorted order
print(x)

#By default the left most index is returned, but we can give side='right' to return the right most index instead
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
