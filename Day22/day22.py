#Task 2

#Find sum, mean, max and min

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Sum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Max =", np.max(arr))
print("Min =", np.min(arr))


#Task 3

#Find median, standard deviation and variance

arr = np.array([10, 20, 30, 40])

print("Median =", np.median(arr))
print("Standard Deviation =", np.std(arr))
print("Variance =", np.var(arr))


#Task 4

#Row-wise sum, column-wise sum, and mean using axis

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Row-wise Sum =", np.sum(arr, axis=1))
print("Column-wise Sum =", np.sum(arr, axis=0))
print("Row-wise Mean =", np.mean(arr, axis=1))
print("Column-wise Mean =", np.mean(arr, axis=0))


#Task 5

#Find index of max and min elements

arr = np.array([10, 20, 30, 40, 50])

print("Index of Max:", np.argmax(arr))
print("Index of Min:", np.argmin(arr))


#Task 6

#Compute cumulative sum and analyze output

arr = np.array([1, 2, 3, 4])
print("Cumulative Sum =", np.cumsum(arr))
