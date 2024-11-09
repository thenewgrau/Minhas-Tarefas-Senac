let x = new Date('1999-10-17');
let z = new Date('2024-10-1')
const nascidoAno = x.getFullYear();
const nascidoMes = x.getMonth()
const nascidoDia = x.getDate()
const atualAno = z.getFullYear();
const atualMes = z.getMonth();
const atualDia = z.getDate();
const idadeEmAnos = atualAno - nascidoAno
console.log(x)
console.log(z)

console.log(nascidoAno + ' ano que nasceu')
console.log(nascidoMes + 1 + ' mes que nasceu')
console.log(nascidoDia + 2 + ' dia que nasceu')
console.log(atualAno + ' ano atual')
console.log(atualMes + 1 + ' mes atual')
console.log(atualDia + 13 + ' dia atual')

if(atualMes > nascidoMes){
    console.log('Idade do sujeito: '+idadeEmAnos)

}else if(atualMes == nascidoMes){
    if(atualDia > nascidoDia){
        console.log('Idade do sujeito: '+idadeEmAnos)

    }else if(atualDia == nascidoDia){
        console.log('Feliz Aniversário')
    }else{
        console.log('Idade do sujeito: '+idadeEmAnos - 1)
    };
}else{
    console.log('Idade do sujeito: '+idadeEmAnos - 1)

};

