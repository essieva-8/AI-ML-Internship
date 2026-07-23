#Task 1

documents = [
    "AI is powerful",
    "AI is amazing"
]

# Create vocabulary manually
vocabulary = set()

for sentence in documents:
    words = sentence.split()
    vocabulary.update(words)

print("Vocabulary:")
print(sorted(vocabulary))


#Task 2

vocabulary = ["I", "love", "AI", "Python"]

sentence = "I love AI"
words = sentence.split()

vector = []

for word in vocabulary:
    vector.append(words.count(word))

print("Vocabulary:", vocabulary)
print("BoW Vector:", vector)


#Task 4

from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love AI",
    "I love Python"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())


#Task 5

from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I love AI",
    "AI is powerful",
    "Python is amazing",
    "I love Python",
    "AI and Python are useful"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(X.toarray())
