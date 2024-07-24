class Transporte:
    def __init__(self, capacidade):
        self._capacidade = capacidade

class Aquatico(Transporte):
    def __init__(self, capacidade, velas):
        super().__init__(capacidade)
        self._velas = velas

    def getInfAq(self):
        print(f"Capacidade {self._capacidade} \nVelas {self._velas}")

class Terrestre(Transporte):
    def __init__(self, capacidade, rodas, cor, numerop, placa):
        super().__init__(capacidade)
        self._rodas = rodas
        self._cor = cor
        self._numeroDePortas = numerop
        self._placa = placa

    def getInfTerra(self):
        print(f"Quantidade de Portas {self._numeroDePortas} \nPlaca {self._placa} \nCor {self._cor} \nQuantidade de rodas {self._rodas}")

class Aereo(Transporte):
    def __init__(self, capacidade, rodas, qntmotores):
        super().__init__(capacidade)
        self._rodas = rodas
        self._quantidadeMotores = qntmotores
    
    def getInfAereo(self):
        print(f"Quantidade de motores {self._quantidadeMotores} \nQuantidade de rodas {self._rodas}")
        
