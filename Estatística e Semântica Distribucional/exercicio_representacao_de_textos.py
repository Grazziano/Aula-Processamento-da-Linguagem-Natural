import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Carregar o arquivo CSV
df = pd.read_csv('Hotel_Reviews.csv')

# Extrair os comentários
comments = df['reviews.text'].fillna('').tolist()  # Supondo que a coluna dos comentários seja 'reviews.text'

# BoW - Bag of Words
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(comments)
bow_feature_names = bow_vectorizer.get_feature_names_out()
bow_data = bow_matrix.toarray()

# Salvar representação BoW em JSON
bow_representation = {
    "features": bow_feature_names.tolist(),
    "data": bow_data.tolist(),
}
with open('bow_representation.json', 'w') as f:
    json.dump(bow_representation, f)

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(comments)
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()
tfidf_data = tfidf_matrix.toarray()

# Salvar representação TF-IDF em JSON
tfidf_representation = {
    "features": tfidf_feature_names.tolist(),
    "data": tfidf_data.tolist(),
}
with open('tfidf_representation.json', 'w') as f:
    json.dump(tfidf_representation, f)

# Bag of N-Gram (Bigramas e Trigramas)
ngram_vectorizer = CountVectorizer(ngram_range=(2, 3))
ngram_matrix = ngram_vectorizer.fit_transform(comments)
ngram_feature_names = ngram_vectorizer.get_feature_names_out()
ngram_data = ngram_matrix.toarray()

# Salvar representação N-Gram em JSON
ngram_representation = {
    "features": ngram_feature_names.tolist(),
    "data": ngram_data.tolist(),
}
with open('ngram_representation.json', 'w') as f:
    json.dump(ngram_representation, f)

print("Representações salvas com sucesso!")
