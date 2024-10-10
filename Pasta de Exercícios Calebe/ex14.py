'''Suponha que você tenha duas matrizes A e B, ambas com tamanho 3x3. Faça um 
programa que calcule a soma das duas matrizes. (SEM USAR FUNÇÃO)
A = [[1, 13, 3],
     [4, 45, 67],
     [7, 80, 9]]

B = [[100, 8, 7]
     [6, 5, 4]
     [3, 25, 10]]

     
SOMA = [[101, 21, 10]
        [10, 50, 71]
        [10, 105, 19]]'''

a = [[1, 13, 3],[4, 45, 67],[7, 80, 9]]

b = [[100, 8, 7],[6, 5, 4],[3, 25, 10]]
lst = []

for f in range(len(a)):
     lhnsm = []

     for i in range(len(a[f])):
        soma = a[f][i] + b[f][i]
        lhnsm.append(soma)

     lst.append(lhnsm)
    
for i in lst:
    print(i)


