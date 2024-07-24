from Ex05 import Pessoa
from Ex05 import Juridica
from Ex05 import Fisica

if __name__ == '__main__':
    fis = Pessoa('Heisenberg','+334 1223-2331','WalterWhite@gmail.com','Andiar Golves, 341')
    fis = Fisica('Heisenberg','+334 1223-2331','WalterWhite@gmail.com','Andiar Golves, 341','321.332.122-34')
    jur =  Pessoa('Jesse','+233 1233-4432','JessePinkMan@Hotmail.com','Amadeus Silva, 211')
    jur = Juridica('Jesse','+233 1233-4432','JessePinkMan@Hotmail.com','Amadeus Silva, 211','4331.3232-344')

jur.negociarJuridica()  
fis.negociarFisica()