from http import client
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://chefsociety:{password}@chefsocietydb.e4h6kbb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)
