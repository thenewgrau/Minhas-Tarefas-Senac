'''Escreva um programa que recebe uma tupla de números inteiros e imprima apenas os 
números maiores do que 5.'''

tupla = (1,2,3,4,5,6,7,8,20,30,40)

for i in tupla:
    
    if i < 5:
        continue
    
    else:
        print(i)