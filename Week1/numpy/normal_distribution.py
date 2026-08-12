#Normal (Gaussian) Distribution
#Use the random.normal() method to get a Normal Data Distribution.
#It has three parameters:
#loc (mean) - Default 0. This parameter determines the location of the peak of the distribution.
#scale (standard deviation) - Default 1. This parameter determines the width of the distribution.
#size - The shape of the returned array.
#https://youtu.be/hfBeF8jdO6U?si=HlDcxr-8bLlspyIk   do watch this video for better understanding of Normal Distribution.

#Generate a random normal distribution of size 2x3

from numpy import random
x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))#Generate a random normal distribution with mean 1 and standard deviation 2
print(x)
