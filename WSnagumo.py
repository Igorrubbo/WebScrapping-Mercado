import mysql.connector
import os
import time
import dotenv
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import date

#Carregar variáveis de ambiente
dotenv.load_dotenv(dotenv.find_dotenv())

#Checar tempo de execução do programa
start_time = time.time()

#Data do dia de hoje em formato dd/mm/yy
today = date.today()
data_hoje = today.strftime("%y-%m-%d")

#conexão com db do google cloud
db = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    passwd = os.getenv('DB_PASSWD'),
    database = 'Teste',
)
mycursor = db.cursor()

# Carregar planilha e produtos com openpyxl
arquivo = r"lista de mercado.xlsx"
wb = load_workbook(arquivo)
ws = wb[wb.sheetnames[0]]
lista_produtos = []
coluna_link = ws['A'][1:]
for cell in coluna_link:
    lista_produtos.append(f'{cell.value}')

# Instanciar um objeto Options e adicionar o argumento "--headless"
opts = webdriver.ChromeOptions()
opts.add_argument(" --headless")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

# Definir o local do webdriver e iniciar ele
chrome_driver = Service(r'C:\Program Files (x86)\Chromedriver\chromedriver.exe')
driver = webdriver.Chrome(options = opts, service = chrome_driver)

def webscrape_nagumo():
    for produto in lista_produtos:
        # Carregar a página HTML e realizar uma pausa para a página poder carregar
        url_dinamica_nagumo = r'http://www.nagumo.com.br/atibaia-lj32-atibaia-alvinopolis-avenida-prof-carlos-alberto-de-carvalho/busca/' + produto.replace(' ', '-')
        driver.get(url_dinamica_nagumo)
        time.sleep(2.5)

        # Começar a usar o Beautiful Soup para puxar os dados
        soup_file = driver.page_source
        site_nagumo = BeautifulSoup(soup_file, 'html.parser')
        main = site_nagumo.findAll(class_ = 'product-grid-default product-grid-default-4 content-dailySale-list-products-product')

        # Função para procurar se o produto solicitado é o mesmo que o encontrado
        def checar_produto():
            nova_lista = produto.split()
            for palavra in nova_lista:
                resultado = (' ' + palavra.upper() + ' ') in (' ' + titulo_html.text.upper() + ' ') #tenho que usar o titulo_html pois preciso colocar o valor da variável titulo_nagumo entre aspas simples para o MYSQL
                if resultado == False:
                    return False

        for item in main[0:6]:
            titulo_auxiliar = item.find(class_ = 'txt-desc-product-itemtext-muted txt-desc-product-item')
            titulo_html = titulo_auxiliar.find(class_ = 'list-product-link') 
            titulo_nagumo = "'" + titulo_html.text + "'"
            link = item.find(class_ = 'list-product-link')
            link_nagumo = "'" + 'http://www.nagumo.com.br' + (link.text, link['href'])[1] + "'"
            #Verificação se existe oferta, caso exista usar o preço correto
            preco_total = item.find(class_ ='area-bloco-preco bloco-preco pr-0')
            preco_oferta = item.find(class_ ='preco-oferta')
            if preco_oferta:
                preco_nagumo = preco_oferta.text.split('R$')[1]
                preco_nagumo = "".join(preco_nagumo.split()).replace(",",".")
                #preco_nagumo = "'" + preco_nagumo + "'"
            else:
                preco_nagumo = preco_total.text.split('R$')[1]
                preco_nagumo = "".join(preco_nagumo.split()).replace(",",".")
                #preco_nagumo = "'" + preco_nagumo + "'"
            #Verificação se existe desconto, caso exista extrair a informação
            desconto_online = item.find(class_ = 'promotion-tip-text')
            outro_desconto = item.find(class_ = 'discount-tag')
            if desconto_online:
                desconto_nagumo = "'" + desconto_online.text + "'"
            elif outro_desconto:
                desconto_nagumo = "'" + outro_desconto.text + "'"
            else:
                desconto_nagumo = "'" + '0%' + "'"

            if checar_produto() != False:
                print('Título do produto: ' + titulo_nagumo)
                print('Link do produto: ' + link_nagumo)
                print('Preço do produto com desconto: R$' + preco_nagumo)
                print('Desconto aplicado: ' + desconto_nagumo)              
                print('---------------------------------------------------')       
                sql = "INSERT INTO preços_nagumo(produto, titulo_nagumo, preço, desconto, dia, link) values(%s, %s, %s, %s, %s, %s)"
                values = (produto, titulo_nagumo, preco_nagumo, desconto_nagumo, data_hoje, link_nagumo)
                mycursor.execute(sql, values)     
                #mycursor.execute(f"INSERT INTO preços_nagumo (produto, titulo_nagumo, preço, desconto, dia, link) VALUES({produto}, {titulo_nagumo}, {preco_nagumo}, {desconto_nagumo}, {data_hoje}, {link_nagumo})")
                db.commit()
                break

webscrape_nagumo()
wb.close()
db.close()
print("--- %s seconds ---" % (time.time() - start_time))