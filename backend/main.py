from fastapi import FastAPI
import psycopg2

app = FastAPI()

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


@app.get("/")
def root():
    return {"Hello":"There"}