from time import sleep

class Pessoa:
    def __init__(self,nome,telefone,mail,end):
        self._nome = nome
        self._telefone = telefone
        self._email = mail
        self._endereco = end

class Fisica(Pessoa):
    def __init__(self, nome, telefone, mail, end, cpf):
        super().__init__(nome, telefone, mail, end)
        self._cpf = cpf

    def negociarFisica(self):
        sleep(1)
        print(f"É {self._nome}, senhor.")
        sleep(1)
        print("Legal, mas pra que preciso disso ?")
        sleep(1)
        print(f"Bl patrão vc que manda. \nNome: {self._nome}\nTelefone: {self._telefone}\nE-mail: {self._email}\nEndereço: {self._endereco}\nCPF: {self._cpf}")
        sleep(1)
        print("Nossa... Morri")

class Juridica(Pessoa):
    def __init__(self, nome, telefone, mail, end, cnpj):
        super().__init__(nome, telefone, mail, end)
        self._cnpj = cnpj
    
    def negociarJuridica(self):
        print(f"Olá me chamo {self._nome}")
        print("Pode-me dizer seu nome ?")
        sleep(2)
        print(f"Muito prazer ! Seja bem vindo a FromDev's, nosso CNPJ é esse ai: {self._cnpj} ")
        sleep(2)
        print("Ficou bobo guri ? Pra entrar na empresa... Vai me passa suas informações pessoais ai")
        sleep(2)
        print("Ótimo, muito bom. Agora você pode ir embora, não gostei da sua voz, não gostei da sua cara, não gostei da sua roupa, não gostei da sua existencia some a vaga vai ser de outro.")