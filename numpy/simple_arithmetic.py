#You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,0])
newarr = np.add(arr1, arr2)
print(newarr)

newarr = np.subtract(arr1, arr2)
print(newarr)

newarr = np.multiply(arr1, arr2)
print(newarr)

newarr = np.divide(arr1, arr2)
print(newarr)

newarr = np.power(arr1, arr2)
print(newarr)

newarr = np.mod(arr1, arr2)
print(newarr)

#divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
newarr = np.divmod(arr1, arr2)
print(newarr)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

