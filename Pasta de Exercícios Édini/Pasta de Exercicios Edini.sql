create database Netflixo;
use Netflixo;

create table Avaliacao(
	id_avaliacao int NOT NULL auto_increment,
    primary key (id_avaliacao),
    bom boolean,
    ruim boolean,
    otimo boolean

);

create table Jogos(
	id_jogo int NOT NULL auto_increment,
    primary key (id_jogo),
    nome char(100),
    categoria char(100),
    classificacao_indicativa int(3)

);

create table Serie(
	id_serie int NOT NULL auto_increment,
    primary key (id_serie),
    nome char(100),
    descricao char(200),
    qnt_ep int(4),
    categoria char(100),
    classificacao_indicativa int(2)

);

create table Filme(
	id_filme int NOT NULL auto_increment,
    primary key (id_filme),
	nome_do_filme char(100),
    duracao int,
    categoria char(100),
    classificacao_indicativa int(2)
    
);

create table Pagamento(
	pag_id int NOT NULL auto_increment,
    primary key (pag_id),
    forma_pag char(20),
    valor_pag float(20)

);

create table Assinatura(
	assinatura_id int NOT NULL auto_increment,
    primary key (assinatura_id),
    assinar_padrao_com_anuncio boolean,
    assinar_padrao boolean,
    assinar_premium boolean

);

create table Usuario(
	id_usuario int NOT NULL auto_increment,
    primary key (id_usuario),
    nome char(50),
    idade int(3),
    email char(50),
    pag_id int,
    assinatura_id int,
    foreign key (pag_id)
		references Pagamento(pag_id),
	foreign key (assinatura_id)
		references Assinatura(assinatura_id)

);

create table Perfil(
	id_perfil int NOT NULL auto_increment,
    primary key (id_perfil),
    adulto boolean,
    nome char(100),
    id_usuario int,
    foreign key (id_usuario) 
		references Usuario(id_usuario)
    
);

create table Continuar(
	id_continuar int NOT NULL auto_increment,
    primary key (id_continuar),
	tempo_exibido int(3),
    episodio int(3),
    temporada int(3),
    id_perfil int,
    id_serie int,
    foreign key (id_perfil) 
		references Perfil(id_perfil),
	foreign key (id_serie)
		references Serie(id_serie)
        
);

create table Minha_Lista(
	id_lista int NOT NULL auto_increment,
    primary key (id_lista),
    id_filme int,
    id_serie int,
    foreign key (id_filme)
		references Filme(id_filme),
	foreign key (id_serie)
		references Serie(id_serie)

);

drop database Netflixo;