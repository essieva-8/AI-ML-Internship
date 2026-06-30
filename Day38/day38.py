#Tasks 2,3,4,5

import pandas as pd
from sklearn.linear_model import LogisticRegression

#1. Pass/Fail Dataset

data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Result": [0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features and Labels
X = df[["Study_Hours"]]
y = df["Result"]

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print("\nPrediction for 5 Study Hours:", prediction)

# Probability
probability = model.predict_proba([[5]])
print("\nProbability:", probability)

#Prediction 1 means Pass.
#Probability 0.15 represents the chance of Fail (15%).
#Probability 0.85 represents the chance of Pass (85%).
#Since the Pass probability is higher, the model predicts Pass.


#2. Disease Dataset

data = {
    "Temperature": [98,99,100,101,102,103,104],
    "Disease": [0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features and Labels
X = df[["Temperature"]]
y = df["Disease"]

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[102]])
print("\nPrediction for Temperature 102:", prediction)

# Probability
probability = model.predict_proba([[102]])
print("\nProbability:", probability)

#Prediction 1 means Disease Detected.
#15% probability indicates No Disease.
#85% probability indicates Disease Present.
#Since the Disease probability is higher, the model predicts Disease Present.


#3. Spam Dataset

data = {
    "Spam_Words": [0,1,2,3,4,5,6],
    "Spam": [0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

# Features and Labels
X = df[["Spam_Words"]]
y = df["Spam"]

# Train Model
model = LogisticRegression()
model.fit(X, y)

# Prediction
prediction = model.predict([[5]])
print("\nPrediction for Spam Words = 5:", prediction)

# Probability
probability = model.predict_proba([[5]])
print("\nProbability:", probability)

#Prediction 1 means the message is Spam.
#5% probability indicates Not Spam.
#95% probability indicates Spam.
#Since the Spam probability is higher, the model predicts Spam.


#Task 6

#| Problem                | Logistic Regression? | Reason                     |
#| ---------------------- | -------------------- | -------------------------- |
#| Pass/Fail Prediction   | Yes                  | Binary Classification      |
#| House Price Prediction | No                   | Predicts continuous values |
#| Spam Detection         | Yes                  | Binary Classification      |
#| Disease Prediction     | Yes                  | Binary Classification      |
#| Salary Prediction      | No                   | Predicts continuous values |



