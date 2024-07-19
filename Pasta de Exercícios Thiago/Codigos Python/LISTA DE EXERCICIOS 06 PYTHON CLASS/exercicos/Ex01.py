class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def getNome(self):
        print(f"Nome: {self.nome}")
    
    def getIdade(self):
        print(f"Idade: {self.idade}")

    def getEnd(self):
        print(f"Endereço: {self.endereco}")

