create database Livraria;
use Livraria;

create table Livros(
	id int NOT NULL auto_increment,
    primary key (id),
    titulo varchar(100),
    autor varchar(50),
    preco float(40),
    quantidade_estoque int(10)

);

insert into Livros(titulo, autor, preco, quantidade_estoque) values
('Suicidio', 'Emile Durkheim', 40.99, 100),
('Hora de Aventura', 'Cartoon Netwoork', 10.99, 420),
('Caco', 'Felipe Neto', 69.69, 12),
('Romualdo', 'Romualdo', 10.40, 1),
('Diário de um Banana', 'Banana', 99.99, 827);

select sum(preco * quantidade_estoque) from Livros;
select avg(preco) from Livros;
select min(preco), max(preco) from Livros;

drop database Livraria;