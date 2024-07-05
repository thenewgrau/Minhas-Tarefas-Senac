ht = float(input("Quantas horas você trabalhou ? "))

h = 40.50

ipd = 0.11

salq = (h * ht)

if salq > 2500:

    salqc = salq * ipd

    salq = salq - salqc

    print("O seu salário liquido é igual a contando com o imposto de renda",salq)
else:
    print("O seu salário líquido é igual a",salq)
