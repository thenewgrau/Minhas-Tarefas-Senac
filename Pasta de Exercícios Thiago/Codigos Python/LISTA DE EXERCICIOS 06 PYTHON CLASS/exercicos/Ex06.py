class Agenda:
    def __init__(self,d,m,a,anot):
        self.dia = d
        self.mes = m
        self.ano = a
        self.anotacao = anot

    def validarData(self):
        print("Digite o dia:")
        self.dia = int(input())
        print("Digite o mês:")
        self.mes = int(input())
        print("Digite o ano:")
        self.ano = int(input())
        print(f"{self.dia}/{self.mes}/{self.ano}")
        
    def anotarTarefa(self):
        print("Anotaí")
        self.anotacao = str(input())

    def mostraAnotacao(self):
        print(f"Anotação: {self.anotacao}")