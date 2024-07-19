class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def calc(self):
        res = 3.14 * (self.raio**2)

Circulov = Circulo(3)

Circulov.calc()