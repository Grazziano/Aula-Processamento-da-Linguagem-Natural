from gensim.models import KeyedVectors

try:
    # Carrega modelo Word2Vec
    model_path = 'cbow_s50.txt'
    word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=False, unicode_errors='ignore')

    analogias = [
        ("homem", "mulher", "rei"),
        ("rei", "mulher", "homem"),
        ("médico", "enfermeira", "engenheiro"),
        ("rápido", "veloz", "grande"),
        ("feliz", "alegre", "triste"),
        ("azul", "cor", "cachorro"),
        ("verde", "cor", "maçã"),
        ("brasil", "brasília", "frança"),
        ("empregado", "trabalho", "mulher"),
    ]

    for analogia in analogias:
        result = word2vec_model.most_similar(positive=[analogia[1], analogia[2]], negative=[analogia[0]])
        print(f"{analogia[0]} : {analogia[1]} :: {analogia[2]} : {result[0][0]}")
        print("#"*40)
except EOFError as e:
        print("Error: Unexpected end of file encountered:", e)
except Exception as e:
        print("An error occurred:", e)
