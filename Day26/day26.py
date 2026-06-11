import  pandas as pd

#Task 2

#1. Create Series
data = pd.Series([10, 20, 30, 40])
print(data)

#2. Create Series with Custom Index
marks = pd.Series([85, 90, 78], index=["Math", "Science", "English"])
print(marks)

#3. Access Series Values
print(marks["Math"])
print(marks["Science"])


#Task 3

#1. Create DataFrame Using Dictionary
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Priya", "Sita", "Ravi"],
    "Marks": [85, 90, 78, 92, 88, 95]
}

df = pd.DataFrame(data)

#2. Print DataFrame
print(df)

#3. Add One More Column
df["Grade"] = ["A", "A+", "B", "A+", "A", "A+"]
print(df)


#Task 4

#1. Access Single Column
print(df["Name"])

#2. Access Multiple Columns
print(df[["Name", "Marks"]])

#3. Print Specific Rows
print(df.iloc[0])      # First row
print(df.iloc[1:3])    # Second and third rows


#Task 5

#1. Use head()
print(df.head())      

#2. Use tail()
print(df.tail())

#3. Use info()
print(df.info())