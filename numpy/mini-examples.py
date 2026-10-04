#******mini projects******

import numpy as np

# 1.tiny prediction[working of ml]
X = np.array([[1, 2],
              [3, 4],
              [5, 6]])      # 3samples, 2features each
w = np.array([0.5, 0.25])   # weights
print(X @ w)    # [1.  2.5  4. ]
# note: this is a linear model, and the output is a linear combination of the inputs and weights.
#Each prediction is feature1 * 0.5 + feature2 * 0.25. A real model does the same thing, but learns the best weights from data.

# 2.analyse random student scores
np.random.seed(0) #seed used to make results repeatable, so you get the same numbers every run
scores = np.random.randint(30, 100, size=50)   # 50 students
print("Scores:", scores)
print("Average:", scores.mean())
print("Highest:", scores.max())
print("Passed (>= 40):", (scores >= 40).sum())
print("Top scorers (> 90):", scores[scores > 90])

# Normalization: a very common ML step
normalized = (scores - scores.mean()) / scores.std()
print(normalized[:5]) 
# note: (scores >= 40).sum() works because True counts as 1, so summing a True/False array counts the Trues. Normalization shifts the data to mean 0 and spread 1, which helps models train.
