'''A partir do exercício anterior crie uma função que inicialize uma matriz de 4 x 4, e peça ao 
usuário para preencher com números inteiros.  Nesta função você irá passar como parâmetro a 
linha que deseja somar, e retornar a soma dos números armazenados na linha.'''

def criaMatrizUser(n):
    matriz = []

    for i in range(4):
        linha = []

        for j in range(4):
            n = int(input(f"Digite o seu número "))
            linha.append(n)
        matriz.append(linha)
    for i in matriz:
        print(i)
    if n > 3:
        n = 3
    print(f"A soma matriz é {sum(matriz[n])}")

criaMatrizUser(2)