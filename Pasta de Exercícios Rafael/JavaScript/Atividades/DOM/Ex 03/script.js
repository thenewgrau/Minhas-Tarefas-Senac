
confirmar.addEventListener('click',function(){
    const user = document.getElementById('usuario').value    
    const pass = document.getElementById('senha').value
    if(user != 'admin'){
        falar.innerHTML = 'ACESSO NEGADO! AUTO DESTRUIÇÃO EM 10 SEGUNDOS...'
    
    }else if(pass != 'senha'){
        falar.innerHTML = 'ACESSO NEGADO! AUTO DESTRUIÇÃO EM 10 SEGUNDOS...'
        
    }else{
        falar.innerHTML =  'Parabéns você fez Login !'
    };


});
