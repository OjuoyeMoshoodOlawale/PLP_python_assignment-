

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        for item in self.cart:
            print(f"{item.name} - ${item.price} x {item.quantity}")

    def checkout(self):
        total = sum(item.calculate_total_price() for item in self.cart)
        print(f"Total amount to pay: ${total}")


# Main Program
product1 = Product("Laptop", 1200, 1)
product2 = Product("Phone", 600, 2)

customer = Customer("Alice", "alice@example.com")
customer.add_to_cart(product1)
customer.add_to_cart(product2)

customer.view_cart()
customer.checkout()
# OOP Assignment - Basic Structure

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        for item in self.cart:
            print(f"{item.name} - ${item.price} x {item.quantity}")

    def checkout(self):
        total = sum(item.calculate_total_price() for item in self.cart)
        print(f"Total amount to pay: ${total}")


# Main Program
product1 = Product("Laptop", 1200, 1)
product2 = Product("Phone", 600, 2)

customer = Customer("Alice", "alice@example.com")
customer.add_to_cart(product1)
customer.add_to_cart(product2)

customer.view_cart()
customer.checkout()
