class ProductDetail:
    def __init__(self, code, label, summary, cost):
        self.code = code
        self.label = label
        self.summary = summary
        self.cost = cost

    def __str__(self):
        return f"{self.code:<5} | {self.label:<20} | {self.summary:<30} | ₱{self.cost:.2f}"

class StockKeeper:
    def __init__(self):
        self.catalog = {}

    def register_product(self):
        try:
            product_code = int(input("Enter product code: "))
            if product_code in self.catalog:
                print("Product code already registered!")
                return

            product_name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            product_price = float(input("Enter product price: "))

            if product_price < 0:
                print("Price cannot be negative!")
                return

            self.catalog[product_code] = ProductDetail(product_code, product_name, product_description, product_price)
            print("Product registered successfully!")

        except ValueError:
            print("Invalid input. Please enter correct values.")

    def display_inventory(self):
        if not self.catalog:
            print("Inventory is empty.")
            return

        print("\n--- Current Inventory ---")
        print("Code  | Name                | Description               | Price")
        print("-" * 70)
        for product in self.catalog.values():
            print(product)

    def modify_product(self):
        try:
            product_code = int(input("Enter product code to modify: "))
            if product_code not in self.catalog:
                print("Product not found!")
                return

            new_name = input("Enter new name (press enter to keep current): ") or self.catalog[product_code].label
            new_description = input("Enter new description (press enter to keep current): ") or self.catalog[product_code].summary
            price_input = input("Enter new price (press enter to keep current): ")
            new_price = float(price_input) if price_input else self.catalog[product_code].cost

            if new_price < 0:
                print("Price cannot be negative!")
                return

            self.catalog[product_code] = ProductDetail(product_code, new_name, new_description, new_price)
            print("Product updated successfully!")

        except ValueError:
            print("Invalid input. Please enter correct values.")

    def remove_product(self):
        try:
            product_code = int(input("Enter product code to remove: "))
            if product_code not in self.catalog:
                print("Product not found!")
                return

            del self.catalog[product_code]
            print("Product removed successfully!")

        except ValueError:
            print("Invalid input. Please enter a valid product code.")

def launch_system():
    inventory = StockKeeper()

    while True:
        print("\n--- Product Management System ---")
        print("1. Register New Product")
        print("2. View Inventory")
        print("3. Modify Product")
        print("4. Remove Product")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            inventory.register_product()
        elif choice == '2':
            inventory.display_inventory()
        elif choice == '3':
            inventory.modify_product()
        elif choice == '4':
            inventory.remove_product()
        elif choice == '5':
            print("Closing system...")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    launch_system()