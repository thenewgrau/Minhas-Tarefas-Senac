'''Faça um algoritmo que calcule a matriz transposta de M, ou seja, o que é linha vira 
coluna. Ao final exiba a transposta. 
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = []
coluna = 0

while len(lst) <= 2:
    nvlst = []
    
    for i in m:
        nvlst.append(i[coluna])

    lst.append(nvlst)
    coluna += 1

for linha in lst:
    print(linha)