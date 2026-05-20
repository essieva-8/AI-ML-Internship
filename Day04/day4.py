#Task 2

#1. Create file and write your details

with open("student.txt", "w") as file:
    file.write("Name: Essie V Ayrookuzhy\n")
    file.write("Course: M.Tech Data Science & Analytics\n")

#2. Read the file and display the contents

with open("student.txt", "r") as file:
    print(file.read())

#3. Append new data

with open("student.txt", "a") as file:
    file.write("Internship: AI/ML Intern\n")

#4. Count number of lines

with open("student.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")

#5. Count number of words
with open("student.txt", "r") as file:
    content = file.read()
    words = content.split()
    print(f"Number of words: {len(words)}")

#Task 3

#1. Handle divide by zero

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")

#2. Handle invalid input

try:
    x = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid number")

#3. Use try–except–else–finally

try:
    x = int(input("Enter number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter a valid number")
else:
    print(f"No error occurred. Result: {result}")
finally:
    print("Execution completed")

#4. Handle file not found error

try:
    with open("student.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

#Task 4

#1. Find longest word in file

with open("student.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

#2. Count vowels in file

with open("student.txt", "r") as file:
    text = file.read().lower()
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    print("Vowel count:", count)

#3. Remove duplicate lines

with open("student.txt", "r") as file:
    lines = file.readlines()
unique_lines = set(lines)
with open("student_unique.txt", "w") as outfile:
    outfile.writelines(unique_lines)
