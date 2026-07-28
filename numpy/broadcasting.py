#Broadcasting is NumPy's mechanism for performing element-wise operations on arrays of different shapes. Instead of requiring both arrays to be identical in size, NumPy automatically "stretches" the smaller array across the larger one without duplicating memory.
#https://youtu.be/P67wiuTx7l0?si=QI6EJhPMcMkIXn58   this video for broadcasting
import numpy as np

# Matrix X: Shape (4, 3) -> 4 samples, 3 features
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
    [10.0, 11.0, 12.0]
])

# Bias Vector b: Shape (3,) -> 1 bias value per feature
b = np.array([0.1, 0.2, 0.3])

# Add bias using Broadcasting
Z = X + b

print("Shape of X:", X.shape)
print("Shape of b:", b.shape)
print("Shape of Z:", Z.shape)
print("\nResult Z:\n", Z)