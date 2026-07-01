#Tasks 2,3,4,5

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

#1. Student result dataset

student = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Result": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(student)

print("Student Dataset")
print(df)

# Features and Labels
X = df[["Study_Hours"]]
y = df["Result"]

# Train Model (K = 3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print("\nPrediction for 5 Study Hours:", prediction)

if prediction[0] == 1:
    print("Result : Pass")
else:
    print("Result : Fail")

# Experiment with Different K Values
print("\nComparison of Different K Values")

for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    pred = model.predict([[5]])
    print("K =", k, "Prediction =", pred)


#2. Disease dataset

disease = {
    "Temperature": [98,99,100,101,102,103],
    "Disease": [0,0,0,1,1,1]
}

df = pd.DataFrame(disease)

print("Disease Dataset")
print(df)

# Features and Labels
X = df[["Temperature"]]
y = df["Disease"]

# Train Model (K = 3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Prediction
prediction = model.predict([[102]])
print("\nPrediction for Temperature 102°F:", prediction)

if prediction[0] == 1:
    print("Disease Detected")
else:
    print("Healthy")

# Experiment with Different K Values
print("\nComparison of Different K Values")

for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    pred = model.predict([[102]])
    print("K =", k, "Prediction =", pred)


#3. Loan approval dataset

loan = {
    "Income": [20000,25000,30000,40000,50000,60000],
    "Approved": [0,0,0,1,1,1]
}

df = pd.DataFrame(loan)

print("Loan Dataset")
print(df)

# Features and Labels
X = df[["Income"]]
y = df["Approved"]

# Train Model (K = 3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Prediction
prediction = model.predict([[45000]])
print("\nPrediction for Income = 45000:", prediction)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

# Experiment with Different K Values
print("\nComparison of Different K Values")

for k in [1,3,5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    pred = model.predict([[45000]])
    print("K =", k, "Prediction =", pred)


#Task 5 - Customer Category dataset

customer = {
    "Purchase":[1000,2000,3000,6000,7000,8000],
    "Category":[0,0,0,1,1,1]
}

df = pd.DataFrame(customer)

X = df[["Purchase"]]
y = df["Category"]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

prediction = model.predict([[6500]])
print(prediction)

if prediction[0]==1:
    print("Premium Customer")
else:
    print("Regular Customer")

