#Task 2

import numpy as np

arr = np.array([1, 2, 3])

#1. Add scalar to array
print(arr + 10)

#2. Multiply array by scalar
print(arr * 5)

#3. Divide array by scalar
print(arr / 2)


#Task 3

a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

#1. Add two compatible arrays
print(a + b)

#2. Multiply arrays
print(a * b)

#3. Observe shape changes
print(a.shape)
print(b.shape)


#Task 4

a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])

#1. Print shapes 
print(a.shape)
print(b.shape)

#2. Compatible shapes
print(a + b)

#3. Incompatible shapes
c = np.array([1, 2, 3])
d = np.array([1, 2])

try:
    print(c + d)
except ValueError as e:
    print("Error:", e)


#Task 5

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

#1. Add scalar
print(matrix + 100)

#2. Multiply matrix
print(matrix * 2)

#3. Normalize values
print(matrix / 60)
