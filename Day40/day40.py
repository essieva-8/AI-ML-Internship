#Task 2,3,4,5

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#1. Student result dataset

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

#Model Building
X = df[["Study_Hours"]]
y = df["Result"]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

#Prediction
prediction = model.predict([[6]])

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

#Root Node: Study_Hours
#Leaf Nodes: Pass, Fail


#2. Loan approval dataset

data = {
    "Income": [25,30,35,45,50,60,70,80],
    "Loan_Status":[0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)
print(df)
X = df[["Income"]]
y = df["Loan_Status"]

#Model Building
model = DecisionTreeClassifier(random_state=42)
model.fit(X,y)

#Prediction
prediction = model.predict([[55]])

if prediction[0]==1:
    print("Loan Approved")
else:
    print("Loan Rejected")

#Root Node: Income
#Leaf Nodes: Approved, Rejected


#3. Disease prediction dataset

data = {
    "Sugar_Level":[80,95,110,130,150,170,190,220],
    "Disease":[0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)
print(df)

X = df[["Sugar_Level"]]
y = df["Disease"]

#Model Building
model = DecisionTreeClassifier(random_state=42)
model.fit(X,y)

#Prediction
prediction = model.predict([[160]])

if prediction[0]==1:
    print("Disease Detected")
else:
    print("Healthy")

#Root Node: Sugar_Level
#Leaf Nodes: Disease, Healthy