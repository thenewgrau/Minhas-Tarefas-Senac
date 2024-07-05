ESQT = float(input("Qual é o saldo estoque do saldo atual ? "))
SANT = float(input("Qual foi o estoque do mês anterior ? "))
ENT = float(input("Qual foi a quantidade comprada no mês ? "))
ND = float(input("Qual foi a quantidade vendida ou utlizada do produto ? "))

ESQT = SANT + ENT - ND

print(f"O saldo do estoque atual é : {ESQT}")