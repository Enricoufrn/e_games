#!/usr/bin/python3
from flask import Flask, request, json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from os import environ
from decimal import Decimal

DB_HOST = environ.get('DB_HOST')
DB_NAME = environ.get('DB_NAME')
DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASSWORD')
if DB_PASSWORD is not None:
    print('###################################')
    print('These are the environment variables: DB_HOST='+DB_HOST+', DB_NAME='+DB_NAME+', DB_USER='+DB_USER+', DB_PASSWORD='+DB_PASSWORD)
    print('###################################')
else:
    print('###################################')
    print('No environment variable appeared!')
    print('###################################')


app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    select_query = "SELECT * FROM USUARIO"
    return run_select_query(select_query)
    
@app.route('/usuario', methods=['GET'])
def obter_usuario_por_nick():
    request_data = request.get_json()
    nickname = request_data['nickname']
    select_query = "SELECT * FROM USUARIO WHERE nickname = \'"+nickname+"\'"
    return run_select_query(select_query)
    
@app.route('/adicionar_usuario', methods=['POST'])
def add_usuario():
    print('Request' + str(request.data))
    insert_query = """INSERT INTO USUARIO (nickname, dt_nasc, p_nome, u_nome, email, senha) VALUES (%s, %s, %s, %s, %s, %s)"""
    request_data = request.get_json()
    val = (request_data['nickname'],request_data['dt_nasc'],request_data['p_nome'],request_data['u_nome'],request_data['email'],request_data['senha'])
    return run_insert_query(insert_query, val, 'USUARIO')
    
@app.route('/update_user', methods=['POST'])
def att_usuario_por_nick():
    request_data = request.get_json()
    old_nickname = request_data['old_nickname']
    print('Request' + str(request.data))
    update_query = """UPDATE USUARIO SET nickname = %s, dt_nasc = %s, p_nome = %s, u_nome = %s, email = %s, senha = %s WHERE nickname = \'"""+old_nickname+"\'"""
    val = (request_data['nickname'],request_data['dt_nasc'],request_data['p_nome'],request_data['u_nome'],request_data['email'],request_data['senha'])
    return run_update_query(update_query, val, 'USUARIO')

@app.route('/games', methods=['GET'])
def obter_games():
    select_query = "SELECT * FROM GAME"
    return run_select_query(select_query)

@app.route('/game', methods=['GET'])
def obter_game_por_id():
    request_data = request.get_json()
    game_id = request_data['game_id']
    select_query = "SELECT * FROM GAME WHERE id = \'"+str(game_id)+"\'"
    return run_select_query(select_query)
    
@app.route('/adicionar_game', methods=['POST'])
def add_game():
    print('Request' + str(request.data))
    insert_query = """INSERT INTO GAME (nome, dt_lanc, estilo, preco, desconto, cnpj_desenvolvedora) VALUES (%s, %s, %s, %s, %s, %s)"""
    request_data = request.get_json()
    val = (request_data['nome'],request_data['dt_lanc'],request_data['estilo'],request_data['preco'],request_data['desconto'], request_data['cnpj_desenvolvedora'])
    return run_insert_query(insert_query, val, 'GAME')
    
@app.route('/update_game', methods=['PUT'])
def att_game_por_id():
    print('Request' + str(request.data))
    update_query = "UPDATE GAME SET nome = %s, dt_lanc = %s, estilo = %s, preco = %s, desconto = %s WHERE id = %s"
    request_data = request.get_json()
    val = (request_data['nome'],request_data['dt_lanc'],request_data['estilo'],request_data['preco'],request_data['desconto'], request_data['id'],)
    return run_update_query(update_query, val, 'GAME')

@app.route('/desenvolvedoras', methods=['GET'])
def obter_desenvolvedoras():
    select_query = "SELECT * FROM DESENVOLVEDORA"
    return run_select_query(select_query)
    
@app.route('/desenvolvedora', methods=['GET'])
def obter_desenvolvedora_cnpj():
    request_data = request.get_json()
    cnpj = request_data['cnpj']
    select_query = "SELECT * FROM DESENVOLVEDORA WHERE cnpj = \'"+cnpj+"\'"
    return run_select_query(select_query)
    
