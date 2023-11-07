import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from string import punctuation
import pandas as pd
import os

print("Started\n")

def download_req(*file):
    for i in file:
        # Download function or code should be added here
        # Example: nltk.download(i)
        pass

download_req('punkt', 'stopwords', 'wordnet')

# Define sample documents
# documents = [
#     "This is the first document.",
#     "This document is the second document.",
#     "And this is the third one.",
#     "Is this the first document?"
# ]

# Tokenize and remove stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def extra_word(i):
    return (
        i.lower() in stop_words
        or i.lower() in punctuation
        or len(i) == 1
        or not (i.isalpha() or i.replace('-', '').isalpha())
    )

# Data
# documents = []
# for i in os.listdir('Input'):
#     if i.endswith('py'):
#         continue
#     for j in os.listdir(f'Input\\{i}'):
#         with open(f'Input\\{i}\\{j}', 'r') as file:
#             documents.append(file.read())


documents = []

# List the directory names in 'Input'
input_directory = 'Input'
directory_names = os.listdir(input_directory)

# Iterate over the directories and read text files
for directory_name in directory_names:
    if directory_name.endswith('py'):
        continue

    directory_path = os.path.join(input_directory, directory_name)

    # Check if it's a directory
    if os.path.isdir(directory_path):
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    documents.append(file.read())



# Tokenize the text into words
tokenized_documents = [word_tokenize(doc) for doc in documents]

filtered_documents = []
for modified_sentence in tokenized_documents:
    lst = []
    for i in modified_sentence:
        if not extra_word(i):
            for pos in ['v', 'a', 'n', 'r']:
                i = lemmatizer.lemmatize(i, pos)
            lst.append(i.lower())
    filtered_documents.append(lst)

# Convert filtered documents back to strings
preprocessed_documents = [" ".join(doc) for doc in filtered_documents]

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents to TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_documents)

# Get the feature names (words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Create a dataframe for the TF-IDF values
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names).transpose()
tfidf_df.to_csv("new.csv", index=False)
print(tfidf_df)

print("\nDone")
