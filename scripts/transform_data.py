from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv
import pandas as pd

def connect_mongoDB(uri):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

def setup_db_colletion(client, db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]
    return db, collection

def rename_columns(collection, map_columns):
    collection.update_many({}, {'$rename': map_columns})
    return True

def query_data(collection, query):

    list_query_data = []
    for doc in collection.find(query):
        list_query_data.append(doc)

    return list_query_data

def make_dataframe(list_data):
    return pd.DataFrame(list_data)

def transform_date_format(df_to_transform, column_date):
    df_to_transform[column_date] = pd.to_datetime(df_to_transform[column_date], format='%d/%m/%Y')
    df_to_transform[column_date] = df_to_transform[column_date].dt.strftime('%Y-%m-%d')
    return df_to_transform

def save_csv_file(df, filename):
    df.to_csv(filename, index=False)
    print(f"CSV file save in {filename}")
    return True

def make_query_dataframe(collection, query, format_date=True):
    list_data = query_data(collection, query)
    df_data = make_dataframe(list_data)
    if format_date:
        df_data = transform_date_format(df_data, 'Data da Compra')

    print('DataFrame create sucessfully!')
    return df_data    

if __name__ == '__main__':

    load_dotenv()
    uri_mongo = os.getenv('MONGO_URI')
    db_name = os.getenv('MONGO_DB_NAME')
    collection_name = os.getenv("MONGO_COLLECTION_NAME")
    
    client = connect_mongoDB(uri_mongo)
    db, collection = setup_db_colletion(client, db_name, collection_name)

    rename_columns(collection, {'lat':'latitude','lon':'longitude'})

    df_livros = make_query_dataframe(collection, {'Categoria do Produto':'livros'})
    save_csv_file(df_livros, 'csv_data/data_livros.csv')

    df_produtos = make_query_dataframe(collection, {'Data da Compra':{'$regex':'/202[1-9]'}})
    save_csv_file(df_produtos, 'csv_data/data_products_21_29.csv')

    client.close()


