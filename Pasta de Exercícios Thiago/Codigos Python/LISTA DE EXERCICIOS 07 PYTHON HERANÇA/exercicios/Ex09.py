class Compra:
    def __init__(self, num, prod, val, valt):
        self._numero = num
        self._produto = prod
        self._valor = val
        self._valorTotal = valt

    def calcularValorTotal(self):
        frete  = self._valor * 0.05
        imposto = self._valor * 0.17
        self._valorTotal = self._valor + frete + imposto
        print(f"Número de pedido {self._numero}")
        print(f"Produto {self._produto}")
        print(f"Calculo do Valor: {self._valorTotal:.2f}")

class Avista(Compra):
    def __init__(self, num, prod, val, valt, desc):
        super().__init__(num, prod, val, valt)
        self._desconto = desc
    
    def getDesconto(self):
        frete  = self._valor * 0.05
        imposto = self._valor * 0.17
        valors = self._valor + frete + imposto
        self._valorTotal = valors * (self._desconto / 100)
        self._valorTotal = valors - self._valorTotal

        print(f"Número de pedido {self._numero}")
        print(f"Produto {self._produto}")
        print(f"Valor com desconto R${self._valorTotal} ")

class Parcela(Compra):
    def __init__(self, num, prod, val, valt):
        super().__init__(num, prod, val, valt)

    def getParcela(self):
        frete  = self._valor * 0.05
        imposto = self._valor * 0.17
        self._valorTotal = self._valor + frete + imposto
        duasvezes =  self._valorTotal / 2
        quatrovezes = self._valorTotal / 4
        oitovezes = self._valorTotal / 8
        dezesvezes = self._valorTotal / 16

        print(f"Em 2x sem juros R${duasvezes:.2f}")
        print(f"Em 4x sem juros R${quatrovezes:.2f}")
        print(f"Em 8x sem juros R${oitovezes:.2f}")
        print(f"Em 16x sem juros R${dezesvezes:.2f}")