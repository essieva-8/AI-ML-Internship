import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Tasks 2, 3, 4, 5, 6

# ==========================
# STUDENT DATASET
# ==========================

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [20, 30, 40, 50, 60, 70, 75, 85, 90, 95]
}

df = pd.DataFrame(data)

print("Student Dataset")
print(df)

# Features and Labels
X = df[["Hours"]]
y = df["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data")
print(X_train)

print("\nTesting Data")
print(X_test)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nActual vs Predicted")
print(results)

# Accuracy Score
accuracy = model.score(X_test, y_test)
print("\nAccuracy Score:", accuracy)


#Result Analysis 

#Good Predictions: Predicted marks are very close to the actual marks, indicating that the model has learned the relationship between study hours and marks effectively.
#Prediction Errors: Any difference between the actual marks and the predicted marks is called a prediction error. Smaller errors indicate better model performance.
#Accuracy Meaning: An accuracy score close to 1 indicates that study hours are a strong predictor of marks and that the model performs well on unseen data.


# ==========================
# SALARY DATASET
# ==========================

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [25000, 30000, 35000, 40000, 45000,
               50000, 55000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)

print("Salary Dataset")
print(df)

# Features and Labels
X = df[["Experience"]]
y = df["Salary"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Actual vs Predicted
result = pd.DataFrame({
    "Actual Salary": y_test.values,
    "Predicted Salary": predictions
})

print("\nActual vs Predicted")
print(result)

# Accuracy Score
score = model.score(X_test, y_test)
print("\nAccuracy Score:", score)


#Result Analysis 

#Good Predictions: Predicted salaries are very close to actual salaries.
#Prediction Errors: Any difference between actual and predicted salary values is a prediction error.
#Accuracy Meaning: An accuracy score close to 1 indicates that experience is a strong predictor of salary.


# ==========================
# SALES DATASET
# ==========================

data = {
    "Advertising": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "Sales": [100, 150, 200, 250, 350, 400, 450, 500, 600, 650]
}

df = pd.DataFrame(data)

print("Sales Dataset")
print(df)

# Features and Labels
X = df[["Advertising"]]
y = df["Sales"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Actual vs Predicted
result = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": predictions
})

print("\nActual vs Predicted")
print(result)

# Accuracy Score
score = model.score(X_test, y_test)
print("\nAccuracy Score:", score)


#Result Analysis

#Good Predictions: Predicted sales values are very close to actual sales values.
#Prediction Errors: The difference between actual sales and predicted sales represents the prediction error.
#Accuracy Meaning: A score near 1 indicates that advertising expenditure strongly influences sales and the model performs well.