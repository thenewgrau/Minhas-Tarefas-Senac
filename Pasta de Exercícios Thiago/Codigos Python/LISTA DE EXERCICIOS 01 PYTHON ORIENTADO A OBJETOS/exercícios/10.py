'''Uma pessoa está interessada em comprar um carro e deseja fazer um
financiamento. Ela tem uma quantia X para dar de entrada, uma taxa de juros é
definida pelo banco e a pessoa pode escolher o número de parcelas que deseja
financiar.
Crie uma função que simule um financiamento, levando em consideração o regime de
juros compostos. O programa deve solicitar ao usuário o valor do veiculo, o valor da
entrada, a taxa de juros e a quantidade de parcelas. Além disso, o programa deve
exibir o valor total pago, a quantia dos juros pagos e o valor de cada parcela. O
programa deve apresentar as informações de forma clara e objetiva, facilitando a
compreensão por parte do usuário.'''

def financiamento(x,juros,parcelas,valorveiculo):
    valorveiculo = valorveiculo - x
    juros = juros / 100
    valorveiculo = valorveiculo / parcelas
   
    
    print(f"Valor do veículo: R${vl:.2f}")
    print(f"% de Juros {jr} %")
    print(f"Quantidade de parcelas {qp}")
    print(f"Entrada: R$ {x:.2f}")
    print(f"Preço de cada parcela: R$ {valorveiculo:.2f}")




print("Digite o valor do veículo")
vl = float(input())
print("Digite os a % de juros")
jr = float(input())
print("Digite a quantidade de parcelas")
qp = int(input())
print("Digite a entrada")
ent = float(input())
financiamento(ent,jr,qp,vl)

