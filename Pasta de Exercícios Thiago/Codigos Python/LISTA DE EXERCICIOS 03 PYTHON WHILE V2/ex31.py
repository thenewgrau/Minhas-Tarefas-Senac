
ano = 2019
anof = 2025
x = 4000

while ano < anof:
    
    if ano == 2019:
        
        print(f"Salário em {ano} foi de R${x:.2f}") 
        ano += 1
    
    elif ano == 2020:
        
        sal = x * 0.15
        sal = x + sal
        print(f"O salário em {ano} foi de {sal:.2f}")
        ano += 1
    
    elif ano > 2020:
        
        sal += sal
        sal = x * 0.30
        sal = sal + x
        (f"O salário do ano de {ano} é R${sal:.2f}")
        ano += 1
            
    