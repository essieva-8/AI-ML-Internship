#Task 2

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Hello! Who are you?"
)

print(response.output_text)


#Task 3

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("AI Chatbot")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user
    )

    print("Bot:", response.output_text)


#Task 4

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

print("AI/ML Chatbot")
print("Ask questions about AI, Python, Machine Learning, or Data Science.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user
    )

    print("Bot:", response.output_text)


#Task 5

#        User
#          │
#          ▼
#   Python Program
#          │
#          ▼
#     OpenAI API
#          │
#          ▼
#    ChatGPT Model
#          │
#          ▼
# Generated Response
#          │
#          ▼
#   Display to User