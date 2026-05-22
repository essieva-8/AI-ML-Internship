#Task 2

#Error 1 
#print("Hello"

print("Hello")

#Error 2
#x = int("abc")

try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")


#Error 3
#nums = [1, 2, 3]
#print(nums[5])

nums = [1, 2, 3]
try:
    print(nums[5])
except IndexError:
    print("Index out of bounds")


#Task 3

#1. Replace Loops with Built-in Functions

#Using a loop
nums = [1, 2, 3, 4]
total = 0
for i in nums:
    total += i
print(total)

#Using a built-in function
nums = [1, 2, 3, 4]
print(sum(nums))

#2. Optimize Sorting

#Before
nums = [5, 2, 1, 4]
nums.sort()
print(nums)

#After 
sorted_nums = sorted([5, 2, 1, 4])
print(sorted_nums)

#3. Reduce Repeated Code

#Before
print(sum([1, 2, 3]))
print(sum([4, 5, 6]))

#After
def get_sum(numbers):
    return sum(numbers)

print(get_sum([1, 2, 3]))
print(get_sum([4, 5, 6]))


#Task 4

#1. Convert: Long code → functions

#Before
nums = [1, 2, 3, 4]
total = 0
for i in nums:
    total += i
print(total)

#After
def calculate_sum(numbers):
    return sum(numbers)

nums = [1, 2, 3, 4]
print(calculate_sum(nums))

#2. Convert: Repeated logic → reusable function

#Before
a = [1, 2, 3]
b = [4, 5, 6]
print(sum(a))
print(sum(b))

#After
def get_sum(numbers):
    return sum(numbers) 

a = [1, 2, 3]
b = [4, 5, 6]
print(get_sum(a))
print(get_sum(b))
