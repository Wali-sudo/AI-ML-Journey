#Matrix multiplication calculates weighted sums. To multiply Matrix A(mxn) by Matrix B(nxp) the inner dimensions must match (n=n) resulting in a matrix of shape(mxp)
#Use @ or np.matmul for standard matrix multiplication. np.dot behaves the same for 2D matrices, but @ is the modern Python operatorfor standard matrix multiplication. np.dot behaves the same for 2D matrices, but @ is the modern Python operator

#e.g: Prediction of dense layer y=x.w+b
import numpy as np
# 2 data samples with 3 features
X = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])
# Weights for 2 output neurons
W = np.array([
    [0.1, 0.4],
    [0.2, 0.5],
    [0.3, 0.6]
])
b = np.array([0.5, 0.5])
# Matrix Multiplication (2, 3) @ (3, 2) -> (2, 2)
predictions = (X @ W) + b
print("Predictions Shape:", predictions.shape)
print("Predictions:\n", predictions)

#Transpose (.T or np.transpose)
import numpy as np
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Original Shape:", A.shape)
print("Original Matrix:\n", A)
# Transpose
A_transposed = A.T
print("\nTransposed Shape:", A_transposed.shape)
print("Transposed Matrix:\n", A_transposed)