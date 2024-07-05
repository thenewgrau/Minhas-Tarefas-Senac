sal = float(input("Digite seu salário "))
retirar = float(input("Digite quanto você quer de empréstimo "))

if retirar > sal * 0.20:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido!")