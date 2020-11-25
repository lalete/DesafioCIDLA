import pymongo
from bson.son import SON
import json

import os

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["dbciencia"]

col = db['fichas']

# select the documents where the field features contains the field 0
cursor = col.find_one()

print(cursor)
