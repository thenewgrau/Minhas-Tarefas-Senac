x = float(input("Digite sua primeira nota "))
y = float(input("Digite sua segunda nota "))

if (x and y > 10 and x and y < 0):
    media = (x + y)/2
    print("A sua média é igual a ",media)
else:
    print("Valor inválido.")
