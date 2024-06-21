from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://institucional.ufpel.edu.br/unidades/id/443"

cursos_cod = [5700, 3900, 3910, 6100, 6400]
url_cursos = "https://institucional.ufpel.edu.br/cursos/cod/"

professores = []
cursos = []
turmas = []
alunos = []

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

try:
    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")

    # print(soup.prettify())

    # captura cursos de graduação 
    for link in soup.select('div#graduacao')[0].find_all("li"):
        cursos.append(link.a.text)

    # captura nomes dos professores
    for link in soup.select('div#servidores')[0].find_all("td"):
        professores.append(link.span.text)
    
    # captura turmas e alunos de cada curso de graduação
    for c in cursos_cod:
        source = requests.get(f"{url_cursos}{c}")
        source.raise_for_status()
        soup = BeautifulSoup(source.text, "html.parser")

        for td in soup.select('div#turmas')[0].find_all("td"):
            if td.a != None:
                turmas.append(td.a.text)

        for td in soup.select('div#alunos')[0].find_all("td"):
            if not isnumber(td.text):
                alunos.append(td.text)

    data = dict( cursos = cursos, professores = professores, turmas = turmas, alunos = alunos )

    # Criando o DataFrame
    df_projetos = pd.DataFrame(dict([ (k, pd.Series(v)) for k, v in data.items() ]))
    # Salvando o DataFrame em um arquivo CSV
    df_projetos.to_csv('data.csv', index=True)
except Exception as e:
    print(e)
