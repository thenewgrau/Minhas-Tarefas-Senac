def fun(**kwargs: float):
    totalst = kwargs['valor'] 
    taxa = kwargs['valor'] * kwargs['taxa']
    dia = kwargs['valor'] * kwargs['quarta']
    total = taxa + dia + totalst
    print(f"Conta S/ Taxas : R${totalst:.2f} \nContas C/ Taxas: \nRodízo: R${totalst:.2f} \nTaxa Serviço: R${taxa:.2f} \nCouvert: {kwargs['couvert']} \nTOTAL R$: {total:.2f}")
    

res = fun(valor=350.99,quarta=0.15,taxa=0.10,couvert=15)
print(res)

