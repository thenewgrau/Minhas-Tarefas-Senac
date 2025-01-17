<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carro Foda Vrum</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    
</body>
</html>

<?php

$criarCarro = new Carro();
$criarCarro->marca = 'Wolkswagen';
$criarCarro->modelo = 'Golf GTI';
$criarCarro->ano = 2023;
$criarCarro->cor = 'vermelho';
$criarCarro->exibirDetalhes();
$criarCarro->alterarCor('preto');


class Carro{
    public $marca;
    public $modelo;
    public $ano;
    public $cor;
    public function exibirDetalhes(){
        echo "
        <div id='agua'>
            <p>
                Opa blz, então, ó, pega a visão, você tem um {$this->marca}
                do modelo {$this->modelo} ano {$this->ano} e a cor dele é {$this->cor}.    
            </p>
        </div>";
    }
    public function alterarCor($novaCor){
        $this->cor = $novaCor;
        echo "
        <div id='agua'>
            <p>
                Opa blz, então, ó, pega a visão, você tem um {$this->marca}
                do modelo {$this->modelo} ano {$this->ano} e a cor pq eu 
                dei uma PINTADA NELE kkk slk ri muito quando eu tava
                fazendo esse exercicio tmj professor meu amigo, a cor ai {$this->cor}.    
            </p>
        </div>";
    }
};

?>

<!-- // https://www.devmedia.com.br/criando-classe-em-php/24371 -->