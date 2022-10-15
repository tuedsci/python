# NUMPY
import numpy as np

# --------------------------------------------------
# BASICS
# --------------------------------------------------

# %% Create an array
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(type(a))

# %% Basic info
print(a.dtype)  # Data type of elements
print(a.size)  # Number of elements

# --------------------------------------------------
# TYPE PROMOTION
# --------------------------------------------------

# %% Promoted to int
a = np.array([True, 1, 2])
print(a, a.dtype)

# %% Promoted to float
a = np.array([True, 1, 2.5])
print(a, a.dtype)

# %% Promoted to str
np.array([1, 2, 3, "A"])
print(a, a.dtype)

# %% Promoted to object (avoid this)
a = np.array([1, 2, "A", [88, 99]])
print(a, a.dtype)

# --------------------------------------------------
# INDEXING & SLICING
# --------------------------------------------------
# %% Index an array
a = np.array([1, 2, 3, 4, 5, 6])

print(a[0])  # First
print(a[2])  # Third
print(a[-1])  # Last
print(a[-2])  # Second to last

# %% Slice an array
print(a[:3])  # First 3
print(a[-3:])  # Last 3
print(a[2:])  # All except first 2
print(a[:-2])  # All except last 2

# --------------------------------------------------
# GENERATION UTILITIES
# --------------------------------------------------

# %% Generate evenly-spaced sequence
print(np.arange(5))  # [0, 1, 2, 3, 4, 5]
print(np.arange(0, 1.0001, 0.1))  # [0.0, 0.1, ..., 1.0]
print(np.linspace(0, 1, 5))  # [0, .25, .5, .75, 1.]

# %% Special matrices
print(np.zeros(3))  # 3D vector of zeroes
print(np.zeros((2, 3)))  # 2x3 matrix of zeroes
print(np.ones(3))  # 3D vectors of ones
print(np.ones(3) * 5)  # 3D vectors of fives
print(np.ones((2, 3)))  # 2x3 matrix of ones

# --------------------------------------------------
# VECTORIZATION
# --------------------------------------------------
a = np.array([1, 2, 3, -5, 0, -10])
a + 10  # Add 10 element-wise
a * 10  # Mult 10 element-wise
a ** 2  # Square element-wise
abs(a)  # Take absolute value element-wise
