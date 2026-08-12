#Used to describe probability where every event has equal chances of occuring. E.g. Generation of random numbers.
#Just like the Normal Distribution, the Uniform Distribution also has three parameters:
#low - Default 0. The lower boundary of the output interval. All random numbers generated will be greater than or equal to low.
#high - Default 1. The upper boundary of the output interval. All random numbers generated will be less than high.
#size - The shape of the returned array.
#https://youtu.be/n_1Z-HVemP0?si=CiqRTX00islKhJ4T watch this video for better understanding of Uniform Distribution.

#Generate a random uniform distribution of size 2x3
from numpy import random
x = random.uniform(size=(2, 3))
print(x)

x = random.uniform(low=1.0, high=10.0, size=(2, 3))#Generate a random uniform distribution with lower boundary 1 and upper boundary 10
print(x)

