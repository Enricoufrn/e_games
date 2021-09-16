/*
 * Script para criação do banco de dados do sistema proposto para a avaliação
 * da segunda unidade da disciplina de banco de dados
 */

CREATE DATABASE E_GAMES;
USE E_GAMES;
CREATE TABLE USUARIO (
	nickname VARCHAR(50) PRIMARY KEY,
	dt_nasc DATE NOT NULL,
	p_nome VARCHAR(50) NOT NULL,
	u_nome VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL,
	senha VARCHAR(20) NOT NULL
);

CREATE TABLE DESENVOLVEDORA (
	cnpj VARCHAR(14) PRIMARY KEY,
	nome_comercial VARCHAR(50) NOT NULL,
	nome_oficial VARCHAR(50) NOT NULL,
	login VARCHAR(20) NOT NULL,
	senha VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL,
	site_oficial VARCHAR(50)
);

CREATE TABLE GAME (
	id SMALLINT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	dt_lanc DATE NOT NULL,
	estilo VARCHAR(50) NOT NULL,
	preco DECIMAL(10,2),
	desconto DECIMAL(10,2),
	cnpj_desenvolvedora VARCHAR(14),
	chaves_vendidas INT NOT NULL DEFAULT 0,
	CONSTRAINT fk_cnpj_desen FOREIGN KEY (cnpj_desenvolvedora) REFERENCES DESENVOLVEDORA (cnpj)
	ON DELETE SET NULL
	ON UPDATE CASCADE
);

CREATE TABLE ADQUIRE (
	nickname VARCHAR(50),
	id_game SMALLINT,
	cod_chave VARCHAR(19) NOT NULL,
	comentario VARCHAR(200),
	nota SMALLINT,
	CONSTRAINT fk_id_game FOREIGN KEY (id_game) REFERENCES GAME (id),
	CONSTRAINT fk_nickname FOREIGN KEY (nickname) REFERENCES USUARIO (nickname),
	PRIMARY KEY (nickname,id_game)
);

CREATE TABLE AMIGO (
	nickname_1 VARCHAR(50),
	nickname_2 VARCHAR(50),
	CONSTRAINT fk_nickname_1 FOREIGN KEY (nickname_1) REFERENCES USUARIO (nickname),
	CONSTRAINT fk_nickname_2 FOREIGN KEY (nickname_2) REFERENCES USUARIO (nickname),
	PRIMARY KEY (nickname_1,nickname_2)
);
