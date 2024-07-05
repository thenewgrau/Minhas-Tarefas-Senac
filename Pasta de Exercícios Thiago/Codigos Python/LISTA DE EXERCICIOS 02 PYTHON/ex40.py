precoporh = float(input("Digite o preço da sua hora amigão (sem maldade) "))
qnth = float(input("Quantas horas você trabalhou ? "))
salbtalv = precoporh * qnth
salini = salbtalv * 0.08
salin = salbtalv - salini
salsindi = salbtalv * 0.05
salsind = salbtalv - salsindi
salb = salsind + salin
salq = salb * 0.11
salq = salb - salq
print(f"O seu salário Bruto é R${salb}")
print(f"Você pagou em INSS R${salini}")
print(f"Você pagou ao sindicato R${salsindi}")
print(f"O Seu salário liquído foi de R${salq}")

