from bs4 import BeautifulSoup
import requests
import pandas as pd

cursos_cod = [5700, 3900, 3910, 6100, 6400]
url_cursos = "https://institucional.ufpel.edu.br/cursos/cod/"

turmas = []
alunos = []


def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

try:
    for c in cursos_cod:
        source = requests.get(f"{url_cursos}{c}")
        source.raise_for_status()
        soup = BeautifulSoup(source.text, "html.parser")
        # print(soup.prettify())

        # for td in soup.select('div#turmas')[0].find_all("td"):
        #     if td.a != None:
        #         turmas.append(td.a.text)
        for td in soup.select('div#turmas')[0].find_all("td"):
            turmas.append(td.text)
        
        for td in soup.select('div#alunos')[0].find_all("td"):
            if not isnumber(td.text):
                alunos.append(td.text)
        
        for td in soup.select('table.tabela-dados')[0].find_all("td"):
            print(td.text)
    
    # for td in soup.select('div.conteudo-principal')[0].find_all("td"):
    #     alunos.append(td.text)

    # print(turmas[0])
    # print(alunos)
    # print(len(alunos))
except Exception as e:
    print(e)
