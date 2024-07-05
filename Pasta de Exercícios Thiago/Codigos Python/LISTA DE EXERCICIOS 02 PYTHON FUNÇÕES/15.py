'''Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com 
pontos de exclamação, conforme o exemplo abaixo (para n = 5)'''

def qnt(n):
    for i in range(1,1+n):
        print("!"*i)

print("Digite a quantidade de '!'")
n = int(input())
qnt(n)