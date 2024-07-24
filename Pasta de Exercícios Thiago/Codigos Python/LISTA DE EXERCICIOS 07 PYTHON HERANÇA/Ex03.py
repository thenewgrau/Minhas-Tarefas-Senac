class Ingresso:
    def __init__(self,preco,setor):
        self._preco = preco
        self._setor = setor

    def setAlterarPreco(self):
        print(f"Preço atual: R${self._preco}")
        print("Digite o novo preço")
        self._preco = float(input())
        print(f"Novo preço: R${self._preco}")

    def mostrarSetor(self):
        print(f"Setor: {self._setor}")


class Vip(Ingresso):
    def __init__(self, preco, setor, bebida, camarote, openBar, openFood, estacionamento):
        super().__init__(preco, setor)
        self._bebida = bebida
        self._camarote = camarote
        self._openBar =  openBar
        self._openFood = openFood   
        self._estacionamento = estacionamento

    def mostrarInformacoes(self):
        print(f"Acesso a openBar: {self._openBar}\nAcesso a openFood: {self._openFood}\nAcesso ao estacionamento: {self._estacionamento}\nAcesso a bebida: {self._bebida}\nAcesso ao camarote: {self._camarote}")

