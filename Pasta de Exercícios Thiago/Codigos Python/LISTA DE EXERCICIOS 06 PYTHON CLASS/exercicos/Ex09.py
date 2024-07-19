class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel,consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def Ligar(self):
        print("Deseja ligar o carro ?[sim][nao]")
        pergunta =  str(input()).upper()
        
        if pergunta == "SIM":
            print('LIGOU !')
            print('VRUMMMM!!!')
        
        else:
            print("Vai ficar desligado ainda morô ?")

    def Abastecer(self):
        print("deseja Abastecer ?[sim][nao]")
        pergunta = str(input()).upper()
        if pergunta == "SIM":
            print("Quanto de nivel deseja abastecer ?")
            qnt = int(input())
            self.nivel = self.nivel + qnt
            print(f"Agora está com o nivel de {self.nivel}")

        else:
            print(f"Continua com o nivel de {self.nivel}")

    def Andar(self):
        print("Deseja andar ?[sim][nao]")
        pergunta = str(input()).upper()

        if pergunta == "SIM":
            print("Quanto deseja andar ?")
            km = int(input())
            gasto = km / self.nivel 
            print(f"Você andou {km} km e gastou {gasto}")

    def calcularImposto(self):
        ipva = self.valor * 2.5
        ipva = ipva / 100
        print(f"IPVA do {self.marca} é R${ipva}")