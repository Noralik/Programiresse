#-------------------------------------------------------------------------------------------------#
# Код 1: Классы для разных типов рыб
#-------------------------------------------------------------------------------------------------#

# Класс рыбы, основной для всех типов рыб
class fish:
    def __init__(self, species, size):
        self.species = species  # Вид рыбы
        self.size = size  # Размер рыбы
        
    def swim(self):
        print("fish:", self.species, "is swimming")  # Рыба плавает

    def eat(self):
        self.eaten += 1  # Рыба ест (счётчик еды увеличивается)

#-------------------------------------------------------------------------------------------------#

# Класс хищной рыбы, наследует от класса fish
class CarnivoreFish(fish):  # хищная рыба
    def __init__(self, species, size):
        super().__init__(species, size)  # Инициализация родительского класса
        self.prey_list = ["stingray", "piranha", "carp", "perches", "shark", "salmon"]  # Список добычи, которую ест хищник
        
    def eat(self, food):
        if food in self.prey_list:
            self.size += 5  # Если еда есть в списке, рыба увеличивает свой размер
        else:
            print("CarnivoreFish don't feed on this")  # Если рыба не ест этот вид пищи
            
    def displayFishInfo(self):
        print(self.size)  # Вывод размера рыбы

#-------------------------------------------------------------------------------------------------#

# Класс травоядной рыбы, наследует от класса fish
class HerbivoreFish(fish):  # травоядная рыба
    def __init__(self, species, size):
        super().__init__(species, size)  # Инициализация родительского класса
        self.plant_list = ["seaweed"]  # Список растений, которые ест травоядная рыба
        
    def eat(self, food):
        if food in self.plant_list:
            self.size += 5  # Если еда есть в списке, рыба увеличивает свой размер
        else:
            print("HerbivoreFish don't feed on this")  # Если рыба не ест этот вид пищи
            
    def displayFishInfo(self):
        print(self.size)  # Вывод размера рыбы

#-------------------------------------------------------------------------------------------------#

# Класс всеядной рыбы, наследует от класса fish
class OmnivoreFish(fish):  # всеядная рыба
    def __init__(self, species, size):
        super().__init__(species, size)  # Инициализация родительского класса
        self.all_eating = ["seaweed", "plankton", "piranha"]  # Список пищи, которую ест всеядная рыба
        
    def eat(self, food):
        if food in self.all_eating:
            self.size += 3  # Если еда есть в списке, рыба увеличивает свой размер
        else:
            print("OmnivoreFish don't feed on this")  # Если рыба не ест этот вид пищи
            
    def displayFishInfo(self):
        print(self.size)  # Вывод размера рыбы

#-------------------------------------------------------------------------------------------------#
        
# Пример создания объектов и вызова методов
Carnivore = CarnivoreFish("shark", 23)
Herbivore = HerbivoreFish("blue acara", 2)
Omnivore = OmnivoreFish("pike", 5)

# Все рыбы едят "seaweed"
allFishes = [Carnivore, Herbivore, Omnivore]
for fish in allFishes:
    fish.eat("seaweed")  # Каждая рыба ест водоросли
  
#-------------------------------------------------------------------------------------------------#
# Код 2: Классы для различных типов воздушных судов
#-------------------------------------------------------------------------------------------------#

# Класс самолёта
class Aircraft:
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model  # Модель самолёта
        self.capacity = capacity  # Вместимость
        self.fuel_capacity = fuel_capacity  # Вместимость бака
        self.fuel_level = fuel_capacity  # Начальный уровень топлива
        
    def take_off(self):
        print(f"{self.model} - We've consumed fuel and took off")  # Самолёт взлетел
        self.consume_fuel()

    def land(self):
        print(f"{self.model} - We've successfully landed")  # Самолёт приземлился
    
    def consume_fuel(self):
        fuel_consumed = 50  # Количество расходуемого топлива
        if self.fuel_level >= fuel_consumed:
            self.fuel_level -= fuel_consumed  # Расходуем топливо
            print(f"{self.model} - Fuel consumed. Remaining fuel: {self.fuel_level}")
        else:
            print(f"{self.model} - Insufficient fuel for the flight")  # Недостаточно топлива

#------------------------------------------------------------------------#

