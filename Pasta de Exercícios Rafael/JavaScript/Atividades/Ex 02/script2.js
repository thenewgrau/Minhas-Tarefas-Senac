const lista1 = [1,2,3,4,5]
const lista2 = [5,6,7,8,9,10]
var listaFinal = lista1.concat(lista2)
var listaFinalLendaria = listaFinal.filter((n)=>{
    if(lista1.indexOf(n) != -1 && lista2.indexOf(n) != -1){
        return false;
    }else{
        return true;
    }
})
console.log(listaFinalLendaria)
