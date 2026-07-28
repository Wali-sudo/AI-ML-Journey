#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)#shuffle() method makes changes to the original array.
print(arr)

print(random.permutation(arr))#permutation() method returns a re-arranged array (and leaves the original array un-changed).