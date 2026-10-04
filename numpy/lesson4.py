#******random numbers,matrix operations*****
import numpy as np
np.random.seed(42)   # makes results repeatable, so you get the same numbers every run

print(np.random.rand(3))   # 3 random floats between 0 and 1
print(np.random.randint(1, 7, size=5))  # 5 dice rolls (1 to 6)
print(np.random.randn(3))   # 3 values from a normal distribution (mean 0, std 1)

items = np.array([10, 20, 30, 40, 50])
print(np.random.choice(items, 2))     # pick 2 random items
np.random.shuffle(items)              # shuffles in place
print(items)

#joining arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate([a, b]))   # [1 2 3 4 5 6]
print(np.vstack([a, b]))        # stacks as rows:    [[1 2 3] [4 5 6]]
print(np.hstack([a, b]))        # side by side:      [1 2 3 4 5 6]

#matrix operations
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
# * multiplies matching positions.
print(A * B)    # element-wise: [[ 5 12] [21 32]]
# @ does true matrix multiplication (row times column)
print(A @ B)    # matrix multiplication: [[19 22] [43 50]]
# transpose:swaps rows and columns
print(A.T)      # transpose (swap rows and columns): [[1 3] [2 4]]
# neural networks are mostly @ repeated many times.

#dot product of 2 vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.dot(v1, v2))   # 1*4 + 2*5 + 3*6 = 32
