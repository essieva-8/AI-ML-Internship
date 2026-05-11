#Task 2

text = "machine learning"

#1. Reverse a string
print(text[::-1])

#2. Count number of words
words = text.split(" ")
print(len(words))

#3. Check palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#4. Replace words
print(text.replace("learning", "intelligence"))

#5. Count vowels
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print(count)

#Task 3

#1. Create a list of 5 students 
students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 85},
    {"name": "C", "marks": 90},
    {"name": "D", "marks": 60},
    {"name": "E", "marks": 78}
]

#2. Print all students
for s in students:
    print(s)

#3. Find average marks
total = 0
for s in students:
    total += s["marks"]
avg = total / len(students)
print("Average:", avg)

#4. Find highest marks
highest = 0
for s in students:
    if s["marks"] > highest:
        highest = s["marks"]
print("Highest:", highest)

#5. Print students with marks > 75
for s in students:
    if s["marks"] > 75:
        print(s["name"])

#Task 4 

import math
import random

#1. Use math modulle to calculate square root and power
print(math.sqrt(25))
print(math.pow(2, 3))

#2. Use random module to generate random numbers and select random elements
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))

#3. Creating your own module

#See mymodule.py for the code of the module

import mymodule
print(mymodule.greet("Essie"))

#Task 5

nums = [10, 20, 30, 40, 30, 20]

#1. Second highest number
nums_unique = list(set(nums))
nums_unique.sort()
print(nums_unique[-2])

#2. Count frequency of characters
text = "helloworld"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

#3. Remove duplicates
unique = list(set(nums))
print(unique)



