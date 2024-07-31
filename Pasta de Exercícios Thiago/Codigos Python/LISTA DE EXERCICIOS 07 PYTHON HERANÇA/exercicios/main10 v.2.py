from Ex10v2 import Transporte
from Ex10v2 import Aquatico
from Ex10v2 import Lancha
from Ex10v2 import Navio
from Ex10v2 import Terrestre
from Ex10v2 import Aereo
from Ex10v2 import AviaoComercial
from Ex10v2 import AviaoMonomotor


if __name__ == "__main__":
    transAereo = Transporte(2)
    transAereo = Aereo(2, 3, 1)
    transTerra = Transporte(4)
    transTerra = Terrestre(4, 4, "Vermelho", 4, "ABQ-2124")
    transAquatico = Transporte(16)
    transAquatico = Aquatico(16, 4)
    transMono = AviaoMonomotor(2, 3, 1)
    transComercio = AviaoComercial(250, 16, 4)
    transLancha = Lancha(2, 0)
    transNavio = Navio(500, 0)



print("Aquatico")
transAquatico.getInfAq()
print()
print("Terrestre")
transTerra.getInfTerra()
print()
print("Aereo")
transAereo.getInfAereo()
print()
transNavio.getInfoNavio()
transLancha.getInfoLancha()
print()
transComercio.getInfoAviaoComercial()
transMono.getInfoMono()