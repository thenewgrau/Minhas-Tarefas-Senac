const lista1 = [1,2,3,4,5]
const lista2 = [5,6,7,8,9,10]
var listaFinal = []
for(i=0; i < lista1.length;i++){
    listaFinal.push(lista1[i])
}

for(j = 0; j < lista2.length; j++){
    listaFinal.push(lista2[j])
}

const listaFinalLendaria = [...new Set(listaFinal)]
console.log(listaFinalLendaria)
