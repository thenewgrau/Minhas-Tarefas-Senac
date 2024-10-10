'''Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais 
elementos. Escreva ao final a matriz obtida. Saída:
[1, 0, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 0, 1, 0, 0]
[0, 0, 0, 1, 0]
[0, 0, 0, 0, 1]
'''
lista = []
for a in range(20):
    linha = []
    
    for i in range(20):
        
        if a == i:
            linha.append(1)

        else:
            linha.append(0)

    lista.append(linha)

for linhas in lista:
    print(linhas)

