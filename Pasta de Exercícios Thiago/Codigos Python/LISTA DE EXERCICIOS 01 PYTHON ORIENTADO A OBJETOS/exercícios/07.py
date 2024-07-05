'''Crie uma função que efetue o cálculo do salário e
como retorno teremos o valor a ser pago conforme o
número de horas trabalhadas. Considere a carga
horária de 40h por semana como salário base, caso
ultrapasse o limite de 40h, o funcionário deve receber
50% a mais por hora excedente.
'''

def calcsalario(salario,horas):
    
    return salario and horas

salario = float(input("Digite seu salário por hora "))
hora = float(input("Digite quantas horas você trabalhou "))

res = salario * hora

if hora > 40:
    horasex = hora - 40
    horasex = horasex * 0.50
    res = salario * (hora + horasex)
    print(f"Seu salário foi de R${res:.2f}")
    
else:
    print(f"Seu salário foi de R${res:.2f}")