'''Crie uma função para calcular a
exponenciação, que necessite dois argumentos
e apresente como resultado a potência. Sendo
base elevado ao expoente.
s'''

def exp(base,expoente):
    exponenciacao = base**expoente
    return exponenciacao

base = int(input("Digite a base "))
expoente = int(input("Digite o expoente "))

res = exp(base,expoente)

print(res)
