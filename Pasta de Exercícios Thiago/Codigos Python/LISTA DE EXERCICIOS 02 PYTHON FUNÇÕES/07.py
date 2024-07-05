'''Crie uma função de um programa de teste para o cálculo do volume de uma esfera. Sendo que o 
raio é passado por parâmetro?'''

def fun(raio):
    v = ((4/3) * 3.14 * ((raio**3)))
    print(f"V = {v}")

print("Digite o valor do raio")
raio = int(input())
fun(raio)