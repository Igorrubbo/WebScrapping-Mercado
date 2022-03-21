import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import time
import mysql.connector
from datetime import date

#Checar tempo de execução do programa
start_time = time.time()

#Data do dia de hoje em formato dd/mm/yy
today = date.today()
data_hoje = today.strftime("%Y-%m-%d")
print(data_hoje)

#conexão com db do google cloud
db = mysql.connector.connect(
    host = '34.151.251.243',
    user = 'root',
    passwd = '459588asd',
    database = 'Teste',
)
mycursor = db.cursor()

# Carregar planilha e produtos com openpyxl
arquivo = r"lista de mercado.xlsx"
wb = load_workbook(arquivo)
ws = wb[wb.sheetnames[0]]
lista_produtos = []
coluna_link = ws['A'][2:]
for cell in coluna_link:
    lista_produtos.append(f'{cell.value}')
#print(lista_produtos)


# Pegar informações do site
def webscrape_mercadolivre():
    for produto in lista_produtos:
        url_dinamica = r'https://lista.mercadolivre.com.br/supermercado/' + produto.replace(' ', '-') + '_OrderId_PRICE_NoIndex_True'
        response = requests.get(url_dinamica)
        site = BeautifulSoup(response.text, 'html.parser')
        time.sleep(1)

        # Método para pegar a classe do item (produtos diferentes tem classes diferentes)
        resultado = site.find('div', attrs={'class': 'ui-search-result__wrapper'})
        primeiro_resultado = list(resultado.children)[0]
        classe_dinamica = str(primeiro_resultado).split('>')[0][12:-1]

        # Função para procurar se o produto encontrado é o mesmo que o solicitado
        def checar_produto(prod, titulo_mercadolivre):
            nova_lista = prod.split()
            for palavra in nova_lista:
                resultado = (' ' + palavra.upper() + ' ') in (' ' + titulo_mercadolivre_html.text.upper() + ' ')
                if resultado == False:
                    return False

        #Garantir que a classe encontrada não seja a classe errada
        i = 0
        while "advertisement" in classe_dinamica:
            i += 1
            aux_classe_dinamica = list(resultado[i].children)[0]
            classe_dinamica = str(aux_classe_dinamica).split('>')[0][12:-1]
        itens = site.findAll('div', attrs={'class': classe_dinamica})

        for item in itens[0:3]:
            # Dados dos itens encontrados
            titulo_mercadolivre_html = item.find('h2', attrs={'class': 'ui-search-item__title'})
            titulo_mercadolivre = "'" + titulo_mercadolivre_html.text + "'"
            link = item.find('a', attrs={'class': 'ui-search-link'})
            link_mercadolivre_html = link.text, link['href']
            link_mercadolivre = "'" + link_mercadolivre_html[1] + "'"
            preco = item.find('div', attrs={'class': "ui-search-price__second-line"})   #Se tiver desconto garantir que o preço com desconto seja pego
            preco_reais = preco.find('span', attrs={'class': "price-tag-fraction"})
            preco_centavos = preco.find('span', attrs={'class': "price-tag-cents"})
            # Condição para caso tenha centavos no preço
            if preco_centavos:
                preco_mercadolivre = preco_reais.text + '.' + preco_centavos.text
            else:
                preco_mercadolivre = preco_reais.text
            desconto_mercadolivre_html = item.find('span', attrs={'class': 'ui-search-price__discount'})  #Se tiver desconto recolher qual é o % de desconto
            if desconto_mercadolivre_html:
                desconto_mercadolivre = "'" + desconto_mercadolivre_html.text + "'"
            else:
                desconto_mercadolivre = "'0%'"

            # Printar os dados
            if checar_produto(produto, titulo_mercadolivre) != False:
                print("Título do produto:", titulo_mercadolivre)
                print('Preço: R$ ' + preco_mercadolivre)
                print('Link do produto:' + link_mercadolivre)
                print(desconto_mercadolivre)
                print('---------------------------------------------------')
                sql = "INSERT INTO preços_mercadolivre(produto, titulo, preço, desconto, dia, link) values(%s, %s, %s, %s, %s, %s)"
                values = (produto, titulo_mercadolivre, preco_mercadolivre, desconto_mercadolivre, data_hoje, link_mercadolivre)
                mycursor.execute(sql, values)
                #mycursor.execute(f'INSERT INTO preços_mercadolivre (produto, titulo, preço, desconto, dia, link) VALUES({produto}, {titulo_mercadolivre}, {preco_mercadolivre}, {desconto_mercadolivre}, STR_TO_DATE({data_hoje}, "%d-%m-%Y"), {link_mercadolivre})')
                db.commit()
                break                


webscrape_mercadolivre()
wb.close()
db.close()
print("--- %s seconds ---" % (time.time() - start_time))