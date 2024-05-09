class Aircraft:
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        
    def take_off(self):
        print(f"{self.model} - We've consumed fuel and took off")
        self.consume_fuel()

    def land(self):
        print(f"{self.model} - We've successfully landed")
    
    def consume_fuel(self):
        fuel_consumed = 50  # Amount of fuel consumed
        if self.fuel_level >= fuel_consumed:
            self.fuel_level -= fuel_consumed
            print(f"{self.model} - Fuel consumed. Remaining fuel: {self.fuel_level}")
        else:
            print(f"{self.model} - Insufficient fuel for the flight")

#------------------------------------------------------------------------#
class PassengerAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)
        self.number_of_passengers = number_of_passengers

    def fly(self, hours):
        self.take_off()
        print(f"{self.model} - Flying for {hours} hours")
        self.land()

#------------------------------------------------------------------------#   
class CargoAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)
        self.cargo_weight = cargo_weight

    def fly(self, hours):
        self.take_off()
        print(f"{self.model} - Flying for {hours} hours with cargo")
        self.land()

#------------------------------------------------------------------------#
class MilitaryAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)
        self.armament_type = armament_type

    def take_off(self):
        print(f"{self.model} - Military aircraft took off")

    def land(self):
        print(f"{self.model} - Military aircraft landed")

aircraft = Aircraft("Airplane", 300, 10000)
aircraft.take_off()
aircraft.land()
print()
PassengerAircraft1 = PassengerAircraft("airbaltic", 878, 750, 238)
PassengerAircraft1.take_off()
PassengerAircraft1.fly(7)
print()
CargoAircraft1 = CargoAircraft("CargoAircraft", 30100, 7500, 712)
CargoAircraft1.take_off()
CargoAircraft1.fly(15)
print()
MilitaryAircraft1 = MilitaryAircraft("MilitaryAircraft", 500, 8000, "Missiles")
MilitaryAircraft1.take_off()
MilitaryAircraft1.land()