# Класс пассажирского самолёта, наследует от Aircraft
class PassengerAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        self.number_of_passengers = number_of_passengers  # Количество пассажиров

    def fly(self, hours):
        self.take_off()  # Взлет
        print(f"{self.model} - Flying for {hours} hours")  # Полёт
        self.land()  # Приземление

#------------------------------------------------------------------------#   

# Класс грузового самолёта, наследует от Aircraft
class CargoAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        self.cargo_weight = cargo_weight  # Вес груза

    def fly(self, hours):
        self.take_off()  # Взлет
        print(f"{self.model} - Flying for {hours} hours with cargo")  # Полёт с грузом
        self.land()  # Приземление

#------------------------------------------------------------------------#

# Класс военного самолёта, наследует от Aircraft
class MilitaryAircraft(Aircraft):
    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        self.armament_type = armament_type  # Тип вооружения

    def take_off(self):
        print(f"{self.model} - Military aircraft took off")  # Военный самолёт взлетает

    def land(self):
        print(f"{self.model} - Military aircraft landed")  # Военный самолёт приземляется

# Пример использования классов
aircraft = Aircraft("Airplane", 300, 10000)
aircraft.take_off()
aircraft.land()

#-------------------------------------------------------------------------------------------------#
#Код 3: Расширение функционала для расхода топлива
#-------------------------------------------------------------------------------------------------#
class Aircraft:
    # Конструктор класса, инициализирует основные параметры самолета
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model  # Модель самолета
        self.capacity = capacity  # Вместимость самолета
        self.fuel_capacity = fuel_capacity  # Емкость топливного бака
        self.fuel_level = fuel_capacity  # Уровень топлива, изначально равен полной емкости

    # Метод для взлета
    def take_off(self):
        if self.fuel_level < 50:  # Если топлива меньше 50, взлет невозможен
            print(f"{self.model} - Insufficient fuel for take-off")
            return False
        print(f"{self.model} - We've consumed fuel and took off")  # Сообщение о взлете
        return True

    # Метод для посадки
    def land(self):
        print(f"{self.model} - We've successfully landed")  # Сообщение о посадке
    
    # Метод для полета
    def fly(self, hours):
        if self.take_off():  # Если взлет прошел успешно
            print(f"{self.model} - Flying for {hours} hours")  # Сообщение о полете
            self.consume_fuel(hours)  # Передаем продолжительность полета для расчета расхода топлива
            
    # Метод для расхода топлива, который может быть переопределен в дочерних классах
    def consume_fuel(self, hours=None):
        pass  # Пустой метод, который можно переопределить в наследниках


class PassengerAircraft(Aircraft):
    # Конструктор для пассажирского самолета
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация через родительский класс
        self.number_of_passengers = number_of_passengers  # Количество пассажиров

    # Метод для полета с учетом расхода топлива
    def fly(self, hours):
        if self.take_off():  # Если взлет успешен
            print(f"{self.model} - Flying for {hours} hours")  # Сообщение о полете
            self.consume_fuel(hours)  # Передаем продолжительность полета для расчета расхода топлива

    # Переопределенный метод расхода топлива
    def consume_fuel(self, hours):
        fuel_consumed = 5 * hours  # Расход топлива: 5 единиц на каждый час полета
        if self.fuel_level < fuel_consumed:  # Если топлива недостаточно для полета
            print(f"{self.model} - Insufficient fuel for {hours} hours of flight")
            self.land()  # Земля на посадку
        else:
            self.fuel_level -= fuel_consumed  # Уменьшаем уровень топлива
            print(f"{self.model} - Fuel consumed for {hours} hours of flight. Remaining fuel: {self.fuel_level}")
            self.land()  # Земля на посадку


class CargoAircraft(Aircraft):
    # Конструктор для грузового самолета
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация через родительский класс
        self.cargo_weight = cargo_weight  # Вес груза

    # Метод для полета с учетом расхода топлива
    def fly(self, hours):
        if self.take_off():  # Если взлет успешен
            print(f"{self.model} - Flying for {hours} hours with cargo")  # Сообщение о полете с грузом
            self.consume_fuel(hours)  # Передаем продолжительность полета для расчета расхода топлива

    # Переопределенный метод расхода топлива
    def consume_fuel(self, hours):
        fuel_consumed = 5 * hours  # Расход топлива: 5 единиц на каждый час полета
        if self.fuel_level < fuel_consumed:  # Если топлива недостаточно для полета
            print(f"{self.model} - Insufficient fuel for {hours} hours of flight")
            self.land()  # Земля на посадку
        else:
            self.fuel_level -= fuel_consumed  # Уменьшаем уровень топлива
            print(f"{self.model} - Fuel consumed for {hours} hours of flight. Remaining fuel: {self.fuel_level}")
            self.land()  # Земля на посадку


