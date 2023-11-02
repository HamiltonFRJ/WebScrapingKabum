import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

urlobject = ['393973', # iPhone 14 Pro Max 512Gb
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
            ] 

for i in urlobject:
  print ("https://www.kabum.com.br/produto/" + i)