<?php

require_once __DIR__ . "/../config/db/database.php";



class LoginController{

    private $cone;

    public function __construct(){
        $cadeira = new Database();
    
        $this->cone = $cadeira->Conexao();
    }

    public function ValidarLogin($nome, $senha){
        $sql = "SELECT * FROM usuario WHERE nome = :nome AND senha = :senha";
        $db = $this->cone->prepare($sql);
        $db->bindParam(":nome", $nome);
        $db->bindParam(":senha", $senha);
        $db->execute();

        $usuario = $db->fetchALL(PDO::FETCH_ASSOC);

        if($usuario){
            return true;
        }else{
            return false;
        }
    
    }
}
