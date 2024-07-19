class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
        

    def getNome(self):
        print(f"Nome: {self.nome}")

    def getCPF(self):
        print(f"CPF: {self.cpf}")

    def getNum(self):
        print(f"Número: {self.numero}")
    
    def getSaldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

    def setDeposito(self,novoSaldo,saldo):
        print("Confirme o valor:")
        novoSaldo = float(input())
        novoSaldo = saldo + novoSaldo
        self.saldo = novoSaldo

    def getSaque(self,saque,saldo):
        print("Digite o valor:")
        saque = float(input())
        saque = saldo - saque
        self.saldo = saque
        if self.saldo < saque:
            print("Não pode ser realizada essa transição !")
        else:
            print("Sucesso !")