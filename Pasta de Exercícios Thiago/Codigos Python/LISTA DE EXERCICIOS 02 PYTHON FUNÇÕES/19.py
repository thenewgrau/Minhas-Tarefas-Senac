'''A partir do exercício anterior crie uma função que inicialize uma matriz de 4 x 4, e peça ao 
usuário para preencher com números inteiros.  Nesta função você irá passar como parâmetro a 
linha que deseja somar, e retornar a soma dos números armazenados na linha.'''

def criaMatriz(x,y):
    coluna = []
    for i in range(x):
        linha = []
        for i in range(y):
            linha.append(1)
        coluna.append(linha)
    for i in coluna:
        print(i)

print("Digite x")
x = int(input())
print("Digite y")
y = int(input())
criaMatriz(x,y)