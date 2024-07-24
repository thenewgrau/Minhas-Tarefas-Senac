from Ex03 import Ingresso
from Ex03 import Vip

if __name__ == '__main__':
    pessoa = Ingresso(20,'Leste')
    pessoa = Vip(20,'Leste','Proibido','Proibido','Proibido','Proibido','Proibido')
    pessoavip = Vip(50,'Norte','Liberada','Liberado','Liberado','Liberado','Liberado')

pessoa.mostrarInformacoes()
pessoa.mostrarSetor()
pessoa.setAlterarPreco()
print()
pessoavip.mostrarInformacoes()
pessoavip.mostrarSetor()
pessoavip.setAlterarPreco()