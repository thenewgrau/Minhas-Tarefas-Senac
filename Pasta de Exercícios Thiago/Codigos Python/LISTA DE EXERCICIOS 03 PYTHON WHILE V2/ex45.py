print("Digite seu salário")
salcarlos = float(input())
saljoao = salcarlos * 0.75
while saljoao < salcarlos:
    salcarlos += salcarlos * 0.02
    saljoao += saljoao * 0.05
    meses = saljoao / 30
    
print(f"João vai precisar de {meses:.0f} meses para chegar no salário de Carlos")
    