val = int(input("Digite seu número "))
somal = str(val)

if val > 0:
    val = somal
    print(sum(int(ab) for ab in somal))
else:
    print("Número inválido!")