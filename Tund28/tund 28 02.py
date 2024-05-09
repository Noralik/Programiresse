class Aircraft:
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        
    def take_off(self):
        if self.fuel_level < 50:
            print(f"{self.model} - Insufficient fuel for take-off")
            return False
        print(f"{self.model} - We've consumed fuel and took off")
        return True

    def land(self):
        print(f"{self.model} - We've successfully landed")
    
    def fly(self, hours):
        if self.take_off():
            print(f"{self.model} - Flying for {hours} hours")
            self.consume_fuel(hours)  # Pass the flight duration to consume_fuel
            
    def consume_fuel(self, hours=None):
        pass  # Placeholder method, can be overridden in subclasses



class PassengerAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)
        self.number_of_passengers = number_of_passengers

    def fly(self, hours):
        if self.take_off():
            print(f"{self.model} - Flying for {hours} hours")
            self.consume_fuel(hours)  # Pass the flight duration to consume_fuel

    def consume_fuel(self, hours):
        fuel_consumed = 5 * hours  # Adjust fuel consumption based on flight duration
        if self.fuel_level < fuel_consumed:
            print(f"{self.model} - Insufficient fuel for {hours} hours of flight")
            self.land()
        else:
            self.fuel_level -= fuel_consumed
            print(f"{self.model} - Fuel consumed for {hours} hours of flight. Remaining fuel: {self.fuel_level}")
            self.land()

class CargoAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)
        self.cargo_weight = cargo_weight

    def fly(self, hours):
        if self.take_off():
            print(f"{self.model} - Flying for {hours} hours with cargo")
            self.consume_fuel(hours)  # Передаем количество часов полета

    def consume_fuel(self, hours):
        fuel_consumed = 5 * hours  # Изменяем расход топлива в зависимости от количества часов
        if self.fuel_level < fuel_consumed:
            print(f"{self.model} - Insufficient fuel for {hours} hours of flight")
            self.land()
        else:
            self.fuel_level -= fuel_consumed
            print(f"{self.model} - Fuel consumed for {hours} hours of flight. Remaining fuel: {self.fuel_level}")
            self.land()


class MilitaryAircraft(Aircraft):
    ALLOWED_WEAPON_TYPES = ["õhk-õhk", "õhk-maa", "antiradar", "luure"]

    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)
        if armament_type not in self.ALLOWED_WEAPON_TYPES:
            raise ValueError(f"Invalid armament type for {model}: {armament_type}")
        self.armament_type = armament_type

    def take_off(self):
        if self.fuel_level < 100:  # Assuming military aircraft consume 100 fuel units for take-off
            print(f"{self.model} - Insufficient fuel for take-off")
            return False
        print(f"{self.model} - Military aircraft took off")
        self.consume_fuel(100)  # Consume 100 fuel units for take-off
        return True

    def land(self):
        print(f"{self.model} - Military aircraft landed")

    

# Testing the code
aircraft = Aircraft("Airplane", 300, 10000)
aircraft.take_off()
aircraft.land()

print()

passenger_aircraft = PassengerAircraft("airbaltic", 878, 750, 238)
passenger_aircraft.fly(7)

print()

cargo_aircraft = CargoAircraft("CargoAircraft", 30100, 7500, 712)
cargo_aircraft.fly(15)

print()

def check_weapon_type(armament_type):
    if armament_type not in MilitaryAircraft.ALLOWED_WEAPON_TYPES:
        raise ValueError(f"Invalid armament type: {armament_type}. Allowed types are: {', '.join(MilitaryAircraft.ALLOWED_WEAPON_TYPES)}")

# Creating MilitaryAircraft object, checking weapon type
armament_type = "Missiles"
if armament_type in MilitaryAircraft.ALLOWED_WEAPON_TYPES:
    military_aircraft = MilitaryAircraft("MilitaryAircraft", 500, 8000, armament_type)
    military_aircraft.take_off()
    military_aircraft.land()
else:
    print(f"Invalid armament type: {armament_type}. Allowed types are: {', '.join(MilitaryAircraft.ALLOWED_WEAPON_TYPES)}")

military_aircraft2 = MilitaryAircraft("MilitaryAircraft", 500, 8000, "õhk-õhk")
military_aircraft2.take_off()
military_aircraft2.land()
