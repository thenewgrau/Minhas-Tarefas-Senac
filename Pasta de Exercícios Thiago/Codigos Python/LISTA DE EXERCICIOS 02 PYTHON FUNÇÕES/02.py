'''Faça uma função que receba a data atual (dia, mês e ano) e exiba-a na tela no formato textual 
por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000. '''

def data(dia,mes,ano): 
    meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    mes = meses[mes-1]
    if dia < 10:
        dia = str(dia)
        print(len(dia[0]),"de",mes,"de",ano)
    else:
        print(dia,"de",mes,"de",ano)
        
print("Digite o dia")
diad = int(input())
print("O mês")
mesd = int(input())
print("Ano")
anod = int(input())

data(diad,mesd,anod)