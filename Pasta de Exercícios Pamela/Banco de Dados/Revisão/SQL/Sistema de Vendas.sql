create database Vendas;
use Vendas;

create table Cliente(
	id_cliente int NOT NULL auto_increment,
    primary key (id_cliente),
    nome char(100),
    cpf char(20),
    telefone char(40)

);

insert into Cliente(nome, cpf, telefone) values('Ana Silva', '111.222.333-44','(11) 91234-5678');
insert into Cliente(nome, cpf, telefone) values('João Souza', '222.333.444-55', '(21) 99876-5432');
select * from Cliente;

create table Produto(
	id_produto int NOT NULL auto_increment,
    primary key (id_produto),
    nome char(100),
    preco float(20)

);

insert into Produto(nome, preco) values('Camiseta', 49.90);
insert into Produto(nome, preco) values('Calça Jeans', 99.90);
select * from Produto;

create table Venda(
	id_venda int NOT NULL auto_increment,
    primary key (id_venda),
    data_venda char(10),
    id_cliente int,
    foreign key (id_cliente)
		references Cliente(id_cliente)
        
);

create table Venda_Produto(
	id_venda int,
    id_produto int,
    foreign key (id_venda)
		references Venda(id_venda),
	foreign key (id_produto)
		references Produto(id_produto)

);

drop database Vendas;