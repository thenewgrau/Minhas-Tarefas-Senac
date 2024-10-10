'''Escreva um programa que recebe uma tupla de números inteiros e imprima a soma de todos os 
números pares da tupla.'''

tupla = (1,2,3,4,5,6,7,8,9,10)
soma = 0

for i in tupla:

    if i % 2 == 0:
        soma += i

    else:
        continue

print(soma)