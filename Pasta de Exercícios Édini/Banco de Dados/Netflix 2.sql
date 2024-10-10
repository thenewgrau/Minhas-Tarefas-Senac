use netflix;

create table usuario(
	id int NOT NULL auto_increment,
    primary key (id),
    nome char(50) NOT NULL,
    idade int(3) NOT NULL,
    email char(100) NOT NULL,
    pag_id int,
    index paga_ind (pag_id),
    foreign key (pag_id)
		references pagamento(id),
	  ass_id int,
    index ass_ind (ass_id),
    foreign key (ass_id)
		references assinatura(id)
    
    
) engine = InnoDB;

insert into usuario(nome, idade, email) values('eduardo',16,'eduardoserafiim05@gmail.com');
select * from usuario;

create table assinatura(
	id int NOT NULL auto_increment,
    primary key (id),
    ass_padrcmanun char(20) NOT NULL,
    ass_padr char(20) NOT NULL,
    ass_premium char(20) NOT NULL,
    pagamento_id int,
    index pagamento_ind (pagamento_id),
    foreign key (pagamento_id)
		references pagamento(id)

) engine = InnoDB;

insert into assinatura(ass_padrcmanun, ass_padr, ass_premium) values('Falso', 'Falso', 'Verdadeiro');
select * from assinatura;

create table pagamento(
	id int NOT NULL auto_increment,
    primary key (id),
    forma_pag char(20) NOT NULL,
    valor_pag float(10) NOT NULL,
    usuar_id int,
    index usuar_ind (usuar_id),
    foreign key (usuar_id)
		references usuario(id)

) engine = InnoDB;

insert into pagamento(forma_pag, valor_pag) values('Crédito', 355.41);
select * from pagamento;

create table perfil(
	id int NOT NULL auto_increment,
    primary key (id),
    tipo char(20) NOT NULL,
    nome char(20) NOT NULL,
    foto blob,
    usuar_id int,
    index usuar_ind (usuar_id),
    foreign key (usuar_id)
		references usuario(id)

) engine = InnoDB;

insert into perfil(tipo, nome, foto) values('Adulto', ' Eduardo');
select * from perfil;

create table continuar(
	id int NOT NULL auto_increment,
    primary key (id),
    ep int,
    temp int,
    temp_exb int,
    perfil_id int,
    index perfil_ind (perfil_id),
    foreign key (perfil_id)
		references perfil(id)

) engine = InnoDB;

insert into continuar(ep, temp, temp_exb) values(10,150,120);
select * from continuar;

create table serie(
	id int NOT NULL auto_increment,
    primary key (id),
    nome char(20) NOT NULL,
    descr char(100) NOT NULL,
    qnt_ep int NOT NULL,
    categoria char(20) NOT NULL,
    class_indi char(20) NOT NULL,
    cont_id int,
    index cont_ind (cont_id),
    foreign key (cont_id)
		references continuar(id)
        
) engine = InnoDB;

insert into serie(nome, descr, qnt_ep, categoria, class_indi) values('Walter', ' waltercomexuxucomagua',12,'Suspense','Infantil');
select * from serie;

create table filme(
	id int NOT NULL auto_increment,
    primary key (id),
    nome char(20) NOT NULL,
    duracao int(3) NOT NULL,
    categoria char(20) NOT NULL,
    class_indi char(20) NOT NULL,
    cont_id int,
    index cont_ind (cont_id),
    foreign key (cont_id)
		references continuar(id)

) engine = InnoDB;

insert into filme(nome, descr, qnt_ep, categoria, class_indi) values('Walter', ' waltercomexuxucomagua',12,'Suspense','Infantil');
select * from filme;

create table avaliacao(
	id int NOT NULL auto_increment,
    primary key (id),
    bom boolean,
    ruim boolean,
    otimo boolean,
    serie_id int,
    filme_id int,
    index serie_ind (serie_id),
    index filme_ind (filme_id),
    foreign key (serie_id) 
		references serie(id),
	foreign key (filme_id)
		references filme(id)
        
) engine = InnoDB;

insert into avaliacao(bom,ruim,otimo) values(false,false,true);
select * from avaliacao;

create table jogos(
	id int NOT NULL auto_increment,
    primary key (id),
    nome char(20) NOT NULL,
    categoria char(20) NOT NULL,
    class_indi char(20) NOT NULL
	
);

insert into jogos(nome, categoria, class_indi) values('Heisenberg','Fodastica','Adulto');
select * from jogos;

create table mylist(
	id int NOT NULL auto_increment,
    primary key (id),
    filme_id int,
    index filme_ind (filme_id),
	foreign key (filme_id)
		references filme(id),
	serie_id int,
    index serie_ind (serie_id),
    foreign key (serie_id)
		references serie(id)

);

select * from mylist;