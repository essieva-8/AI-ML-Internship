#Task 2

students = [
    {"name": "Alice", "marks": 95},
    {"name": "Bob", "marks": None},
    {"name": "Charlie", "marks": 40},
    {"name": "David", "marks": -20},
    {"name": "Eve", "marks": 72},
    {"name": "Frank", "marks": 85}
]

#Remove None values, Remove negative values and Keep only valid data

cleaned = []

for s in students:
    if s["marks"] is not None and s["marks"] >= 0:
        cleaned.append(s)

print(cleaned)


#Task 3

#1. Add pass/fail field

for s in cleaned:
    s["status"] = "Pass" if s["marks"] >= 50 else "Fail"

#2. Convert to percentage 

for s in cleaned:
    s["percentage"] = s["marks"]

#3. New calculated field 

for s in cleaned:
    s["grade"] = "A" if s["marks"] >= 75 else "B" if s["marks"] >= 50 else "C"

print(cleaned)


#Task 4

#1. Sort students by marks

cleaned.sort(key=lambda x: x["marks"], reverse=True)
print("Sorted Students:", cleaned)

#2. Print top 3 students

print("Top 3 Students:")
for i, s in enumerate(cleaned[:3], start=1):
    print(f"{i}. {s['name']}: {s['marks']}")


#Task 5

#1. Group pass and fail

result = {"pass": [], "fail": []}

for s in cleaned:
    if s["marks"] >= 50:
        result["pass"].append(s)
    else:
        result["fail"].append(s)

print(result)

#2. Count each group

print("\nPass Count:", len(result["pass"]))
print("Fail Count:", len(result["fail"]))


#Task 6

#1. Average marks

marks = [s["marks"] for s in cleaned]
average = sum(marks) / len(marks)
print("\nAverage Marks:", average)

#2. Highest marks 

highest = max(marks)
print("Highest Marks:", highest)

#3. Lowest marks

lowest = min(marks)
print("Lowest Marks:", lowest)