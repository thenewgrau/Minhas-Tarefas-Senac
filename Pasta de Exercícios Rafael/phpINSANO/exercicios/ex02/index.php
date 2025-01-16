<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Noto+Sans+KR:wght@100..900&family=Quicksand:wght@300..700&family=Roboto+Slab:wght@100..900&display=swap" rel="stylesheet">
</head>
<body>
    
</body>
</html>

<?php
function calculadora($opcao,$num1,$num2){
    if($opcao == 1){
        $val = $num1 + $num2; 
        $soma = "<div id='agua'>
            <h1>
                Parabéns você está na soma 
            </h1>
            <p>
                {$num1} + {$num2} = {$val}
            </p>
        </div>" ;
        echo $soma;
        
    }else if($opcao == 2){
        $val = $num1 - $num2;
        $subtracao = "<div id='agua'>
        <h1>
            Parabéns você está na subtração, observe que o primeiro número sempre subtrairá o segundo e não o inverso.
        </h1>
        <p>
            {$num1} - {$num2} = {$val}
        </p>
    </div>" ;
        echo $subtracao;

    }elseif($opcao == 3){
        $val = $num1 * $num2;
        $multiplicacao = "<div id='agua'>
        <h1>
            parabéns eu também fecho com a multiplicação !!!
        </h1>
        <p>
            {$num1} x {$num2} = {$val}
        </p>
        </div>";
        echo $multiplicacao;
    }elseif($opcao == 4){
        $val = $num1 / $num2;
        $divisao = "<div id='agua'>
        <h1>
            acho que você está infelizmente na divisão, eu não fecho com divisão. Mas tem que agradar o cliente né então ta aí...
        </h1>
        <p>
            {$num1} % {$num2} = {$val}
        </p>
        </div>";
        echo $divisao;
    }else{
        echo "<div id='agua'>
        <h1>
            ESCOLHE UM NÚMERO DE 1 A 4 CARA SÓ ISSO, SE VOCÊ DIGITAR OUTRO CLARAMENTE NÃO VAI FUNCIONAR A CALCULADORA...
        </h1>
        <p> 
            Opa blz só pra avisar tem que mudar a variavel 'opcao' pra conseguir mudar os calculos blz salve.
        </p>
        </div>";
    };
};

$opcao = 0;
$num1 = 2;
$num2 = 2;

calculadora($opcao,$num1,$num2);

?>