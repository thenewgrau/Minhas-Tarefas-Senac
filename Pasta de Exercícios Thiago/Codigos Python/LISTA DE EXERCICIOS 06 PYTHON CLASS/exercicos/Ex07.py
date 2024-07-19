class Triangulo:
    def __init__(self,la,lb,lc):
        self.ladoA = la
        self.ladoB = lb
        self.ladoC = lc

    def calcPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print(f"Perímetro: {perimetro}")

    def getMlado(self):
        if self.ladoA > self.ladoB:
            print("O maior lado é A")
        
        elif self.ladoB < self.ladoC:
            print("O maior lado é C")

        else:
            print("O maior lado é B")