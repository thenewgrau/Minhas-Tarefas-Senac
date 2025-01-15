create database Desafio;
use Desafio;

create table Aluno(
	id_aluno int NOT NULL auto_increment,
    primary key (id_aluno),
    nome char(100),
    idade int(3),
    RA int(20),
    numero_matricula int(20),
    endereco char(40),
    telefone char(20),
    email char(100),
    inep int(20),
    sexo char(20),
    data_nascimento date,
    curso char(20),
    nota1 decimal(5,2),
    nota2 decimal(5,2),
	nota3 decimal(5,2),
    nota4 decimal(5,2),
    media_boletim decimal(5,2)

);

create table Professor(
	id_professor int NOT NULL auto_increment,
    primary key (id_professor),
    nome char(100),
    idade int(3),
    materia char(40),
    CFEP int(20),
    modelo_do_carro_que_utiliza_diariamente_sim_e_necessario char(50)

);

drop database Desafio;