#Task 2

#1. Create a class Car with variables: name and price.

class Car:
    name = ""
    price = 0

#2. Create an object and print the values.

c1 = Car()
c1.name = "BMW"
c1.price = 5000000

print("Car:", c1.name, "\nPrice:", c1.price)


#Task 3

#Create class Student, initialize name & marks and print details

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Alice", 85)
print("Name:", s1.name, "\nMarks:", s1.marks)


#Task 4

#Create method to: 1. Check pass/fail  2. Calculate grade

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

s1 = Student("Rahul", 76)
print("Result:", s1.is_pass())
print("Grade:", s1.grade())


#Task 5

#1.Create list of students

students = [
    Student("John", 80),
    Student("Sara", 90),
    Student("Alex", 70),
    Student("Mia", 85),
    Student("Raj", 60)
]

#2. Print all students

for s in students:    
    print("Name:", s.name, ", Marks:", s.marks)

#3. Find topper

topper = max(students, key=lambda s: s.marks)
print("\nTopper:", topper.name, "with marks", topper.marks)


#Task 6

#1. Create class BankAccount with methods: deposit, withdraw, check balance

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.check_balance())

#2. Create class Product with attributes: name, price and calculate discount.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, discount_percent):
        discount = self.price * discount_percent / 100
        return self.price - discount

p1 = Product("Laptop", 50000)
print("Discounted Price:", p1.discount_price(20))
