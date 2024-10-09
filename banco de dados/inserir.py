import sqlite3

#Passo1 - Conexão com o banco de dados
conexao = sqlite3.connect('departamento.db')

#Passo 2 - Verificar se a tabela existe ou não
tabela = """
CREAT TABLE IF NOT EXISTS  funcionário(
    codigo INTEGER PRIMARY KEY  AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo 3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco
consulta = conexao.cursor()

#Passo 4 -   Executar o comando de criação da tabela
consulta.execute(tabela)

#INSERIR DADOS NA TABELA
#Passo  5  -  Solicitar dados do usuário
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salario do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Passo 6 - criando comando SQL para inserir ps dados da tabela
sql = "INSERIR INTO  funcionário VALUES(?,?,?,?)"# Colocamos ? no lugar dos dados reais, para evitar possiveis ataques de sql injection. Isso é uma implementação da biblioteca  sqlite3.

#Passo 7 - Organizar os dados que irão subsituir os ? no comando SQL
campos = (None , nome, salario, cargo)# Criando uma tupla com os dados que irão substituir ?. Ao informar o valor 'None' estamos dizendo que será atribuido o valor padrão do AUTOINCREMENT