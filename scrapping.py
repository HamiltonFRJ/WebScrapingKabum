import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

# Coloque na variavel url a pagina de produtos que quer ler
url = 'https://www.kabum.com.br/promocao/MENU_PCGAMER'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# Obtem o numero de produtos da pagina definida na url 
qtd_itens = soup.find('div', id='listingCount').get_text().strip()
# Organizando a variavel de qtd_itens para manter apenas o int
index = qtd_itens.find(' ')
qtd = qtd_itens[:index]

# Dividindo a quantidade de produtos totais pela quantidade em cada pagina, para identificar quantas paginas serao passadas
ultima_pagina = math.ceil(int(qtd)/ 20)

# Criando o dicionario que terá a marca, preco novo e preco antigo de produtos
dic_produtos = {'marca':[], 'precoNovo':[]}

# Faz o acesso em cada página, alterando o page number da url
for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.kabum.com.br/promocao/MENU_PCGAMER?page_number={i}&page_size=20&facet_filters=&sort='
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    # Encontre cada div de produto com a class 'productCard' para a obtencao das informacoes
    produtos = soup.find_all('div', class_=re.compile('productCard'))

    # Encontra os identificadores de marca, precoEmPromo e antigoPreco
    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        precoNovo = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        # precoAntigo = produto.find('span', class_=re.compile('oldPriceCard')).get_text().strip()

        print(marca, precoNovo)

        dic_produtos['marca'].append(marca)
        dic_produtos['precoNovo'].append(precoNovo)
    

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/hamil/WebScrapingBF/tabela.csv', encoding='utf-8', sep=';')
