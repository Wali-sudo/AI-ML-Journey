#Vectorization means applying operations directly to entire arrays rather than iterating through individual items using a Python for loop.
#https://youtu.be/rtKqOlQEtDo?si=FSbwqA1qWZyCKhF4
import numpy as np
import time
# Generate 1 million random values
np.random.seed(42)
y_true = np.random.rand(1_000_000)
y_pred = np.random.rand(1_000_000)
# --- Approach 1: Python For Loop ---
start_time = time.time()
errors = []
for i in range(len(y_true)):
    diff = y_true[i] - y_pred[i]
    errors.append(diff ** 2)
mse_loop = sum(errors) / len(y_true)
loop_time = time.time() - start_time
# --- Approach 2: NumPy Vectorization ---
start_time = time.time()
mse_vec = np.mean((y_true - y_pred) ** 2)
vec_time = time.time() - start_time

print(f"Loop Time:         {loop_time:.4f} seconds")
print(f"Vectorized Time:   {vec_time:.4f} seconds")
print(f"Speedup Factor:    {loop_time / vec_time:.1f}x faster!")