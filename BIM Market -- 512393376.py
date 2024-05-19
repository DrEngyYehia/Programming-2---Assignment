class product:
    supermarket_name = "BIM Market"
    
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year):
        self.__product_ID = product_ID
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.weight = weight
        self.exp_date = expiration_date
        self.year = year

    def product_detail(self):
        print("\n========! Product Details !========")
        print("Supermarket Name:", self.supermarket_name)
        print("Product ID:", self.__product_ID)
        print("Name:", self.name)
        print("Price", self.price)
        print("Manufacturer:", self.manufacturer)
        print("Weight:", self.weight, "grams")
        print("Expiration Date:", self.exp_date)
        print("Year:", self.year)

    def set_product_id(self, product_ID):
        self.__product_ID = product_ID
        
    def transaction(self):
        print("\n please choose an option from 1 or 2 or 3 or 4:\n")
        print("1:) Add a new Product")
        print("2:) Display Product Details")
        print("3:) Change/Edit product_ID")
        print("4:) Exit the sub-system")
        print("5:) Exit the Supermarket cashier system")
        while True:
            try:
                option = int(input("Enter 1, 2, 3, or 4\n"))
            except:
                print("Error: choose from 1, 2, 3 or 4 only")
                continue
            else:
                if option == 1:
                    product_ID = int(input("Enter the new product ID: "))
                    name = input("Enter the new product name: ")
                    price = float(input("Enter the new product price: "))
                    manufacturer = input("Enter the manufacturer: ")
                    weight = float(input("Enter the product weight in (grams): "))
                    expiration_date = input("Enter the expiration date: ")
                    year = int(input("Enter production year: "))
                    newproduct = product(product_ID, name, price, manufacturer, weight, expiration_date, year)
                    print("Product added successfully!")
                    print("\n please choose an option from 1 or 2 or 3 or 4:")
                    print("1:) Add a new Product")
                    print("2:) Display Product Details")
                    print("3:) Change/Edit product_ID")
                    print("4:) Exit the sub-system")
                    print("5:) Exit the Supermarket cashier system")
                elif option == 2:
                    self.product_detail()
                elif option == 3:
                    product_ID = int(input("Enter product ID: "))
                    self.change_product_id(product_ID)
                elif option == 4:
                    print(" Exiting the sub system ")
                    break
                elif option == 5:
                    print(" Exiting the Supermarket cashier system ")
                    break
                else:
                    print("invalid number")
                    continue


class Healthy(product):
    def __init__(self, product_ID, name, price, manufacturer, weight, expiration_date, year, components, calories=0):
        self.calories = calories
        self.comp = components
        super().__init__(product_ID, name, price, manufacturer, weight, expiration_date, year)

    def Healthy_product_detail(self):
        super().product_detail()
        print("calories:", self.calories)
        print("components:", self.comp)

    def set_calories(self, calories):
        self.calories = calories

    def compute_total_calories(self):
        total_calories = self.calories * self.weight
        return total_calories

    def check_calories_components(self):
        print(" the total calories:" ,self.compute_total_calories() )
        print(f" the components of the product: {self.comp}")

    def trans(self):
        print("\n please choose an option:\n")
        print("1) Add a new Healthy Product")
        print("2) Display Healthy Product Details")
        print("3) Change/Edit calories (By 1 gram)")
        print("4) Check the calories and the components")
        print("5) compute total calories of the healthy product")
        print("6) Exit the sub-system")
        while True:
            try:
                choice = int(input("enter 1, 2, 3, 4, 5, or 6\n"))
            except:
                print("error: choose from 1, 2, 3, 4, 5 or 6 only")
                continue
            else:
                if choice == 1:
                    product_ID = int(input("Enter Healthy product ID: "))
                    name = input("Enter Healthy product name: ")
                    price = float(input("Enter Healthy product price: "))
                    manufacturer = input("Enter manufacturer: ")
                    weight = float(input("Enter Healthy product weight (grams): "))
                    expiration_date = input("Enter expiration date: ")
                    year = int(input("Enter production year: "))
                    new_healthy_product = Healthy(product_ID, name, price, manufacturer, weight, expiration_date, year)
                    component1 = input("enter the first component ")
                    component2 = input("enter the second component ")
                    component3 = input("enter the third component ")
                    component4 = input("enter the fourth component ")
                    components = [component1, component2, component3, component4]
                    new_healthy_product.comp = components
                    print(" New Healthy Product added successfully!")
                elif choice == 2: 
                    self.Healthy_product_detail()
                elif choice == 3:
                    calories = int(input("Enter product calories: "))
                    self.set_calories(calories)
                elif choice == 4:
                    self.check_calories_components()
                elif choice == 5:
                    print(self.compute_total_calories())                            
                elif choice == 6:
                    print("Exiting the subsystem")
                    break
                else:
                    print("Invalid number.")
                    continue

product_1 = product(512393376, "Farfalle Pasta", 110, "Agnesi Italy", 500, 2025, 2021)
product_2 = Healthy(323242323, "granola", 200, "kellogs", 400, 2023, 2021, "oats, honey, proteins")

def choose_system():
    print('=============== BIM Market system==============')
    print("which sub-system do you wanna use?")
    print("1:) Product")
    print("2:) Healthy Product")
    print("3:) Exit supermarket system")
    while True:
        try:
            choice_1 = int(input(" please enter your choice from 1 or 2 or 3:\n "))
        except:
            print("enter a valid number")
        else:
            if choice_1 == 1:
                product_1.transaction()
            elif choice_1 == 2:
                product_2.trans()   
            elif choice_1 == 3:
                print(" Exiting the supermarket system ")
                print(" Thanks for using our system ")
                break

choose_system()