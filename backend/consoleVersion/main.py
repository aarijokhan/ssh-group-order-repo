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
    
class MarketplaceAPI:
    def __init__(self, base_url='https://api.restful-api.dev/grocery'):
        self.base_url = base_url

    def fetchProducts(self):
        """Fetch products from the marketplace API"""
        products = [
            Product('1', 'Milk', 1.99, 'Dairy'),
            Product('2', 'Bread', 1.50, 'Bakery'),
            Product('3', 'Bananas', 2.99, 'Fruits'),
            Product('4', 'Eggs', 3.49, 'Dairy'),
            Product('5', 'Cheese', 4.50, 'Dairy'),
            Product('6', 'Apples', 2.50, 'Fruits'),
            Product('7', 'Chicken', 5.99, 'Meat'),
            Product('8', 'Chocolate', 3.99, 'Sweets'),
            Product('9', 'Carrots', 1.29, 'Vegetables'),
            Product('10', 'Potatoes', 0.99, 'Vegetables'),
            Product('11', 'Orange Juice', 2.99, 'Beverages'),
            Product('12', 'Yogurt', 1.75, 'Dairy'),
            Product('13', 'Pasta', 1.89, 'Pantry'),
            Product('14', 'Tomato Sauce', 2.49, 'Pantry'),
            Product('15', 'Beef', 6.99, 'Meat'),
            Product('16', 'Salmon', 8.99, 'Meat'),
            Product('17', 'Cookies', 3.49, 'Sweets'),
            Product('18', 'Watermelon', 4.99, 'Fruits'),
            Product('19', 'Butter', 2.79, 'Dairy'),
            Product('20', 'Cereal', 3.99, 'Pantry'),
            Product('21', 'Lettuce', 1.49, 'Vegetables'),
            Product('22', 'Coca-Cola', 1.99, 'Beverages'),
            Product('23', 'Tea Bags', 2.89, 'Beverages'),
            Product('24', 'Ice Cream', 4.99, 'Frozen'),
            Product('25', 'Pizza', 6.49, 'Frozen'),
            Product('26', 'Shrimp', 7.99, 'Meat'),
            Product('27', 'Onions', 1.19, 'Vegetables'),
            Product('28', 'Grapes', 3.29, 'Fruits'),
            Product('29', 'Peanut Butter', 3.99, 'Pantry'),
            Product('30', 'Honey', 4.49, 'Pantry')
        ]
        return products

def display_categories(products):
    """Display available product categories"""
    # Extract unique categories
    categories = sorted(set(product.category for product in products))

    print("\n" + "=" * 40)
    print("🛍️ PRODUCT CATEGORIES 🛍️".center(40))
    print("=" * 40)

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    return categories

def browse_and_select_products(student, available_products):
    """Enhanced category-based product browsing and selection"""
    while True:
        # Display categories
        categories = display_categories(available_products)
        
        # Add an exit option
        print("\n0. 🔙 Back to Main Menu")

        try:
            # Get category selection
            category_choice = int(input("\nEnter category number to browse (0 to go back): "))
            
            # Exit option
            if category_choice == 0:
                return

            # Validate category selection
            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]
                category_products = [p for p in available_products if p.category == selected_category]

                while True:
                    # Display products in the selected category
                    print(f"\n{selected_category.upper()} PRODUCTS:")
                    for i, product in enumerate(category_products, 1):
                        print(f"{i}. {product.name} - £{product.price:.2f}")
                    
                    # Add navigation options
                    print("\n0. 🔙 Back to Categories")

                    try:
                        product_choice = input("Enter product number to add to cart (0 to go back): ")
                        
                        # Convert to integer
                        product_choice = int(product_choice)

                        # Go back to categories
                        if product_choice == 0:
                            break

                        # Validate product selection
                        if 1 <= product_choice <= len(category_products):
                            selected_product = category_products[product_choice - 1]
                            
                            # Find the actual product in available_products
                            actual_product = next(
                                (p for p in available_products if p.id == selected_product.id), 
                                None
                            )
                            
                            if actual_product:
                                if student.addToCart(actual_product):
                                    print(f"{actual_product.name} added to cart.")
                                
                                # Ask if user wants to continue shopping or go back
                                continue_shopping = input("Add another item? (y/n): ").lower()
                                if continue_shopping != 'y':
                                    break
                            else:
                                print("Product not found.")
                        else:
                            print("Invalid product number.")
                    
                    except ValueError:
                        print("Please enter a valid number.")

            else:
                print("Invalid category number.")

        except ValueError:
            print("Please enter a valid number.")

