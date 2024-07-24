from Ex10 import Transporte
from Ex10 import Aquatico
from Ex10 import Terrestre
from Ex10 import Aereo

if __name__ == "__main__":
    transAereo = Transporte(2)
    transAereo = Aereo(2, 3, 1)
    transTerra = Transporte(4)
    transTerra = Terrestre(4, 4, "Vermelho", 4, "ABQ-2124")
    transAquatico = Transporte(16)
    transAquatico = Aquatico(16, 4)

print("Aquatico")
transAquatico.getInfAq()
print()
print("Terrestre")
transTerra.getInfTerra()
print()
print("Aereo")
transAereo.getInfAereo()