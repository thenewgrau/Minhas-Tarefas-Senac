use Biblioteca;

create table Usuario(
	id INT NOT NULL auto_increment,
    primary key (id),
    nome char,
    idade int,
    email char,
    telefone char
    
);


create table Livro(
	id INT NOT NULL auto_increment,
    primary key (id),
    nome_livro char,
    data_lanca char

);

create table Empréstimo(
	id INT NOT NULL auto_increment,
    primary key (id),
    tempo_devolucao int,
    usuario_id int,
    livro_id int,
    index livro_ind (livro_id),
    index usuario_ind (usuario_id),
    foreign key (usuario_id)
		references Usuario(id),
	foreign key (livro_id)
		references Livro(id)

);

create table Autor(
	nome_autor char NOT NULL,
    idade int NOT NULL

);



