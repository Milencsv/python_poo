from produto import Produto, Eletronico

prod1 = Produto("Armário", 758.99)
eletro1 = Eletronico("Escova de dentes", 50.00 , 220)

prod1.descrever()
prod1.calcularDesconto(10)

eletro1.descrever()
eletro1.calcularDesconto(30)