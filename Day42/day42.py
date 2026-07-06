#Tasks 2,3,4

import pandas as pd
from sklearn.naive_bayes import GaussianNB

#1. Student Result Prediction

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Hours"]]
y = df["Result"]

# Create and Train Model
model = GaussianNB()
model.fit(X, y)

# Prediction
prediction = model.predict([[4]])

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")


#2. Disease Prediction

data = {
    "Temperature": [98, 99, 100, 101, 102, 103],
    "Disease": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Temperature"]]
y = df["Disease"]

# Create and Train Model
model = GaussianNB()
model.fit(X, y)

# Prediction
prediction = model.predict([[100]])

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Disease Detected")
else:
    print("Healthy")

#3. Spam Detection

data = {
    "OfferWords": [1, 2, 3, 5, 6, 7],
    "Spam": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["OfferWords"]]
y = df["Spam"]

# Create and Train Model
model = GaussianNB()
model.fit(X, y)

# Prediction
prediction = model.predict([[6]])

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Spam Email")
else:
    print("Not Spam")


#Task 5

#Given:
#Total Emails = 200
#Spam Emails = 150

#1. Probability of Spam

#P(Spam) = 150 / 200 = 0.75
#75% chance that an email is spam.

#2. Probability of Not Spam

#Number of Not Spam Emails: P(Not Spam) = 50 / 200 = 0.25
#25% chance that an email is not spam.

