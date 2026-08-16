#Task 1

conversation = [
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hi! How can I help you?"
    },
    {
        "role": "user",
        "content": "My name is Rahul."
    },
    {
        "role": "assistant",
        "content": "Nice to meet you Rahul!"
    },
    {
        "role": "user",
        "content": "I am from Kerala."
    }
]

print("Conversation History:")
print()

for message in conversation:
    print(message["role"].capitalize() + ":", message["content"])


#Task 2

from openai import OpenAI

# Create OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Conversation history
conversation = []

print("AI Chatbot with Conversation Memory")
print("Type 'bye' to exit.")
print("-----------------------------------")

while True:

    user = input("You: ")

    # Exit condition
    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    # Store user message
    conversation.append({
        "role": "user",
        "content": user
    })

    # Send conversation history to AI model
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=conversation
    )

    # Get AI response
    answer = response.output_text

    print("Bot:", answer)

    # Store assistant response
    conversation.append({
        "role": "assistant",
        "content": answer
    })


#Task 4

print("Conversation Flow:")
print("User Message")
print("   ↓")
print("Store Previous Messages")
print("   ↓")
print("Send Chat History")
print("   ↓")
print("AI Model")
print("   ↓")
print("Generate Context-Aware Response")
print("   ↓")
print("Display Response")
print("   ↓")
print("Store Assistant Response")
print("   ↓")
print("Continue Conversation")


#Task 5

print("""1. Customer Support
   Chatbots can remember customer issues during the conversation.

2. Healthcare
   Chatbots can remember patient symptoms while chatting.

3. Banking
   Chatbots can remember account-related queries during the current session.

4. Education
   Chatbots can remember a student's previous questions.

5. E-commerce
   Chatbots can remember shopping preferences and previous requests.""")