#Task 2

#Add, Multiply and Divide 2 arrays 

import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Division:", a / b)


#Task 3

#Add, Multiply and Subtract a constant to an array

arr = np.array([1, 2, 3])

print("Add Constant:", arr + 10)
print("Multiply:", arr * 2)
print("Subtract Constant:", arr - 1)


#Task 4

#Find square root, logarithm and round values 

arr1 = np.array([1, 4, 9, 16])
print("Square Root:", np.sqrt(arr1))
print("Log Values:", np.log(arr1))

arr2 = np.array([1.2, 2.7, 3.5])
print("Rounded:", np.round(arr2))


#Task 5

#Find sum, mean, max and min of an array

arr = np.array([10, 20, 30, 40])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))


#Task 6

#Row-wise and column-wise sum

arr = np.array([[1, 2],
                [3, 4]])

print("Row-wise Sum:", np.sum(arr, axis=1))
print("Column-wise Sum:", np.sum(arr, axis=0))


#Task 7

arr = np.array([10, 20, 35, 40, 50])

#1. Filter values > 20
print("Values > 20:", arr[arr > 20])

#2. Filter even numbers
print("Even Numbers:", arr[arr % 2 == 0])