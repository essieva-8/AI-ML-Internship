import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')


#Task 2: Tokenization

from nltk.tokenize import word_tokenize

text = "Artificial Intelligence is changing the world."
tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)


#Task 3: Stop Words Removal

from nltk.corpus import stopwords

text = "I want to book a train ticket to Delhi."

tokens = word_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("\nAfter Stop Word Removal:")
print(filtered_words)


#Task 4: Stemming   

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["Playing", "Running", "Reading", "Learning"]

for word in words:
    stemmed_word = stemmer.stem(word.lower())
    print(word, "->", stemmed_word)


#Task 5: Build a Chatbot

print("AI College Chatbot")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    tokens = word_tokenize(user)

    if "fee" in tokens or "fees" in tokens:
        print("Bot: The course fee is ₹15,000.")

    elif "duration" in tokens:
        print("Bot: The course duration is 3 months.")

    elif "eligibility" in tokens:
        print("Bot: Please check the college admission requirements for eligibility.")

    elif "contact" in tokens or "number" in tokens:
        print("Bot: You can contact us at 9876543210.")

    elif "location" in tokens or "college" in tokens:
        print("Bot: The college is located in Kochi.")

    else:
        print("Bot: Sorry! I couldn't understand your question.")