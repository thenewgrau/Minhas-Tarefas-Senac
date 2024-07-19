class Nf:
    def __init__(self,num,tipo,serie,cnpj,razao,data,valorproduto,icms,frete,ipi,valortotal):
        self.numero = num
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razaosocial = razao
        self.data = data
        self.valorproduto = valorproduto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valortotal = valortotal

    def obterNumero(self):
        print("Digite o número")
        num = int(input())
        self.numero = num

    def obterDataEmissao(self):
        print("Digite a data")
        data = str(input())
        self.data = data

    def setalterarRazaoSocial(self):
        print(f"Atual: {self.razaosocial}")
        print(f"Digite a nova Razão Social: ")
        razaosocialfoda = str(input())
        self.razaosocial = razaosocialfoda
        print(f"Nova: {self.razaosocial}")

    def calcularValorTotal(self):
        impostos = self.icms + self.ipi
        valortotals = (self.valorproduto + self.frete)
        self.valortotal =  valortotals * impostos
        self.valortotal = self.valortotal + valortotals
        print(f"Valor total: {self.valortotal}")

    def notinhaFiscal(self):
        print('Número:',self.numero)
        print(f'Tipo: {self.tipo}')
        print(f"Série: {self.serie}")
        print(f"CNPJ: {self.cnpj}")
        print(f"Razão Social: {self.razaosocial}")
        print(f"Data: {self.data}")
        print(f"Valor do produto: R${self.valorproduto}")
        print(f"ICMS: {self.icms}")
        print(f"Frete: {self.frete}")
        print(f"IPI: {self.ipi}")
        print(f"Valortotal: {self.valortotal}")