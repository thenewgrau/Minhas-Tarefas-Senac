const botao = document.getElementById("botaors")
const body = document.getElementsByClassName("body")
botao.addEventListener('click',function(){
    console.log('ola mundo !')
    body[0].innerHTML += "<div> <p> Olá Mundo ! </p> </div>"

});
