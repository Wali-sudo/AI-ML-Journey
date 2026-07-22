import numpy as np

arr =  np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # This will print elements from index 1 to 3 (2, 3, 4)

arr = np.array([10, 20, 30, 40, 50])
print(arr[2]+arr[4])  # This will print the sum of elements at index 2 and 4 (30 + 50 = 80)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1, 2])  # This will print the element at row 1, column 2 (6) 

arr =np.array([1, 2, 3, 4, 5], ndmin=3)# when we use ndmin=3 with 1D array, it creates a 3-dimensional array which is actually a 1D array
print(arr[0,0,2])  # This will print the element at index [0, 0, 2] (3)

#we can also use negative indexing to access elements from the end of the array. For example:
arr = np.array([10, 20, 30, 40, 50])
print(arr[-1])  # This will print the last element of the array (50)
print(arr[-2])  # This will print the second-to-last element of the array (40)