class Filme:
    def __init__(self,nome,duracao):
        self._nome = nome
        self._duracao = duracao
    
    def Play(self):
        print(f"Nome: {self._nome} \nDuração: {self._duracao}")

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
    
    def acaoMaster(self):
        print("BOOOM! EXPLODIU ")

class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(self, nome, duracao)
        
    def Dramaturgo(self):   
        print("MORREU LENTAMENTE")

class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(self, nome, duracao)
    
    def Sus(self):
        print("SERA QUE ELE VAI PEGAR A FACA ?")
