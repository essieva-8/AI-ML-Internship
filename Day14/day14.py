#Task 2

#1. Convert Dictionary to JSON

import json

data = {    "name": "John",    "age": 30,
    "city": "New York"  }
json_data = json.dumps(data)
print(json_data)

#2. Convert JSON to Dictionary

json_data = '{"name": "John", "age": 30, "city": "New York"}'   
data = json.loads(json_data)
print(data)

#3. Write JSON to a file

data = {    "name": "John",    "age": 30,
    "city": "New York"  }
with open('data.json', 'w') as file:
    json.dump(data, file)
print("Data written to data.json")

#4. Read JSON from file

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)


#Task 3

#Create CSV File & Write Student Data

import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 30, "New York"])
    writer.writerow(["Jane", 25, "Los Angeles"])
print("Data written to data.csv")

#Read CSV File & Print Formatted Output

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")


#Task 4

#Read CSV → Convert to Dictionary → Save as JSON

import csv
import json
data_list = []

#Read CSV
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data_list.append(row)

#Save as JSON
with open("data.json", "w") as file:
    json.dump(data_list, file)

print("CSV data converted to JSON successfully!")
