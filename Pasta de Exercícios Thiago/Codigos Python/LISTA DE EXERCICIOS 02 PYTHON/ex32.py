idade = int(input("Qual a sua idade ? "))
if idade >= 5 and idade <= 12:
    print("Você está na categoria Infantil")
elif idade >= 13 and idade <=17:
    print("Você está na categoria Juvenil")
elif idade >= 18:
    print("Você está na categoria Sênior")