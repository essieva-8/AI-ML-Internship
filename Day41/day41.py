#Tasks 2,3,4,5

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#1. Student Result Dataset

data = {
    "Study_Hours":[1,2,3,4,6,7,8],
    "Result":[0,0,0,0,1,1,1]
}

df = pd.DataFrame(data)

print("Student Dataset")
print(df)

X = df[["Study_Hours"]]
y = df["Result"]

for trees in [10,50,100]:

    model = RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )

    model.fit(X,y)
    prediction = model.predict([[5]])

    print(f"\nTrees = {trees}")
    print("Prediction for 5 Study Hours:",prediction)
    

#2. Disease Dataset

data = {
    "Temperature":[98,99,100,101,102,103],
    "Disease":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)

print("Disease Dataset")
print(df)

X = df[["Temperature"]]
y = df["Disease"]

for trees in [10,50,100]:

    model = RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )

    model.fit(X,y)

    prediction = model.predict([[101]])

    print(f"\nTrees={trees}")
    print("Disease status:",prediction)


#3. Loan Approval Dataset

data = {
    "Income":[20000,30000,40000,50000,60000,70000,80000],
    "Loan_Status":[0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

print("Loan Approval Dataset")
print(df)

X = df[["Income"]]
y = df["Loan_Status"]

for trees in [10,50,100]:

    model = RandomForestClassifier(
        n_estimators=trees,
        random_state=42
    )

    model.fit(X,y)
    prediction = model.predict([[65000]])

    print(f"\nTrees={trees}")
    print("Loan Approval Status:",prediction)




