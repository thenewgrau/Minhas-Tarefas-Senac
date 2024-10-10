'''Escreva um programa que recebe uma tupla de números inteiros e imprima o maior número 
da tupla. (SEM USAR FUNÇÃO)'''

tupla = (3, 6, 2, 9, 1, 7, 5)
maior = 0

for i in tupla:

    if i > maior:
        maior += 1
        maior = i        
    
    else:
        continue

print(maior)