bsmai = float(input("Digite a Base Maior do seu Trapésio "))
bsmen = float(input("Digite a Base Menor do seu Trapésio "))
h = float(input("Digite a Altura do seu Trapésio "))

if bsmai or bsmen > 0:
    a = (((bsmai + bsmen)*h)/2)
    print(f"A área do seu trapésio é {a}")
else:
    print("As bases do seu trapésio devem ser maiores que 0")