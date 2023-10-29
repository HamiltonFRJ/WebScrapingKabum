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

ultima_pagina = math.ceil(int(qtd)/ 2)



dic_produtos = {'marca': [], 'precoV:' [], ':' []}