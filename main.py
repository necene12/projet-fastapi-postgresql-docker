import csv
import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

app = FastAPI()

engine = create_engine(os.getenv("DB_URI"))
metadata = MetaData()

products = Table('products', metadata,
    Column('product_id', String, primary_key=True),
    Column('asins', String),
    Column('brand', String),
    Column('categories', String),
    Column('dateAdded', String),
    Column('dateUpdated', String),
    Column('imageURLs', String),
    Column('keys', String),
    Column('manufacturer', String),
    Column('manufacturerNumber', String),
    Column('name', String),
    Column('primaryCategories', String),
    Column('sourceURLs', String),
    Column('weight', String)    
)

price = Table('price', metadata,
    Column('product_id', String, primary_key=True),
    Column('amountMax', String),
    Column('amountMin', String),
    Column('availability', String),
    Column('condition', String),
    Column('currency', String),
    Column('dateSeen', String),
    Column('isSale', String),
    Column('merchant', String),
    Column('shipping', String),
    Column('sourceURLs', String) 
)

@app.post("/create_files")
def create_file():
    df = pd.read_csv('https://query.data.world/s/b6r62f3bsjalbhxttweer2cqzszmbv')
    # construction du dataframe des prix de produits
    df_price = df[['id', 'prices.amountMax', 'prices.amountMin', 'prices.availability',
           'prices.condition', 'prices.currency', 'prices.dateSeen',
           'prices.isSale', 'prices.merchant', 'prices.shipping',
           'prices.sourceURLs']]
    #renommage de la colonne id en id_product
    df_price.rename(columns = {'id':'product_id','prices.amountMax':'amountMax','prices.amountMin':'amountMin','prices.availability':'availability',
                               'prices.condition':'condition','prices.currency':'currency','prices.dateSeen':'dateSeen','prices.isSale':'.isSale',
                               'prices.merchant':'merchant','prices.shipping':'shipping','prices.sourceURLs':'sourceURLs'}, inplace = True)
    # contruction du data frame des caractéristiques des produits
    df_product = df[['id', 'asins', 'brand', 'categories', 'dateAdded',
           'dateUpdated', 'imageURLs', 'keys', 'manufacturer',
           'manufacturerNumber', 'name', 'primaryCategories', 'sourceURLs','weight']]
    df_product.rename(columns = {'id':'product_id'}, inplace = True)
    # écriture des fichiers sources des bases de données
    df_price.to_csv('bdd_prix.csv', sep=";", index=False)
    df_product.to_csv('bdd_produits.csv', sep=";", index=False)
    return "Files created successfully"

@app.post("/create_schema")
def create_schema():
    metadata.create_all(engine)
    return {"message": "Schema created successfully"}

@app.post("/load_data")
def load_data():
    with open("username.csv") as f:
        next(f)
        conn = engine.connect()
        conn.execute(users.insert(), [{'product_id': row[0], 'asins': row[1]} for row in csv.reader(f)])
    return {"message": "Data loaded successfully"}

@app.get("/request_data")
def request_data():
    conn = engine.connect()
    result = conn.execute("SELECT * FROM users")
    return [{"product_id": row[0], "asins": row[1]} for row in result]

if __name__ == '__main__':
    app.run()
