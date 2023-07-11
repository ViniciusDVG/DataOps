import pandas as pd
from pymongo import MongoClient

# Step 1: Create DataFrame

df1 = {
    "Carro": ["Onix","Polo","Sandero","Fiesta","City"],
    "Cor": ["Prata","Branco","Prata","Vermelho","Preto"],
    "Montadora": ["Chevrolet","Volkswagen","Renault","Ford","Honda"]
}

df2 = {
    "Montadora": ["Chevrolet","Volkswagen","Renault","Ford","Honda"],
    "Pais": ["EUA","Alemanha","França","EUA","Japao"]
}

# Create DataFrame
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)


# Step 2: Transform

# Convert DataFrame to dictionary
data_dict1 = df1.to_dict(orient='records')
data_dict2 = df2.to_dict(orient='records')

# Step 3: Load - Save data to MongoDB

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/?authMechanism=DEFAULT?")

# Select the database
db = client['dataops']

# Select the collection
collection_carros = db['Carros']
collection_montadora = db['Montadoras']

# Insert data into collection
collection_carros.insert_many(data_dict1)
collection_montadora.insert_many(data_dict2)




