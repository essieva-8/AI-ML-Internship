# Task 2

#1. Print personal details

name = "Essie V Ayrookuzhy"
age = 24
course = "M.Tech Data Science and Analytics"

print("Name:", name)
print("Age:", age)
print("Course:", course)

#2. Add, subtract, multiply two numbers

num1 = 10
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

#3. Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#4. Find the largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)

#5. Take input and display it

text = input("Enter something: ")
print("You entered:", text)

#Task 3

#1. Check whether a number is positive, negative, or zero

num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

#2. Find the largest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#3. Grade system based on marks

marks = int(input("Enter marks: "))

if marks > 90:
    print("Grade: A")
elif marks >= 70 and marks <= 90:
    print("Grade: B")
else:
    print("Grade: C")

# Task 4

#1. Print numbers from 1 to 20

for i in range(1, 21):
    print(i)

#2. Print even numbers (from 1 to 20)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#3. Print sum of first N numbers

n = int(input("Enter value of N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "numbers is:", total)

#4. Reverse numbers from 10 to 1

for i in range(10, 0, -1):
    print(i)

#Task 5

#1. Function to add two numbers

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("Sum:", result)

#2. Function to check whether a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("It is a Prime number")
else:
    print("It is not a Prime number")

#3. Function to find factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

#Task 7

#1. Print pattern

for i in range(1, 5):
    print("*" * i)

#2. Reverse a number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)


#3. Count digits in a number

num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)