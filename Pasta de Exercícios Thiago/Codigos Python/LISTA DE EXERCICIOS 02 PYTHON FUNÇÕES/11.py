'''Elabore uma função que receba por parâmetro dois valores X e Z. Calcule e retorne o 
resultado de XZ para o programa principal. Atenção não utilize nenhuma função pronta de 
exponenciação. 
'''

def fun(x,y):
    cnt = 0
    while cnt < y:
        res = x * x
        cnt += 1
    
    print(res)

print("Digite a base")
x = int(input())
print("Digite a exponenciação")
y = int(input())

fun(x,y)