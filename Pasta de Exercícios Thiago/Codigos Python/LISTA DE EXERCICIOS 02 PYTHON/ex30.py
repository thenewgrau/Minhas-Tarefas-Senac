estado = input("Digite o seu estado entre : MG, SP, RJ e MS ")
vali = float(input("Qual o valor do seu produto para ser calculado o imposto sobre ele ? "))
if estado == "MG":
    valf = vali * 0.07
    valf = valf + vali
    print(f"O valor final do seu produto com 7% de imposto sobre ele por estar no estado de Minas Gerais ficará {valf}")
elif estado == "SP":
    valf = vali * 0.12
    valf = valf + vali
    print(f"O valor final do seu produto com 12% de imposto sobre ele por estar no estado de São Paulo ficará {valf}")
elif estado == "RJ":
    valf = vali * 0.15
    valf = valf + vali
    print(f"O valor final do seu produto com 15% de imposto sobre ele por estar no estado de Rio de Janeiro ficará {valf}")
elif estado == "MS":
    valf = vali * 0.08
    valf = valf + vali
    print(f"O valor final do seu produto com 8% de imposto sobre ele por estar no estado de Mato Grosso do Sul ficará {valf}")
else:
    print("Digite um estado dentre dos listados.")