<?php
class Database
{
    private $servidor = "localhost";
    private $dbnome = "whatsapp";
    private $user = "root";
    private $pass = "";
    
    public function Conexao(){
        try {
            $cone = new PDO(
                    "mysql:host=" . $this->servidor . ";dbname=" . $this->dbnome, $this->user,$this->pass
            );

            $cone->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
            return $cone;
        } catch (\Throwable $th) {
            echo $th->getMessage();
        }
    }

}

$teste = new Database();
$teste->Conexao();


?>