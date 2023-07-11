from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')
result = client['dataops']['Carros'].aggregate([
    {
        '$lookup': {
            'from': 'Montadoras', 
            'localField': 'Montadora', 
            'foreignField': 'Montadora', 
            'as': 'Montadoras'
        }
    }, {
        '$unwind': {
            'path': '$Montadoras'
        }
    }, {
        '$group': {
            '_id': '$Montadoras.Pais', 
            'Carro': {
                '$push': '$Carro'
            }
        }
    }
])