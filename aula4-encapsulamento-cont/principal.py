from funcionario import Funcionario
funcionario1 = Funcionario("Robervaldo", 2500)
print(funcionario1.getNome())

funcionario1.setNome("Gleicianny")

print("Parabéns pela sua transição sem volta, agora seu nome é ",funcionario1.getNome())

#Estamos tentando acessar o atributo salário
print("Seu slaário atual é: ", funcionario1.salario)

funcionario1.salario = 5000

print("Seu slaário atual é: ", funcionario1.salario)
