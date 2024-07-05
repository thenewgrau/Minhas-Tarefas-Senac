horast = float(input("Digite quantas horas você trabalhou hoje "))
horast = horast * 32.50
horase = float(input("Digite quantas horas extras você teve hoje "))
horase = horase * 44.50

sal = horast + horast
salb = sal * 0.11
salb = sal - salb

print(f"Você receberá R${sal} em salário liquido.")
print(f"Você receberá R${salb} como salário bruto, contando os impostos do INSS de 11%.")