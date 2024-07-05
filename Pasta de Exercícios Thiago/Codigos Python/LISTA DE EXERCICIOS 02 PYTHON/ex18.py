s = input("Digite o seu sexo M ou F ")
h = float(input("Digite a sua altura "))

if s == "M":
    res = (72.7 * h) - 58
    print(f"O seu peso ideal é {res:.2f}")
elif s == "F":
    res = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {res:.2f}")
else:
    print("Alguma das informações está incorreta.")