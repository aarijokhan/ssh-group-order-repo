from fastapi import FastAPI
import psycopg2
import os
import uuid

app = FastAPI()

# Default Root 
@app.get("/")
def root():
    return {"Hello":"There"}

from models import (
    Products, Student, GroupOrders
)
# Code to connect to the database from Generative AI
databasePassword = os.getenv('DATABASE_PASSWORD')

def retrieveDatabaseConnection():
    return psycopg2.connect(
        host = databasePassword,
        port=25749,
        database='ssh',
        user='avnadmin',
        password= 'AVNS_6TcZ6F1yK_cHP93dRi7' ,
        sslmode='require' 
    )

def fetchingProductsFromDatabase():
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

def fetchingGroupOrders(groupOrderId: str):
    try:
        isConnecting = retrieveDatabaseConnection()
        with isConnecting.cursor() as pointer:
            pointer.execute("SELECT * FROM group_orders WHERE group_order_id = %s", (groupOrderId,))
            row = pointer.fetchone()
            if row: 
                return GroupOrders(
                    order_id = str(row[0]),
                    start_time = row[1],
                    delivery_fee = 5.99
                )
            return None
    except Exception as e:
        print(f"{e}")
        return None
    finally:
        if 'connection' in locals():
            isConnecting.close()

def fetchingGroupOrderParticipants(groupOrderId: str):
    try:
        isConnecting = retrieveDatabaseConnection()
        with isConnecting.cursor() as pointer:
            pointer.execute("SELECT * FROM group_order_participants WHERE group_order_id = %s", (groupOrderId,))
        return[
            {
                "studentId": row[1],
                "studentName": row[2],
                "cart_total": row[3],
                "delivery_cost": row[4]
            }
            for row in pointer.fetchall()
        ]
    except Exception as e:
        print(f"{e}")
        return []
    finally:
        if 'connection' in locals:
            isConnecting.close()

@app.get("/products")
async def getProducts():
    return fetchingProductsFromDatabase()

studentsBeingAdded ={}

@app.post("/students")
async def createAStudent(name:str, amountInWallet: float):
    idOfStudent = str(uuid.uuid4())
    studentsBeingAdded[idOfStudent] = Student(studentId = idOfStudent, nameOfStudent = name, amountInWallet = amountInWallet)
    return studentsBeingAdded[idOfStudent]

SAMPLE_STUDENTS = [
    {
        'id': str(uuid.uuid4()),
        'name': 'Aarij',
        'wallet': 100.00,
        'cart': [
            {'id': '1', 'name': 'Chicken', 'price': 8.99, 'category': 'Meat'},
            {'id': '5', 'name': 'Tomato', 'price': 1.99, 'category': 'Vegetables'},
            {'id': '6', 'name': 'Milk', 'price': 3.49, 'category': 'Dairy'},
            {'id': '7', 'name': 'Cookies', 'price': 3.49, 'category': 'Snacks'},
            {'id': '8', 'name': 'Water', 'price': 1.49, 'category': 'Beverages'}
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Saad',
        'wallet': 75.50,
        'cart': [
            {'id': '2', 'name': 'Beef', 'price': 12.49, 'category': 'Meat'},
            {'id': '9', 'name': 'Cheese', 'price': 4.99, 'category': 'Dairy'},
            {'id': '10', 'name': 'Potato Chips', 'price': 2.99, 'category': 'Snacks'},
            {'id': '11', 'name': 'Tea', 'price': 2.49, 'category': 'Beverages'},
            {'id': '12', 'name': 'Peach', 'price': 1.29, 'category': 'Fruits'}
        ]
    },
    {
        'id': str(uuid.uuid4()),
        'name': 'Hasaan',
        'wallet': 50.25,
        'cart': [
            {'id': '3', 'name': 'Lamb', 'price': 9.99, 'category': 'Meat'},
            {'id': '13', 'name': 'Yogurt', 'price': 2.99, 'category': 'Dairy'},
            {'id': '14', 'name': 'Brownie', 'price': 4.49, 'category': 'Snacks'},
            {'id': '15', 'name': 'Pineapple Juice', 'price': 2.49, 'category': 'Beverages'},
            {'id': '16', 'name': 'Banana', 'price': 0.59, 'category': 'Fruits'}
        ]
    }
]
    

