function somaDosPares(arrayEx){
    let somaPares = 0
    for(let i = 0; i < arrayEx.length; i++ ){
        if(arrayEx[i] % 2 == 0){
            somaPares += arrayEx[i]
        };
    };
    return somaPares;
};
const arrayFodona = [1, 2, 3, 4, 5, 6];
const resultado = somaDosPares(arrayFodona);
console.log(resultado);