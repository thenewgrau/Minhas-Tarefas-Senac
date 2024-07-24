from Ex01 import Filme
from Ex01 import Acao
from Ex01 import Drama
from Ex01 import Suspense

if __name__ == "__main__":
    filmeAcao = Acao('Anjos da Noite','120')
    filmeDrama = Drama('Titanic','150')
    filmeSuspense =  Suspense('Long Legs','60')
    
filmeAcao.Play()    
filmeAcao.acaoMaster()
print()
filmeDrama.Play()
filmeDrama.Dramaturgo()
print()
filmeSuspense.Play()
filmeSuspense.Sus()