#Task 2

#1. Find Maximum and Minimum in a List

nums = [10, 20, 5, 40, 15, 25]

maximum = nums[0]
minimum = nums[0]

for n in nums:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print("Max:", maximum)
print("Min:", minimum)


#2. Find Second Largest

nums = [10, 20, 5, 40, 15, 25]
nums_sorted = sorted(nums)
print("Second Largest:", nums_sorted[-2])


#3. Remove Duplicates

nums = [1, 2, 2, 3, 4, 4]
unique_nums = list(set(nums))
print("Unique elements:", unique_nums)


#4. Count Even and Odd Numbers

nums = [10, 21, 34, 42, 53, 61, 72]
even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


#Task 3

#1. Reverse String

text = "python"
print("Reversed:", text[::-1])


#2. Check Palindrome

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#3. Count Characters

text = "intelligence"
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print("Character Count:", count)


#4. Count Vowels and Consonants

text = "intelligence"
vowels = "aeiou"
v = 0
c = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)


#Task 4

#1. Create Student List

students = [
    {"name": "Ayush", "marks": 70},
    {"name": "Bharat", "marks": 90},
    {"name": "Catherine", "marks": 40}
]

#2. Find Topper

topper = students[0]
for s in students:
    if s["marks"] > topper["marks"]:
        topper = s

print("Topper:", topper)


#3. Calculate Average Marks

total = 0
for s in students:
    total += s["marks"]

average = total / len(students)
print("Average Marks:", average)


#4. Filter Passed Students

passed_students = [s for s in students if s["marks"] >= 50]
print("Passed Students:", passed_students)


#Task 5

#1. Find Second Smallest Number

nums = [10, 20, 5, 40, 15, 25]
nums.sort()
print("Second Smallest:", nums[1])


#2. Merge Two Lists Without Duplicates

a = [1, 2, 3]
b = [3, 4, 5]

merged = list(set(a + b))
print("Merged List:", merged)


#3. Find Frequency of Elements

nums = [11, 22, 34, 22, 34, 22]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print("Frequency:", freq)