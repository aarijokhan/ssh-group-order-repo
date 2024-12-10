import uuid
import random
from datetime import datetime, timedelta
import psycopg2
import requests


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
        self.group_order = None

    def canAffordProduct(self, product):
        return self.wallet >= product.price

    def addToCart(self, product):
        if self.canAffordProduct(product):
            self.cart.append(product)
            return True
        else:
            print(
                f"Insufficient funds. {product.name} costs £{product.price:.2f}, "
                f"but you only have £{self.wallet:.2f} in your wallet."
            )
            return False

    def removeFromCart(self, product):
        self.cart.remove(product)

    def viewCart(self):
        if not self.cart:
            print("Your cart is empty.")
            return False

        print("\nYour Cart:")
        for i, product in enumerate(self.cart, 1):
            print(f"{i}. {product.name} - £{product.price:.2f}")
        return True

    def getCartTotal(self):
        return sum(product.price for product in self.cart)

    def checkout(self):
        cart_total = self.getCartTotal()

        if not self.group_order:
            print("Error: Not part of a group order.")
            return False

        individual_delivery_cost = self.group_order.DELIVERY_FEE / len(self.group_order.participants)
        total_cost = cart_total + individual_delivery_cost

        if self.wallet >= total_cost:
            self.wallet -= total_cost
            print(
                f"Checkout successful. Charged £{cart_total:.2f} + £{individual_delivery_cost:.2f} delivery. "
                f"Remaining wallet balance: £{self.wallet:.2f}"
            )
            self.cart.clear()

            # Save the group order to the database
            self.group_order.save_to_database()
            return True
        else:
            print(
                f"Insufficient funds. Total cost is £{total_cost:.2f}, "
                f"but you only have £{self.wallet:.2f} in your wallet."
            )
            return False


class GroupOrder:
    DELIVERY_FEE = 5.99

    def __init__(self):
        self.order_id = str(uuid.uuid4())
        self.participants = []
        self.start_time = datetime.now()

    def addParticipant(self, student):
            self.participants.append(student)
            student.group_order = self
            print(f"Student {student.name} joined the order.")

    def calcIndividualCost(self, student):
        individual_delivery_cost = self.DELIVERY_FEE / len(self.participants) if self.participants else 0
        return student.getCartTotal() + individual_delivery_cost

    def displayOrderSummary(self):
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

    def save_to_database(self):
        try:
            connection = psycopg2.connect(
                host='pg-2e6d194e-sepp-prototype.l.aivencloud.com',
                port=25749,
                database='ssh',
                user='avnadmin',
                password='AVNS_HTFha2EWahHmllf6fuj',
                sslmode='require'
            )

            with connection:
                with connection.cursor() as cursor:
                    # Insert group order details
                    cursor.execute(
                        """
                        INSERT INTO group_orders (id, start_time, delivery_fee)
                        VALUES (%s, %s, %s)
                        """,
                        (self.order_id, self.start_time, self.DELIVERY_FEE)
                    )

                    # Insert participants
                    for student in self.participants:
                        cart_total = student.getCartTotal()  # Ensure this is recalculated
                        delivery_cost = self.DELIVERY_FEE / len(self.participants)
                        total_cost = cart_total + delivery_cost

                        cursor.execute(
                            """
                            INSERT INTO group_order_participants (
                                group_order_id, student_id, student_name,
                                cart_total, delivery_cost, total_cost
                            )
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            (self.order_id, student.id, student.name,
                             cart_total, delivery_cost, total_cost)
                        )


        except (Exception, psycopg2.Error) as error:
            print(f"Error saving group order to the database: {error}")

        finally:
            if 'connection' in locals():
                connection.close()


def fetch_products_from_database():
    try:
        connection = psycopg2.connect(
            host='pg-2e6d194e-sepp-prototype.l.aivencloud.com',
            port=25749,
            database='ssh',
            user='avnadmin',
            password='AVNS_HTFha2EWahHmllf6fuj',
            sslmode='require'
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            products = [
                Product(
                    str(row[0]),
                    row[1],
                    float(row[2]),
                    row[3]
                ) for row in cursor.fetchall()
            ]

        return products

    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to PostgreSQL database: {error}")
        return []
    finally:
        if 'connection' in locals():
            connection.close()





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

        categories = display_categories(available_products)

        print("\n0. 🔙 Back to Main Menu")

        try:
            category_choice = int(input("\nEnter category number to browse (0 to go back): "))

            if category_choice == 0:
                return

            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]
                category_products = [p for p in available_products if p.category == selected_category]

                while True:

                    print(f"\n{selected_category.upper()} PRODUCTS:")
                    for i, product in enumerate(category_products, 1):
                        print(f"{i}. {product.name} - £{product.price:.2f}")

                    print("\n0. 🔙 Back to Categories")

                    try:
                        product_choice = input("Enter product number to add to cart (0 to go back): ")

                        product_choice = int(product_choice)

                        if product_choice == 0:
                            break


                        if 1 <= product_choice <= len(category_products):
                            selected_product = category_products[product_choice - 1]


                            actual_product = next(
                                (p for p in available_products if p.id == selected_product.id),
                                None
                            )

                            if actual_product:
                                if student.addToCart(actual_product):
                                    print(f"{actual_product.name} added to cart.")

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

    available_products = fetch_products_from_database()


    group_order = GroupOrder()

    available_products = fetch_products_from_database()
    group_order = GroupOrder()

    # Use valid UUIDs for student IDs
    student2 = Student(str(uuid.uuid4()), 'Aarij', 200)
    student3 = Student(str(uuid.uuid4()), 'Hasaan', 30)
    student4 = Student(str(uuid.uuid4()), 'Fizan', 10)

    joinOrd = input(f"Student ___ has started a group order: {group_order.order_id}, would you like to join? (y/n): ")

    if joinOrd.lower() == 'y':
        group_order.addParticipant(student2)
        group_order.addParticipant(student3)
        group_order.addParticipant(student4)

        student2.cart = random.sample(available_products, min(3, len(available_products)))
        student3.cart = random.sample(available_products, min(3, len(available_products)))
        student4.cart = random.sample(available_products, min(3, len(available_products)))

        student_name = input("Enter your name: ")
        student_wallet = 0
        student = Student(str(uuid.uuid4()), student_name, student_wallet)

        group_order.addParticipant(student)

        while True:
            print("\n" + "=" * 40)
            print(f"🛒 STUDENT MARKETPLACE MENU 🛒".center(40))
            print("=" * 40)
            print("\nOptions:")
            print("1. 📋 Browse Products by Category")
            print("2. 🧾 View Cart")
            print("3. ❌ Remove Item from Cart")
            print("4. 📊 View Order Summary")
            print("5. 💳 Checkout")
            print("6. 💰 View Wallet")
            print("7. ➕ Top up Wallet")
            print("8. 🚪 Exit")
            print("=" * 40)

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
                            topup = float(input("Enter the amount you would like to top up: "))
                            if topup > 0 and topup < 100000:
                                student.wallet += topup
                                print(f"Wallet Balance: £{student.wallet:.2f}")
                            else:
                                print("Invalid top-up amount. Please enter a positive value less than £100,000.")
                        except ValueError:
                            print("Please enter a valid number.")

                    case 8:
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
