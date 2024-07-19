class Pessoa:
    def __init__(self,nome,altura,peso,idade,feiura,monstruosidade):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.feiura = feiura
        self.monstruosidade = monstruosidade

    def nomedalenda(self):
        print(f"Nome: {self.nome}")

    def alturadalenda(self):
        print(f"Altura: {self.altura}") 

    def pesodalenda(self):
        print(f"Peso: {self.peso}")

    def idadedalenda(self):
        print(f"Idade: {self.idade}") 

    def feiuradalenda(self):
        print(f"Feiura: {self.feiura}") 

    def monstro(self):
        print(f"Monstruosidade: {self.monstruosidade}")

pessoa1 = Pessoa('Heisenberg',1.75,76.44,20,'Máxima','Máxima') 
pessoa2 = Pessoa('Christopher Araujo',2.75,93.44,23,'Média','Miníma') 
pessoa3 = Pessoa('Felipe Neto',1.98,86.24,40,'Minima','Média') 

print("Teste 1")
print("Nomes das lendas")
print("-"*90)
pessoa1.nomedalenda()
pessoa2.nomedalenda()
pessoa3.nomedalenda()

print("Altura das Lendas")
print("-"*90)

pessoa1.alturadalenda()
pessoa2.alturadalenda()
pessoa3.alturadalenda()

print("Peso dos monstros")
print("-"*90)

pessoa1.pesodalenda()
pessoa2.pesodalenda()
pessoa3.pesodalenda()

print("Idade das Lendas")
print("-"*90)

pessoa1.idadedalenda()
pessoa2.idadedalenda()
pessoa3.idadedalenda()

print("Nivel de Feiura")
print("-"*90)

pessoa1.feiuradalenda()
pessoa2.feiuradalenda()
pessoa3.feiuradalenda()

print("Nivel de monstruosidade")
print("-"*90)

pessoa1.monstro()
pessoa2.monstro()
pessoa3.monstro()

print("Teste 2")
pessoa1 = Pessoa('Heisenberg',1.89,76.44,54,'Minima','Minima') 
pessoa2 = Pessoa('Christopher Araujo',3.75,103.44,700,'Média','Média') 
pessoa3 = Pessoa('Felipe Neto',1.30,71.24,30,'Máxima','Máxima')

print("Nomes das lendas")
print("-"*90)
pessoa1.nomedalenda()
pessoa2.nomedalenda()
pessoa3.nomedalenda()

print("Altura das Lendas")
print("-"*90)

pessoa1.alturadalenda()
pessoa2.alturadalenda()
pessoa3.alturadalenda()

print("Peso dos monstros")
print("-"*90)

pessoa1.pesodalenda()
pessoa2.pesodalenda()
pessoa3.pesodalenda()

print("Idade das Lendas")
print("-"*90)

pessoa1.idadedalenda()
pessoa2.idadedalenda()
pessoa3.idadedalenda()

print("Nivel de Feiura")
print("-"*90)

pessoa1.feiuradalenda()
pessoa2.feiuradalenda()
pessoa3.feiuradalenda()

print("Nivel de monstruosidade")
print("-"*90)

pessoa1.monstro()
pessoa2.monstro()
pessoa3.monstro()