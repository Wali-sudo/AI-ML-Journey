import numpy as np
arr =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(f"Original array: {arr}")
print(f"Shape of original array: {arr.shape}")
arr1 = arr.reshape(2,6)
print(f"Reshaped array (3x4):{arr1}")
print(f"Shape of reshaped array: {arr1.shape}")

arr2 =arr.reshape(6,1,2)
print(f"Reshaped array:{arr2}")
print(f"Shape of reshaped array: {arr2.shape}")

#reshape is a view of the original array, so modifying the reshaped array will also modify the original array
#-1 can be used to automatically calculate the size of one dimension based on the size of the other dimensions. For example, if you want to reshape an array into a 2D array with 3 rows and an unknown number of columns, you can use -1 for the column dimension: