class Cliente:
    def __init__(self, nome, idade, fone, email):
        self._nome = nome
        self.idade = idade
        self.fone = fone
        self.email = email

    def Comprar(self):
        print(f'{self._nome} realiza compras')

    def getNome(self):
        return self._nome
    

class Premium(Cliente):
    def __init__(self, nome, idade, fone, email, areaVip=True, desconto=20):
        super().__init__(nome, idade, fone, email)
        self.areaVip = areaVip
        self._desconto = desconto
    
    def ComprarVip(self):
        print(f'{self._nome} compra com desconto de {self._desconto}%')
    
cli = Cliente('Heisenberg','52','+556728381922','walterwhite@outlook.com')
cli = Premium('Heisenberg','52','+556728381922','walterwhite@outlook.com')
cli.Comprar()
cli.ComprarVip()
