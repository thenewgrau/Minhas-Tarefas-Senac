abv = float(input("Digite o valor de aquisição "))

if abv < 50:
    abc = abv * 0.45
    abc = abv + abc
    print("O Valor de venda com 45% de lucro será ",abc)
elif abv > 50:
    abx = abv * 0.30
    abx = abx + abv
    print("O valor de venda com 30% de lucro será ",abx)