import math
from collections import Counter


# Lista de palavras
words_list = ["ARARAQUARA", "UFPEL", "PELOTAS", "PROGRAMAÇÃO", "PYTHON"]


def calculate_entropy(word):
  # Conta a quantidade de cada caractere na string
  qtd = Counter(word)
  # Número total de caracteres
  total_chars = len(word)
  # Calcula e retorna a entropia
  return -sum((qtd[char] / total_chars) * math.log2(qtd[char] / total_chars) for char in qtd)


# Calcula e imprime o resultado da entropia para cada palavra no array
for word in words_list:
  entropy = calculate_entropy(word)
  print(f"Resultado entropia da palavra '{word}': {entropy:.2f}")
