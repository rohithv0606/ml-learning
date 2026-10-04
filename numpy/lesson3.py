#****array math and statistics****
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)     # [11 22 33 44]
print(b - a)     # [ 9 18 27 36]
print(a * b)     # [ 10  40  90 160]
print(b / a)     # [10. 10. 10. 10.]
print(a ** 2)    # [ 1  4  9 16]

m = np.array([[1, 2, 3],
              [4, 5, 6]])
#this is how ml code applies one set of weights to many rows of data.
print(m + 10)               # adds 10 to every value
print(m * np.array([1, 0, 1]))  # multiplies each row by [1, 0, 1]

#statistics functions
scores = np.array([55, 70, 85, 90, 40])
print(scores.sum())    # 340
print(scores.mean())   # 68.0
print(scores.max())    # 90
print(scores.min())    # 40
print(scores.std())    # standard deviation (spread of the values)
print(np.median(scores))  # 70

#axis idea in 2d arrays
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(m.sum())          # 21, everything
print(m.sum(axis=0))    # [5 7 9], down each column
print(m.sum(axis=1))    # [ 6 15], across each row

#reshaping  arrays.total no of values should be same.
x = np.arange(1, 7)     # [1 2 3 4 5 6]
print(x.reshape(2, 3))  # 2 rows, 3 columns
print(x.reshape(3, 2))  # 3 rows, 2 columns

marks = np.array([[80, 90, 70],
                  [60, 75, 85],
                  [95, 65, 78]])
#avg of all marks
print(marks.mean())  # 77.88888888888889
#avg of each student (row-wise)
print(marks.mean(axis=1))  # [80. 73.33333333 79.33333333]
#each subsect average (column-wise)
print(marks.mean(axis=0))  # [78.33333333 76.66666667 77.66666667]
#adding 5 marks to each student
print(marks + 5)  # [[85 95 75] [65 80 90] [100 70 83]]
y=np.arange(1, 13).reshape(3, 4)
print(y)  # [[ 1  2  3  4] [5  6  7  8] [ 9 10 11 12]]
