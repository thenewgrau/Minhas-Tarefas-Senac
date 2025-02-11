<?php

require_once __DIR__ . "/../config/db/database.php";



class UsuarioController{

    private $cone;

    public function __construct(){
        $cadeira = new Database();
    
        $this->cone = $cadeira->Conexao();
    }

    public function CatchUsers(){
        $sql = "SELECT * FROM usuario";
        $db = $this->cone->prepare($sql);
        $db->execute();

        $usuario = $db->fetchALL(PDO::FETCH_ASSOC);

        if($usuario){
            return $usuario;
        }else{
            return false;
        }
    
    }
    
    public function criarUsuario($nome, $senha) {
        try {
            $sql = "INSERT INTO usuario(nome, senha) VALUES(:nome, :senha)";
            $db = $this->cone->prepare($sql);
            $db->bindParam(":nome", $nome);
            $db->bindParam(":senha", $senha);
            if ($db->execute()) {
                return true;
            } else {
                return false;
            }
        } catch (\Throwable $th) {
           
        }
    }

    public function confirmarUsuario($id){
        try {
            $sql = 'select * from usuario where id = :id';
            $db = $this->cone->prepare($sql);
            $db->bindParam(":id", $id); 
            $db->execute();
            $usuario = $db->fetch(PDO::FETCH_ASSOC);
            
            if($usuario){
                return $usuario;
            }else{
                return false;
            }

        } catch (\Throwable $th) {
            //throw $th;
        }

    }

    public function updateUsuario($nome, $senha, $id){
        $sql = 'UPDATE usuario SET nome = :nome, senha = :senha WHERE id = :id';
        $db = $this->cone->prepare($sql);
        $db->bindParam(":nome", $nome);
        $db->bindParam(":senha", $senha);
        $db->bindParam(":id", $id);
        
        if($db->execute()){ 
            return true;
        }else{
            return false;
        }
    }

    public function deleteUsuario($id){
        $sql = 'DELETE FROM usuario WHERE id = :id';
        $db = $this->cone->prepare($sql);
        $db->bindParam(":id", $id);
        
        if($db->execute()){
            return true;
        }else{
            return false;
        }
    

    }
}
