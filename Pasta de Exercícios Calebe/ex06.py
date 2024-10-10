'''Considere uma lista de tuplas em que cada tupla representa informações sobre um 
aluno, contendo o nome e a nota de uma disciplina. Escreva um programa que recebe 
essa lista e imprima o nome do aluno que obteve a maior nota.

alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]'''

alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]
nota = 0
nome = 0

for tupla in alunos:

    if tupla[1] > nota:
        nota = tupla[1]
        nome = tupla

print(nome[0])

