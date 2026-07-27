import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))#This method returns a copy of the array, leaving the original array unchanged.

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

#If you use the sort() method on a 2-D array, both arrays will be sorted
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

