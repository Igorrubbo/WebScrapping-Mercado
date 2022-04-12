# Programa de WebScrapping de preços de produtos de mercado e cálculo de inflação pessoal

Esse programa ainda está em desenvolvimento.👷‍♂️👨‍💻

![](https://i.imgur.com/opq2UyM.png)  

Fonte: <a href="https://www.toptal.com/python/web-scraping-with-python/">toptotal.com</a>

Comecei esse projeto com três objetivos em mente: pesquisa de preço, cálculo de inflação pessoal e meu desenvolvimento pessoal em Python. 

Para cumprir o primeiro objetivo é necessário extrair os preços dos produtos que eu e minha família consumimos com frequência dos sites do Mercado Livre e do Nagumo e realizar uma pequena análise da diferença de preços entre os produtos. As bibliotecas BeautifulSoup e Selenium são usadas para acessar, navegar e extrair os dados dos preços dos produtos que constam em uma lista em excel que é acessada por meio da biblioteca openpyxl.  

O segundo objetivo necessita apenas de uns poucos passos a mais do que o primeiro, sendo necessário uma rotina de extração de dados para se construir um banco de dados, no caso estou usando SQL Server para armazenar os dados. Para não ter que inserir os dados de forma manual no banco de dados, utilizo do pyodb para acessar o banco de dados, que está armazenado na nuvem por meio do serviço de banco de dados na nuvem do Microsoft Azure. Dessa forma, consigo automatizar esse processo de extração de dados para análise no tempo devido, provavelmente no final de cada ano.  

O terceiro objetivo tem sido alcançado com sucesso, que é meu desenvolvimento como programador. Diversos desafios foram enfrentados, tecnologias novas aprendidas e a certeza de que é essa a área em que desejo passar minha vida trabalhando se estabeleceu.

🛠 Ferramentas utilizadas no projeto:  
- Python - Como linguagem de programação principal  
- VSCode - IDE escolhido para o desenvolvimento do código  
- Git - Utilizado para controle de versão e registro de atividades  
- Excel - A lista de produtos a serem pesquisados se encontra em uma planilha excel  
- SQL Server - Base de dados escolhida para desenvolvimento do projeto  
- Microsoft Azure - Serviço em nuvem escolhido para desenvolvimento do projeto  

📚 Bibliotecas utilizadas:  
- Beautiful Soup e Selenium - ferramentas principais para WebScrapping  
- dotenv - criação de variáveis de ambiente para tornar dados de login do servidor Azure local  
- pyodb - para acessar o banco de dados do SQL Server  
- openpyxl - para acessar lista de produtos  
- time - informar tempo de execução dos programas  

Situação atual do projeto (31/03):

✌ Implementado:
- WebScrapping do Mercado Livre e do Nagumo
- Servidor SQL Server criado no Azure e conexão estabelecida com o programa
- Variáveis de ambiente criadas

⏳ A ser implementado:
- Automatização de coleta de dados por meio de recurso na nuvem
- Realização de análise e visualização dos dados coletados
- WebScrapping de preços de gasolina, energia e água
- (talvez) WebScrapping de site shopper.com.br
