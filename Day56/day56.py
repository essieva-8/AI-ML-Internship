# Import Word2Vec
from gensim.models import Word2Vec

# Task 2: Create a small dataset with 5 sentences
sentences = [
    ["i", "love", "ai"],
    ["ai", "is", "amazing"],
    ["i", "love", "python"],
    ["python", "is", "powerful"],
    ["ai", "and", "python", "are", "useful"]
]


# Task 3: Train the Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1
)


# Task 4: Print word vectors
print("Word Vector for 'ai':")
print(model.wv["ai"])

print("\nWord Vector for 'python':")
print(model.wv["python"])


# Task 5: Find similar words
print("\nWords similar to 'ai':")
print(model.wv.most_similar("ai"))

print("\nWords similar to 'python':")
print(model.wv.most_similar("python"))