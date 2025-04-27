# no comment pls
# n=(5*20)/(40*2+20); print("answers ", n)

# Loend a=[]
a = [0]*5
# [0, 0, 0, 0, 0]

# for i in range (0,5): # [0, 0, 0, 0, 0]  =  [0, 1, 2, 3, 4]
# for i in range (5):   # [0, 0, 0, 0, 0]  =  [0, 1, 2, 3, 4]
for i in range(0, 5):   # [0, 0, 0, 0, 0]  =  [-1, 0, 1, 2, 3]
#     a[i] = i          # [0, 1, 2, 3, 4]
#     a[i] = i + 1      # [1, 2, 3, 4, 5]
    a[i] = i - 1        # [-1, 0, 1, 2, 3]

print(a)  # print Loend a

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

A = []
for i in range(0, 5):
    A.append(i)
#     A.append(i+1)
#     A.append(i-1)

print(A)

A = []
for i in range(0, 5):  # элементов 5
    A.append(i+1)      # каждый элемент +1
    A.append("privet") # пишет после каждого элемента привет
A.append(6)            # вышли из цикла "- tab." 

print(A)  # принт ААААААААА

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # comprehesive list
D = [i*3 for i in range(0, 11)]
##print(D)

F1 = [0 if i % 2 == 0 else i for i in D]
print(F1)

F2 = [i if i % 2 == 0 else 0 for i in D]
print(F2)

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def search_array(A: list, x: int):
    """Searching for number x in list A
    """
    N = len(A)
    for i in range(N):
        if A[i] == x:
            return i
    return -1

def test_search_array():
    A1 = [5, 7, 4, 2]
    m = search_array(A1, 7)
    if m == 1:
        print("test1 - OK!")
    else:
        print("test1 - Fail!")

    A2 = [-5, -7, -6, -9]
    m = search_array(A2, -6)
    if m == 2:
        print("test2 - OK!")
    else:
        print("test2 - Fail!")

    A3 = [23, 17, 10, 15, 25, 10]
    m = search_array(A3, 10)
    if m == 2:
        print("test3 - OK!")
    else:
        print("test3 - Fail!")

test_search_array()

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def factorize(x):
    """factorizing integer number x
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x = x // divisor
        else:
            divisor = divisor + 1

factorize(106)

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Классы

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Alice", 20)
p1.greet()

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(4, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Наследование классов

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

dog1 = Dog("Buddy")
dog1.sound()

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Импорт классов и объектов

# Внутри одного файла
class Car:
    def __init__(self, model):
        self.model = model

    def show(self):
        print(f"Car model: {self.model}")

# можно создать объект на основе Car
my_car = Car("BMW")
my_car.show()  # Car model: BMW

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Импорт из другого файла

# Допустим, у нас есть файл vehicle.py:
# ---- vehicle.py ----
# class Truck:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def show(self):
#         print(f"Truck brand: {self.brand}")
# ----------------------

# Тогда в основном файле можно написать:
# from vehicle import Truck

# И создать объект Truck
# truck = Truck("Volvo")
# truck.show()  # Truck brand: Volvo

# Также можно импортировать несколько классов сразу
# from vehicle import Truck, Car

# Или импортировать весь файл:
# import vehicle
# и потом обращаться так:
# t = vehicle.Truck("Mercedes")
# t.show()

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