class MilitaryAircraft(Aircraft):
    # Разрешенные типы вооружений для военных самолетов
    ALLOWED_WEAPON_TYPES = ["õhk-õhk", "õhk-maa", "antiradar", "luure"]

    # Конструктор для военного самолета
    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация через родительский класс
        if armament_type not in self.ALLOWED_WEAPON_TYPES:  # Проверка на допустимость типа вооружения
            raise ValueError(f"Invalid armament type for {model}: {armament_type}")
        self.armament_type = armament_type  # Тип вооружения

    # Переопределенный метод взлета для военных самолетов
    def take_off(self):
        if self.fuel_level < 100:  # Для военных самолетов требуется минимум 100 единиц топлива для взлета
            print(f"{self.model} - Insufficient fuel for take-off")
            return False
        print(f"{self.model} - Military aircraft took off")  # Сообщение о взлете
        self.consume_fuel(100)  # Расход 100 единиц топлива на взлет
        return True

    # Метод посадки для военного самолета
    def land(self):
        print(f"{self.model} - Military aircraft landed")  # Сообщение о посадке


# Пример использования:
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

# Проверка допустимости типа вооружения для военного самолета
def check_weapon_type(armament_type):
    if armament_type not in MilitaryAircraft.ALLOWED_WEAPON_TYPES:
        raise ValueError(f"Invalid armament type: {armament_type}. Allowed types are: {', '.join(MilitaryAircraft.ALLOWED_WEAPON_TYPES)}")

# Создание объекта MilitaryAircraft и проверка типа вооружения
armament_type = "Missiles"  # Пример недопустимого типа вооружения
if armament_type in MilitaryAircraft.ALLOWED_WEAPON_TYPES:
    military_aircraft = MilitaryAircraft("MilitaryAircraft", 500, 8000, armament_type)
    military_aircraft.take_off()
    military_aircraft.land()
else:
    print(f"Invalid armament type: {armament_type}. Allowed types are: {', '.join(MilitaryAircraft.ALLOWED_WEAPON_TYPES)}")

# Создание военного самолета с допустимым типом вооружения
military_aircraft2 = MilitaryAircraft("MilitaryAircraft", 500, 8000, "õhk-õhk")
military_aircraft2.take_off()
military_aircraft2.land()

#-------------------------------------------------------------------------------------------------#
#Код 4: Расширение
#-------------------------------------------------------------------------------------------------#
# Класс Aircraft представляет общий функционал для всех типов самолетов
class Aircraft:
    # Конструктор класса для инициализации модели, вместимости и емкости топливного бака
    def __init__(self, model, capacity, fuel_capacity):
        self.model = model  # Модель самолета
        self.capacity = capacity  # Вместимость самолета (количество пассажиров или груз)
        self.fuel_capacity = fuel_capacity  # Емкость топливного бака
        self.fuel_level = fuel_capacity  # Уровень топлива, инициализируется максимальным значением

    # Метод для взлета самолета
    def take_off(self):
        fuel_consumption = 250  # Расход топлива при взлете (зафиксированная величина)
        print(f"{self.model} - Взлетел")  # Вывод сообщения о взлете
        self.consume_fuel(fuel_consumption)  # Расходуем топливо
        print(f"Уровень топлива: {self.fuel_level}/{self.fuel_capacity}")  # Выводим текущее количество топлива

    # Метод для посадки самолета
    def land(self):
        print(f"{self.model} - Приземлился")  # Сообщение о посадке
        print(f"Уровень топлива: {self.fuel_level}/{self.fuel_capacity}")  # Показываем остаток топлива

    # Метод для расхода топлива
    def consume_fuel(self, fuel_consumption):
        self.fuel_level -= fuel_consumption  # Уменьшаем уровень топлива на величину расхода


