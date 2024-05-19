class Product:
    supermarket_name = "BIM Supermarket"
    
    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.expiration_date = expiration_date
        self.year = year

    def print_details(self):
        print("\nProduct Details:")
        print("Supermarket Name:", self.supermarket_name)
        print("Product ID:", self.__product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight)
        print("Expiration Date:", self.expiration_date)
        print("Year:", self.year)

    def change_product_id(self, new_product_id):
        self.__product_id = new_product_id


class Healthy(Product):
    
    def __init__(self, product_id, name, price, manufacturer, weight, expiration_date, year, components):
        super().__init__(product_id, name, price, manufacturer, weight, expiration_date, year)
        self.calories = 0
        self.components = components

    def add_calories(self, calories):
        self.calories += calories

    def print_details(self):
        super().print_details()
        print("Calories:", self.calories)
        print("Components:", self.components)

    def compute_total_calories(self):
        total_calories = self.calories * self.weight
        return total_calories


product = None
healthy_product = None


def product_subsystem():
    global product
    while True:
        print("\nProduct Sub-System:")
        print("1. Add new Product")
        print("2. Display Product Details")
        print("3. Change/Edit product ID")
        print("4. Exit the sub-system")
        print("5. Exit the Supermarket cashier system")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                product_id = input("Enter product ID: ")
                name = input("Enter name: ")
                price = float(input("Enter price: "))
                manufacturer = input("Enter manufacturer: ")
                weight = float(input("Enter weight: "))
                expiration_date = input("Enter expiration date: ")
                year = int(input("Enter year: "))

                product = Product(product_id, name, price, manufacturer, weight, expiration_date, year)
                print("Product added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == 2:
            if product:
                product.print_details()
            else:
                print("\nNo product added yet !")

        elif choice == 3:
            if product:
                new_product_id = input("Enter new product ID: ")
                product.change_product_id(new_product_id)
                print("Product ID changed successfully.")
            else:
                print("\nNo product added yet !")

        elif choice == 4:
            break

        elif choice == 5:
            exit()

        else:
            print("Invalid choice. Please try again.")

def healthy_subsystem():
    global healthy_product
    while True:
        print("\nHealthy Sub-System:")
        print("1. Add new Healthy Product")
        print("2. Display Healthy Product Details")
        print("3. Change/Edit calories (calories per gram)")
        print("4. Check calories and components of Healthy Product")
        print("5. Compute total calories of the Healthy Product based on weight")
        print("6. Exit the sub-system")
        print("7. Exit the Supermarket cashier system")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                product_id = input("Enter product ID: ")
                name = input("Enter name: ")
                price = float(input("Enter price: "))
                manufacturer = input("Enter manufacturer: ")
                weight = float(input("Enter weight: "))
                expiration_date = input("Enter expiration date: ")
                year = int(input("Enter year: "))
                components = input("Enter components (comma-separated): ").split(", ")

                healthy_product = Healthy(product_id, name, price, manufacturer, weight, expiration_date, year, components)
                print("Healthy Product added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == 2:
            if healthy_product:
                healthy_product.print_details()
            else:
                print("No healthy product added yet.")

        elif choice == 3:
            if healthy_product:
                try:
                    calories = int(input("Enter calories per gram: "))
                    healthy_product.add_calories(calories)
                    print("Calories updated successfully.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No healthy product added yet.")

        elif choice == 4:
            if healthy_product:
                print("Calories:", healthy_product.calories)
                print("Components:", healthy_product.components)
            else:
                print("No healthy product added yet.")

        elif choice == 5:
            if healthy_product:
                total_calories = healthy_product.compute_total_calories()
                print("Total Calories:", total_calories)
            else:
                print("No healthy product added yet.")

        elif choice == 6:
            break

        elif choice == 7:
            exit()

        else:
            print("Invalid choice. Please try again.")


def choose_system():
    while True:
        print('=============== BIM Market system ===============')
        print("Which sub-system do you want to use?")
        print("1) Product")
        print("2) Healthy Product")
        print("3) Exit supermarket system")
        
        try:
            choice = int(input("Please enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Enter a valid number.")
            continue
        
        if choice == 1:
            product_subsystem()
        elif choice == 2:
            healthy_subsystem()
        elif choice == 3:
            print("Exiting the supermarket system")
            print("Thanks for using our system")
            break
        else:
            print("Invalid choice. Please try again.")


choose_system()
