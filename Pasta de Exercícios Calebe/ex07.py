'''Faça um algoritmo que efetue a soma dos valores de uma matriz 3x3 e exiba o 
resultado da soma. R=45
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
soma = 0
 
for linha in matriz:
    for i in linha:
        soma += i
 
print(soma)