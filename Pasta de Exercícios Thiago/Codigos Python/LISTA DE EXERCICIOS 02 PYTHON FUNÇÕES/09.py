'''Elabore uma função que receba dois valores numéricos e um símbolo. Este símbolo representara 
a operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma 
adição, se for − uma subtração, se for / uma divisão e se for ∗ será efetuada uma multiplicação. '''

def fun(raio,altura):
    v = (3.141592 * (raio**2) * altura)
    print(f"Volume : {v}")

print("Digite o valor do raio")
raio = float(input())
print("Digite o valor da altura")
altura = float(input())
fun(raio,altura)