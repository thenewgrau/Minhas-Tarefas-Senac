anos = int(input("Digite sua idade em anos : "))
meses = int(input("Digite sua idade em mesês agora : "))
dias = int(input("Digite sua idade agora em dias : "))

anos = 365 * anos
meses = 30 * meses
soma = anos + meses + dias

print(f"Você tem {soma} dias. ")