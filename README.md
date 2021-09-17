# e_games
Projeto desenvolvido para a avaliação da segunda unidade da disciplina de banco de dados do DCA-UFRN.
O foco maior do projeto foi a modelagem dos dados e a desenvolvimento dos scripts para a criação do banco de dados e consultas.
Para isso a API foi desenvolvida tomando como base um projeto disponibilizado pelo professor Eduardo, onde o objetivo maior é a vizualização
do funcionamento do banco de dados lidando com as diferentes consultas feitas pela API.
## Endpoints para as querys solicitadas
* Amigos de um usuário : '/amigos_usuario', method = GET, body = {"nickname": "nickname_usuario"}
* Games de um usuário : '/aquisicoes_usuario', method = GET, body = {"nickname": "nickname_usuario"}
* Listar games e suas notas : '/games_notas', method = GET

