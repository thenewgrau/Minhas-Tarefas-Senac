const form = document.getElementById('form')
const username = document.getElementById('username')
const email = document.getElementById('email')
const password = document.getElementById('password')
const password2= document.getElementById('password2')

function ShowError(input, message){
    const formControl = input.parentElement;
    formControl.classname = 'form-control error'
    const small = formControl.querySelector("small")
    small.innerHTML = message
    console.log(small)
}


function checkRequired(listaInput){
    listaInput.forEach(function (input){
        if(input.value == ""){
            ShowError(input, "Campo Obrigatório")
        }
    })
}


form.addEventListener('submit', function(e){
    e.preventDefault()
    checkRequired([username,email,password,password2])

})