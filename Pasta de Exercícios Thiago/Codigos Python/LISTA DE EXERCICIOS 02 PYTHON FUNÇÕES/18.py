'''Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a 
saída para n = 6 seria'''

def caracoles(n,ast='*'):
    
    for i in range(1,1+n):
        print(' '*(n-i),ast*i, end='')
        print(ast*(i-1), end='')
        print()
        
    


print("Digite n")
n = int(input())
caracoles(n)