<?php
require_once __DIR__ . "/../controller/loginController.php";
$loginController = new LoginController();

if($_SERVER["REQUEST_METHOD"] == "POST"){
    switch($_GET["acao"]){
        case 'validarlogin':
            $resultado = $loginController->ValidarLogin($_POST["nome"],$_POST["senha"]);
            if($resultado){
                header("Location: ../view/home/index.php");
            }else{
                header("Location: ../view/index.php");
            }
            break;

        default:
            echo "Achei nada não";
            break;  
    }
}   