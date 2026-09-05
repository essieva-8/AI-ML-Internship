#Task 1

# ConversationBufferMemory 
from langchain.memory import ConversationBufferMemory

# Create conversation memory
memory = ConversationBufferMemory()

# Simple rule-based chatbot
def chatbot(user_input):

    # Save the user's message
    memory.chat_memory.add_user_message(user_input)

    # Convert input to lowercase
    text = user_input.lower()

    # Generate response
    if "name" in text and "what is my name" not in text:
        response = "Nice to meet you! I will remember your name."

    elif "python" in text:
        response = "Python is a popular programming language used in AI, ML, and data science."

    elif "learn next" in text:
        response = "Since you are learning Python, you can next explore NumPy, Pandas, and Machine Learning."

    elif "data scientist" in text:
        response = "Python is very useful for becoming a data scientist."

    elif "what is my name" in text:
        # Search previous messages for the name
        history = memory.buffer

        if "Essie" in history:
            response = "Your name is Essie."
        else:
            response = "I don't remember your name yet."

    elif "what am i learning" in text:
        history = memory.buffer

        if "Python" in history:
            response = "You are learning Python."
        else:
            response = "I don't remember what you are learning."

    else:
        response = "That's interesting! Tell me more."

    # Save chatbot response
    memory.chat_memory.add_ai_message(response)

    return response


#Task 2

# Ask five related questions
questions = [
    "My name is Essie.",
    "I am learning Python.",
    "What should I learn next?",
    "I want to become a data scientist.",
    "What am I learning?"
]

# Conversation
for i, question in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")
    answer = chatbot(question)
    print("Chatbot:", answer)


# Display conversation memory
print("\n" + "=" * 50)
print("CONVERSATION MEMORY")
print("=" * 50)

print(memory.buffer)


#Task 3

from langchain.memory import ConversationBufferWindowMemory

# Create conversation memory with a window of 5
memory = ConversationBufferWindowMemory(k=5)


# Simple rule-based chatbot
def chatbot(user_input):

    # Store user message
    memory.chat_memory.add_user_message(user_input)

    text = user_input.lower()

    # Generate response
    if "my name is" in text:
        response = "Nice to meet you! I will remember your name."

    elif "learning python" in text:
        response = "That's great! Python is useful for AI and data science."

    elif "learn next" in text:
        response = "You can learn NumPy, Pandas, and Machine Learning next."

    elif "data scientist" in text:
        response = "Python is an excellent language for becoming a data scientist."

    elif "what is my name" in text and "what am i learning" in text:

        history = memory.buffer

        name = "Essie" if "Essie" in history else "Unknown"
        language = "Python" if "Python" in history else "Unknown"

        response = f"Your name is {name} and you are learning {language}."

    else:
        response = "I remember our recent conversation."

    # Store chatbot response
    memory.chat_memory.add_ai_message(response)

    return response


# Ask five related questions
questions = [
    "My name is Essie.",
    "I am learning Python.",
    "What should I learn next?",
    "I want to become a data scientist.",
    "What is my name and what am I learning?"
]


# Run the conversation
for i, question in enumerate(questions, 1):

    print(f"\nQuestion {i}: {question}")

    answer = chatbot(question)

    print("Chatbot:", answer)


# Display memory
print("\n" + "=" * 50)
print("CONVERSATION WINDOW MEMORY")
print("=" * 50)

print(memory.buffer)


#Task 4

from langchain.memory import ConversationBufferMemory

# Create conversation memory
memory = ConversationBufferMemory()


# Simple chatbot
def chatbot(user_input):

    # Store user message
    memory.chat_memory.add_user_message(user_input)

    text = user_input.lower()

    # Generate response
    if "my name is" in text:
        response = "Nice to meet you! I will remember your name."

    elif "i live in" in text or "my city is" in text:
        response = "That's great! I will remember your city."

    elif "i am a" in text or "my profession is" in text:
        response = "Great! I will remember your profession."

    elif "what is my name" in text:
        history = memory.buffer

        if "Essie" in history:
            response = "Your name is Essie."
        else:
            response = "I don't remember your name."

    elif "which city" in text or "where do i live" in text:
        history = memory.buffer

        if "Kochi" in history:
            response = "You live in Kochi."
        else:
            response = "I don't remember your city."

    elif "what is my profession" in text:
        history = memory.buffer

        if "data scientist" in history.lower():
            response = "You are a data scientist."
        else:
            response = "I don't remember your profession."

    elif "tell me about myself" in text:
        history = memory.buffer

        name = "Essie" if "Essie" in history else "Unknown"
        city = "Kochi" if "Kochi" in history else "Unknown"
        profession = "Data Scientist" if "data scientist" in history.lower() else "Unknown"

        response = (
            f"Your name is {name}, you live in {city}, "
            f"and you are a {profession}."
        )

    else:
        response = "I will remember this information."

    # Store chatbot response
    memory.chat_memory.add_ai_message(response)

    return response


# Create the conversation
questions = [
    "My name is Essie.",
    "I live in Kochi.",
    "I am a data scientist.",
    "What is my name?",
    "Tell me about myself."
]


# Run conversation
for i, question in enumerate(questions, 1):

    print(f"\nUser {i}: {question}")

    answer = chatbot(question)

    print("Chatbot:", answer)


# Display stored conversation
print("\n" + "=" * 50)
print("CONVERSATION MEMORY")
print("=" * 50)

print(memory.buffer)


#Task 5

from tabulate import tabulate

# Table data
data = [
    [
        "Buffer Memory",
        "Stores complete conversation",
        "Complete context; simple",
        "High token usage; memory grows",
        "Short/medium conversations"
    ],
    [
        "Window Memory",
        "Stores only recent N messages",
        "Lower token usage; good for long chats",
        "Older information is forgotten",
        "Long conversations"
    ],
    [
        "Summary Memory",
        "Stores a summary of the conversation",
        "Saves memory and tokens",
        "Some details may be lost in summarisation",
        "Long conversations"
    ],
    [
        "Entity Memory",
        "Stores important information about entities",
        "Retains important facts",
        "Requires identifying useful information",
        "Personal assistants, customer support"
    ]
]

# Column headings
headers = [
    "Memory Type",
    "Description",
    "Advantages",
    "Disadvantages",
    "Suitable Use Cases"
]

# Print table
print(tabulate(data, headers=headers, tablefmt="grid"))