

lista_de_produtos = [] # LISTA TOTAL DE ITENS 
codigo = 0 # O CODIGO FAZ A CONTAGEM DE QUANTOS CODIGOS EXISTEM NA LISTAGEM DE CODIGOS
codigot = [] # CODIGOS TOTAIS CRIADOS
terminar = 1 # FINALIZAR O PROGRAMA COM 0
qntt = [] # QUANTIDADE TOTAL DE ITENS
precof = [] # PREÇO TOTAL DOS ITENS 

while terminar == 1:# CRIA UM LOOP ENQUANTO TERMINAR FOR IGUAL A UM.
    print("_"*90)
    print("Digite:(0), (1), (2), (3), (4), (5) ou (6) \n(0) Para Encerrar o programa  \n(1) Para visualizar todos os produto e seus códigos \n(2) Para Adicionar um produto \n(3) Para Retirar um produto \n(4) Ver um item especifico do estoque \n(5) Atualizar preço de produto \n(6) Atualizar Quantidade de produto ")
    escolher = int(input())# O PROGRAMA PEDE PARA O USUARIO FORNECER UM INPUT DE 0 A 6 E ASSIM PROCESSEDE DEPOIS DA INFORMAÇÃO
    print("_"*90)
    if escolher == 0:# SE O USUARIO COLOCAR 0 NO INPUT. O PROGRAMA É ENCERRADO 
        
        terminar = 0 # ISSO FAZ QUE O PROGRAMA TERMINE POR QUE O WHILE ESTÁ RODANDO EM LOOP NO TERMINAR, QUANDO É IGUAL A 0 O PROGRAMA RECONHECE QUE TERMINAR NÃO É MAIS IGUAL A 1 E ASSIM ENCERRA POR SER 0. 
        print("_"*90)
        print("Encerrado.")# O PROGRAMA CONFIRMA QUE O PROGRAMA FOI ENCERRADO.
        print("_"*90)
    
    else: # CASO O ESCOLHER NÃO FOR IGUAL A ZERO O PROGRAMA NÃO TERMINA E CONTINUA OPERANDO NORMALMENTE.
        
        if escolher == 1:# O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 1
            
            if len(lista_de_produtos) == 0:# SE A QUANTIDADE DE LEN DA LISTA_DE_PRODUTOS FOR IGUAL A ZERO. O PROGRAMA PRINTA A MENSAGEM, POR CONTA QUE NÃO HÁ NENHUM PRODUTO CADRASTADO NO PROGRAMA AINDA.
            
                print("Não há produtos no estoque ainda !")# O PROGRAMA INFORMA QUE NÃO HÁ PRODUTO AINDA NO ESTOQUE
            
            else:# CASO TENHA PRODUTO O PROGRAMA CONTINUA OPERANDO NORMALMENTE
                
                i = 0 # ATRIBUI O VALOR 0 PARA A VARIAVEL I
                
                while i < len(lista_de_produtos):#O PROGRAMA EMPRIME A MENSAGEM DE CODIGOS ATÉ QUE I FOR IGUAL A LEN DE LISTA DE PRODUTOS
                
                    print("_"*90)# REALIZA UMA "ORGANIZAÇÃO" PARA MELHOR VISUALIZAÇÃO DOS PRODUTOS
                    print("                 QUANTIDADE DE PRODUTOS")
                    print(f"Código : {codigot[i]}, Nome do produto {lista_de_produtos[i]}")# FAZ O PRINT DA LISTAGEM DE CODIGOS DISPONIVEIS E A LISTAGEM DE PRODUTOS DISPONIVEIS
                    print("_"*90)
                    i += 1
    
        elif escolher == 2:# O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 2

            print("Qual o nome do produto você quer adicionar ?")# O PROGRAMA IMPRIME A PERGUNTA
            nmdoprdt = str(input() )# NMDOPRDT SIGNIFICA NOME DO PRODUTO UMA VARIAVEL PARA SER ADICIONADA EM LISTA DE PRODUTOS E O PROGRAMA RECEBE A INFORMAÇÃO DADA PELO INPUT DO USUARIO E SALVA NA VARIAVEL
            
            if nmdoprdt in lista_de_produtos:# O PROGRAMA VERIFICA SE JÁ EXISTE UM NOME 
                
                print("Já existe um produto cadastrado com esse nome! \nCaso queira colocar ou retirar a quantidade do produto vá em (4)")# O PROGRAMA AVISA QUE JÁ EXISTE UM NOME 
                print("_"*90)
            
            else:#CASO NÃO HAJA O PROGRAMA CONTINUA PERGUNTANDO AS SEGUINTES INFORMAÇÕES:
                
                codigo = codigo + 1# O CODIGO RECEBE MAIS UM PARA CONTINUAR A CONTAÇÃO DE PRODUTOS DE DIFERENTES CODIGOS PARA QUE NÃO HAJA CODIGOS IGUAIS
                codigot.append(codigo)# A VARIAVEL CODIGO É ADICIONADA NA LISTAGEM DE CODIGOS.
                lista_de_produtos.append(nmdoprdt)# A VARIAVEL NMDOPRDT(NOMEDOPRODUTO) É ADICONADA NA LISTAGEM DE LISTA_DE_PRODUTOS
                print(f"O código do seu produto é {codigo}")# ELE INFORMA O CÓDIGO DO PRODUTO. E SEMPRE SOMA +1 DEPOIS 
                preco = float(input("Informe o preço do seu produto : "))# ELE PEDE PARA INFORMAR O PREÇO DO PRODUTO
                qnt = int(input("Qual a quantidade disponivel do produto : "))# ELE PEDE A QUANTIDADE DO PRODUTO
                precof.append(preco) # A LISTA DE PREÇOS RECEBE O PREÇO QUE O USUARIO FORNECEU
                qntt.append(qnt)# A LISTA DE QUANTIDADE RECEBE A QUANTIDADE QUE O USUARIO FORNECEU
                print("Confirmado !")# O PROGRAMA INFORMA QUE AS INFORMAÇÕES FORAM RECEBIDAS
                print("_"*90)
        
        elif escolher == 3:# O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 3
            
            print("Digite o código que você deseja remover ")# O PROGRAMA PEDE PARA O USUARIO INFORMAR O CODIGO DO PRODUTO PARA SER RETIRADO DA LISTA
            codigorem = int(input())# O PROGRAMA RECEBE O CODIGO
            codigot.remove(codigorem)# O PROGRAMA TIRA O CODIGO RECEBIDO DA LISTA
            codigo = codigo
            print("Digite o nome do produto que você deseja remover ")# O PROGRAMA PEDE PARA O USUARIO FORNECER O NOME DESSE CODIGO
            listarem = str(input(""))# O PROGRAMA RECEBE O NOME
            
            if listarem in lista_de_produtos:

                lista_de_produtos.remove(listarem)# O PROGRAMA TIRA O NOME DA LISTA
                print("Item removido com sucesso !")# O PROGRAMA INFORMA QUE AS INFORMAÇÕES FORAM CONCLUIDAS
                print("_"*90)
            
            else:
               
                print("Esse nome não está cadastrado no sistema ! tente novamente")
                print("_"*90)

        elif escolher == 4:# O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 4
            
            print("Digite o código do seu produto ")# O PROGRAMA PEDE PARA O USUARIO FORNECER O CODIGO DO PRODUTO
            omaga = int(input())# O PROGRAMA RECEBE O CODIGO
           
            if omaga in codigot:# O PROGRAMA VERIFICA SE ESSE CODIGO EXISTE NA LISTAGEM

                print(f"Codigo do produto : {omaga}")# O PROGRAMA INFORMA NOVAMENTE O CODIGO DO PRODUTO
                omaga = (omaga - 1) # RETIRA UM POR CAUSA QUE QUANDO UMA LISTA É LIDA PELO COMPUTADOR ELA COMEÇA DO 0 QUANDO SE COMEÇA DO -1 O PRODUTO QUE SE ENCONTRA EM 0 PODE SER LIDO CORRETAMENTE
                print(f"Nome do produto : {lista_de_produtos[omaga]}")# --------------------------------------
                print(f"Preço do produto : R${precof[omaga]}")# O PROGRAMA FALA AS CARACTERISTICAS DO CODIGO.
                print(f"Quantidade em estoque2 : {qntt[omaga]}")# -------------------------------------------
                print("_"*90)# PARA MELHOR ORGANIZAÇÃO DO CODIGO
            else:
                print("Esse código não esta cadastrado no sistema ! tente novamente.")
                print("_"*90)
        elif escolher == 5: # O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 5
            
            print("Qual o código do produto ?")# O PROGRAMA PERGUNTA QUAL É O CODIGO DO PRODUTO
            omaga = int(input())# O USUÁRIO INFORMA O CODIGO DO PRODUTO
            
            if omaga in codigot:# O PROGRAMA VERIFICA SE EXISTE ESSE CODIGO DENTRO DA LISTAGEM DE CODIGOS EXISTENTES
                
                omaga = omaga -1# A VARIAVEL "OMAGA" É SUBTRAIDA POR CONTA QUE EM LISTAS O PROGRAMA COMEÇA EM 0, QUANDO COMEÇADO EM -1 O PROGRAMA CONSEGUE LER 0 ASSIM ATRIBUINDO CORRETAMENTE O CODIGO PARA CADA PRODUTO
                print("Qual sera o preço atual ?")# O PROGRAMA PERGUNTA QUAL O PREÇO ATUAL DO PRODUTO
                adcprc = float(input())# O USUÁRIO INFORMA O PREÇO NOVO
                
                if adcprc < 0:# O PROGRAMA VERIFICA SE O VALOR INFORMADO PELO USUARIO É MENOR QUE 0
                    
                    print("Valores abaixo de 0 não são permitidos !")# AVISA QUE NÃO SÃO PERMITIDOS VALORES ABAIXO DE 0, POR CAUSA QUE NÃO DÁ PRA TER ESTOQUE NEGATIVO NÉ, DUR..
                    print("_"*90)

                else:# CONTINUA COM O PROGRAMA NORMALMENTE
                    precof.remove(precof[omaga])# O PROGRAMA RETIRA DA LISTA PRECOF( PRECO_FINAL ), NO LOCAL DE OMAGA ()
                    precof.append(adcprc)# O PROGRAMA ADICIONA O NOVO PREÇO FORNECIDO PELO USUARIO PELA VARIAVEL ADCPRC ( ADICIONAR_PRECO )
                    print(f"Preço atual : R${adcprc}")# O PROGRAMA INFORMA A QUANTIDADE ATUAL DO PRODUTO NO ESTOQUE
            
            else:# CASO O CODIGO FORNECIDO PELO USUARIO PELA VARIAVEL OMAGA NÃO ESTIVER NA LISTA DE CODIGOS O PROGRAMA ENVIA UMA MENSAGEM
            
                print("O produto ainda não está cadastrado no sistema !")# MENSAGEM QUE O PROGRAMA ENVIA CASO NÃO EXISTA O CODIGO FORNECIDO PELO USUARIO NA LISTA DE CODIGOS EXISTENTES
                print("_"*90)

        elif escolher == 6:# O PROGRAMA CONTINUA QUANDO O USUARIO FORNECE O INPUT 6
            
            print("Qual o código do produto ?")# O PROGRAMA PERGUNTA QUAL O CODIGO
            omaga = int(input())# O USUARIO FORNECE O CODIGO
            
            if omaga in codigot:# O PROGRAMA VERIFICA SE O CODIGO ESTÁ NA LISTAGEM DE CODIGOS
                
                omaga = omaga - 1# A VARIAVEL "OMAGA" É SUBTRAIDA POR CONTA QUE EM LISTAS O PROGRAMA COMEÇA EM 0, QUANDO COMEÇADO EM -1 O PROGRAMA CONSEGUE LER 0 ASSIM ATRIBUINDO CORRETAMENTE O CODIGO PARA CADA PRODUTO
                print("Qual será a quantidade atual do produto ?")# O PROGRAMA PERGUNTA QUAL A QUANTIDADE ATUAL DE ESTOQUE
                adcqnt = int(input())# O USUARIO FORNECE A QUANTIDADE ATUAL DE ESTOQUE
                qntt.remove(qntt[omaga])# O PROGRAMA REMOVE A QUANTIDADE ANTIGA DE ESTOQUE
                qntt.append(adcqnt)# E LOGO EM SEGUIDA ADICIONA A QUANTIDADE FORNECIDA ATUALMENTE PELO USUARIO
                print(f"A quantidade atual do produto é {adcqnt}")# O PROGRAMA INFORMA QUE A QUANTIDADE DO PRODUTO ATUAL É A QUE ELE INSERIU CONFIRMANDO OS DADOS DELE

            else:# E POR FIM SE CASO O CODIGO OFERECIDO PELO USUARIO NÃO ESTIVER DENTRO DA LISTAGEM DE CODIGOS O PROGRAMA ENVIA A MENSAGEM
            
                print("O produto ainda não está cadastrado no sistema !")# MENSAGEM ENVIADA PELO PROGRAMA
                print("_"*90)

                #FIM!!!! EBA