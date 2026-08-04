#Task 2 - Load the GloVe Model

import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
print("Model Loaded Successfully!")


#Task 3 - Print the Vector for "king"

print(model["king"])


#Task 4 - Find the Top 5 Similar Words for "computer"

print(model.most_similar("computer", topn=5))


#Task 5 - Research One Real-World Application of FastText and Explain Why It Is Suitable

print("FastText is widely used in spam email detection systems. It converts email text into meaningful word vectors and helps machine learning models classify emails as spam or non-spam.")

print("""Why FastText is suitable: Handles misspelled words commonly found in spam emails.
                                   Understands rare and unseen words using character n-grams.
                                   Produces meaningful word representations even when exact words are absent from the training data.
                                   Offers fast training and inference, making it practical for large-scale applications.
""")


