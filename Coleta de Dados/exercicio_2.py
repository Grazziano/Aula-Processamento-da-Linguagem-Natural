from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://institucional.ufpel.edu.br/unidades/id/443"

data = {
    'Professores': [],
    'Cursos': [],
}

try:
    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")

    # print(soup.prettify())

    print("Cursos de Graduação")
    print("===================")
    for link in soup.select('div#graduacao')[0].find_all("li"):
        # print(link.a.text)
        data["Cursos"].append(link.a.text)

    print()

    print("Professores de Graduação")
    print("===================")
    for link in soup.select('div#servidores')[0].find_all("td"):
        # print(link.span.text)
        data["Professores"].append(link.span.text)
    
    # Criando o DataFrame
    # df_projetos = pd.DataFrame(data)
    # Salvando o DataFrame em um arquivo CSV
    # df_projetos.to_csv('/mnt/data/projetos_computacao.csv', index=False)
except Exception as e:
    print(e)
