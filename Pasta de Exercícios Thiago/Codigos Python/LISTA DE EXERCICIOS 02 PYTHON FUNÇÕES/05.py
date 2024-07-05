'''Crie uma função de um programa de teste para o cálculo do volume de uma esfera. Sendo que o 
raio é passado por parâmetro? '''

def det(n1,n2,n3):
    lst = [n1,n2,n3]
    print(f"Maior : {max(lst)}")

print("Digite o primeiro número")
n1 = int(input())
print("Digite o segundo número")
n2 = int(input())
print("Digite o terceiro número")
n3 = int(input())

det(n1,n2,n3)