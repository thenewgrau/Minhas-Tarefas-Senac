## MODULO CLIENTE ##

class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        print(f"Nome do Cliente: {self.nome}")

    def getIdade(self):
        print(f"Idade do Cliente: {self.idade}")