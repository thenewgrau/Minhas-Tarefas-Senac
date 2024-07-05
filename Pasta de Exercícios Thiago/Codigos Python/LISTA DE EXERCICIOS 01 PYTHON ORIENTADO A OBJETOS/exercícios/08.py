'''Um pescador, comprou um PC para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do MS (50 Kg) deve pagar
uma multa de R$ 4,00 por quilo excedente. O pescador precisa que
você crie uma função para ler a quantidade de peixes e calcular o
excesso. Gravar na variável excesso a quantidade de quilos além do
limite e na variável multa o valor da multa que o pescador deverá
pagar. Imprima os dados do programa com as mensagens adequadas.
'''

def controle(excesso, multa, peso, qnt):
    
    return excesso, multa, peso, qnt

print("Qual o peso de cada peixe ?")
peso = float(input())
print("Quantos peixes você pegou ?")
qnt = int(input())

excesso = peso * qnt

if excesso > 50:
    excesso = excesso - 50
    multa = excesso * 4.00
    print(f"Você excedeu {excesso} KG")
    print(f"Sua multa será de R${multa}")
    print(f"Limite aceitável do regulamento de pesca do MS : 50 KG")
    
else:
    print("Fique tranquilo dessa vez não passou do regulamento... tome cuidado... hehehe...")
    print(f"KG : {excesso}")