<?php

$listaFODA = [1,2,3,4,5,6,7,8,9,10];
$soma = 0;
 
for($i=0; $i < count($listaFODA); $i++){
    if($listaFODA[$i] % 2 != 0){
      
    }else{
        $soma += $listaFODA[$i];
        
    };
};

echo $soma;



?>