'''Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos 
e segundos, e os converta em segundos.'''

def tempo(hr,min,seg):
    hr = hr * 3600
    min = min * 60
    seg = seg + hr + min
    print(f"Tempo : {seg} segundos")


print("Digite as horas")
hr = int(input())
print("Digite os minutos")
min = int(input())
print("Digite os segundos")
seg = int(input())

tempo(hr,min,seg)