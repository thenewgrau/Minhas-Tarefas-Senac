'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() 
e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda 
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

def sorteio(n):
    numeros = []

    for i in range(n):
        numeros.append(randint(0,100))
    return numeros

def somaPar(x):
    soma = 0

    for i in x:

        if i % 2 ==0:
            soma += i

    return soma


af = sorteio(5)
print(somaPar(af))
