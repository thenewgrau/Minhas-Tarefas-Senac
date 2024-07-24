from Ex04 import Passagem
from Ex04 import passagemAviao
from Ex04 import passagemOnibus
from time import sleep

if __name__ == '__main__':
    paso = Passagem(1350,10)
    pasv = Passagem(3543,230)
    paso = passagemOnibus(1350,10,'ABQ-1233', 'B-3')
    pasv = passagemAviao(3543,230,'PA-22','CHEKIN-233')

paso.mostrarPlaca()
paso.mostrarLeito()
paso.abastecer()

print()

pasv.mostrarPortao()
pasv.mostrarCheckin()
pasv.decolar()
