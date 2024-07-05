'''Construa uma função que receba uma string como parâmetro e devolva outra string com os 
caracteres  embaralhados.  Por  exemplo:  se  função  receber  a  palavra python,  pode 
retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize 
em  sua  função  que  todos  os  caracteres  serão  devolvidos  em  caixa  alta  ou  caixa  baixa, 
independentemente de como foram digitados. '''

def carac(pala):
    print(pala[::-1])

print("Digite a palavra")
pala = str(input())

carac(pala)