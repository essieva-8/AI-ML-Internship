import pandas as pd 

#Task 2

#1. Create student dataset
student_data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

df_student = pd.DataFrame(student_data)
print(df_student)

#2. Create salary dataset
salary_data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}

df_salary = pd.DataFrame(salary_data)
print(df_salary)

#3. Create sales dataset
sales_data = {
    "Month": [1, 2, 3, 4, 5],
    "Sales": [1000, 1500, 2000, 2500, 3000]
}

df_sales = pd.DataFrame(sales_data)
print(df_sales)


#Task 3

#Train linear regression model, Use fit(), Understand learning process

from sklearn.linear_model import LinearRegression

#1. Train using Student data
X = df_student[["Hours"]]
y = df_student["Marks"]

student_model = LinearRegression()
student_model.fit(X, y)
print("Model Trained Successfully")

#2. Train using Salary data
X = df_salary[["Experience"]]
y = df_salary["Salary"]

salary_model = LinearRegression()
salary_model.fit(X, y)
print("Model Trained Successfully")

#3. Train using Sales data
X = df_sales[["Month"]]
y = df_sales["Sales"]

sales_model = LinearRegression()
sales_model.fit(X, y)
print("Model Trained Successfully")


#Task 4

#1. Predict marks
student_prediction = student_model.predict(pd.DataFrame({"Hours": [6]}))
print("Predicted Marks for 6 Hours:", student_prediction)

#2. Predict Salary
salary_prediction = salary_model.predict(pd.DataFrame({"Experience": [6]}))
print("Predicted Salary for 6 Years Experience:", salary_prediction)

#3. Predict Sales values
sales_prediction = sales_model.predict(pd.DataFrame({"Month": [6]}))
print("Predicted Sales for Month 6:", sales_prediction)


#Task 5

#1. Identify input/output

#| Dataset | Input (Feature) | Output (Label) |
#| ------- | --------------- | -------------- |
#| Student | Hours           | Marks          |
#| Salary  | Experience      | Salary         |
#| Sales   | Month           | Sales          |

#2. Explain X and y

# X contains the input data(features) used for training the model.
# y contains the target values(labels) that the model should predict.

#3. Explain training logic

# Model learns the relationship between X and y. After learning the pattern, it predicts output for new input values.


#Task 6

#1. House price prediction - Predict house prices using area
data = {
    "Area": [1000, 1200, 1500, 1800, 2000],
    "Price": [4000000, 4800000, 6000000, 7200000, 8000000]
}

df = pd.DataFrame(data)
X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict(pd.DataFrame({"Area": [2200]}))

print("Predicted House Price:", prediction)

#2. Weather prediction - Predict rainfall using temperature
data = {
    "Temperature": [25, 28, 30, 32, 35],
    "Rainfall": [90, 70, 50, 30, 10]
}

df = pd.DataFrame(data)
X = df[["Temperature"]]
y = df["Rainfall"]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict(pd.DataFrame({"Temperature": [27]}))

print("Predicted Rainfall:", prediction)

#3. Employee salary prediction - Predict salary based on experience
data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)
X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict(pd.DataFrame({"Experience": [6]}))

print("Predicted Salary:", prediction)
