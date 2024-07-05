'''Um comerciante possui uma loja de artigos de R$ 1,99. Para
agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu
uma tabela que contém o número de itens que o cliente comprou e ao
lado o valor da conta. Desta forma a atendente do caixa precisa apenas
contar quantos itens o cliente está levando e olhar na tabela de preços.
Você foi contratado para desenvolver uma função que monta esta
tabela de preços, que conterá os preços de 1 até 50 produtos,
conforme o exemplo abaixo:
'''

def tabela(preco,qnt):
    
    return preco and qnt

while True:
    preco = 1.99
    qnt = int(input("quantos produtos você quer ? "))
    
    if qnt >= 50:
        print("Valores acima de 50 são extritamente proibidos. e voce sera preso.")

    else:
        print("Lojas Quase Dois - Tabela de preços")
        
        for i in range(qnt):
            print(i+1, f"- R$ {preco:.2f}")
            preco += 1.99
    