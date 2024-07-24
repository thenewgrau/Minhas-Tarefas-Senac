from Ex08 import Casa
from Ex08 import Apartamento
from Ex08 import Terreno
from Ex08 import Chacara
from time import sleep

if __name__ == "__main__":
    casa = Casa(23312, 3433, 2000, "Grande", "Pequeno")
    ap = Apartamento(2111, 5000, 2000, 3, "Compartilhado")
    ter = Terreno(22311, 200000, 23000, 4000)
    cac = Chacara(12123, 5000000, 50000, "POTENTE !!!", "Gigantesca")

casa.obterParcelaIPTU()
sleep(1)
casa.setValorAluguel()
sleep(1)
casa.getInformaCasa()
sleep(1)
print()

ap.getInformaAp()
sleep(1)
print()

ter.getInformaTerreno()
sleep(1)
print()

cac.getInformaChacara()
