import uuid
import random
from datetime import datetime, timedelta


class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
class Student:
    def __init__(self, id, name, wallet):
        self.id = id
        self.name = name
        self.cart = []
        self.wallet = wallet
        self.group_order = None  # Track the group order the student is in

    def canAffordProduct(self, product):
        """Check if student has enough money to buy a product"""
        return self.wallet >= product.price

    def addToCart(self, product):
        """Add a product to the student's cart if affordable"""
        if self.canAffordProduct(product):
            self.cart.append(product)
            return True
        else:
            print(f"Insufficient funds. {product.name} costs £{product.price:.2f}, but you only have £{self.wallet:.2f} in your wallet.")
            return False

    def removeFromCart(self, product):
        """Remove a product from the student's cart"""
        self.cart.remove(product)

    def viewCart(self):
        """View items in the cart with their index"""
        if not self.cart:
            print("Your cart is empty.")
            return False
        
        print("\nYour Cart:")
        for i, product in enumerate(self.cart, 1):
            print(f"{i}. {product.name} - £{product.price:.2f}")
        return True

    def getCartTotal(self):
        """Calculate the total cost of items in the cart"""
        return sum(product.price for product in self.cart)
    
    def checkout(self):
        """Process checkout, deducting cart total plus individual delivery fee from wallet"""
        cart_total = self.getCartTotal()
        
        # Ensure the student is part of a group order
        if not self.group_order:
            print("Error: Not part of a group order.")
            return False
        
        # Calculate individual delivery cost
        individual_delivery_cost = self.group_order.DELIVERY_FEE / len(self.group_order.participants)
        total_cost = cart_total + individual_delivery_cost
        
        if self.wallet >= total_cost:
            self.wallet -= total_cost
            print(f"Checkout successful. Charged £{cart_total:.2f} + £{individual_delivery_cost:.2f} delivery. Remaining wallet balance: £{self.wallet:.2f}")
            self.cart.clear()
            return True
        else:
            print(f"Insufficient funds. Total cost is £{total_cost:.2f}, but you only have £{self.wallet:.2f} in your wallet.")
            return False
        
class GroupOrder:
    DELIVERY_FEE = 5.99

    def __init__(self):
        self.order_id = str(uuid.uuid4())
        self.participants = []
        self.start_time = datetime.now()

    def addParticipant(self, student):
        """Add a student to the group order within 4-hour window"""
        time_elapsed = datetime.now() - self.start_time
        if time_elapsed <= timedelta(hours=4):
            self.participants.append(student)
            student.group_order = self  # Link the student to this group order
            print(f"Student {student.name} joined the order.")
        else:
            print("Cannot join order: 4-hour time limit exceeded.")

    def calcIndividualCost(self, student):
        """Calculate the individual cost including shared delivery fee"""
        # Only charge delivery fee if there are participants
        individual_delivery_cost = self.DELIVERY_FEE / len(self.participants) if self.participants else 0
        return student.getCartTotal() + individual_delivery_cost

    def displayOrderSummary(self):
        """Display a comprehensive summary of the group order"""
        print("\n=== Order Summary ===")
        print(f"Order ID: {self.order_id}")
        print(f"Number of participants: {len(self.participants)}")

        for student in self.participants:
            print(f"\nStudent: {student.name}")
            print("Items in cart:")
            for product in student.cart:
                print(f"- {product.name}: £{product.price:.2f}")
            
            individual_total = self.calcIndividualCost(student)
            print(f"Individual total (including delivery): £{individual_total:.2f}")

        total_order_cost = sum(self.calcIndividualCost(student) for student in self.participants)
        print(f"\nTotal Order Cost: £{total_order_cost:.2f}")