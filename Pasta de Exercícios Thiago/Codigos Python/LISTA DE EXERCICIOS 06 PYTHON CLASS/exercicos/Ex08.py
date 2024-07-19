class alunoAcademia:
    def __init__(self,nome,idade,peso,altura,mensalidade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcularIMC(self):
        imc = ((self.altura**2) / self.peso)
        print(f"seu IMC é: {imc}")
        if imc < 18.5:
            print("Magro ein pai")

        elif imc > 18.5 and imc < 24.9:
            print("Ta Blz, ta joia, ta normal")

        elif imc > 24.9 and imc < 29.9:
            print("Tá no sobrepeso ein")

        elif imc > 29.90 and imc < 39.9:
            print("Opa Obesidade isso ai")
        
        elif imc > 39:
            print("Ta grave a situação ai viu")

    def obtervalorMensalidade(self):
        if self.idade < 18:
            print("Vai ter que pagar R$90.00")
        
        else:
            print("R$120.00 ainda, se lascou")