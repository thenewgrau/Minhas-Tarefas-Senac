class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def areaCirculo(self):
        area = (self.raio**2) * 3.1415
        print(f"Área: {area}")
    
    def raioCirculo(self):
        print(f"Raio: {self.raio}")

    def circunferenciaCirculo(self):
        circ =  (self.raio**2) * (3.1415**2)
        print(f"Circunferência: {circ}")