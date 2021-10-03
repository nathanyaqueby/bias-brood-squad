import re
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from warnings import simplefilter

# Ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# Calculate cosine similarity scores
def get_similar_articles(q, sim_data, df):
    print("Query:", q)
    print("Articles with the highest cosine similarity scores: \n")
    q = [q]
    q_vec = vectorizer.transform(q).toarray().reshape(sim_data.shape[0], )
    sim = {}
    for i in range(10):
        sim[i] = np.dot(sim_data.loc[:, i].values, q_vec) / np.linalg.norm(sim_data.loc[:, i]) * np.linalg.norm(q_vec)

    sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)

    for k, v in sim_sorted:
        if v != 0.0:
            print("Similarity score:", v)
            print(f"Title:", df["Title"][k])
            print(f"Dated:", df["Dated"][k])
            print(f"Description:", docs[k])
            print("\n")


# Load new, cleaned dataset
df = pd.read_csv(r"sabio_dataset.csv")

# Turn the first 50.000 object descriptions into list
descriptions = df['Description'][:50000].tolist()

# Clean descriptions
descriptions_clean = []

for d in descriptions:
    document_test = re.sub(r"[^\x00-\x7F]+", ' ', d)
    document_test = re.sub(r"@\w+", '', document_test)
    document_test = document_test.lower()
    document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
    document_test = re.sub(r'[0-9]', '', document_test)
    document_test = re.sub(r'\s{2,}', ' ', document_test)
    descriptions_clean.append(document_test)

docs = descriptions_clean

# Create Term-Document Matrix with TF-IDF weighting
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

# Create a DataFrame
sim_data = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names())

# Initialize the search engine using a query/keyword
q1 = "java"
get_similar_articles(q1, sim_data, df)
