import matplotlib.pyplot as plt

#Task 2

#Create a Simple Line Graph, Add Labels, Add Title
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()


#Task 3

#Add marker, Change line style, Add grid
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, linestyle="--", marker="o", label="Marks")

plt.title("Styled Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.legend()
plt.grid()
plt.show()


#Task 4

#1. Student Marks Comparison
students = ["A", "B", "C", "D"]
marks = [80, 90, 75, 85]

plt.bar(students, marks)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

#2. Sales Comparison
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [200, 300, 250, 400]

plt.bar(months, sales)

plt.title("Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

#3. Product Comparison
products = ["Laptop", "Mobile", "Tablet"]
sales = [50, 80, 40]

plt.bar(products, sales)

plt.title("Product Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


#Task 5

#1. Department Distribution
data = [40, 30, 20, 10]
labels = ["IT", "HR", "Finance", "Sales"]

plt.pie(data, labels=labels)
plt.title("Department Distribution")
plt.show()

#2. Expense Analysis
expenses = [3500, 2500, 2000, 2000]
labels = ["Rent", "Food", "Travel", "Shopping"]

plt.pie(expenses, labels=labels)
plt.title("Expense Analysis")
plt.show()

#3. Course Popularity
courses = [50, 30, 15, 5]
labels = ["Python", "AI", "Web", "Cyber"]

plt.pie(courses, labels=labels)
plt.title("Course Popularity")
plt.show()


#Task 6

#1. Height vs Weight
height = [150, 160, 170, 180]
weight = [50, 65, 72, 90]

plt.scatter(height, weight)

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")
plt.show()

#2. Study Hours vs Marks
hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 75, 90]

plt.scatter(hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

#3. Temperature vs Sales
temperature = [20, 25, 30, 35, 40]
sales = [100, 140, 200, 260, 300]

plt.scatter(temperature, sales)

plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.title("Temperature vs Sales")
plt.show()