class Aluno:
    def __init__(self,nome,ra,nota1:float,nota2:float,nota3:float,nota4:float,notafi:float):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.notafinal = notafi

    def getNome(self):
        print(f"Nome do aluno: {self.nome}")

    def getRa(self):
        print(f"RA: {self.ra}")

    def getNota1(self):
        print(f'1ª Nota: {self.nota1}')

    def getNota2(self):
        print(f'2ª Nota: {self.nota2}')

    def getNota3(self):
        print(f'3ª Nota: {self.nota3}')

    def getNota4(self):
        print(f'4ª Nota: {self.nota4}')

    def getNotaFi(self):
        self.notafinal = ((self.nota1 + self.nota2 + self.nota3 + self.nota4)/4)
        print(f"Nota Final: {self.notafinal}")
        if self.notafinal < 5.0:
            print("Reporvado !")
        
        elif self.notafinal > 5.0 and self.notafinal < 6.9:
            print("Recuperação !")
        
        else:
            print("Aprovado !")