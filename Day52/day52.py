#Task 1 - Tokenize: I love Machine Learning

text = "I love Machine Learning"
tokens = text.split()
print(tokens)


#Task 2 - Convert: HELLO WORLD to lowercase.

text = "HELLO WORLD"
lowercase_text = text.lower()
print(lowercase_text)


#Task 3 - Remove punctuation from: Python!!! is Awesome???

import string

text = "Python!!! is Awesome???"
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print(clean_text)


#Task 4 - Identify stop words in: The cat is sitting on the chair

stop_words = {"the", "is", "on", "a", "an"}
text = "The cat is sitting on the chair"
tokens = text.split()
stop_word_tokens = [token for token in tokens if token.lower() in stop_words]
print(stop_word_tokens)


#Task 5 - Clean this sentence: AI 2025 is AMAZING!!!

import re

text = "AI 2025 is AMAZING!!!"
text = text.lower()
text = re.sub(r'[^a-zA-Z\s]', '', text)

print(text)