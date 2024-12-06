import uuid
import random
from datetime import datetime, timedelta


class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category