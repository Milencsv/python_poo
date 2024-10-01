class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def exibirDados(self):
        print(f"O aluno {self.nome}, de {self.idade} anos, está com {self.altura} metros de altura e pesando {self.peso}kg")

    def calcularImc(self):
        imc = self.peso/(self.altura**2)
        print(f"O imc do {self.nome} é {imc:.2f}")