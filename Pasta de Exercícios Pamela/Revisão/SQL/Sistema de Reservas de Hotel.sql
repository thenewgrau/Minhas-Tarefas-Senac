create database Reservas;
use Reservas;

create table Quarto(
	id_quarto int NOT NULL auto_increment,
    primary key (id_quarto),
    tipo_quarto char(100),
    preco_diaria float(20)

);

insert into Quarto(tipo_quarto, preco_diaria) values('Suite Luxo', 350.00);
insert into Quarto(tipo_quarto, preco_diaria) values('Quarto Standard', 150);
select * from Quarto;

create table Hospede(
	id_hospede int NOT NULL auto_increment,
    primary key (id_hospede),
    nome char(100),
    cpf char(20)

);

insert into Hospede(nome, cpf) values('Carlos Pereira', '123.456.789-00');
insert into Hospede(nome, cpf) values('Maria Oliveira', '987.654.321-00');
select * from Hospede;

create table Reserva(
	id_reserva int NOT NULL auto_increment,
    primary key (id_reserva),
    data_inicio char(10),
    data_fim char(10),
    id_quarto int,
    id_hospede int,
    foreign key (id_quarto) 
		references Quarto(id_quarto),
	foreign key (id_hospede)
		references Hospede(id_hospede)

);

drop database Reservas;