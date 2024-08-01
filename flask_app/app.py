from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient('mongodb://admin:admin@mongodb:27017/')
db = client['ventes']

@app.route('/', methods=['GET'])
def get_data():
    ventes = db.ventes.find()
    ventes_list = list(ventes)
    return json_util.dumps(ventes_list), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
