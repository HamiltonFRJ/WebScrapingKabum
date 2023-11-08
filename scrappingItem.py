import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

urlarray = ['393973', # iPhone 14 Pro Max 512Gb
             '496065', # iPhone 14 Plus 128Gb
             '463074', # iPhone 14 Apple 128GB
             '347001', # iPhone 13 Apple 128GB
             '463232', # Apple Watch Series 8
             '381070', # Samsung Galaxy Watch 5 Bt
             '422463', # Samsung Galaxy S23 Ultra 256GB
             '466777', # Xiaomi Poco F5 256Gb
             '95217', # SSD 960 GB Kingston A400
             '378464', # SSD 500GB Crucial BX500
             '238670', # Playstation 5 Sony SSD 825GB
             '433571', # Cadeira De Escritorio Elements Sophy
             '164854', # RTX 3060 Asus Dual
             '212528', # RTX 3070 O8G V2 OC Asus Dual
             '353735', # Fone de Ouvido Samsung Galaxy Buds 2
             '148877', # Fone de Ouvido Samsung Galaxy Buds Pro
             '63197', # Headset Gamer HyperX Cloud II
             '220056', # Mouse Sem Fio Wireless Logitech, Mx Master 3
             '474963', # Teclado Sem Fio Logitech MX Keys S
             '226391', # Interruptor Paralelo Inteligente 3 Way KaBuM! Smart 500
             '115094', # Interruptor KaBuM! Smart
             '388917', # Kindle 11 Geração Amazon, 16 GB Preto
             #################################################################### -- Novos produtos
             '398962', # iPhone 14 Pro Max 256Gb
             '469012', # Braço articulado de monitor Vesa
            ] 

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"}

# Criando o dicionario que as informacoes a serem armazenadas
dic_produtos = {'marca':[], 'precoPix':[],'precoParcelado':[], 'precoAntigo':[],}

# Faz o acesso em cada página, alterando o id do produto
for i in urlarray:
    url_pag = f'https://www.kabum.com.br/produto/{i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    # Encontre a coluna de produto
    produto = soup.find('div', class_=re.compile('col-purchase'))

    # Encontra os identificadores de marca, precoEmPromo e antigoPreco
    marca = produto.find('h1', class_=re.compile('dVrDvy')).get_text().strip()
    precoPix = produto.find('h4', class_=re.compile('finalPrice'))
    if (precoPix):
        precoPix = precoPix.get_text().strip()
    else:
        precoPix = "Indisponivel"
    precoParcelado = produto.find('b', class_=re.compile('regularPrice'))
    if (precoParcelado):
        precoParcelado = precoParcelado.get_text().strip()
    else:
        precoParcelado = precoPix
    precoAntigo = produto.find('span', class_=re.compile('oldPrice'))
    if (precoAntigo):
        precoAntigo = precoAntigo.get_text().strip()
    else:
        precoAntigo = precoPix
    
    print(marca, precoPix, precoParcelado, precoAntigo)

    dic_produtos['marca'].append(marca)
    dic_produtos['precoPix'].append(precoPix) 
    dic_produtos['precoParcelado'].append(precoParcelado) 
    dic_produtos['precoAntigo'].append(precoAntigo) 

df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/hamil/WebScrapingBF/tabela.csv', encoding='utf-8', sep=';')
