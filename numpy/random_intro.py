#Random number does NOT mean a different number every time. Random means something that can not be predicted logically
#Random numbers generated through a generation algorithm are called pseudo random,can be predicted if the algorithm is known. Random numbers generated through a physical process are called true random numbers, can not be predicted even if the process is known.
#True random numbers are generated through physical processes like keystrokes, mouse movements, data on network etc
#We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels)

from numpy import random
x = random.randint(100)#Generate a random integer from 0 to 100
print(x)

#rand() generate random float numbers between 0 and 1
x = random.rand(5)#Generate 5 random float numbers between 0 and 1
print(x)

x = random.rand(3, 5)#Generate a 2D array of random float numbers between 0 and 1 with 3 rows and 5 columns
print(x)

x=random.randint(100, size=(5))#Generate an array of 5 random integers from 0 to 100
print(x)

x = random.randint(100, size=(3, 5))#Generate a 2D array of random integers from 0 to 100 with 3 rows and 5 columns
print(x)

#uniform() generates random float numbers between the given range
x = random.uniform(10, 50, 5)#Generate an array of 5 random float numbers between 10 and 50
print(x)