def main():
    # [Previous main function code remains the same until the menu section]
    # Copy all the previous code before the menu display...
    # Initialize marketplace
    
    marketplace = MarketplaceAPI()
    available_products = marketplace.fetchProducts()

    # Create a group order
    group_order = GroupOrder()
    student2 = Student('2', 'Aarij', 200)
    student3 = Student('3', 'Hasaan', 30)
    student4 = Student('4', 'Fizan', 10)

    
    joinOrd = input(f"Student ___ has created a group order: {group_order.order_id} , would you like to join? (press y to join, n to not join.) ")    
    
    if joinOrd == 'y' or joinOrd == 'Y':

        print("You have joined the order!")

      

        # Add student to order
        group_order.addParticipant(student2)
        group_order.addParticipant(student3)
        group_order.addParticipant(student4)

   
    

        student2.cart = random.sample(available_products, min(3, len(available_products)))
        student3.cart = random.sample(available_products, min(3, len(available_products)))
        student4.cart = random.sample(available_products, min(3, len(available_products)))
    

        # Input for student
        student_name = input("Enter student name: ")
        student_id = str(uuid.uuid4())  # Generate a unique ID
        student_wallet = 0
        student = Student(student_id, student_name, student_wallet)

        group_order.addParticipant(student)

        while True:
            # Enhanced menu display
            print("\n" + "=" * 40)
            print(f"🛒 STUDENT MARKETPLACE MENU 🛒".center(40))
            print("=" * 40)
            print("\nOptions:")
            print("1. 📋 Browse Products by Category")  # Changed from "View Available Products"
            print("2. 🧾 View Cart")
            print("3. ❌ Remove Item from Cart")
            print("4. 📊 View Order Summary")
            print("5. 💳 Checkout")
            print("6. 💰 View Wallet")
            print("7. ➕ Top up Wallet")
            print("8. 🚪 Exit")
            print("=" * 40)

            # Get user choice
            try:
                choice = int(input("\nEnter your choice (1-8): "))

                match choice:
                    case 1:
                        # Browse and select products by category
                        browse_and_select_products(student, available_products)

                    case 2:
                        # View cart
                        student.viewCart()

                    case 3:
                        # Remove item from cart
                        if student.viewCart():
                            try:
                                remove_choice = input("Enter the number of the item to remove: ")
                                remove_index = int(remove_choice) - 1
                        
                                if 0 <= remove_index < len(student.cart):
                                    removed_product = student.cart[remove_index]
                                    student.removeFromCart(removed_product)
                                    print(f"{removed_product.name} removed from cart.")
                                else:
                                    print("Invalid item number.")
                    
                            except ValueError:
                                print("Please enter a valid number.")
                    
                    case 4:
                        group_order.displayOrderSummary()

                    case 5:
                        # Checkout
                        student.checkout()

                    case 6:
                        # View wallet
                        print(f"Wallet Balance: £{student.wallet:.2f}")

                    case 7:
                        # Top up wallet
                        try:
                            topup = float(input("Enter the amount you would like to top up £: "))
                            if topup > 0 and topup < 100000:
                                student.wallet += topup
                                print(f"Wallet Balance: £{student.wallet:.2f}")
                            else:
                                print("Invalid top-up amount. Please enter a positive value less than £100,000.")
                        except ValueError:
                            print("Please enter a valid number.")

                    case 8:
                        # Exit the program
                        print("\n" + "=" * 40)
                        print("Thank you for using the marketplace!".center(40))
                        print("Goodbye! 👋".center(40))
                        print("=" * 40)
                        break

            except Exception as e:
                print(f"An error occurred: {e}")
    
    elif joinOrd == 'n' or joinOrd == 'N':
        print("Goodbye!")


    

if __name__ == "__main__":
    main()