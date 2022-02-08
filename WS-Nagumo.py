from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import time

# Instantiate an Options object and add the "--headless" argument
#opts = Options()

opts = webdriver.ChromeOptions()
opts.add_argument(" --headless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

# Set the location of the webdriver and instantiate a webdriver
chrome_driver = Service(r'C:\Program Files (x86)\Chromedriver\chromedriver.exe')
driver = webdriver.Chrome(options = opts, service = chrome_driver)

# Load the HTML page and pause so the page has time to load
driver.get(r'C:\Users\Igor\Documents\PythonEstudos\WebScrapping\WS-Mercado\HTML para teste\not-milk - Supermercado Nagumo - Compre Online em Atibaia_SP.html')
#driver.get(r'http://www.nagumo.com.br/atibaia-lj32-atibaia-alvinopolis-avenida-prof-carlos-alberto-de-carvalho/busca/not-milk')
time.sleep(1)

# Put the page source into a variable and create a BS object from it
soup_file = driver.page_source
site_nagumo = BeautifulSoup(soup_file, 'html.parser')
main = site_nagumo.find(class_ = 'flex fww fww-products')

titulo_auxiliar = main.find(class_ = 'txt-desc-product-itemtext-muted txt-desc-product-item')
titulo_nagumo = titulo_auxiliar.find(class_ = 'list-product-link')
print(titulo_nagumo.text)

link_nagumo = main.find(class_ = 'list-product-link')
novo_link = link_nagumo.text, link_nagumo['href']
print((link_nagumo.text, link_nagumo['href'])[1])

preco_total_nagumo = main.find(class_='area-bloco-preco bloco-preco pr-0')
print(preco_total_nagumo.text)

