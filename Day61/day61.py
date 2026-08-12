#Task 1: Convert the sentence to lowercase

text = "HELLO, I WANT TO BOOK A TICKET."
lowercase_text = text.lower()
print(lowercase_text)


#Task 2: Tokenize the sentence

text = "I love learning Artificial Intelligence."
tokens = text.split()
print(tokens)


#Task 3: Identify Intent and Entities

text = "Book a flight to Chennai on Friday."

# Identify intent
intent = "Flight Booking"

# Identify entities
destination = "Chennai"
date = "Friday"

print("User Message:", text)
print("Intent:", intent)
print("Entities:")
print("Destination:", destination)
print("Date:", date)


#Task 4: Tokenize a sentence using split()

text = "I want to book a hotel in New York."
tokens = text.split()
print("Tokens:")
print(tokens)


#Task 5: Stemming vs Lemmatization

print("Stemming vs Lemmatization")
print("-" * 65)

print(f"{'Stemming':<30} | {'Lemmatization':<30}")
print("-" * 65)

print(f"{'Faster':<30} | {'Slower':<30}")
print(f"{'Removes suffixes':<30} | {'Uses dictionary':<30}")
print(f"{'May produce invalid words':<30} | {'Produces valid words':<30}")
print(f"{'Less accurate':<30} | {'More accurate':<30}")