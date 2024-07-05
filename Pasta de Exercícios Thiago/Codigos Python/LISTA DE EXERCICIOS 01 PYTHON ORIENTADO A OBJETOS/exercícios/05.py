'''Escreva um programa com uma função chamada
somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item
antes do imposto. A função “altera” o valor de custo para
incluir o imposto sobre vendas. Por fim deve retornar o novo
valor para o usuário considerando o percentual do imposto'''

def somaImposto(taxaImposto, custo):
    taxa = (custo * (taxaImposto/100))
    taxa = taxa + custo
    return taxa 

print("Digite o custo")
custo = float(input())
print("Agora a % de taxa")
taxaImposto = float(input())

valorf = somaImposto(taxaImposto,custo)
print(f"Valor final : {valorf:.2f}")
