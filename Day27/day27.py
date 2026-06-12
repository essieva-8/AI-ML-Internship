import  pandas as pd

#Task 2

#1. Create CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Marks': [78, 90, 85, 60, 95],                                
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']
}
df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)

#2. Read CSV file using pandas
df = pd.read_csv('students.csv')

#3. Print dataset
print(df)


#Task 3

#1. Select single column
print(df["Name"])

#2. Select multiple columns
print(df[["Name", "City"]])

#3. Print specific column values
print(df.loc[3, "Marks"])
print(df.iloc[1, 2])


#Task 4

#1. Select row using loc
print(df.loc[0]) 

#2. Select row using iloc
print(df.iloc[1])

#3. Slice rows
print(df[2:5])


#Task 5

#1. Filter marks > 80
print(df[df["Marks"] > 80])

#2. Filter city names
print(df[df["City"] == "New York"])

#3. Combine conditions
print(df[(df["Marks"] > 80) & (df["City"] == "New York")])