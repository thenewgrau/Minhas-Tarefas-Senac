''' Escreva um programa que recebe uma tupla de números inteiros e imprima apenas os 
números pares. '''

tupla = (1,2,3,4,5,76,7,23,34,45,234)

for i in tupla:

    if i % 2 == 0:
        print(i)

    else:
        continue