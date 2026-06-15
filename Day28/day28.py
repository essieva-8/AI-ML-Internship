import pandas as pd
import numpy as np

# Task 2

#1. Create dataset with missing values
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}

df = pd.DataFrame(data)
print(df)

#2. Detect Missing Values
print(df.isnull())

#3. Count Missing Values
print(df.isnull().sum())


#Task 3

#1. Drop Rows with Missing Values
print(df.dropna())

#2. Drop Columns with Missing Values
print(df.dropna(axis=1))


#Task 4

#1. Fill with text
print(df.fillna("Unknown"))

#2. Fill with mean value
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)


#Task 5

#1. Create Duplicate Rows
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Rahul"],
    "Marks": [85, 90, 78, 85],
    "City": ["Kochi", "Trivandrum", "Kollam", "Kochi"]
}
df = pd.DataFrame(data)
print(df)

#2. Detect Duplicates
print(df.duplicated())

#3. Remove Duplicates
print(df.drop_duplicates())


#Task 6

#1. Rename Columns
df.rename(columns={"Marks": "Score"}, inplace=True)
print(df)

#2. Change Data Type
df["Score"] = df["Score"].astype(int)

#3. Print Data Types
print(df.dtypes)



