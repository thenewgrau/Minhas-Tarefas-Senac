valorv = float(input("Digite o valor da venda "))
if valorv < 20000:
    valorf = valorv * 0.14 + 400
    print(f"A comissão do vendedor é R${valorf:.2f}")
else:
    if valorv >= 20000 and valorv < 40000:
        valorf = valorv * 0.14 + 500
        print(f"A comissão do vendedor é R${valorf:.2f}")
    elif valorv >= 40000 and valorv < 60000:
        valorf = valorv * 0.14 + 550
        print(f"A comissão do vendedor sobre venda é R${valorf:.2f}")
    elif valorv >=60000 and valorv < 80000:
        valorf = valorv * 0.14 + 600
        print(f"A comissão do vendedor sobre a venda é R${valorf:.2f}")
    elif valorv >= 80000 and valorv < 100000:
        valorf = valorv * 0.14 + 650
        print(f"A comissão do vendedor é R${valorf:.2f}")
    elif valorv >= 100000:
        valorf = valorv * 0.16 + 700
        print(f"A comissão do valor é R${valorf:.2f}")