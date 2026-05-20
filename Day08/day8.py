#Task 2

#1. Function to find factorial

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))  

#2. Function to check prime number

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  

#3. Function to reverse string

def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

#4. Function to calculate average

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(calculate_average([1, 2, 3, 4, 5]))


#Task 3

#1. Factorial using Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#2. Sum of Numbers using Recursion

def sum_of_nums(n):
    if n == 0:
        return 0
    return n + sum_of_nums(n-1)
print(sum_of_nums(5))

#3. Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')
print()


#Task 4

#1. Lambda function to find squares

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)

#2. Double all values

nums = [1, 2, 3]
doubles = list(map(lambda x: x*2, nums))
print(doubles)

#3. Convert list to uppercase

words = ["ai", "ml", "python"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)


#Task 5

#1. Filter even numbers

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

#2. Filter students with marks > 50

students = [
    {"name": "Alice", "marks": 60},
    {"name": "Bob", "marks": 40},
    {"name": "Charlie", "marks": 85}
]
filtered_students = list(filter(lambda s: s["marks"] > 50, students))
print(filtered_students)

#3. Filter words with length > 5

words = ["hello", "world", "python", "programming"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)


#Task 6

#1. Sum of digits using recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)  
print(sum_of_digits(12345))

#2. Flatten nested list

def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(nested_list))

#3. Count occurrences using dictionary

def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict
        
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_occurrences(items))
