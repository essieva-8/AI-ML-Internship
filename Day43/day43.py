#Tasks 2,3,4

import pandas as pd
from sklearn.svm import SVC

#1. Student Result Prediction

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

# Features and Labels
X = df[["Hours"]]
y = df["Result"]

# Create SVM Model
student_model = SVC()

# Train the Model
student_model.fit(X, y)

# Make Prediction
prediction = student_model.predict([[4]])

print("Prediction for 4 Study Hours:", prediction)
print("Pass" if prediction[0] == 1 else "Fail")   


#2. Disease Prediction  

data = {
    "Temperature": [97, 98, 99, 100, 101, 102],
    "Disease": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

# Features and Labels
X = df[["Temperature"]]
y = df["Disease"]

# Create SVM Model
disease_model = SVC()

# Train the Model
disease_model.fit(X, y)

# Make Prediction
prediction = disease_model.predict([[100]])

print("Prediction for Temperature 100°F:", prediction)
print("Disease Detected" if prediction[0] == 1 else "Healthy")


#3. Spam Detection

data = {
    "Spam_Words": [1, 2, 3, 5, 7, 9],
    "Spam": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

# Features and Labels
X = df[["Spam_Words"]]
y = df["Spam"]

# Create SVM Model
spam_model = SVC()

# Train the Model
spam_model.fit(X, y)

# Make Prediction
prediction = spam_model.predict([[4]])

print("Prediction for 4 Spam Words:", prediction)
print("Spam" if prediction[0] == 1 else "Not Spam")





