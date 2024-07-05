menu = input("A mini calculadora possui 4 tipos de calculo eles são : Soma, Subtração, Multiplicação e Divisão. Escolha uma das alternativas para realizar um calculo ")

if menu == "Soma":
    x = int(input("Escolha seu primeiro número para somar "))
    y = int(input("Agora mais um número para somar "))
    soma = x + y
    print(f"A Soma dos seus números é {soma}")
elif menu == "Subtração":
    x = int(input("Escolha seu primeiro número para subtrair "))
    y = int(input("Agora mais um número para subtrair "))
    sub = x - y 
    print(f"A subtração dos seus número é {sub}")

elif menu == "Multiplicação":
    x = int(input("Escolha seu primeiro número para multiplicar "))
    y = int(input("Agora mais um número para multiplicar "))
    mul = x * y
    print(f"A multiplicação dos seus número é {mul}")
elif menu == "Divisão":
    x = int(input("Escolha seu primeiro número para dividir "))
    y = int(input("Agora mais um número para dividir "))
    div = x / y
    print(f"A divisão dos seus números é {div}")

    

