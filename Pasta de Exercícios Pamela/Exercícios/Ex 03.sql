create database Animes;
use Animes;

create table Personagem(
	id int NOT NULL auto_increment,
    primary key (id),
	nome varchar(100),
    nome_poder varchar(100),
    valor_ataque float(20),
    valor_defesa float(20)
    
);

insert into Personagem(nome, nome_poder, valor_ataque, valor_defesa) values
('walter', 'super quimica', 600, 200),
('fish', 'agua', 12.50, 2969),
('jesse', 'drogas', 532, 21),
('robert', 'mouse', 999, 1),
('joaosales', 'garrafa', 1, 92),
('eliel', 'morcegos', 1, 1),
('matheus', 'cabelo', 1, 34),
('henrico', 'bancos de dados', 9999, 1);

select count(nome) from Personagem;
select avg(valor_ataque) from Personagem;
select min(valor_defesa), max(valor_defesa) from Personagem;
select sum(valor_ataque) from Personagem group by nome_poder;
select count(distinct valor_ataque) from Personagem;

drop database Animes;