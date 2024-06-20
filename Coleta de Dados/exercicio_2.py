from bs4 import BeautifulSoup
import requests

url = "https://institucional.ufpel.edu.br/unidades/id/443"

try:
    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")

    # soup.find("div", {"id": "graduacao"})
    cursos = soup.select('div#graduacao')

    print(cursos)

    for curso in cursos:
        name = curso.find('li').a.text
        print(name)
except Exception as e:
    print(e)
