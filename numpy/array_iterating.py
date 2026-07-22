import numpy as np
#printing elements of a 1D array
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
#printing rows of a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
# printing all elements of a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)
#printing rows of a 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
# printing all elements of a 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)
#printing all elements of a 3D array using nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
#Converting Data Type on Existing Arrays
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  #op_dtypes specifies the data type to which the array elements should be converted during iteration. In this case, 'S' indicates that the elements should be converted to string type.
  #astype() method is used to convert the data type of the array elements to the specified type. In this case, it converts the elements to string type. In this case, the elements of the array are converted to string type during iteration, and then printed as strings. For large files or arrays, this can be more memory-efficient than creating a new array with the converted data type.
  #flags=['buffered'] is used to enable buffered iteration, which allows for efficient iteration over large arrays without creating a new array with the converted data type. This can be more memory-efficient than creating a new array with the converted data type.
  print(x)
#iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):#arr[row slice, column slice]
  print(x)

#Enumeration means mentioning sequence number of somethings one by one.

#enumerated iteration using ndenumerate()
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

#enumerated iteration using ndenumerate() for 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)