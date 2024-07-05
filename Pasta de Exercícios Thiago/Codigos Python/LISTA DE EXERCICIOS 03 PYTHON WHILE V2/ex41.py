terminar = True

while terminar == True:
    print("Digite o valor de R1")
    r1 = float(input())
    print("Digite o valor de R2")
    r2 = float(input())
    resis = (((r1*r2))/(r1+r2))
    print(f"valor da resistência {resis}")
    if resis == 0:
        print("Programa finalizado.")
        terminar = False
    