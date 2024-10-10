create database Biblioteca;
use Biblioteca;

create table Livro(
	id_livro int NOT NULL auto_increment,
    primary key (id_livro),
    titulo char(50), 
    isbn char(20),
    categoria char(30)

);

create table Autor(
	id_autor int NOT NULL auto_increment,
    primary key (id_autor),
    nome char(100),
    data_nascimento char(10)

);

create table Livro_Autor(
	id_livro int,
    id_autor int, 
    foreign key (id_livro)
		references Livro(id_livro),
	foreign key (id_autor)
		references Autor(id_autor)

);

create table Emprestimo(
	id_emprestimo int NOT NULL auto_increment,
    primary key (id_emprestimo),
    data_emprestimo char(10),
    data_devolucao char(10),
    id_livro int,
    foreign key (id_livro)
		references Livro(id_livro)
    
);