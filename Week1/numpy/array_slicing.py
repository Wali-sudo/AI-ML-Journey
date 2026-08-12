#[start:stop:step] is the syntax for slicing in Python, where 'start' is the index to start the slice, 'stop' is the index to end the slice (exclusive), and 'step' is the interval between indices.
#[start:stop] start index is inclusive, stop index is exclusive.

import numpy as np
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[2:8:2])  # This will print elements from index 2 to 7 with a step of 2
print(arr[:5])  # This will print elements from the beginning to index 4
print(arr[5:9])  # This will print elements from index 5 to 8
print(arr[::3])  # This will print every third element from the array

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])


#for 2D arrays [rowslice, colslice]
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])  # This will print the subarray from rows 0 to 1 and columns 1 to 2
print(arr2d[::2, ::2])  # This will print every second row and every second column of row 1 and 3
