menu = input("Escolha uma das opções dentre : Soma, Diferença, Produto, Divisão ")
if menu == "Soma":
    x = int(input("Escolha seu primeiro número para somar "))
    y = int(input("Agora mais um número para somar "))
    soma = x + y
    print(f"A soma dos dois números é {soma}")
elif menu == "Diferença":
    x = int(input("Escolha seu primeiro número para fazer a diferença "))
    y = int(input("Agora mais um número para a diferença "))
    if x > y:
        dif = x - y
        print(f"A diferença dos números é {dif}")
    else:
        dif = y - x
        print(f"A diferença entre eles é {dif}")
elif menu == "Produto":
    x = int(input("Escolha seu primeiro número para calcular o produto dentre eles "))
    y = int(input("Agora mais um número para calcular o produto "))
    prod = x * y
    print(f"O produto entre os dois é {prod}")
elif menu == "Divisão":
    x = int(input("Escolha seu primeiro número para dividir "))
    y = int(input("Agora mais um número para dividir "))
    if x == 0:
        print("O Denominador não pode ser igual a 0 !")
    else:
        div = x / y
        print(f"A Divisão entre os números é {div}")