import seaborn as sns 
import matplotlib.pyplot as plt
 
#Task 2

#1. Create line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

sns.lineplot(x=x, y=y)
plt.title("Line Plot")
plt.show()

#2. Add style
sns.set_style("darkgrid")

sns.lineplot(x=x, y=y)
plt.title("Line Plot")
plt.show()

#3. Compare data trends
months = [1, 2, 3, 4, 5]
sales1 = [10, 20, 30, 40, 50]
sales2 = [15, 25, 35, 45, 55]

sns.lineplot(x=months, y=sales1, label="Product A")
sns.lineplot(x=months, y=sales2, label="Product B")
plt.title("Compare Data Trends")
plt.legend()
plt.show()


#Task 3

#1. Student Marks Comparison
students = ["A", "B", "C", "D"]
marks = [85, 90, 78, 92]

sns.barplot(x=students, y=marks)
plt.title("Student Marks Comparison")
plt.show()

#2. Sales Comparison
products = ["Laptop", "Mobile", "Tablet"]
sales = [120, 180, 90]

sns.barplot(x=products, y=sales)
plt.title("Sales Comparison")
plt.show()

#3. Employee Salary Comparison
employees = ["John", "Sara", "David"]
salary = [40000, 55000, 50000]

sns.barplot(x=employees, y=salary)
plt.title("Employee Salary Comparison")
plt.show()


#Task 4

#1. Height vs Weight
height = [150, 160, 170, 180, 190]
weight = [50, 60, 65, 75, 85]

sns.scatterplot(x=height, y=weight)
plt.title("Height vs Weight")
plt.show()

#2. Study Hours vs Marks
hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 75, 90]

sns.scatterplot(x=hours, y=marks)
plt.title("Study Hours vs Marks")
plt.show()

#3. Temperature vs Sales
temperature = [20, 25, 30, 35, 40]
sales = [100, 120, 150, 180, 200]

sns.scatterplot(x=temperature, y=sales)
plt.title("Temperature vs Sales")
plt.show()


#Task 5

#Create histogram, Analyze frequency, Use random dataset
import numpy as np

data = np.random.randint(1, 100, 100)

sns.histplot(data)
plt.title("Histogram")
plt.show()


#Task 6

#1. Detect outliers
data = [10, 20, 30, 40, 50, 100]

sns.boxplot(x=data)
plt.title("Outlier Detection")
plt.show()

#2. Analyze salary dataset
salary = [25000, 30000, 35000, 40000, 45000, 100000]

sns.boxplot(x=salary)
plt.title("Salary Dataset Analysis")
plt.show()

#3. Analyze marks dataset
marks = [55, 60, 65, 70, 75, 80, 95]

sns.boxplot(x=marks)
plt.title("Marks Dataset Analysis")
plt.show()


#Task 7

#1. Course Count
courses = ["AI", "Web", "AI", "Cloud", "AI"]

sns.countplot(x=courses)
plt.title("Course Count")
plt.show()

#2. Department Count
departments = ["IT", "HR", "IT", "Finance", "HR", "IT"]

sns.countplot(x=departments)
plt.title("Department Count")
plt.show()

#3. Product Category Count
categories = ["Electronics", "Clothing", "Electronics",
              "Books", "Clothing", "Electronics"]

sns.countplot(x=categories)
plt.title("Product Category Count")
plt.show()
