# from http.client import HTTPException
from fastapi import FastAPI, HTTPException
import psycopg2
import os
import uuid
from datetime import datetime

app = FastAPI()


# Default Root
@app.get("/")
def root():
    return {"Hello": "There"}


from models import (
    Products, Student, GroupOrders
)

# Code to connect to the database from Generative AI
databasePassword = os.getenv('DATABASE_PASSWORD')


def retrieveDatabaseConnection():
    return psycopg2.connect(
        host='pg-2e6d194e-sepp-prototype.l.aivencloud.com',
        port=25749,
        database='ssh',
        user='avnadmin',
        password='AVNS_6TcZ6F1yK_cHP93dRi7',
        sslmode='require'
    )


def fetchingProductsFromDatabase():
    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as pointer:
            pointer.execute("SELECT * FROM products")
            return [
                Products(id=str(row[0]), name=row[1], price=float(row[2]), category=row[3]) for row in
                pointer.fetchall()
            ]
    except Exception as e:
        print(f"{e}")
        return []
    finally:
        if 'connection' in locals():
            connection.close()


def fetchingGroupOrders(groupOrderId: str):
    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as pointer:
            pointer.execute("SELECT * FROM group_orders WHERE id = %s", (groupOrderId,))
            row = pointer.fetchone()
            if row:
                return GroupOrders(
                    order_id=str(row[0]),
                    start_time=row[1],
                    delivery_fee=5.99
                )
            return None
    except Exception as e:
        print(f"{e}")
        return None
    finally:
        if 'connection' in locals():
            connection.close()


def fetchingGroupOrderParticipants(groupOrderId: str):
    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as pointer:
            pointer.execute("SELECT * FROM group_order_participants WHERE group_order_id = %s", (groupOrderId,))
        return [
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
        if 'connection' in locals():
            connection.close()


@app.get("/products")
async def getProducts():
    return fetchingProductsFromDatabase()


studentsBeingAdded = {}


# @app.post("/students")
# async def createAStudent(name: str, amountInWallet: float):
#     id_student = str(uuid.uuid4())
#     studentsBeingAdded[id_student] = Student(studentId=id_student, name=name, wallet=amountInWallet)
#     return studentsBeingAdded[id_student]
@app.post("/students")
async def createAStudent(name: str, amountInWallet: float):
    id_student = str(uuid.uuid4())
    studentsBeingAdded[id_student] = Student(
        id=id_student,  # Note the 'id', not 'studentId'
        name=name,
        wallet=amountInWallet
    )
    return studentsBeingAdded[id_student]

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


@app.post("/group_orders/")
async def createTheGroupOrder():
    order_id = str(uuid.uuid4())

    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO group_orders(id, start_time, delivery_fee) VALUES (%s, %s, %s)",
                (order_id, datetime.now(), 5.99)
            )

            indexOfStudent = 0
            while indexOfStudent < len(SAMPLE_STUDENTS):
                studentsToInsert = SAMPLE_STUDENTS[indexOfStudent]
                totalOfCart = sum(product['price'] for product in studentsToInsert['cart'])
                indexOfStudent = indexOfStudent + 1

                cursor.execute("""
                                INSERT INTO group_order_participants
                                (group_order_id, student_id, student_name, cart_total, delivery_cost, total_cost)
                                VALUES(%s, %s, %s, %s, %s, %s)
                               """,
                               (order_id, studentsToInsert['id'], studentsToInsert['name'], totalOfCart, 1.5,
                                totalOfCart + 1.5)
                               )
                studentsBeingAdded[studentsToInsert['id']] = Student(
                    id=studentsToInsert['id'],
                    name=studentsToInsert['name'],
                    wallet=studentsToInsert['wallet'],
                    cart=[Products(**product) for product in studentsToInsert['cart']],
                    group_order_id=order_id
                )
                connection.commit()
            return {
                "order_id": order_id,
                "start_time": datetime.now(),
                "delivery_fee": 5.99,
                "predefined_students": [
                    {
                        "id": s['id'],
                        "name": s['name'],
                        "wallet": s['wallet'],
                        "cart_total": sum(p['price'] for p in s['cart'])
                    } for s in SAMPLE_STUDENTS
                ]
            }
    except Exception as e:
        print(f"{e}")


@app.get("/students/{student_id}")
async def getStudents(id_student: str):
    try:
        chosen_student = studentsBeingAdded.get(id_student)
        return chosen_student
    except Exception as e:
        print(f"{e}")


def isStudentAlreadyInGroup(order_id: str, id_student: str) -> None:
    participants_of_group = fetchingGroupOrderParticipants(order_id)

    for participant in participants_of_group:
        if participant['student_id'] == id_student:
            raise HTTPException(status_code=400, detail="Student is already in the group!")


def doesStudentExist(id_student: str) -> dict:
    try:
        student = studentsBeingAdded.get(id_student)
        return student
    except Exception as e:
        print("{e}")
        raise HTTPException(status_code=400, detail="Student has not been found!")


@app.post("/group_orders/{order_id}/join/")
async def joinTheGroupOrder(order_id: str, id_student: str):
    group_order = fetchingGroupOrders(order_id)

    if not group_order:
        raise HTTPException(status_code=404, detail="No group order with this id found!")

    student_joining_group = doesStudentExist(id_student)

    isStudentAlreadyInGroup(order_id, id_student)

    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as pointer:
            pointer.execute(
                """
                INSERT INTO group_order_participants (
                    group_order_id, student_id, student_name,
                    cart_total, delivery_cost, total_cost
                ) VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    order_id,
                    id_student,
                    student_joining_group.name,
                    0,
                    0,
                    0
                )
            )
            student_joining_group.group_order_id = order_id

            connection.commit()

            return {
                "order_id": order_id,
                "student_id": id_student,
                "message": "Group order has been joined successfully"
            }
    except Exception as e:
        print(f"{e}")

    finally:
        if connection:
            connection.close()

@app.post("/students/{student_id}/cart/")
async def addingToTheCart(id_student: str, product_id: str):
    student_registered = studentsBeingAdded.get(id_student)

    if not student_registered:
        raise HTTPException(status_code=404, detail="Student not found")
    
    products = fetchingProductsFromDatabase()
    product_corpus = None
    for product in products:
        if product.id == product_id:
            product_corpus = product
            break
    
    if not product_corpus:
        raise HTTPException(status_code=404, detail="Product not found")
    
    initial_cart_total = 0
    for product in student_registered.cart:
        initial_cart_total += product.price
    student_registered.cart.append(product_corpus)

    cart_total = initial_cart_total

    try:
        connection = retrieveDatabaseConnection()
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE group_order_participants SET cart_total = %s WHERE student_id = %s AND group_order_id = %s",
                (cart_total + product_corpus.price, id_student, student_registered.group_order_id)
            )
            connection.commit()
        return student_registered.cart
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error adding to cart")

