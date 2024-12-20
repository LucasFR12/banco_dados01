import pymysql.cursors

# É preciso passar os dados abaixo para conectar-se ao banco de dados
con = pymysql.connect(
    #host="",
    #user="",
    #password="",
    #port=,
    #db="",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)


def criar_tabela(nome_tabela, colunas):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {nome_tabela} ({colunas})")
            con.commit()
            print(f"Tabela '{nome_tabela}' criada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro {e}.")


def excluir_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            comando_sql = f"DROP TABLE {nome_tabela}"
            cursor.execute(comando_sql)
            con.commit()
            print(f"Tabela '{nome_tabela} excluida com sucesso.'")
    except Exception as e:
        print(f"Ocorreu um erro {e}.")

def deletar(nome_tabela, id):
    try:
        with con.cursor() as cursor:
            comando_sql = f"DELETE FROM {nome_tabela} WHERE id = {id}"
            cursor.execute(comando_sql)
            con.commit()
            print(f"id: {id} deletado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro {e}.")

def inserir_valor(nome_tabela, nome_coluna, *valores):
    try:
        with con.cursor() as cursor:
            sub_valores = ', '.join(['%s'] * len(valores))
            comando_sql = f"INSERT INTO {
                nome_tabela} ({nome_coluna}) VALUES ({sub_valores})"
            cursor.execute(comando_sql, valores)
            con.commit()
            print(f"'{valores}' foi adicionado em '{
                  nome_coluna}' com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro {e}")


def modificar_valor(nome_tabela, nome_coluna, id, novo_valor):
    try:
        with con.cursor() as cursor:
            comando_sql = f"UPDATE {nome_tabela} SET {
                nome_coluna} = '{novo_valor}' WHERE id = '{id}'"
            cursor.execute(comando_sql)
            con.commit()
            print(f"{nome_coluna} do id:{id} modificado para -> '{novo_valor}' com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro {e}.")


def mostrar_tabela(nome_tabela):
    try:
        with con.cursor() as cursor:
            comando_sql = f"SELECT * FROM {nome_tabela}" # Utilize ORDER BY para ordenar
            cursor.execute(comando_sql)
            con.commit()
            res = cursor.fetchall()
            for i in res:
                for k, v in i.items():
                    print(f"{k}: {v}", end=' - ')
                print()
    except Exception as e:
        print(f"Ocorreu um erro {e}.")


# ==================================================================
# OBSERVAÇÂO:
# Todos os parâmetros deve ser passados entre aspas 'simples' exceto o id que será um INTEGER
# ==================================================================

con.close()