@app.route('/adicionar_desenvolvedora', methods=['POST'])
def add_desenvolvedora():
    print('Request' + str(request.data))
    insert_query = """INSERT INTO DESENVOLVEDORA (cnpj, nome_comercial, nome_oficial, login, senha, email, site_oficial) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    request_data = request.get_json()
    val = (request_data['cnpj'],request_data['nome_comercial'],request_data['nome_oficial'],request_data['login'],request_data['senha'], request_data['email'], request_data['site_oficial'])
    return run_insert_query(insert_query, val, 'DESENVOLVEDORA')
    
@app.route('/update_desenvolvedora', methods=['PUT'])
def att_desenvolvedora_cnpj():
    print('Request' + str(request.data))
    update_query = "UPDATE DESENVOLVEDORA SET nome_comercial = %s, nome_oficial = %s, login = %s, senha = %s, email = %s, site_oficial = %s WHERE cnpj = %s"
    request_data = request.get_json()
    val = (request_data['nome_comercial'],request_data['nome_oficial'],request_data['login'],request_data['senha'], request_data['email'], request_data['site_oficial'],request_data['cnpj'])
    return run_update_query(update_query, val, 'DESENVOLVEDORA')
    
@app.route('/delete_desenvolvedora', methods=['DELETE'])
def delete_desenvolvedora_cnpj():
    request_data = request.get_json()
    cnpj = request_data['cnpj']
    print('Request' + str(request.data))
    delete_query = "DELETE FROM DESENVOLVEDORA WHERE cnpj = \'"+cnpj+"\'"
    return run_delete_query(delete_query,'DESENVOLVEDORA')
    
@app.route('/amigos', methods=['GET'])
def obter_amizades():
    select_query = "SELECT * FROM AMIGO"
    return run_select_query(select_query)
    
@app.route('/amigos_usuario', methods=['GET'])
def obter_amizades_usuario():
    request_data = request.get_json()
    nickname = request_data['nickname']
    select_query = "SELECT AMIGO.nickname_2 FROM AMIGO LEFT JOIN USUARIO ON USUARIO.nickname = AMIGO.nickname_1  WHERE USUARIO.nickname = \'"+nickname+"\' UNION SELECT AMIGO.nickname_1 FROM AMIGO LEFT JOIN USUARIO ON USUARIO.nickname = AMIGO.nickname_2  WHERE USUARIO.nickname = \'"+nickname+"\'"
    return run_select_query(select_query)
    
@app.route('/novo_amigo', methods=['POST'])
def add_amigo_usuario():
    print('Request' + str(request.data))
    insert_query = """INSERT INTO AMIGO (nickname_1, nickname_2) VALUES (%s, %s)"""
    request_data = request.get_json()
    val = (request_data['nickname_1'],request_data['nickname_2'])
    return run_insert_query(insert_query, val, 'AMIGO')
    
@app.route('/deletar_amigo', methods=['DELETE'])
def delete_amigo_usuario():
    request_data = request.get_json()
    nickname_1 = request_data['nickname_1']
    nickname_2 = request_data['nickname_2']
    print('Request' + str(request.data))
    delete_query = "DELETE FROM AMIGO WHERE nickname_1 = \'"+nickname_1+"\' AND nickname_2 = \'"+nickname_2+"\'"
    return run_delete_query(delete_query,'AMIGO')
    
@app.route('/aquisicoes', methods=['GET'])
def obter_aquisicoes():
    select_query = "SELECT * FROM ADQUIRE"
    return run_select_query(select_query)
    
@app.route('/aquisicoes_usuario', methods=['GET'])
def obter_aquisicoes_usuario():
    request_data = request.get_json()
    nickname = request_data['nickname']
    select_query = "SELECT * FROM ADQUIRE WHERE nickname = \'"+nickname+"\'"
    return run_select_query(select_query)
    
@app.route('/nova_aquisicao', methods=['POST'])
def add_aquisicao_usuario():
    print('Request' + str(request.data))
    insert_query = """INSERT INTO ADQUIRE (nickname,id_game,cod_chave,comentario,nota) VALUES (%s, %s, %s, %s, %s)"""
    request_data = request.get_json()
    val = (request_data['nickname'],request_data['game_id'],request_data['cod_chave'],request_data['comentario'],request_data['nota'])
    game_id = request_data['game_id']
    update_query = "UPDATE GAME SET chaves_vendidas = chaves_vendidas + 1 WHERE id = \'"+str(game_id)+"\'"
    run_update_query(update_query,None,'GAME')
    return run_insert_query(insert_query,val,'ADQUIRE')
    
@app.route('/desfazer_aquisicao', methods=['DELETE'])
def desfazer_aquisicao():
    request_data = request.get_json()
    nickname = request_data['nickname']
    game_id= request_data['game_id']
    print('Request' + str(request.data))
    delete_query = "DELETE FROM ADQUIRE WHERE nickname = \'"+nickname+"\' AND id_game = \'"+str(game_id)+"\'"
    update_query = "UPDATE GAME SET chaves_vendidas = chaves_vendidas + 1 WHERE id = \'"+str(game_id)+"\'"
    run_update_query(update_query,None,'GAME')
    return run_delete_query(delete_query,'ADQUIRE')
    
@app.route('/games_notas', methods=['GET'])
def obter_games_notas():
    select_query = "SELECT GAME.nome ,AVG(ADQUIRE.nota) FROM GAME, ADQUIRE WHERE GAME.id = ADQUIRE.id_game GROUP BY GAME.nome;"
    return run_select_query(select_query)
    
@app.route('/games_gratis', methods=['GET'])
def obter_games_gratis():
    select_query = "SELECT * FROM GAME WHERE preco = 0"
    return run_select_query(select_query)
    
@app.route('/games_em_promocao', methods=['GET'])
def obter_games_promocoes():
    select_query = "SELECT * FROM GAME WHERE desconto != 0"
    return run_select_query(select_query)
    
@app.route('/games_mais_vendidos', methods=['GET'])
def obter_games_mais_vendidos():
    select_query = "SELECT * FROM GAME ORDER BY chaves_vendidas DESC"
    return run_select_query(select_query)
    
@app.route('/games_mais_vendidos_estilo', methods=['GET'])
def obter_games_mais_vendidos_estilo():
    request_data = request.get_json()
    estilo = request_data['estilo']
    select_query = "SELECT * FROM GAME WHERE estilo = \'"+estilo+"\' ORDER BY chaves_vendidas"
    return run_select_query(select_query)
    
@app.route('/games_desenvolvedora', methods=['POST'])
def obter_games_desen_cnpj():
    request_data = request.get_json()
    cnpj = request_data['cnpj']
    select_query = "SELECT * FROM GAME WHERE cnpj_desenvolvedora = \'"+cnpj+"\'"
    return run_select_query(select_query)

def get_database_connection():
    return mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)

def run_insert_query(query, values, table_name):
    connection = get_database_connection()
    res = ''
    id = None
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        id = cursor.lastrowid
        if id is not None:
            res += 'Record with id('+str(id)+') inserted successfully into '+table_name+' table'
        else: 
            res += str(cursor.rowcount) + ' Record inserted successfully into '+table_name+' table'
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res += "Failed to insert record into table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return (res,id)
    
def run_update_query(query, values, table_name):
    connection = get_database_connection()
    res = ''
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        res += 'Update successfully into '+table_name+' table'
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res += "Failed to update table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return json.dumps(res, cls=DecimalEncoder)
    
def run_delete_query(query,table_name):
    connection = get_database_connection()
    res = ''
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        res += 'Successful deletion into '+table_name+' table'
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res += "Failed to delete from table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return (res)

def run_select_query(query):
    connection = get_database_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        for x in res:
            print(x)
        print(res)
        cursor.close()
    except mysql.connector.Error as error:
        res = "Failed to select from table {}".format(error)
        print(res)
    finally:
        if connection.is_connected():
            connection.close()
    return json.dumps(res, cls=DecimalEncoder)

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
