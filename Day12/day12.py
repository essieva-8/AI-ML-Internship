#Task 2

#1. Square Numbers

nums = [1, 2, 3, 4, 5]
squares = [x * x for x in nums]
print(squares)

#2. Find Even Numbers

nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
print(even)

#3. Convert Strings to Uppercase

names = ["ai", "ml", "python"]
upper = [n.upper() for n in names]
print(upper)

#4. Filter Numbers > 50

nums = [10, 25, 60, 80, 45, 90]
greater = [x for x in nums if x > 50]
print(greater)


#Task 3

#1. Create Number-Square Dictionary 

nums = [1, 2, 3, 4, 5]
square_dict = {x: x * x for x in nums}
print(square_dict)

#2. Filter Even Numbers

nums = [1, 2, 3, 4, 5, 6]
even_dict = {x: x * x for x in nums if x % 2 == 0}
print(even_dict)

#3. Map Names to Lengths

names = ["AI", "Machine", "Python"]
lengths = {name: len(name) for name in names}
print(lengths)


#Task 4

#1. Remove Duplicates

nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print(unique)

#2. Find Common Elements

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)

#3. Find Union and Difference

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a - b)


#Task 5

#1. Create Generator for Numbers

def numbers(n):
    for i in range(n):
        yield i

for num in numbers(5):
    print(num)

#2. Generate Even Numbers

def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

#3. Fibonacci Using Generator

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)


#Task 6

#1. Combine 2 Lists

names = ["A", "B", "C"]
marks = [80, 90, 95]
combined = list(zip(names, marks))
print(combined)

#2. Print Index + Value

names = ["AI", "ML", "Python"]

for i, name in enumerate(names):
    print(i, name)

#3. Convert Zip Result to Dictionary

names = ["A", "B", "C"]
marks = [80, 90, 95]
result = dict(zip(names, marks))
print(result)
