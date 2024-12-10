from fastapi import FastAPI
import psycopg2

app = FastAPI()

from models import (
    Products, Student, GroupOrders
)
# Code to connect to the database from Generative AI
def retrieveDatabaseConnection():
    return psycopg2.connect(
        host ='pg-2e6d194e-sepp-prototype.l.aivencloud.com',
        port=25749,
        database='ssh',
        user='avnadmin',
        password='AVNS_HTFha2EWahHmllf6fuj',
        sslmode='require' 
    )

def fetchingProductsFromDatabse():
    try:
        isConnecting = retrieveDatabaseConnection()
        with isConnecting.cursor() as pointer:
            pointer.execute("SELECT * FROM products")
            return [
                Products(id = str(row[0]), name = row[1], price = float(row[2]), category = row[3]) for row in pointer.fetchall()
            ]
    except Exception as e:
        print(f"{e}")
        return []
    finally:
        if 'connection' in locals():
            isConnecting.close()

          
        


@app.get("/")
def root():
    return {"Hello":"There"}