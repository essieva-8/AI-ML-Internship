#Task 2

import numpy as np

#Find average marks, highest marks, lowest marks and topper

marks = np.array([
    [85, 78, 90],
    [70, 88, 60],
    [95, 92, 89]
])

print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

total = np.sum(marks, axis=1)
topper = np.argmax(total)

print("Total Marks:", total)
print("Topper Index:", topper)


#Task 3

image = np.array([
    [50, 100],
    [150, 200]
])

#1. Increase brightness
bright = image + 50

#2. Decrease brightness
dark = image - 30

#3. Normalize pixels
normalized = image / np.max(image)

print(bright)
print(dark)
print(normalized)


#Task 4

arr = np.array([10, 25, 60, 40, 80, 15, 90])

#1. Filter values > 50
filtered = arr[arr > 50]

#2. Replace low values (<20) with 0
modified = np.where(arr < 20, 0, arr)

#3. Count filtered values
count = len(filtered)

print(filtered)
print(modified)
print(count)


#Task 5

#1. Convert 1D → 2D
arr1 = np.arange(12)
arr2 = arr1.reshape(3, 4)

#2. Convert 2D → 1D
arr3 = arr2.reshape(-1)

#3. Create 3D dataset
arr4 = np.arange(24).reshape(2, 3, 4)

print(arr2)
print(arr3)
print(arr4)


#Task 6

#1. Attendance Dataset
attendance = np.random.randint(0, 2, size=(5, 7))

#2. Marks Dataset
marks = np.random.randint(40, 101, size=(5, 3))

#3. Weather Dataset (Temperature)
weather = np.random.randint(20, 41, size=(7,))

print("Attendance:")
print(attendance)

print("\nMarks:")
print(marks)

print("\nWeather:")
print(weather)