#concatenate joins elements inside the existing array dimensions. It connects array entries end-to-end like link cars on a train.
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])
# Joining two arrays using np.concatenate
result=np.concatenate((arr1,arr2))
print(result)


arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6]])
# Joining two arrays using np.concatenate along axis 0
result2=np.concatenate((arr3,arr4),axis=0)#axis=0 means joining along rows, axis=1 means joining along columns
print(result2)

arr5=np.array([[1,2],[3,4]])
arr6=np.array([[5,6],[7,8]])
result3=np.concatenate((arr5,arr6),axis=1)
print(result3)

#stack creates a brand-new dimension. It takes the input arrays, keeps them intact as individual items, and bundles them inside a new wrapper array (like stacking whole sheets of paper on top of each other).
arr7=np.array([1,2,3])
arr8=np.array([4,5,6])
# Joining two arrays using np.vstack
result4=np.vstack((arr7,arr8))#vstack means joining along vertical axis
print(result4)

arr9=np.array([1,2,3])
arr10=np.array([4,5,6])
# Joining two arrays using np.hstack
result5=np.hstack((arr9,arr10))#hstack means joining along horizontal axis
print(result5)  
