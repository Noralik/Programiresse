class CoffeeMachine:
    def __init__(self, brand, water_limit):
        self.brand = brand
        self.water_level = 650
        self.water_limit = water_limit
    
    def add_water(self, amount):
        if self.water_level + amount <= self.water_limit:
            self.water_level += amount
            print("Water added successfully.")
            self.show_water_level()
        else:
            print("Water limit exceeded!")
    
    def serve_cup(self, size):
        if size in {300, 500, 750}:
            if self.water_level < size:
                print("Not enough water!")
            else:
                print(f"You chose a {'small' if size == 300 else 'medium' if size == 500 else 'large'} size ({size}ml).")
                self.water_level -= size
        else:
            print("Invalid choice!")
            self.serve_cup(int(input("How many milliliters? (300/500/750): ")))

    def show_water_level(self):
        print(f"Current water level: {self.water_level}ml")

    def order_coffee(self):
        self.serve_cup(int(input("How many milliliters? (300/500/750): ")))
        if input("Would you like to order another cup? (yes/no): ").lower() == "yes":
            self.order_coffee()
        else:
            print("Thank you for using our coffee machine.")

def main():
    default_water_amount = 650
    acc1 = CoffeeMachine("123456789", default_water_amount)
    acc1.add_water(default_water_amount)
    acc1.show_water_level()
    acc1.order_coffee()

if __name__ == "__main__":
    main()
