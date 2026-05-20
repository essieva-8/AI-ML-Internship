#Section B

#1. Check Palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#2. Largest Number in List

nums = [10, 45, 67, 23, 89]

largest = max(nums)
print("Largest number:", largest)

#3. Count Vowels in String

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)

#4. Create Dictionary and Print Values

student = {
    "name": "Asha",
    "age": 20,
    "grade": "A"
}
for value in student.values():
    print(value)


#Section C

 # Take 5 student marks and store in list
 # Calculate average and topper mark

marks = []

for i in range(5):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

average = sum(marks) / len(marks)
topper = max(marks)

print("Marks:", marks)
print("Average:", average)
print("Topper mark:", topper)


#Task 1

#1. Reverse List

lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)

#2. Count Words in String

text = input("Enter a sentence: ")
words = text.split()
print("Word count:", len(words))

#3. Remove Duplicates

nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)

#4. Second Largest Number

lst = [10, 20, 45, 67, 89]
lst.sort()
print("Second largest:", lst[-2])
