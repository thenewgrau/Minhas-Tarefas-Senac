from Ex02 import Professor
from Ex02 import Aluno

if __name__ == '__main__':
    profe = Professor('Walter',53,'Química Quantica','Química',14,3.415)
    alu = Aluno('Eduardo',16,0,0,0,0,101411512)

profe.informarProfessor()
alu.informarAluno()
alu.calcMedia()