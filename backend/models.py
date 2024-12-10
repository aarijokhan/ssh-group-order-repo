from datetime import datetime
from pydantic import BaseModel
from typing import List
from dataclasses import dataclass, field

class Products(BaseModel):
    id: str
    name: str
    price: float
    category: str

class Student(BaseModel):
    id: str
    name: str
    wallet: float
    cart: List[Products] = field(default_factory=list)
    group_order_id: str = None

class GroupOrders(BaseModel):
    order_id: str
    start_time: datetime = datetime.now()
    delivery_fee : float