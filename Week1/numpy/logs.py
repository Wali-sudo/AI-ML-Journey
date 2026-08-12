import numpy as np
arr = np.arange(1, 10)#arange(start,stop,step)
print(arr)
print(np.log2(arr))#base 2

print(np.log10(arr))#base 10

print(np.log(arr))#base e

#NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter

from math import log
import numpy as np
#frompyfunc() converts a regular Python function into a NumPy function
#log (from Python's built-in math module): The function being converted.
#2 (nin): The number of input arguments the function expects.
#1 (nout): The number of outputs the function produces.
nplog = np.frompyfunc(log, 2, 1)
#log15(100)
print(nplog(100, 15))