from pymongo import MongoClient

Mongo_URI = 'mongodb://localhost'

client = MongoClient(Mongo_URI)

db = client['pppprueba']
collection = db['fichas']

collection.insert_one({"nombre": "miguel" , "edad": 20})

results = collection.find()                 #funcion para buscar una coleccion en la base de datos.

for r in results:                           #recorre results buscando todos los archivos con la casilla nombre.
    print(r['nombre'])

#collection.delete_many(["nombre":miguel ]) sirve para borrar a todos los archivos con nombre de miguel.
#collection.delete_one() para borrar 1 archivo.

numero_de_fichas = collection.count_documents({})  #sirve para contar el numero de fichas de la base de datos.
