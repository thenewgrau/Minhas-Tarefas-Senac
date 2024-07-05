nome = input("Qual seu nome ? ")
saldo = int(input("Qual o seu saldo ? " ))
saque = int(input("Quanto você deseja sacar ? "))

if(saque > saldo):
    print("Você não possui saldo suficiente para executar o saque. \nPor favor digite outro valor.")
else:
    saldo = saldo - saque
    print(f"Parabens {nome}, você concluiu o saque e ainda possui {saldo} reais. ")