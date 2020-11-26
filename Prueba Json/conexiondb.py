import pymongo
from bson.son import SON
import json

import os

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.dbciencia

col = db.datos

dat= json.load(open('historiales_clinicos.json'))

#Para importar datos 
#with open('historiales_clinicos.json') as data_file:
 #   data = json.loads(data_file.read())
  #  print(type(data))

docs = []
for doc in dat:
    doc.pop('_id')
    docs.append(doc)
_id = db ['fichas'].insert_many(docs)
     
    
    

