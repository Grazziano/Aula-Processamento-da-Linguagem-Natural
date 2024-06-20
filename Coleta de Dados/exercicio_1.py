from bs4 import BeautifulSoup

# Carrega o arquivo HTML
with open('pagina.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Cria o objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontra todas as tags <div>
articles = soup.find_all('div')

# Itera sobre cada tag <div> e extrai as informações desejadas
for i, article in enumerate(articles, start=1):
    title = article.find('h1').text
    content = article.find('p').text
    print(f'Artigo {i}:')
    print(f'Título: {title}')
    print(f'Conteúdo: {content}')
    print('-' * 30)
