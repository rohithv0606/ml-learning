#***********indexing and slicing in numpy***************
import numpy as np
a=np.array([1, 2, 3, 4, 5])
print(a)
print(a[0])  # Accessing the first element
print(a[2])  # Accessing the third element  
print(a[-1])  # Accessing the last element

#2d arrays in numpy
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a[0, 1])     # 2 (row 0, column 1)
print(a[1])        # [4 5 6]  (whole row 1)
print(a[:, 0])     # [1 4 7]  (whole column 0)
print(a[0:2, 1:])  # [[2 3]
                   #  [5 6]]  (rows 0-1, columns 1 onward)

#boolean indexing
nums = np.array([5, 12, 8, 20, 3, 15])
print(nums>10)  # [False  True False  True False  True]
print(nums[nums>10])  # [12 20 15]  (elements greater than 10)
print(nums[nums%2==0])  # [12  8 20]  (even elements)
nums[0] = 100
nums[nums < 10] = 0
print(nums)

data = np.array([[10, 20, 30, 40],
                 [50, 60, 70, 80],
                 [90, 100, 110, 120]])
print(data[1,2])  # 70 (row 1, column 2)
print(data[2, :])  # [ 90 100 110 120] (whole row 2)
print(data[:, 1])  # [ 20  60 100] (whole column 1)
print(data[0:2,2:4])  # [[30 40]
                     #  [70 80]]  (rows 0-1, columns 2-3) 
print(data[data>60])  # [ 70  80  90 100 110 120] (elements greater than 60)
data[data < 50] = 0
print(data) 
