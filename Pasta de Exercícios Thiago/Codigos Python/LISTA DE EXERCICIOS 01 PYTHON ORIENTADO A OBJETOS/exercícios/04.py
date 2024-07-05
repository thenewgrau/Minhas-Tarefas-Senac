#Escreva um programa, com uma função que necessite de um argumento. A função retornar o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def nump(p):
    print("P")

def numn(n):
    print("N")

while True:    
    x = int(input("Digite seu número positivo ou negativo "))

    if x > 0:
        nump("P")

    else:
        numn("N")