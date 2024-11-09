const cont = document.getElementById("contagem")
const falar = document.getElementById('falatorio')
const body = document.getElementsByClassName("body")

contador = 1
botao.addEventListener('click',function(){
    falar.innerHTML = `${contador}`
    contador ++
});