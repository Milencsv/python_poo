class Pessoa:
    #Método Construtor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

    #Criando Métodos
    def exibirHobby(self):
        print(f"-Olá, meu hobby no momento é {self.hobby}")
    
    def mudarHobby(self, novoHobby):
        self.hobby = novoHobby
        print(f"Meu hobby mudou para {novoHobby}")