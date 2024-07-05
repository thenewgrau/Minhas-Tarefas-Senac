alunos = 1
numdoal = 1
soma = 0
cntnt = 1
qnt = 0
medt  = []
alunomaiorqst = 0

while alunos < 10:
    print(f"Aluno {numdoal} \nDigite a sua {cntnt} nota : ")
    nota = float(input())
    soma += nota
    qnt += 1
    cntnt += 1
    if qnt == 4:
        medt.append(soma/4)
        if soma/4 >= 7:
            alunomaiorqst = alunomaiorqst + 1
        
        alunos += 1
        numdoal += 1
        print(medt)
        cntnt = 1
        qnt = 0
        soma = 0

print("Alunos que estão com a média maior que 7 :",alunomaiorqst)
