from time import sleep

class Passagem:
    def __init__(self, preco, assento):
        self._preco = preco
        self._assento = assento

    def setAlterarPreco(self):
        print(f"Preço atual da passagem: R${self._preco}")
        print("Digite o novo preço")
        self._preco = float(input())
        print(f"Novo preço R${self._preco}")

    def escolherAssento(self):
        print("Escolhe seu assento")
        self._assento = int(input())

class passagemOnibus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self._placa = placa
        self._leito = leito
    
    def mostrarPlaca(self):
        print(f"Placa do ônibus: {self._placa}")

    def mostrarLeito(self):
        print(f"Leito do ônibus: {self._leito}")

    def abastecer(self):
        print("O ônibus vai abastecer !!!! se prepara pra ir ao banheiro !!!!")

class passagemAviao(Passagem):
    def __init__(self, preco, assento, portaoemb, checkin):
        super().__init__(preco, assento)
        self._portao = portaoemb
        self._checkin = checkin
    
    def mostrarPortao(self):
        print(f"Portão de embarque {self._portao}")

    def mostrarCheckin(self):
        print(f"Checkin: {self._checkin}")

    def decolar(self):
        print("Decolando em 3")
        sleep(1)
        print("Decolando em 2")
        sleep(1)
        print("Decolando em 1")
        sleep(1)
        print("DECOLOU !!!!")
