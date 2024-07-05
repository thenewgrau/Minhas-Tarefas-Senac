vendap = int(input('Quantos pãeszinho você vendeu hoje ? '))
vendap = vendap * 0.12
vendab = int(input('Quantas broas você vendeu hoje ? '))
vendab =  vendab * 1.50

vendat1 = vendap + vendab
vendat = round(vendat1 * 0.10,2)

print(f'Você arrecadou {vendap} reais em pãeszinhos')
print(f'Você arrecadou {vendab} reais broas')
print(f'Na soma dos pãeszinhos e broas é : {vendat1}')
print(f"O total que você deve colocar a poupança é : {vendat} ")