# Класс PassengerAircraft наследует от Aircraft и добавляет функционал для пассажирских самолетов
class PassengerAircraft(Aircraft):
    # Конструктор для пассажирского самолета, учитывающий количество пассажиров
    def __init__(self, model, capacity, fuel_capacity, number_of_passengers):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        self.number_of_passengers = number_of_passengers  # Количество пассажиров

    # Метод для полета с учетом времени
    def fly(self, hours):
        fuel_consumption = 750 * hours  # Расход топлива для пассажирского самолета: 750 единиц на час
        print(f"{self.model} - Полет на {hours} часов с {self.number_of_passengers} пассажирами, {fuel_consumption}")
        self.consume_fuel(fuel_consumption)  # Потребляем топливо
        self.fuel_capacity = self.fuel_capacity - fuel_consumption  # Уменьшаем топливную емкость
        print(self.fuel_capacity)  # Показываем оставшуюся топливную емкость


# Класс CargoAircraft наследует от Aircraft и добавляет функционал для грузовых самолетов
class CargoAircraft(Aircraft):
    # Конструктор для грузового самолета, учитывающий вес груза
    def __init__(self, model, capacity, fuel_capacity, cargo_weight):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        self.cargo_weight = cargo_weight  # Вес груза

    # Метод для полета с учетом времени
    def fly(self, hours):
        fuel_consumption = 150 * hours  # Расход топлива для грузового самолета: 150 единиц на час
        print(f"{self.model} - Полет на {hours} часов с весом груза {self.cargo_weight}, {fuel_consumption}")
        self.consume_fuel(fuel_consumption)  # Потребляем топливо
        self.fuel_capacity = self.fuel_capacity - fuel_consumption  # Уменьшаем топливную емкость
        print(self.fuel_capacity)  # Показываем оставшуюся топливную емкость


# Класс MilitaryAircraft наследует от Aircraft и добавляет функционал для военных самолетов с учетом типа вооружения
class MilitaryAircraft(Aircraft):
    # Список допустимых типов вооружений
    ALLOWED_WEAPON_TYPES = ["Воздушная-воздушная", "Воздушная-наземная", "Антирадар", "Разведка"]

    # Конструктор для военного самолета, учитывающий тип вооружения
    def __init__(self, model, capacity, fuel_capacity, armament_type):
        super().__init__(model, capacity, fuel_capacity)  # Инициализация родительского класса
        # Проверка на допустимость типа вооружения
        if armament_type.capitalize() not in self.ALLOWED_WEAPON_TYPES:
            raise ValueError(f"Недопустимый тип вооружения для {model}: {armament_type}")
        self.armament_type = armament_type.capitalize()  # Инициализация типа вооружения

    # Метод для полета с учетом времени и типа вооружения
    def fly(self, hours):
        # В зависимости от типа вооружения меняется расход топлива
        if self.armament_type == "Воздушная-воздушная":
            fuel_consumption = 80 * hours
        elif self.armament_type == "Воздушная-наземная":
            fuel_consumption = 120 * hours
        elif self.armament_type == "Антирадар":
            fuel_consumption = 150 * hours
        elif self.armament_type == "Разведка":
            fuel_consumption = 100 * hours
        print(f"{self.model} - Полет на {hours} часов с типом вооружения {self.armament_type}, {fuel_consumption}")
        self.consume_fuel(fuel_consumption)  # Потребляем топливо
        self.fuel_capacity = self.fuel_capacity - fuel_consumption  # Уменьшаем топливную емкость
        print(self.fuel_capacity)  # Показываем оставшуюся топливную емкость


# Создание объектов и проведение полетов
# Пример создания пассажирского самолета и выполнения полета
passenger_plane = PassengerAircraft("Пассажирский самолёт", 500, 20000, 200)
passenger_plane.fly(2)  # Полет на 2 часа
print()

# Пример создания грузового самолета и выполнения полета
cargo_plane = CargoAircraft("Грузовой самолёт", 400, 15000, 10000)
cargo_plane.fly(3)  # Полет на 3 часа
print()

# Пример создания военного самолета и выполнения полета
military_plane = MilitaryAircraft("Военный самолёт", 1, 12000, "Разведка")
military_plane.fly(1)  # Полет на 1 час
print()
