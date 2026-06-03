#Task 2

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

#1. Access first element
print(arr[0])

#2. Access last element
print(arr[-1])

#3. Slice array
print(arr[1:4])


#Task 3

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

#1. Access element
print(arr[1, 2])

#2. Print row
print(arr[0])

#3. Print column
print(arr[:, 1])


#Task 4

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

#1. Access layer
print(arr[0])

#2. Access row inside layer
print(arr[0][1])

#3. Access single element
print(arr[1, 0, 2])


#Task 5

arr = np.array([10, 20, 30, 40, 50])

#1. Extract sub-array
print(arr[1:4])

#2. Step slicing
print(arr[::2])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

#3. Slice rows and columns
print(arr2[:, 1:3])


#Task 6

arr = np.array([10, 20, 30, 40, 50])

#1. Filter values > 25
print(arr[arr > 25])

#2. Filter values between range
print(arr[(arr > 20) & (arr < 50)])

#3. Replace values conditionally
arr[arr > 30] = 100
print(arr)