'''Faça um programa que leia uma matriz 3x3, como a do exemplo abaixo, e em seguida, 
mostrar a posição onde se encontram o maior e o menor valor. (SEM USAR FUNÇÃO)
M = [[1, 120, -3], [4, 5, 250], [7, 0, 9]]'''

m = [[1, 120, -3],
     [4, 5,  250],
     [7, 0,    9]]

maior = 0
coluna_maior = 0
menor = 0
coluna_menor = 0
linha_maior = 0
linha_menor = 0

for i in m:
    linha = []

    for a in i:
        linha.append(a)

        if a > maior:
            maior = a
            linha_maior = m.index(i)
            coluna_maior = linha.index(a)

        else:
            if a < menor:
                menor = a
                linha_menor = m.index(i)
                coluna_menor = linha.index(a)
                

print(f"Maior : {maior}")
print(f"Coluna Maior : {coluna_maior}")
print(f"Linha Maior : {linha_maior}")
print("-"*90)
print(f"Menor : {menor}") 
print(f"Coluna Menor : {coluna_menor}")
print(f"Linha Menor : {linha_menor}")