#Task 2

#1. Create marks prediction dataset

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 45, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[7]])
print("Predicted Marks:", prediction)

#2. Predict salary

data = {
    "Experience": [1,2,3,4,5,6,7],
    "Salary": [25000,30000,36000,42000,50000,57000,65000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[8]])
print("Predicted Salary:", prediction)

#3. Predict sales values

data = {
    "Advertising": [10,20,30,40,50,60],
    "Sales": [100,180,260,340,420,500]
}

df = pd.DataFrame(data)

X = df[["Advertising"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[70]])
print("Predicted Sales:", prediction)


#Task 3

#1. Pass/fail prediction

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Hours": [1,2,3,4,5,6],
    "Result": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[7]])
if prediction == 1:
    print(prediction,"-Pass")
else:
    print(prediction,"-Fail")

#2. Spam/not spam example

data = {
    "Keyword_Count": [1,2,3,6,8,10],
    "Spam": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Keyword_Count"]]
y = df["Spam"]

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[7]])

if prediction == 1:
    print(prediction, "-Spam Email")
else:
    print(prediction, "-Not Spam")

#3. Disease prediction example

data = {
    "Temperature": [97,98,99,100,101,102],
    "Disease": [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Temperature"]]
y = df["Disease"]

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[101]])

if prediction == 1:
    print(prediction, "-Disease Detected")
else:
    print(prediction, "-Healthy")


#Task 4

#| Problem                           | Type           |
#| --------------------------------- | -------------- |
#| House Price Prediction            | Regression     |
#| Face Recognition                  | Classification |
#| Weather Forecasting               | Regression     |
#| Fraud Detection                   | Classification |
#| Student Marks Prediction          | Regression     |


#Task 5

#1. Create regression dataset, Identify features & labels

data = {
    "Experience (Years)": [1, 2, 3, 4, 5, 6],
    "Salary": [25000, 32000, 40000, 48000, 56000, 65000]
}

df = pd.DataFrame(data)

print("Regression Dataset")
print(df)

# Features and Labels
X = df[["Experience (Years)"]]
y = df["Salary"]

print("\nFeature (X):")
print(X)

print("\nLabel (y):")
print(y)

#2. Create classification dataset, Identify features & labels

data = {
    "Study Hours": [1, 2, 3, 4, 5, 6],
    "Result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

print("Classification Dataset")
print(df)

# Features and Labels
X = df[["Study Hours"]]
y = df["Result"]

print("\nFeature (X):")
print(X)

print("\nLabel (y):")
print(y)


#Task 6

#1. Explain why salary prediction is regression

# Salary prediction is a regression problem because the output is a continuous numerical value. Salaries can take many different values such as ₹25,000, ₹37,500, or ₹62,800, rather than belonging to fixed categories.

#2. Explain why spam detection is classification

# Spam detection is a classification problem because the output belongs to one of two categories: Spam or Not Spam. The model predicts a class label instead of a numerical value.

#3. Compare output types

#| Regression Output | Classification Output   |
#| ----------------- | ----------------------- |
#| Predicts numbers  | Predicts categories     |
#| Continuous values | Discrete labels         |
#| Example: Salary   | Example: Spam Detection |
#| Output: ₹50,000   | Output: Spam / Not Spam |

