'''  Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721'''

def rev(num):
   num = str(num)
   print(num[::-1])
    
    
print("Digite o número")
num = int(input())
rev(num)