#Task 2

#1. Create File with Student Data

with open("students.txt", "w") as file:
    file.write("John,80\n")
    file.write("Sara,90\n")
    file.write("Alex,70\n")
    file.write("Mia,85\n")
    file.write("Raj,60\n")

#2. Read and Store in List of Dictionary

students = []

with open("students.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

#3. Print All Students

print("\nAll Students:")
for s in students:
    print(s)

#4. Find Average Marks

total = sum(s["marks"] for s in students)
average = total / len(students)
print("Average Marks:", average)

#5. Find Topper

topper = max(students, key=lambda x: x["marks"])
print("Topper:", topper["name"])


#Task 3

#1. Filter Students with Marks > 75

filtered = [s for s in students if s["marks"] > 75]
print("Students with marks > 75:", filtered)

#2. Count Number of Students

print("Total Students:", len(students))

#3. Find Lowest Marks

lowest = min(students, key=lambda x: x["marks"])
print("Lowest Marks:", lowest)

#4. Sort Students by Marks

sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Students sorted by marks:", sorted_students)


#Task 4

#1. Function to calculate average

def calculate_average(students):
    total = sum(s["marks"] for s in students)
    return total / len(students)

print("Average Marks:", calculate_average(students))

#2. Function to find topper

def get_topper(students):
    return max(students, key=lambda x: x["marks"])
print("Topper:", get_topper(students))

#3. Function to filter students

def filter_students(students, threshold):
    return [s for s in students if s["marks"] > threshold]
filtered_students = filter_students(students, 75)
print("Students with marks > 75:", filtered_students)


#Task 5

#1. Find student with second highest marks

second_highest = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Student with second highest marks:", second_highest[1])

#2. Count number of passed/failed students

passed = len([s for s in students if s["marks"] >= 65])
failed = len([s for s in students if s["marks"] < 65])
print("Passed Students:", passed)
print("Failed Students:", failed)

#3. Convert data into dictionary format

students_dict = {s["name"]: s["marks"] for s in students}
print("Students Dictionary:", students_dict)
