

terminar = True

while terminar == True:
    num = float(input("Digite o número "))
    numquadr = num**2
    numcubo = num**3
    numraiz = num**0.5
    print(f"O quadrado do número : {numquadr} \nO cubo do númnero : {numcubo} \nA raíz quadrada do número : {numraiz}")
    print("_"*90)

    if num <= 0:
        print("Finalizado.")
        terminar = False