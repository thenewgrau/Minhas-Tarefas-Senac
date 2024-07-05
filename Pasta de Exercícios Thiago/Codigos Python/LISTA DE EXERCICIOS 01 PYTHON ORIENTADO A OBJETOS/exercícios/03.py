# Crie uma função que imprima a quantidade de dígitos de um determinado número inteiro informado.

def fun(qnt):
    qnt = str(qnt)
    dgt = len(qnt)
   
    return dgt
    
qnt = int(input("Digite o número "))

fim = fun(qnt)
print(f"O seu número possui {fim} digitos.")