class Pessoa:
    #Criar o método construtor
    def __init__(self,nome, altura, idade):
        #estamos criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usafos como valores dos atributos. 
        self.nome = nome
        self.altura = altura
        self.idade = idade  #Atributo da classe  =   informação da classe
    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura é {self.altura} e sua idades é {self.idade}")

#CRIANDO OS OBJETOS
p1 = Pessoa("Daniel", 1.82, 75)
p2 = Pessoa("Victor", 1.76, 69)

p1.exibirDados()
p2.exibirDados()