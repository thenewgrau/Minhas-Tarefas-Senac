cst = float(input("Digite o custo de fábrica do seu carro "))
if cst < 12000:
    cstf = cst * 0.05
    cstf = cstf + cst
    ##sem imposto
    print(f"O custo será de {cstf}")
elif cst >= 12000 and cst < 25000:
    cstf = cst * 0.25
    cstf = cstf + cst
    print(f"O custo será de {cstf}")
elif cst > 25000:
    cstf = cst * 0.35
    cstf = cstf + cst
    print(f"O custo será de {cstf}")
  