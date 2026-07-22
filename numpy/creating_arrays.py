import numpy as np
arr=np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))#type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

#0D

arr=np.array(42)
print(arr)
print(arr.ndim)#ndim: This attribute returns an integer that tells us the number of dimensions of the array. In above code it shows that arr is 0D array.

#1D

arr=np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

#2D

arr=np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

#3D

arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.ndim)

#Higher Dimensional Arrays

arr=np.array([1,2,3,4], ndmin=4)#ndmin: This argument specifies the minimum number of dimensions that the resulting array should have. In above code it shows that arr is 4D array. 
print(arr)
print(arr.ndim)