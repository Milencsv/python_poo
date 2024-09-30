class Pessoa: # classe possui atributos e métodos. Atributos falam "o que é" e os métodos falam "o que faz""
    #Atributos
    nome = "Victor"
    peso = 69
    altura = 1.76
    escolaridade = "Ensino Médio"

    #Métodos
    def falar(self, texto):
        print(f"Tenho algo para te dizer: {texto}")

#CRIANDO OS OBJETOS
pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("A semana mal começou e já tá um inferno :)")