x = float(input("Digite um dos lados do triângulo "))
y = float(input("Digite o segundo lado do triângulo "))
z = float(input("Digite o ultimo lado do triângulo "))
if x != y and x != z and y != z:
    print("é um triângulo escaleno pois seus três lados são diferentes.")
else:
    if x == y and x == z and y == z:
        print("é um triângulo equilátero pois possui todos os lados iguais")
    else:
        print("é um triângulo isósceles pois possui dois lados iguais")