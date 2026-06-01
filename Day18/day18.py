#Task 2

import numpy as np

#1. 1D Array
arr1 = np.array([1, 2, 3, 4])

#2. 2D Array
arr2 = np.array([[1, 2],
                 [3, 4]])

#3. 3D Array
arr3 = np.array([[[1, 2],
                  [3, 4]]])

print("1D Array:\n", arr1)
print("2D Array:\n", arr2)
print("3D Array:\n", arr3)


#Task 3

#Print the shape, dimensions, and data type of the 2D array
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)


#Task 4

#1. Zero Matrix
print(np.zeros((2, 3)))

#2. Ones Matrix
print(np.ones((2, 2)))

#3. Identity Matrix
print(np.eye(3))

#4. Range Array
print(np.arange(1, 10))


#Task 5

#1. Access the first element
print(arr1[0])

#2. Slice array
print(arr1[1:3])

#3. Access element in 2D array
print(arr2[0, 1])


#Task 6

#1. Convert 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6])
arr_2d = arr.reshape(2, 3)
print(arr_2d)

#2. Convert 2D to 1D
arr_1d = arr_2d.reshape(-1)
print(arr_1d)