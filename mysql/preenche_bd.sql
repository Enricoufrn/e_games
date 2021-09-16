insert into USUARIO(nickname,dt_nasc,p_nome,u_nome,email,senha) values
('zezinhoMatador','2005-05-13','José','Luis','JoséLuis@email.com','12345'),
('MateuzinUmaBala','2000-08-03','Matheus','Da Silva','Matheus@email.com','12345'),
('mariagamer', '1999-03-15', 'Maria', 'Moraes Mendes', 'maria@gamer.com', 'maria147258'),
('pedrogamer', '2002-10-21', 'Pedro', 'Lima Gomes', 'pedro@gamer.com', 'pedro987654'),
('anagamer', '2001-06-05', 'Ana', 'Ferreira dos Santos', 'ana@gamer.com', 'ana321987'),
('miguelgamer', '2007-01-01', 'Miguel', 'Machado Alves', 'miguel@gamer.com', 'miguel789123');


insert into DESENVOLVEDORA (cnpj,nome_comercial,nome_oficial,login,senha,email,site_oficial) values
('9379499400014','Valve','Valve Corporation','valve','valve123456','valve@valve.com','www.valvesoftware.com'),
('62902822000115', 'Rockstar', 'Rockstar Games', 'rockstar', 'rockstar123456', 'rockstar@rockstar.com', 'www.rockstargames.com'),
('31088439000141', 'Ubisoft', 'Ubisoft', 'ubisoft', 'ubisoft123456', 'ubisoft@ubisoft.com', 'www.ubisoft.com.com'),
('8327215309823','CD Project','CD Project Red','cdpred','cdpred123','CDProRed@email.com','www.CDPR.com');


insert into GAME(nome,dt_lanc,estilo,preco,desconto,chaves_vendidas,cnpj_desenvolvedora) values
('Assassins Creed Odyssey','2018-10-05','RPG',179.90,10.00,0,'31088439000141'),
('Counter-Strike: Global Offensive','2012-08-12', 'FPS', 0.00, 0.00,2,'9379499400014'),
('Grand Theft Auto V','2015-04-14', 'Action', 268.88, 157.61,1,'62902822000115'),
('The Witcher 3','2015-05-15', 'RPG',79.90,0,1,'8327215309823');


insert into AMIGO(nickname_1,nickname_2) values
('anagamer','mariagamer'),
('anagamer','pedrogamer'),
('anagamer','MateuzinUmaBala'),
('zezinhoMatador','MateuzinUmaBala'),
('zezinhoMatador','pedrogamer');

insert into ADQUIRE(nickname,id_game,cod_chave,comentario,nota) values
('zezinhoMatador',2,'1234-abcd-aaaa-bbbb','Cheio de hacker, uma porcaria','1'),
('anagamer',3,'4321-0101-abbb-cddc','Muito bom',10),
('anagamer',4,'gjjs-sdas-w343-2dg5','Muito bom',10),
('MateuzinUmaBala',2,'34jg-df78-fdsf-345d','Concordo com o zezinhoMatador',3);


