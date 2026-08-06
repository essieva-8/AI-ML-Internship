#Task 1

while True:

    print("\n============================")
    print("   COLLEGE ENQUIRY CHATBOT")
    print("============================")

    print("1. Course Fee")
    print("2. Course Duration")
    print("3. Eligibility")
    print("4. College Location")
    print("5. Contact Number")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Course Fee: ₹15,000")

    elif choice == "2":
        print("Course Duration: 3 Months")

    elif choice == "3":
        print("Eligibility: Plus Two Pass")

    elif choice == "4":
        print("Location: Kochi")

    elif choice == "5":
        print("Contact Number: 9876543210")

    elif choice == "6":
        print("Thank You for Visiting!")
        break

    else:
        print("Invalid Choice! Please try again.")


#Task 2

while True:

    print("\n============================")
    print("   COLLEGE ENQUIRY CHATBOT")
    print("============================")

    print("1. Course Fee")
    print("2. Course Duration")
    print("3. Eligibility")
    print("4. College Location")
    print("5. Contact Number")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Course Fee: ₹15,000")

    elif choice == "2":
        print("Course Duration: 3 Months")

    elif choice == "3":
        print("Eligibility: Plus Two Pass")

    elif choice == "4":
        print("Location: Kochi")

    elif choice == "5":
        print("Contact Number: 9876543210")

    elif choice == "6":
        print("Hostel Information: Hostel facilities are available.")

    elif choice == "7":
        print("Placement Information: Placement assistance is provided.")

    elif choice == "8":
        print("Thank You for Visiting!")
        break

    else:
        print("Invalid Choice! Please try again.")


#Task 3

responses = {
    "1": "Course Fee: ₹15,000",
    "2": "Course Duration: 3 Months",
    "3": "Eligibility: Plus Two Pass",
    "4": "Location: Kochi",
    "5": "Contact Number: 9876543210",
    "6": "Hostel Information: Hostel facilities are available.",
    "7": "Placement Information: Placement assistance is provided."
}

while True:

    print("\n============================")
    print("   COLLEGE ENQUIRY CHATBOT")
    print("============================")

    print("1. Course Fee")
    print("2. Course Duration")
    print("3. Eligibility")
    print("4. College Location")
    print("5. Contact Number")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "8":
        print("Goodbye!")
        break
    
    #Task 4
    print(responses.get(choice, "Invalid Choice! Please try again."))


#Task 5

responses = {
    "1": "Course Fee: ₹15,000",
    "2": "Course Duration: 3 Months",
    "3": "Eligibility: Plus Two Pass",
    "4": "Location: Kochi",
    "5": "Contact Number: 9876543210",
    "6": "Hostel Information: Hostel facilities are available.",
    "7": "Placement Information: Placement assistance is provided."
}

while True:

    print("\n============================")
    print("   COLLEGE ENQUIRY CHATBOT")
    print("============================")

    print("1. Course Fee")
    print("2. Course Duration")
    print("3. Eligibility")
    print("4. College Location")
    print("5. Contact Number")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "8":
        print("Thank You for Visiting!")
        break

    response = responses.get(choice)

    if response:
        print("\nBot:", response)
    else:
        print("\nBot: Invalid Choice! Please select a valid option.")
        continue

    again = input("\nWould you like to continue? (yes/no): ").lower()

    if again == "no":
        print("Bot: Thank You! Goodbye!")
        break

    elif again == "yes":
        print("Bot: Sure! Here is the menu again.")

    else:
        print("Bot: Invalid response. Exiting...")
        break
