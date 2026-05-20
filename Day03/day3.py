#Task 2

#1. Create a list of 10 numbers

numbers = [5, 12, 7, 20, 3, 14, 9, 2, 18, 11]
print(numbers)

#2. Find sum of list elements

total = 0
for n in numbers:
    total = total + n

print("Sum of elements:", total)

#3. Find maximum number

maximum = numbers[0]
for n in numbers:
    if n > maximum:
        maximum = n

print("Maximum number:", maximum)

#4. Print even numbers from list

print("Even numbers in the list:")
for n in numbers:
    if n % 2 == 0:
        print(n)

#5. Reverse a list

reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)

#Task 3

#1. Create student dictionary (name, age, marks)

student = {
    "name": "Arun",
    "age": 20,
    "marks": 85
}

print(student)

#2. Update marks

student["marks"] = 92
print("Updated marks:", student["marks"])

#3. Add new key (grade)

student["grade"] = "A"
print(student)

#4. Print all keys and values

for key, value in student.items():
    print(key, ":", value)

#Task 4

#1. Count number of characters

text = "Artificial Intelligence"

count = 0
for ch in text:
    count += 1

print("Number of characters:", count)

#2. Reverse a string

reversed_text = text[::-1]
print("Reversed string:", reversed_text)

#3. Check if string is palindrome

if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#4. Count vowels

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"

count = 0
for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)

#Task 5

#1. Remove duplicates from list using set

numbers = [5, 12, 7, 20, 3, 14, 9, 2, 18, 11, 5, 12]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

#2. Find common elements between two sets

set1 = {5, 12, 7, 20, 3}
set2 = {7, 3, 15, 20, 9}
common = set1.intersection(set2)

print("Common elements:", common)
set(numbers)

#Task 6

#1. Create list of squares from 1–10

squares = [n*n for n in range(1, 11)]
print("Squares:", squares)

#2. Create list of even numbers from 1–20

even_numbers = [n for n in range(1, 21) if n % 2 == 0]
print("Even numbers:", even_numbers)


