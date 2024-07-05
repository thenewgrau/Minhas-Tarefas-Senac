'''Elabore uma função chamada desenhaLinha(). Ele deve desenhar uma linha na tela usando 
vários símbolos de igual (Ex: ========). A função recebe por parâmetro quantos sinais de igual 
serão mostrados. '''

def desenhaLinha(qnt):
    print("="*qnt)

print("Quantas vezes '=' deve ser printado ?")
qnt = int(input())

desenhaLinha(qnt)