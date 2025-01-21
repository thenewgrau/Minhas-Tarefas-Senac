<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campos do Jordão</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div id="fechadura">
        <form method="POST">
            <h1>Nome</h1>
            <input type="text" name='nomeFoda'>
            <h1>Email</h1>
            <input type="email" name='emailFoda'>

            <button id="maratona" type='submit'>ACEITO</button>
        </form>
    </div>
</body>
</html>

<?php

if ($_SERVER["REQUEST_METHOD"] == "POST"){

    $nome = htmlspecialchars($_POST["nomeFoda"]);
    $email = htmlspecialchars($_POST["emailFoda"]);

    if($nome == NULL){
        echo "
        <div id='aguasClaras'>
            <p>Digita o nome lenda</p>
        </div>
        
        ";
    }else if($email == NULL){
        echo "
        <div id='aguasClaras'>
            <p>Opa desculpa ai mas você tem que digitar o email tá?</p>
        </div>
        
        ";
    }else{
        echo "
        <div id='agua'>
            <p>
                Nome: {$nome} <br>
                Email: {$email}
            </p>
        </div>
        ";
    }

};

?>
