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

class GroupOrders(BaseModel):
    groupOrderId: str
    participantsOfOrder: List[str] = field(default_factory=list)
    timeOfOrder: datetime = datetime.now()