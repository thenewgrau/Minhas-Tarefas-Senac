from time import sleep

class Funcionario:
    def __init__(self, nome, matricula, salario):
        self._nome = nome
        self._matricula = matricula
        self._salario = salario

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def baterMeta(self):
        print(f"Olá {self._nome}, bateu sua meta hoje?")
        pergunta = str(input())
        metas  = 0
        
        if pergunta == "sim":
            metas += 1
            print(f"Parabés {self._nome}, agora trabalhe mais escravo.")
            print(f"O seu salário de R${self._salario} vai abaixar também sinto muito")

        else:
            print("VAI BATER META AGORA!!!!!!!!!")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)
    
    def obterSenha(self):
        senha = 0000
        print("Fala a senha senhor gerente")
        senhaDigitar = int(input())
       
        if senhaDigitar != senha:
            print("TEMOS UM IMPOSTOR ATIVAR AUTO DESTRUICAO HACKER ")
            print('3')
            sleep(1)
            print('2')
            sleep(1)
            print('1')
            sleep(1)
            print("BOOOOM !!!")

        else:
            print("seja bem vindo senhor gerente hehe")
            print(f"Nome: {self._nome}\nMatricula: {self._matricula}\nSalario: R${self._salario}")
                
