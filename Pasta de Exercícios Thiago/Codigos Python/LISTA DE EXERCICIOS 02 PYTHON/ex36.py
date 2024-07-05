sal = float(input("Digite o seu salário "))
temps = float(input("Quantos anos de serviço você possui ? "))
if sal <= 500 and temps == 1 :
    salf = sal * 0.25
    salf = salf + sal
    ##NÃO POSSUI BÔNUS
    print(f"O seu salário sofreu um reajuste e será de R${salf:.2f}")
elif sal > 500 and sal <= 1000 and temps > 1 and temps <= 3:
    salf = sal * 0.20
    salf = ((salf + sal) + 100) 
    ##100 de bônus.
    print(f"O seu salário sofreu reajuste e você passará a receber R${salf:.2f} ao invés de R${sal:.2f}")
elif sal > 1000 and sal <= 1500 and temps > 4 and temps <= 6:
    salf = sal * 0.15
    salf = ((salf + sal) + 200)
    ##bonus de 200
    print(f"O seu salário sofreu reajuste e você passará a receber R${salf:.2f} ao invés de R${sal:.2f}")
elif sal > 1500 and sal <= 2000 and temps > 6 and temps <= 10:
    salf = sal * 0.10
    salf = ((salf + sal) + 300)
    ##bonus de 300
    print(f"O seu salário sofreu reajuste e você passará a receber R${salf:.2f} ao invés de R${sal:.2f}")
elif sal > 2000 and temps > 10:
    salf = sal + 500
    ##bonus de 500
else:
    print(f"Você infelizmente não possui nenhuma das caracteristicas para sofrer um aumento de salário.")