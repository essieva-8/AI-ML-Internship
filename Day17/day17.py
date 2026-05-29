#Task 2

import math

#1. Square root
print(math.sqrt(25))

#2. Power
print(math.pow(2, 4))

#3. Round numbers
print(math.ceil(2.3))
print(math.floor(2.9))

#4. Pi value
print(math.pi)


#Task 3

import random

#1. Generate random number
print(random.randint(1, 100))

#2. Pick random element
print(random.choice(["apple", "banana", "orange"]))

#3. Generate list of random numbers
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)


#Task 4

import datetime

#1. Current date
now = datetime.datetime.now()
print(now)

#2. Format date
print(now.strftime("%Y-%m-%d"))

#3. Extract year and month
print("Year:", now.year)
print("Month:", now.month)


#Task 5

import matplotlib.pyplot as plt

#1. Line graph
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y)
plt.title("Line Graph")
plt.show()

#2. Bar chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

#3. Student marks graph
students = ["A", "B", "C", "D"]
marks = [85, 90, 78, 92]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()