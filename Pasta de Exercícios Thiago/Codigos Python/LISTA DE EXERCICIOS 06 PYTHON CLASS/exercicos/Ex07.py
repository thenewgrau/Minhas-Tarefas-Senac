class Triangulo:
    def __init__(self,lA,lB,lC):
        self.ladoA = lA
        self.ladoB = lB
        self.ladoC = lC

    def calcularPerimetro(self):
        soma = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro: {soma}")

    def getMaiorLado(self):
        if self.ladoA > self.ladoB:
            print(f"Maior lado: A \nValor: {self.ladoA}")

        elif self.ladoB > self.ladoC:
            print(f"Maior lado: B \nValor: {self.ladoB}")

        else:
            print(f"Maior lado: C \nValor: {self.ladoC}")