from Ex06 import Funcionario
from Ex06 import Vendedor
from Ex06 import Gerente

if __name__ == '__main__':
    ger =  Funcionario('Willy Wonka',3231,10000)
    fun = Funcionario('Walter White',23123,999)
    ger = Gerente('Willy Wonka',3231,10000)
    fun = Vendedor('Walter White', 23123,999)

fun.baterMeta()
ger.obterSenha()