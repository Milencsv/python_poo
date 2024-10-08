from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Audamarques", 25)
aluno1= Aluno("Tchequino", 13, 696)
prof1 = Professor("Albumquerco", 49, "Filosofia")

pessoa1.info()

aluno1.info()
aluno1.estudar()

prof1.info()
prof1.ensinar()