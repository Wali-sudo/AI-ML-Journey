import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
#The copy SHOULD NOT be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
#The view SHOULD be affected by the changes made to the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)
#The original array SHOULD be affected by the changes made to the view.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
#The base of the copy SHOULD be None, while the base of the view SHOULD be the original array.
#base attribute tells you if an array owns its memory or if it is just a view borrowing memory from another array.