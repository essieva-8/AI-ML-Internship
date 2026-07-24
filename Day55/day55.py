#Task 2

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Documents
documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and Transform
X = vectorizer.fit_transform(documents)

# Print TF-IDF Matrix
print("TF-IDF Matrix:\n")
print(X.toarray())


#Task 3

print("Vocabulary:")
print(vectorizer.get_feature_names_out())


#Task 4

# Bag of Words
bow = CountVectorizer()

bow_matrix = bow.fit_transform(documents)

print("===== Bag of Words =====")
print("Vocabulary:")
print(bow.get_feature_names_out())

print("\nBoW Matrix:")
print(bow_matrix.toarray())

# TF-IDF
tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(documents)

print("\n===== TF-IDF =====")
print("Vocabulary:")
print(tfidf.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())


#Task 5

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

print("\nTF-IDF Scores:\n")

for i, doc in enumerate(X.toarray()):
    print(f"Document {i+1}:")
    for word, score in zip(feature_names, doc):
        if score > 0:
            print(f"{word:<10} : {score:.3f}")
    print()
