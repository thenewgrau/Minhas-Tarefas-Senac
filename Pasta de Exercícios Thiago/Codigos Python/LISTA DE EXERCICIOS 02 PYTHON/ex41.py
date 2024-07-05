import math

a = int(input("Digite o valor de a "))
b = int(input("Digite o valor de b "))
c = int(input("Digite o valor de c "))
delt = (b**2) - (4 * a * c)
xis = (-b + math.sqrt(delt) ) / (2*a)
xisdois = (-b  - math.sqrt(delt) ) / (2*a)
if delt < 0:
    print("Não existe raiz.")
elif delt == 0:
    print("Raiz única.")
elif delt > 0:
    print(f"X^1, correspode á {xis}")
    print(f"X^2, corresponde á {xisdois}")