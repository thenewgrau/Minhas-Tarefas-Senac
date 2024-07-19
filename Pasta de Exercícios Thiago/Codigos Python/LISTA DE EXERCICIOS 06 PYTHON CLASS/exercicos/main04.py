from Ex04 import Conta

user = Conta('Eduardo','123.456.789-10','+55 (67) 99123-3221',0)
print("Bem Vindo !")   
user.getNome()
user.getCPF()
user.getNum()

while True: 
    print("Siga as instruções abaixo:")
    print("[1] Para ver Saldo")
    print("[2] Para Depositar")
    print("[3] Para Sacar")
    x = int(input())

    if x == 1:
        saldo = user.getSaldo()
        

    elif x == 2:
        print("Digite o seu saldo")
        saldo = float(input())
        print("Quanto deseja depositar ?")
        novoSaldo = float(input())
        user.setDeposito(novoSaldo,saldo)
         
    elif x == 3:
        user.getSaque(saque=0,saldo=float(input()))
        
    else:
        print("Selecione uma das opções !")