<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Castelho Ha Tim Bum</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Noto+Sans+KR:wght@100..900&family=Oswald:wght@200..700&family=Quicksand:wght@300..700&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&family=Roboto+Slab&display=swap" rel="stylesheet">
</head>
<body>
    <div id="fechadura">
        <form method="POST" id="formatura">
            <input type="number" id="cimento"  name='valorFoda'>
            <select name="operacao" id="op">
                <option value="soma">+</option>
                <option value="subtracao">-</option>
                <option value="divisao">/</option>
                <option value="multiplicacao">*</option>
            </select>
            <input type="number" id="cimento" name='valorFoda2'>
            <button id="maratona" type='submit'>ACEITO</button>
        </form>
    </div>
</body>
</html>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    
    $valor = htmlspecialchars($_POST["valorFoda"]);
    $valor2 = htmlspecialchars($_POST["valorFoda2"]);
    $tipo = htmlspecialchars($_POST['operacao']);
    if($valor == NULL || $valor2 == NULL || $valor == NULL && $valor2 == NULL){
        $uai = "<p> precisa dos valores </p>";
        echo $uai;
    };

    
    if($tipo == "soma" || $tipo == "SOMA"){
        $valorfinar = $valor + $valor2;
        $print = "
        <p>{$valorfinar}<p>
        ";
        echo $print;
    }
    else if($tipo == "subtração" || $tipo == "subtracao" || $tipo == "SUBTRACAO" || $tipo == "SUBTRAÇÃO"){
        $valorfinar = $valor - $valor2;
        $print = "
        <p>{$valorfinar}<p>
        ";
        echo $print;
    }
    else if($tipo == "divisão" || $tipo == "DIVISÃO" || $tipo == "divisao" || $tipo =="DIVISAO"){
        $valorfinar = $valor / $valor2;
    
        $print = "
        <p>{$valorfinar}<p>
        ";
        echo $print;
    }
    else if($tipo == "multiplicação" || $tipo == "MULTIPLICAÇÃO" || $tipo == "multiplicacao" || $tipo =="MULTIPLICACAO"){
        $valorfinar = $valor * $valor2;
        $print = "
        <p>{$valorfinar}<p>
        ";
        echo $print;
    }
    else{
        $uai = "<p> precisa da operação tbm moço </p>";
        echo $uai;
    }

};
?>
