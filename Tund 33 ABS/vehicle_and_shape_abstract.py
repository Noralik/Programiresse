from abc import ABC, abstractmethod
import math as m
#------------------------------------------------------------------------------------------------#
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#------------------------------------------------------------------------------------------------#
#class Circle(Shape):
#
#  def __init__(self, radius):
#      self.radius = radius
#   
#  def area(self):
#    return m.pi * self.radius ** 2
#------------------------------------------------------------------------------------------------#
class military_vehicles(ABC):

  @abstractmethod
  def __init__(self, name):
    self.name = name
    
  @abstractmethod
  def move(self):
    pass
  
  @abstractmethod
  def atack(self):
    pass

#------------------------------------------------------------------------------------------------#
class tank(military_vehicles):

  def __init__(self, name):
    self.name = name
  
  def move(self):
    return"The tank is moving"
  
  def atack(self, obj):
    return"The tank is atacking", obj.name
    
#------------------------------------------------------------------------------------------------#
class aircraft(military_vehicles):

  def __init__(self, name):
    self.name = name

  def move(self):
    return"The aircraft is moving"
  
  def atack(self, obj):
    return"The aircaft is atacking", obj.name


#------------------------------------------------------------------------------------------------#
vehicles = [tank("T34"), aircraft("B2")]
tank1 = tank("T34")
aircraft1 = aircraft("B2")

for vec in vehicles:
  print(vec.move())
  print(vec.atack(vec))
#------------------------------------------------------------------------------------------------#
# circle1 = Circle(5)
# print(circle1.area())
