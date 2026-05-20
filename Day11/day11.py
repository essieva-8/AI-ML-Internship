#Task 2

#1. Create class Animal

class Animal:
    def __init__(self, name):
        self.name = name

#2. Create class Dog inheriting Animal

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

#3. Add method sound()

    def sound(self):
        return "Woof!"  

d = Dog("Tomy", "Golden Retriever")
print(d.sound())


#Task 3

#Parent class → Vehicle, Child class → Car, Override method start()

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.start()


#Task 4

#Create class BankAccount, make balance private and create methods: deposit, withdraw, check balance

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.__balance


b = BankAccount(1000)
b.deposit(500)
b.withdraw(300)
print(b.check_balance())


#Task 5

#1. Create: Class Person

class Person:
    def __init__(self, name):
        self.name = name

#2. Create: Class Employee(inherits Person). Add name, salary, and display details.

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

e = Employee("Alice", 50000)
e.display()
