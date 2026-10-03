import numpy as np
#using numpy array
a=np.array([1,2,3,4])
print(a*2) #2,4,6,8 
#without using numpy array
nums=[1,2,3,4]
print(nums*2) #[1, 2, 3, 4, 1, 2, 3, 4] #list is repeated twice

#zeros function creates an array filled with zeros, and ones function creates an array filled with ones.
print(np.zeros(5))     # five 0s
print(np.ones((2, 3))) # 2rows,3columns of 1s
#array of evenly spaced values can be created using the arange function, and the linspace function can be used to create an array of evenly spaced values over a specified interval.
print(np.arange(0, 10, 2)) # 0, 2, 4, 6, 8
print(np.linspace(0, 1, 5)) # 5 evenly spaced values from 0 to 1

a = np.array([[1, 2, 3],
              [4, 5, 6]])
#shape attribute returns the dimensions of the array
print(a.shape) # (2, 3) means 2rows,3columns
#ndim attribute returns the number of dimensions
print(a.ndim)  # 2 dimensions
#dtype attribute returns the data type of the array elements
print(a.dtype) # data type, like int64

x=np.arange(1,11)
print(x) # [1 2 3 4 5 6 7 8 9 10]
print(x*3) # [ 3  6  9 12 15 18 21 24 27 30]
y=np.zeros((3,4))
print(y) # 3rows,4columns of 0s
print(np.shape(y)) # (3, 4)