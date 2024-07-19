## MODULO PRODUTO ##

class Produto:
    def __init__(self,nome,desc,preco:float,qntEstoq:int):
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.qntEstoq = qntEstoq 

    def getNome(self):
        print(f"Nome do Produto : {self.nome}")
    
    def getEstoque(self):
        print(f"Quantidade em estoque: {self.qntEstoq}")

    def getDesc(self):
        print(f"Descrição: {self.desc}")

    def getPreco(self):
        print(f"Preço: {self.preco}")
