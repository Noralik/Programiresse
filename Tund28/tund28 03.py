class Aircraft:
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model
        self.capacity = capacity
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        
    def take_off(self):
        fuel_consumption = 250  # расход топлива при взлете
        print(f"{self.model} - Взлетел")
        self.consume_fuel(fuel_consumption)
        print(f"Уровень топлива: {self.fuel_level}/{self.fuel_capacity}")
    
    def land(self):
        print(f"{self.model} - Приземлился")
        print(f"Уровень топлива: {self.fuel_level}/{self.fuel_capacity}")
    
    def consume_fuel(self, fuel_consumption):
        self.fuel_level -= fuel_consumption

class PassengerAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)
        self.number_of_passengers = number_of_passengers

    def fly(self, hours):
        fuel_consumption = 750 * hours
        print(f"{self.model} - Полет на {hours} часов с {self.number_of_passengers} пассажирами",{fuel_consumption})
        self.consume_fuel(fuel_consumption)
        self.fuel_capacity = self.fuel_capacity - fuel_consumption
        print(self.fuel_capacity)


class CargoAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)
        self.cargo_weight = cargo_weight

    def fly(self, hours):
        fuel_consumption = 150 * hours
        print(f"{self.model} - Полет на {hours} часов с весом груза {self.cargo_weight}",{fuel_consumption})
        self.consume_fuel(fuel_consumption)
        self.fuel_capacity = self.fuel_capacity - fuel_consumption
        print(self.fuel_capacity)


class MilitaryAircraft(Aircraft):
    ALLOWED_WEAPON_TYPES = ["Воздушная-воздушная", "Воздушная-наземная", "Антирадар", "Разведка"]

    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)
        if armament_type.capitalize() not in self.ALLOWED_WEAPON_TYPES:
            raise ValueError(f"Недопустимый тип вооружения для {model}: {armament_type}")
        self.armament_type = armament_type.capitalize()

    def fly(self, hours):
        if self.armament_type == "Воздушная-воздушная":
            fuel_consumption = 80 * hours
        elif self.armament_type == "Воздушная-наземная":
            fuel_consumption = 120 * hours
        elif self.armament_type == "Антирадар":
            fuel_consumption = 150 * hours
        elif self.armament_type == "Разведка":
            fuel_consumption = 100 * hours
        print(f"{self.model} - Полет на {hours} часов с типом вооружения {self.armament_type}",{fuel_consumption})
        self.consume_fuel(fuel_consumption)
        self.fuel_capacity = self.fuel_capacity - fuel_consumption
        print(self.fuel_capacity)


# Создание объектов и проведение полетов
# armament_type = "Антирадар"
# military_aircraft = None
# 
# if armament_type.capitalize() not in MilitaryAircraft.ALLOWED_WEAPON_TYPES:
#     print(f"Недопустимый тип вооружения для военного самолета: {armament_type}")
# else:
#     military_aircraft = MilitaryAircraft("F-16", 1, 18000, armament_type)
#     military_aircraft.take_off()
#     military_aircraft.fly(2)
#     military_aircraft.land()

# aircraft = Aircraft("Самолёт", 300, 10000)
# print(aircraft.fuel_capacity)
# aircraft.take_off()
# aircraft.land()
# print()
passenger_plane = PassengerAircraft("Пассажирский самолёт", 500, 20000, 200)
passenger_plane.fly(2)
print()
cargo_plane = CargoAircraft("Грузовой самолёт", 400, 15000, 10000)
cargo_plane.fly(3)
print()
military_plane = MilitaryAircraft("Военный самолёт", 1, 12000, "Разведка")
military_plane.fly(1)
print()