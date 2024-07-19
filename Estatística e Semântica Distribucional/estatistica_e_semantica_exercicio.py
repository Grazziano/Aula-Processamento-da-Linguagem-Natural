import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from nltk.tokenize import word_tokenize

# 1. Carregar o arquivo CSV
df = pd.read_csv('Hotel_Reviews.csv')

# 2. Pré-processamento: Concatenar todas as reviews em uma única lista de palavras
all_reviews = ' '.join(df['reviews.text'].fillna('').tolist())  # Supondo que a coluna dos comentários seja 'Review'
tokens = word_tokenize(all_reviews.lower())  # Tokenizar e transformar para minúsculas

# 3. Criação da Matriz Termo-Contexto
target_words = ['location', 'price', 'cleaning', 'service']
context_window = 5
contexts = defaultdict(list)

for i, word in enumerate(tokens):
    if word in target_words:
        left_context = tokens[max(0, i-context_window):i]
        right_context = tokens[i+1:i+context_window+1]
        contexts[word].extend(left_context + right_context)

# Construir a matriz termo-contexto
vocabulary = list(set(tokens))
vocab_index = {word: idx for idx, word in enumerate(vocabulary)}
term_context_matrix = np.zeros((len(target_words), len(vocabulary)))

for i, word in enumerate(target_words):
    for context_word in contexts[word]:
        if context_word in vocab_index:
            term_context_matrix[i][vocab_index[context_word]] += 1

# 4. Calcular a Similaridade do Cosseno
cos_sim = cosine_similarity(term_context_matrix)

# Extrair as similaridades para as palavras alvo
location_price_sim = cos_sim[target_words.index('location')][target_words.index('price')]
cleaning_service_sim = cos_sim[target_words.index('cleaning')][target_words.index('service')]

print('Similaridade do Cosseno entre location e price:', location_price_sim)
print('Similaridade do Cosseno entre cleaning e service:', cleaning_service_sim)
