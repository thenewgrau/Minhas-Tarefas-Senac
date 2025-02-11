<?php
require_once __DIR__ . "/../controller/usuarioController.php";
$usuarioController = new UsuarioController();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    switch ($_GET["acao"]) {
        case 'create':
            $resultado = $usuarioController->criarUsuario($_POST["nome"], $_POST["senha"]);
            if ($resultado) {
                header("Location: ../view/home/index.php"); 
            } else {
                return false;
            }
            break;
    
        case 'update':
            $resultado = $usuarioController->updateUsuario($_POST['nome'],$_POST['senha'],$_POST['usuario_id']);
            if($resultado){
                header("Location: ../view/home/index.php");
            }else{
                header("Location: ../view/cadastro/index.php?acao=($_POST[id])");
            }
            break;
        case 'delete':
            $resultado = $usuarioController->deleteUsuario($_POST['id']);
            if($resultado){
                header("Location: ../view/home/index.php");
            }else{
                header("Location: ../view/cadastro/index.php?acao=($_POST[id])");
            }
            break;

        default:
            echo "Ação não encontrada!";
            break;
    }
}

