#Task 2

#1. Convert 1D → 2D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)

#2. Convert 1D → 3D

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(1, 2, 3)
print(reshaped)

#3. Invalid Reshape

arr = np.array([1, 2, 3, 4, 5, 6])
try:
    reshaped = arr.reshape(2, 4)        
except ValueError as e:
    print("Error:", e)


#Task 3

#1. Convert 2D → 1D

arr = np.array([[1, 2],
                [3, 4]])
flat = arr.flatten()
print(flat)

#2. Compare Flatten vs Ravel

arr = np.array([[1, 2],
                [3, 4]])

flat1 = arr.flatten()
flat2 = arr.ravel()
print("Flatten:", flat1)
print("Ravel:", flat2)


#Task 4

#Transpose Matrix & Verify Rows and Columns

arr = np.array([[1, 2],
                [3, 4]])
print(arr.T)


#Task 5

#1. Vertical Stack 

a = np.array([1, 2])
b = np.array([3, 4])

print(np.vstack((a, b)))

#2. Horizontal Stack

a = np.array([1, 2])
b = np.array([3, 4])

print(np.hstack((a, b)))


#Task 6

#1. Split Array

arr = np.array([1, 2, 3, 4, 5, 6])
print(np.split(arr, 3))

#2. Split Rows

arr = np.array([[1, 2],
                [3, 4]])

print(np.vsplit(arr, 2))





