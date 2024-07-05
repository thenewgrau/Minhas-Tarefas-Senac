'''Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra 
for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a 
média ponderada, com pesos 5, 3 e 2. '''

def temp(graus):
    f = (graus * ((9.0/5.0)) + 32)
    print(f"Temperatura em Fahrenhit: {f} F")
         
print("Digite a temperatura")
graus = float(input())
temp(graus)