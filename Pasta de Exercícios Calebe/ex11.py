'''Dada uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do 
maior valor. (SEM USAR FUNÇÃO)
matriz = [[1, 2, 11, 13], [4, 15, 16, 60], [7, 8, 19, 200], [20, 100, 5, 3]]'''

m = [[-3]]
maior = 0

for i in m:

    for a in i:
        
        if a > maior:
            maior += 1
            maior = a

        else:
            continue

print(maior)