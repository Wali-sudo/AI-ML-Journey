#Addition is done between two arguments whereas summation happens over n elements
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

#If you specify axis=1, NumPy will sum the numbers in each array.
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

newarr = np.sum([arr1, arr2], axis=0)
print(newarr)

#Cummulative sum means partially adding the elements in array.E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
newarr = np.cumsum(arr1)
print(newarr)