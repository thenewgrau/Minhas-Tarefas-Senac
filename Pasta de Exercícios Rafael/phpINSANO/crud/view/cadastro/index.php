<?php

require __DIR__ . "/../../controller/usuarioController.php";
$usuarioController = new UsuarioController();

$acao = 'create';
$cadastro = '<h1>Cadastrar Perfil</h1>';
$usuario = [

    
    'nome' => '',
    'senha' => '',
    'id' => ''
    
];

if(isset($_GET['acao'])){
    $id = $_GET['acao'];
    $cadastro = '<h1>Editar Perfil</h1>';
    $usuario = $usuarioController->confirmarUsuario($id);
    $acao = 'update';

}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $acao ?></title>
</head>
<body>
    <?php echo $cadastro ?>
    <form action="../../router/usuarioAutonomista.php?acao=<?php echo $acao ?>" method="POST">
        <input type="hidden" value="<?php echo $usuario['id'] ?>" name="usuario_id">
        <input type="text" name="nome" placeholder="Digite seu nome" value="<?php echo $usuario['nome'] ?>">
        <input type="password" name="senha" placeholder="Digite sua senha" value="<?php echo $usuario['senha'] ?>">
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>