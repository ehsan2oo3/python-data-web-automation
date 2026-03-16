import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])

# Basic statistics
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
print("Matrix Transpose:\n", matrix.T)

# Random numbers
random_numbers = np.random.randint(1, 100, size=5)
print("Random Numbers:", random_numbers)