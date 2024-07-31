class Imovel:
    def __init__(self, insc, valora, iptu):
        self._inscricaoMunicipal = insc
        self._valorAluguel = valora
        self._iptu = iptu

    def obterParcelaIPTU(self):
        larg = float(input("Digite a largura do seu imovel "))
        comp = float(input("Digite agora o comprimento do seu imóvel "))
        area = larg * comp
        self._iptu = (area * 1000)*0.01
        print(f"Parcela do IPTU: R${self._iptu:.2f}")

    def setValorAluguel(self):
        print()
        print(f"Valor atual: R${self._valorAluguel}")
        print("Diga o valor do alguel")
        valorAlu = float(input())
        self._valorAluguel = valorAlu
        print(f"Valor do aluguel: R${self._valorAluguel}")

class Casa(Imovel):
    def __init__(self, insc, valora, iptu, piscina, banheiro):
        super().__init__(insc, valora, iptu)
        self._piscina = piscina
        self._banheiro = banheiro

    def getInformaCasa(self):
        print(f"Inscrição: {self._inscricaoMunicipal}\nValor Alugel R${self._valorAluguel}\nIPTU: R${self._iptu}\nPiscina {self._piscina}\nBanheiro {self._banheiro}")

class Apartamento(Imovel):
    def __init__(self, insc, valora, iptu, quartos, elevador):
        super().__init__(insc, valora, iptu)
        self._quartos = quartos
        self._elevador = elevador

    def getInformaAp(self):
        print(f"Inscrição: {self._inscricaoMunicipal}\nValor Alugel R${self._valorAluguel}\nIPTU: R${self._iptu}\nQuartos {self._quartos}\nElevador {self._elevador}")

class Terreno(Imovel):
    def __init__(self, insc, valora, iptu,aream2):
        super().__init__(insc, valora, iptu)
        self._areaM2 = aream2

    def getInformaTerreno(self):
        print(f"Inscrição: {self._inscricaoMunicipal}\nValor Alugel R${self._valorAluguel}\nIPTU: R${self._iptu}\nArea em metros quadrados {self._areaM2}")

class Chacara(Imovel):
    def __init__(self, insc, valora, iptu, churrasqueira, areadel ):
        super().__init__(insc, valora, iptu)
        self._churrasqueira = churrasqueira
        self._areaDeLazer = areadel

    def getInformaChacara(self):
        print(f"Inscrição: {self._inscricaoMunicipal}\nValor Alugel R${self._valorAluguel}\nIPTU: R${self._iptu}\nChurrasqueira {self._churrasqueira} \nArea de Lazer {self._areaDeLazer}")
        
    
