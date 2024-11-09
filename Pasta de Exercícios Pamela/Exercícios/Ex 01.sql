create database VO;
use VO;

create table Vendas(
	id int NOT NULL auto_increment,
    primary key (id),
    cliente varchar(100),
    produto varchar(100),
    quantidade int(3),
    preco_unitario float(40)

);

insert into Vendas(cliente, produto, quantidade, preco_unitario) values
('Walter', 'Maisena',5, 12.40),
('White', 'Corrimão', 2, 20),
('Jesse', 'Marmitex', 1, 20),
('Fit Palt', 'Turbo 2.5 TSI', 6, 120),
('Antonio', 'Fiat Palio', 3, 120),
('Felipe', 'Serra Elétrica', 1, 100);

select quantidade * preco_unitario from Vendas;
select sum(quantidade) from Vendas;
select min(preco_unitario), max(preco_unitario) from Vendas;

drop database VO;