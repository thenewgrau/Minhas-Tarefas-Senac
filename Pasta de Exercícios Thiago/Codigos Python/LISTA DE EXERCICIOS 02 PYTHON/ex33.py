
# ADICIONAR IF SE A QUANTIDADE FOR UMA
quero = int(input("Digite o código do seu lanche "))
if quero == 100:
    quant = int(input("Quantos cachorro(s) quente(s) você quer ? "))
    if quant == 1:
        quero = 12.00
        print(f"O seu Cachorro Quente vai te custar R${quero:.2f}.")
    else:
        quero = quant * 12
        print(f"Você pediu {quant} Cachorros Quentes e vai dar R${quero:.2f}")
elif quero == 102:
    quant = int(input("Quantos X-Salada(s)você quer ? "))
    if quant == 1:
        quero = 18.50
        print(f"Você pediu {quant} X-Salada e custará {quero:.2f}")
    else:
        quero = quant * 18.50
        print(f"Você pediu {quant} X-Saladas e será cobrado R${quero:.2f}")
elif quero == 103:
    quant = int(input("Quantos X-Bacon(s) você quer "))
    if quant == 1:
        quero = 25.50
        print(f"Você pediu apenas {quant} X-Bacon e custará {quero:.2f}")
    else:
        quero = quant * 25.50
        print(f"Você pediu {quant} X-Bacons e será cobrado R${quero:.2f}")
elif quero == 104:
    quant = int(input("Quantos X-Burger(es) você deseja nobre senhor ? "))
    if quant == 1:
        quero = 17.00
        print(f"Você pediu um X-Burger e será cobrado R${quero:.2f}")
    else:
        quero = quant * 17.00
        print(f"Você pediu {quant} de X-Burger(es) e será cobrado R${quero:.2f}")
elif quero == 105:
    quant = int(input("Quantos Sucos de Laranja você quer ? "))
    if quant == 1:
        quero == 9.50
        print(f"Você pediu um suco de laranja e será cobrado R${quero:.2f}")
    else:
        quero = quant * 9.50
        print(f"Você pediu {quant} Sucos de Laranja e será cobrado R${quero:.2f}")
elif quero == 106:
    quant = int(input("Quantos refrigerantes você quer ? ")) 
    if quant == 1:
        quero = 6.00
        print(f"Você pediu um refrigerante e será cobrado {quero:.2f}")
    else:
        quero = quant * 6.00
        print(f"Você pediu {quant} de Refrigerantes e será cobrado R${quero:.2f}")
else:
    print("DIGITE UM CÓDIGO EXISTENTE SEU ADERBAL!")