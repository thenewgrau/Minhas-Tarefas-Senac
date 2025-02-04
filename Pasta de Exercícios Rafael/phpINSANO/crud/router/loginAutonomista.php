<?php
require_once __DIR__ . "/../controller/loginController.php";
$loginController = new LoginController();

if($_SERVER["REQUEST_METHOD"] == "POST"){
    switch($_GET["acao"]){
        case 'validarlogin':
            $resultado = $loginController->ValidarLogin($_POST["nome"],$_POST["senha"]);
            echo $resultado;
            break;

        default:
            echo "Achei nada não";
            break;  
    }
}   