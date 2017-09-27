import sqlite3


def restart_database():

    cursor.execute('DROP TABLE table_1')


def create_table(column_name, column_type, table_name='table_1'):

    SQL = 'CREATE TABLE {} ({} {} PRIMARY KEY AUTOINCREMENT)'.format(table_name, column_name, column_type)
    cursor.execute(SQL)


def add_column(new_column, column_type, table_name='table_1'):
    SQL = "ALTER TABLE {} ADD COLUMN '{}' {}".format(table_name, new_column, column_type)
    cursor.execute(SQL)


def insert_row(*values, table_name='table_1'):
    SQL = "INSERT OR IGNORE INTO {tn} (column_2, column_3) VALUES ('{}', '{}')".format(tn=table_name, *values)
    cursor.execute(SQL)


def update_row(column_name, new_value, row_id, table_name='table_1'):
    SQL = "UPDATE {} SET {}=('{}') WHERE column_1 = ({})".format(table_name, column_name, new_value, row_id)
    cursor.execute(SQL)


def select_all(table_name='table_1'):
    SQL = "SELECT * FROM {}".format(table_name)
    cursor.execute(SQL)

    return cursor.fetchall()


# More secure against injection attacks
def select_row(row_pk, table_name='table_1'):
    SQL = "SELECT * FROM {} WHERE column_1 = ?".format(table_name)
    cursor.execute(SQL, (row_pk,))

    return cursor.fetchall()


# May help against injection attacks. Useful to clean parameters names
def clean_name(value):
    return ''.join(character for character in value if character.isalnum())


# Connecting to the database file
with sqlite3.connect('my_first_db.sqlite') as conn:
    cursor = conn.cursor()

    restart_database()

    # Creating a new table
    create_table('column_1', 'INTEGER')

    # Adding new columns to a existing table
    add_column('column_2', 'TEXT')
    add_column('column_3', 'TEXT')

    # Inserting rows
    insert_row('a', 'ab')
    insert_row('b', 'bc')
    insert_row('c', 'cd')

    # Updating row value
    update_row('column_2', 'Updated value', 2)

    # Querying the database
    print(select_all())
    print(select_row(2))

    conn.commit()