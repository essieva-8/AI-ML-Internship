#Task 2

#1. Create list of marks

marks = [85, 90, 78, 92, 88]

#2. Find average mark

avg=sum(marks) / len(marks)
print("Average mark:", avg)

#3. Find max and min marks

max_mark = max(marks)
min_mark = min(marks)           
print("Maximum mark:", max_mark)
print("Minimum mark:", min_mark)

#4. Count total students

count = len(marks)
print("Total students:", count)


#Task 3

#1. Remove None values

marks = [80, 90, None, 70]
cleaned = [m for m in marks if m is not None]
print("Cleaned data:", cleaned)

#2. Remove negative values

nums = [10, -5, 20, -2, 30]
cleaned = [n for n in nums if n >= 0]
print("Cleaned data:", cleaned)

#3. Clean invalid data

data = [50, "hello", 70, None, 90]

cleaned_data = [x for x in data if type(x) == int]
print("Valid Data:", cleaned_data)


#Task 4

#1. Find passed students

marks = [80, 40, 90, 31, 75, 68]

passed = [m for m in marks if m >= 50]
print("Passed Students:", passed)

#2. Filter marks > 75

above_75 = [m for m in marks if m > 75]
print("Marks Above 75:", above_75)

#3. Filter even numbers

even = [m for m in marks if m % 2 == 0]
print("Even Numbers:", even)


#Task 5

#1. Convert marks to percentage

marks = [80, 90, 75, 68]
scaled = [m / 100 for m in marks]
print("Percentage:", scaled)

#2. Multiply values

multiplied = [m * 10 for m in marks]
print("Multiplied Values:", multiplied)

#3. Normalize data

normalized = [m / max(marks) for m in marks]
print("Normalized Data:", normalized)