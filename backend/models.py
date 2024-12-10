from datetime import datetime
from pydantic import BaseModel
from typing import List
from dataclasses import dataclass, field

class Products(BaseModel):
    productId: str
    nameOfProduct: str
    priceOfProduct: float
    foodType: str

class Student(BaseModel):
    studentId: str
    nameOfStudent: str
    amountInWallet: float
    studentCart: List[Products] = field(default_factory=list)
    groupOrderId: str = None

class GroupOrders(BaseModel):
    groupOrderId: str
    timeOfOrder: datetime = datetime.now()
    deliveryFee = float