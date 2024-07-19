class Cachorro:
    def __init__(self,nome,cor,peso,niveldefofura):
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.niveldefofura = niveldefofura

    def latir(self):
        print(f"{self.nome} latiu !")

    def dormir(self):
        print(f"{self.nome} dormiu...")

    def coloracao(self):
        print(f"{self.nome} era  {self.cor}")

    def pes(self):
        print(f"{self.nome} pesava {self.peso} KG")

    def fof(self):
        print(f"A fofura de {self.nome} estava no nivel {self.niveldefofura}")    

cachorro1 = Cachorro('Snoopy','Preto',7.65,2)
cachorro2 = Cachorro('Filó','Branca',5.34,1)
cachorro3 = Cachorro('Xodó','Marrom',4.1,3)


print("-"*90)
cachorro1.latir()
cachorro2.latir()
cachorro3.latir()

print("-"*90)
cachorro1.dormir()
cachorro2.dormir()
cachorro3.dormir()

print("-"*90)
cachorro1.coloracao()
cachorro2.coloracao()
cachorro3.coloracao()

print("-"*90)
cachorro1.pes()
cachorro2.pes()
cachorro3.pes()

print("-"*90)
cachorro1.fof()
cachorro2.fof()
cachorro3.fof()

print("-"*90)
print("Te amo",cachorro1.nome)
print("Te amo",cachorro2.nome)
print("Te amo",cachorro3.nome)