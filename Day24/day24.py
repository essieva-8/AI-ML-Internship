#Task 2

import numpy as np

#1. Generate Random Integer
print(np.random.randint(1, 10))

#2. Generate Array of Integers
print(np.random.randint(1, 100, size=5))

#3. Create Random Matrix
print(np.random.randint(1, 100, size=(3, 3)))


#Task 3

#1. Generate Decimal Values
print(np.random.rand(5))

#2. Create 2D Decimal Matrix
print(np.random.rand(3, 4))


#Task 4

#1. Pick Random Color
colors = ['red', 'blue', 'green', 'yellow', 'orange']
print(np.random.choice(colors))

#2. Generate Multiple Choices
print(np.random.choice(colors, size=5))

#3. Simulate Random Names
names = ["Asha", "Rahul", "Neha", "Arjun", "Meera"]
print(np.random.choice(names, size=3))


#Task 5

#1. Shuffle Array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

#2. Shuffle Student IDs
student_ids = np.array([101, 102, 103, 104, 105])
np.random.shuffle(student_ids)
print(student_ids)


#Task 6

#1. Create Marks Dataset
marks = np.random.randint(40, 100, size=(5, 3))
print(marks)

#2. Create Attendance Dataset
attendance = np.random.randint(60, 101, size=(5, 1))
print(attendance)

#3. Create Random Image Matrix
image = np.random.randint(0, 256, size=(3, 3))
print(image)