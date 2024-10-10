'''Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na 
diagonal principal. (SEM USAR FUNÇÃO)
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0 

for i in range(len(m)):
    for a in range(len(m[i])):
        if i == a:
            soma += m[i][a]

print(soma)