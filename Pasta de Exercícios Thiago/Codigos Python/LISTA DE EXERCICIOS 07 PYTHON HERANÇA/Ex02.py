class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

class Professor(Pessoa):
    def __init__(self, nome, idade, formacao, disciplina, cargaHoraria, salario):
        super().__init__(nome,idade)
        self._formacao = formacao
        self._disciplina = disciplina
        self._cargaHoraria = cargaHoraria
        self._salario = salario

    def informarProfessor(self):
        print(f"Nome: {self._nome}\nIdade: {self._idade}\nFormação: {self._formacao}\nDisciplina: {self._disciplina}\nCarga Horária: {self._cargaHoraria} horas\nSalário: R${self._salario}")
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, nt1, nt2, nt3, nt4, matricula):
        super().__init__(nome, idade)
        self._nota1 = nt1
        self._nota2 = nt2
        self._nota3 = nt3
        self._nota4 = nt4
        self._matricula = matricula

    def informarAluno(self):
        print(f"Nome: {self._nome}\nIdade: {self._idade}\nMatricula: {self._matricula}")
    
    def calcMedia(self):
        print("Digite sua 1º nota")
        self._nota1 =  float(input())
        print("Digite sua 2º nota")
        self._nota2 =  float(input())
        print("Digite sua 3º nota")
        self._nota3 = float(input())
        print("Digite sua 4º nota")
        self._nota4 =  float(input())

        media = ((self._nota1 + self._nota2 + self._nota3 + self._nota4) / 4)
        print(f"Média: {media}")