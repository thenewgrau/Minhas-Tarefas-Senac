from Ex09 import Compra
from Ex09 import Avista
from Ex09 import Parcela
from time import sleep

if __name__ ==  "__main__":
    compraum = Compra(34 , "Hot Wheels", 3000, 0)
    compraum = Avista(34, "Hot Wheels", 3000, 0, 30)
    compradois = Compra(22, "Celular", 5431, 0)
    compradois = Parcela(22,"Celular", 5431, 0)

compraum.calcularValorTotal()
sleep(1)
print()
compradois.calcularValorTotal()
sleep(1)
print()
compraum.getDesconto()
sleep(1)
print()
compradois.getParcela() 