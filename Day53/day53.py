#Task 2 - Stem the following words: Playing, Working, Learning, Running

import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["Playing", "Working", "Learning", "Running"]

print("Stemmed Words:")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")


#Task 3 - Lemmatize: Cars, Children, Mice, Dogs

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["Cars", "Children", "Mice", "Dogs"]

print("Lemmatized Words:")
for word in words:
    print(f"{word} -> {lemmatizer.lemmatize(word)}")


#Task 4 - Compare outputs of: Stemming, Lemmatization

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["playing", "working", "learning", "running", "studies", "mice"]

print("{:<12} {:<12} {:<12}".format("Word", "Stemmed", "Lemmatized"))

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos="v")
    print("{:<12} {:<12} {:<12}".format(word, stem, lemma))


#Task 5 - Create a table containing: Word, Stemmed, Lemmatized for 10 words.

words = ["playing", "working", "learning", "running", "studies", "mice", "children", "cars", "dogs", "cats"]

print("{:<12} {:<12} {:<12}".format("Word", "Stemmed", "Lemmatized"))

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos="v")
    print("{:<12} {:<12} {:<12}".format(word, stem, lemma))
