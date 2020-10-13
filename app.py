from pymongo import MongoClient

Mongo_URI = 'mongodb://localhost'

client = MongoClient(Mongo_URI)

db = client['pppprueba']
collection = db['fichas']

collection.insert_one({"nombre": "miguel" , "edad": 20})