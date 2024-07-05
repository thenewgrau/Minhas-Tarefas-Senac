terminar = True

while terminar == True:
    print("_"*90)
    print("Digite o número de escolha \nAdição(1) \nSubtração(2) \nMultiplicação(3) \nDivisão(4) \nSair(5)")
    print("_"*90)
    escolher = int(input())
    
    if escolher == 1:
        print("Digite o número que você deseja somar")
        num1 = int(input())
        print("Digite o outro agora")
        num2 = int(input())
        smt = num1 + num2
        print(f"A somatória deles é : {smt}")
    
    elif escolher == 2:
        print("Digite o número que deseja subtrair")
        num1 = int(input())
        print("Agora digite o segundo número")
        num2 = int(input())

        if num1 < num2:
            smt = num2 - num1
            print(f"Subtração : {smt}")

        else:
            smt = num1 - num2
            print(f"Subtração : {smt}")

    elif escolher == 3:
        print("Digite o primeiro número para multiplicar")
        num1 = int(input())
        print("Agora digite o segundo número")
        num2 = int(input())
        smt = num1*num2
        print(f"A multiplicação de {num1} e {num2} é {smt}")

    elif escolher == 4:
        print("Escolha o número que será divido")
        num1 = float(input())
        print("Digite o divisor")
        num2 = float(input())
        smt = num1/num2
        print(f"A divisão entre {num1} e {num2} é {smt}")

    elif escolher == 5:
        print("Programa Finalizado.")
        terminar = False

    else:
        print("Digite um número válido!")