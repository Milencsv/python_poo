from academia import Aluno
listaAlunos = []

for contador in range (2):
    nome = input("Digite o nome do aluno: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    peso = float(input(f"Digite o peso de {nome}: "))
    altura = float(input(f"Digite  a altura de {nome}: "))

    pessoa = Aluno(nome, idade, peso, altura)
    listaAlunos.append(pessoa)

listaAlunos[0].exibirDados()
listaAlunos[0].calcularImc()

listaAlunos[1].exibirDados()
listaAlunos[1].calcularImc()

# while True:
#     nome = input("Digite o nome do aluno: ")
#     idade = int(input(f"Digite a idade de {nome}: "))
#     peso = float(input(f"Digite o peso de {nome}: "))
#     altura = float(input(f"Digite  a altura de {nome}: "))
#     experiencia = input("para adicionar mais um digite (sim) do contrário digite (não): ")
#     pessoa[nome, idade, peso, altura]= nome, idade, peso,altura
    
#     if experiencia == "não":
#         break
#     elif experiencia == "sim":
#         continue
    
# pessoa = Aluno(nome, idade, peso, altura)
# pessoa.exibirDados()
# pessoa.calcularImc()