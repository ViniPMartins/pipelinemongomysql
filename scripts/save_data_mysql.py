import os
from dotenv import load_dotenv
import mysql.connector
import pandas as pd

load_dotenv()

def connect_mysql():
    cnx = mysql.connector.connect(
        host = os.getenv('MYSQL_HOST'),
        user = os.getenv('MYSQL_USER'),
        password = os.getenv('MYSQL_PASSWORD')
    )
    print(cnx)
    cursor = cnx.cursor(buffered=True)
    return cnx, cursor

def create_database(cursor, db_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print('Database created!')
    except Exception as e:
        print(e)

def create_table_mysql(cursor, sql_create_table):
    try:
        cursor.execute(sql_create_table)
        print('Table created!')
    except Exception as e:
        print(e)

def insert_values_mysql(cnx, cursor, sql_insert_data, lista_data_livros):
    try:
        cursor.executemany(sql_insert_data, lista_data_livros)
        cnx.commit()
        print(f'{cursor.rowcount} values inserted!')
    except Exception as e:
        print(e)

def create_dataframe(path):
    df = pd.read_csv(path)
    return df

def create_tuples_data(df):
    lista_df = [tuple(values) for idx, values in df.iterrows()]
    return lista_df

if __name__ == '__main__':

    cnx, cursor = connect_mysql()
    db_name = 'dbprodutos'
    create_database(cursor, db_name)
    tab_name = 'tb_products_21_29'
    
    sql_create_table = f'''CREATE TABLE IF NOT EXISTS {db_name + "." + tab_name} (
        id VARCHAR(100),
        produto VARCHAR(100),
        cat_produto VARCHAR(100),
        preco FLOAT(10,2),
        frete FLOAT(10,2),
        data_compra DATE,
        vendedor VARCHAR(100),
        local_compra VARCHAR(100),
        avaliacao_compra INT,
        tipo_pagamento VARCHAR(100),
        quantidade_parcelas INT,
        latitude FLOAT(10,2),
        longitude FLOAT(10,2),
        PRIMARY KEY (id)
    );
    '''
    create_table_mysql(cursor, sql_create_table)

    df_livros = create_dataframe('./csv_data/data_products_21_29.csv')
    lista_df_livros = create_tuples_data(df_livros)

    sql_insert_data = f"INSERT INTO {db_name + "." + tab_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    insert_values_mysql(cnx, cursor, sql_insert_data, lista_df_livros)

    cursor.close()
    cnx.close()


