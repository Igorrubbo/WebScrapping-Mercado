# Programa de WebScrapping de preços de produtos de mercado

Esse programa ainda está em desenvolvimento.

Comecei esse projeto com dois objetivos em mente: pesquisa de preço e cálculo de inflação pessoal.
A algum tempo me pergunto se vale mais a pena comprar produtos no mercado local ou no mercado livre, com isso decidi escrever um programa para automatizar essa pesquisa para mim.
A ideia é extrair os preços dos produtos que eu e minha família consome com frequência dos sites do Mercado Livre e do Nagumo e realizar uma pequena análise da diferença de preços entre os produtos.
O segundo objetivo necessita apenas de uns poucos passos a mais do que o primeiro, sendo necessário uma rotina de extração de dados para se construir um banco de dados, no caso está sendo usado SQL Server.
Esse banco de dados será usado para verificar a variação dos preços dos produtos.
Mas além desse banco de dados de mercado também é necessário alguns dados a mais, como preço da gasolina, da energia, da água e outros.
Depois de que todos esses dados forem extraídos, será questão apenas de realizar uma breve análise e visualização de dados.

Ferramentas utilizadas no projeto:
Python - Como linguagem de programação principal
VSCode - IDE escolhido para o desenvolvimento do código
Git - Utilizado para controle de versão e registro de atividades
Excel - A lista de produtos a serem pesquisados se encontra em uma planilha excel
SQL Server - Base de dados escolhida para desenvolvimento do projeto
Microsoft Azure - Serviço em nuvem escolhido para desenvolvimento do projeto

Bibliotecas utilizadas:
Beautiful Soup e Selenium - ferramentas principais para WebScrapping
dotenv - criação de variáveis de ambiente para tornar dados de login do servidor Azure local
pyodb - para acessar o banco de dados do SQL Server
openpyxl - para acessar lista de produtos
time - informar tempo de execução dos programas

Situação atual do projeto (31/03):

Implementado:
- WebScrapping do Mercado Livre e do Nagumo
- Servidor SQL Server criado no Azure e conexão estabelecida com o programa
- Variáveis de ambiente criadas

A ser implementado:
- Automatização de coleta de dados por meio de recurso na nuvem
- Realização de análise e visualização dos dados coletados
- WebScrapping de preços de gasolina, energia e água
- (talvez) WebScrapping de site shopper.com.br
