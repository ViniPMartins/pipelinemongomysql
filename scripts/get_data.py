from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import os
from dotenv import load_dotenv

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

def create_database(cli, db_name):
    db = cli[db_name]
    return db

def create_collection(db, collection_name):
    coll = db[collection_name]
    return coll

def get_api_json_data(url_api):
    response = requests.get(url_api)
    return response.json()

def insert_data_mongoDB(coll, data):
    coll.insert_many(data)
    return collection.count_documents({})

if __name__ == '__main__':

    load_dotenv()
    uri_mongo = os.getenv('MONGO_URI')
    db_name = os.getenv('MONGO_DB_NAME')
    collection_name = os.getenv("MONGO_COLLECTION_NAME")
    
    client = connect_mongoDB(uri_mongo)
    db = create_database(client, db_name)
    collection = create_collection(db, collection_name)

    url_api = 'https://labdados.com/produtos'
    data = get_api_json_data(url_api)
    print(f"Registros obtidos na API: {len(data)}")

    n_docs = insert_data_mongoDB(collection, data)
    print(f"Registros inseridos no mongoDB: {n_docs}")

    client.close()
