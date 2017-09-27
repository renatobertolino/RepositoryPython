import sqlite3

def reiniciar_banco():

    cursor.execute('DROP TABLE tabela_1')

def criar_tabela(nome_coluna, tipo_coluna, nome_tabela='tabela_1'):

    SQL = 'CREATE TABLE {} ({} {} PRIMARY KEY AUTOINCREMENT)'.format(nome_tabela, nome_coluna, tipo_coluna)
    cursor.execute(SQL)


with sqlite3.connect('primeiro_db.sqlite') as conn:
    cursor = conn.cursor()

    reiniciar_banco()