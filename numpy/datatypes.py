#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O  - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr.dtype)
print(arr)

arr1=np.array([1,2,3,4,5],dtype='f')
print(arr1.dtype)
print(arr1)

#For i, u, f, S and U we can define size as well.

arr2=np.array([1,2,3,4,5],dtype='i4')
print(arr2.dtype)
print(arr2)

#ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

arr3=np.array([a,2,3,4,5],dtype='i2')
print(arr3.dtype)
print(arr3)

#The best way to change the data type of an existing array, is to make a copy of the array with the astype() method

arr4=arr2.astype('f8')
print(arr4.dtype)
print(arr4)
print(arr2.dtype)
print(arr2)