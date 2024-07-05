'''Escreva uma função que receba como parâmetro a quantidade de alunos para apresentar um 
trabalho. Esta função deve solicitar ao usuário os nomes de alunos de uma sala de aula. Após 
cadastrar a quantidade informada de alunos a função deve sortear e retornar para o usuário o 
aluno(a) que irá apresentar o trabalho primeiro.'''

from random import choice

def sorteiaAluno(n):
    cnt = 0
    lst = []
    while cnt < n:
        lst.append(input("Digite um nome: "))
        cnt += 1
        
    print(f"O primeiro aluno(a) a apresentar será: {choice(lst)}")


print("Digite a quantidade de nomes")
n = int(input())

sorteiaAluno(n)