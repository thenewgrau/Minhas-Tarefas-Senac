nome = input("Qual seu nome ? ")

larguraA = float(input("Qual é a largura do lado A ? "))
larguraB = float(input("Qual é a largura do lado B ? "))

valor1 = ((larguraA + larguraB)/2)

comprimentoA = float(input("Qual é o comprimento do lado A ? "))
comprimentoB = float(input("Qual é o comprimento do lado B ? "))

valor2 = ((comprimentoA + comprimentoB)/2)

area = valor1 * valor2
valortotal = 750 * area

print(f"{nome}, com a área de {area} metros quadrados, o valor do seu terrenos é R${valortotal}.")