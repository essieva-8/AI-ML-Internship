#Task 1

data = [
    [1, "Hi", "Greeting"],
    [2, "Hello", "Greeting"],
    [3, "Good morning", "Greeting"],
    [4, "Hey there", "Greeting"],
    [5, "Bye", "Goodbye"],
    [6, "See you later", "Goodbye"],
    [7, "Track my order", "Order Tracking"],
    [8, "Where is my order?", "Order Tracking"],
    [9, "Where is my package?", "Order Tracking"],
    [10, "Check my order status", "Order Tracking"],
    [11, "Cancel my order", "Order Cancellation"],
    [12, "I want to cancel my order", "Order Cancellation"],
    [13, "Refund my payment", "Refund"],
    [14, "I want a refund", "Refund"],
    [15, "Please refund my money", "Refund"]
]

print("No. | User Message              | Intent")
print("-" * 55)

for row in data:
    print(f"{row[0]:<3} | {row[1]:<25} | {row[2]}")


#Task 2

messages = [
    "Where is my order?",
    "Cancel my booking.",
    "Hi!",
    "Refund my money."
]

intents = [
    "Order Tracking",
    "Order Cancellation",
    "Greeting",
    "Refund"
]

for i in range(len(messages)):
    print("User Message:", messages[i])
    print("Intent:", intents[i])
    print()


#Task 3

training_data = [
    ["What courses are available?", "Course Enquiry"],
    ["Which courses does the college offer?", "Course Enquiry"],
    ["Tell me about the available programmes.", "Course Enquiry"],
    ["What can I study at this college?", "Course Enquiry"],

    ["How can I apply for admission?", "Admission Enquiry"],
    ["What is the admission procedure?", "Admission Enquiry"],
    ["How do I get admission?", "Admission Enquiry"],
    ["When does admission start?", "Admission Enquiry"],

    ["What is the college fee?", "Fee Enquiry"],
    ["How much is the tuition fee?", "Fee Enquiry"],
    ["Tell me about the course fees.", "Fee Enquiry"],
    ["What are the fees for the programme?", "Fee Enquiry"],

    ["Is hostel accommodation available?", "Hostel Enquiry"],
    ["Does the college provide hostel facilities?", "Hostel Enquiry"],
    ["How can I apply for the hostel?", "Hostel Enquiry"],
    ["Is there a hostel for students?", "Hostel Enquiry"],

    ["What are the college timings?", "College Timings"],
    ["When does the college open?", "College Timings"],
    ["What time do classes start?", "College Timings"],
    ["What are the working hours?", "College Timings"],

    ["Where is the college located?", "Location Enquiry"],
    ["What is the college address?", "Location Enquiry"],
    ["How can I reach the college?", "Location Enquiry"],
    ["Where can I find the college?", "Location Enquiry"],

    ["Is the college open today?", "General Enquiry"]
]

print("No. | User Message                              | Intent")
print("-" * 75)

for i, data in enumerate(training_data, 1):
    print(f"{i:<3} | {data[0]:<42} | {data[1]}")


#Task 4

training_data = {
    "hello": "Greeting",
    "hi": "Greeting",
    "good morning": "Greeting",
    "bye": "Goodbye",
    "see you": "Goodbye",
    "track order": "Order Tracking",
    "where is my order": "Order Tracking",
    "cancel my order": "Order Cancellation",
    "refund": "Refund"
}

user = input("You: ").lower()

found = False

for text, intent in training_data.items():
    if text in user:
        print("Predicted Intent:", intent)
        found = True
        break

if not found:
    print("Intent not recognized.")


#Task 5

print("Training Dataset")
print("       ↓")
print("Text Preprocessing")
print("       ↓")
print("Feature Extraction")
print("       ↓")
print("Machine Learning Model")
print("       ↓")
print("Intent Prediction")
print("       ↓")
print("Generate Response")