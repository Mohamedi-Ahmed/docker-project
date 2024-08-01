import json
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@mongodb:27017/')
db = client['ventes']  

with open('ventes.json') as file:
    ventes = json.load(file)

db.ventes.insert_many(ventes)
print("Data inserted successfully!")