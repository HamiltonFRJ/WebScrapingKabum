import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

# Coloque na variavel url a pagina de produtos que quer ler
url = 'https://www.kabum.com.br/promocao/MENU_PCGAMER'

urlobject = {'https://www.kabum.com.br/produto/393973/', # iPhone 14 Pro Max 512Gb
             'https://www.kabum.com.br/produto/496065/', # iPhone 14 Plus 128Gb
             'https://www.kabum.com.br/produto/463074/', # iPhone 14 Apple 128GB
             'https://www.kabum.com.br/produto/347001/', # iPhone 13 Apple 128GB
             'https://www.kabum.com.br/produto/463232/', # Apple Watch Series 8
             'https://www.kabum.com.br/produto/381070/', # Samsung Galaxy Watch 5 Bt
             'https://www.kabum.com.br/produto/422463/', # Samsung Galaxy S23 Ultra 256GB
             'https://www.kabum.com.br/produto/466777/', # Xiaomi Poco F5 256Gb
             'https://www.kabum.com.br/produto/95217/', # SSD 960 GB Kingston A400
             'https://www.kabum.com.br/produto/378464/', # SSD 500GB Crucial BX500
             'https://www.kabum.com.br/produto/238670/', # Playstation 5 Sony SSD 825GB
             'https://www.kabum.com.br/produto/433571/', # Cadeira De Escritorio Elements Sophy
             'https://www.kabum.com.br/produto/164854/', # RTX 3060 Asus Dual
             'https://www.kabum.com.br/produto/212528/', # RTX 3070 O8G V2 OC Asus Dual
             'https://www.kabum.com.br/produto/353735/', # Fone de Ouvido Samsung Galaxy Buds 2
             'https://www.kabum.com.br/produto/148877/', # Fone de Ouvido Samsung Galaxy Buds Pro
             'https://www.kabum.com.br/produto/63197/', # Headset Gamer HyperX Cloud II
             'https://www.kabum.com.br/produto/220056/', # Mouse Sem Fio Wireless Logitech, Mx Master 3
             'https://www.kabum.com.br/produto/474963/', # Teclado Sem Fio Logitech MX Keys S
             'https://www.kabum.com.br/produto/226391/', # Interruptor Paralelo Inteligente 3 Way KaBuM! Smart 500
             'https://www.kabum.com.br/produto/115094/', # Interruptor KaBuM! Smart
             'https://www.kabum.com.br/produto/388917/', # Kindle 11 Geração Amazon, 16 GB Preto
            } 

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