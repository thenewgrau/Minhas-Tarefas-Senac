from Produto import Produto
from Cliente import Cliente

p1 = Produto("Omo","Delicioso",14.99,55)
p1.getNome()
p1.getEstoque()
p1.getDesc()
p1.getPreco()

print("-"*90)

cli = Cliente("Rodrigo Faro",63)
cli.getNome()
cli.getIdade()
