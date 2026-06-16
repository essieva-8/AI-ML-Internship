#Task 2

import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera", "Priya"],
    "Department": ["AI", "Web", "AI", "Web", "AI"],
    "Salary": [50000, 40000, 60000, 45000, 55000],
    "City": ["Delhi", "Chennai", "Bangalore", "Chennai", "Mumbai"],
    "Category": ["A", "B", "A", "B", "C"]
}

df = pd.DataFrame(data)

# 1. Sort salary ascending
print(df.sort_values("Salary"))

# 2. Sort salary descending
print(df.sort_values("Salary", ascending=False))

# 3. Sort by multiple columns
print(df.sort_values(["Department", "Salary"]))


#Task 3

#1. Group by Department
print(df.groupby("Department"))

#2. Group by City
print(df.groupby("City"))

#3. Group by Category
print(df.groupby("Category"))


#Task 4

#1. Find Average Salary
print(df.groupby("Department")["Salary"].mean())

#2. Find Total Salary
print(df.groupby("Department")["Salary"].sum())

#3. Count Employees
print(df.groupby("Department")["Name"].count())


#Task 5

#Find mean, max and min
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))


#Task 6

#1. Count Departments
print(df["Department"].nunique())

#2. Count Repeated Values
print(df["Department"].value_counts())

#3. Analyse Category Frequency
print(df["Category"].value_counts())