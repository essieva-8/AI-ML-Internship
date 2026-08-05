#Task 1

print("AI Assistant")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "your name":
        print("Bot: I'm an AI Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")


#Task 2

print("===================================")
print("   College Enquiry Chatbot")
print("===================================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Welcome to our college.")

    elif user == "fees":
        print("Bot: The course fee is ₹15,000.")

    elif user == "duration":
        print("Bot: The course duration is 3 months.")

    elif user == "location":
        print("Bot: Our college is located in Kochi.")

    elif user == "admission":
        print("Bot: Admissions are open now.")

    elif user == "contact":
        print("Bot: You can contact the college office for more information.")

    elif user == "bye":
        print("Bot: Thank you! Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")


#Tasks 3, 4, 5

print("======================================")
print("       COLLEGE ENQUIRY CHATBOT")
print("======================================")
print("Type 'bye' to exit.\n")

# Task 3: Dictionary
faq = {
    "fees": "Course fee is ₹15,000.",
    "duration": "Course duration is 3 months.",
    "location": "We are located in Kochi.",
    "contact": "Call us at 9876543210.",
    "admission": "Admissions are open now.",
    "courses": "We offer various courses."
}


while True:

    user = input("You: ").lower()

    # Exit
    if user == "bye":
        print("Bot: Thank you! Goodbye!")
        break

    # Greeting
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! Welcome to our college.")
        continue

    # Task 4: Keyword Matching
    found = False

    for key in faq:

        if key in user:
            print("Bot:", faq[key])
            found = True
            break

    # Task 5: Default Response
    if not found:
        print("Bot: Sorry! Please contact our office.")