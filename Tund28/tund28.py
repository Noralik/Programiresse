class fish:
    def __init__(self, species, size):
        self.species = species
        self.size = size
        
    def swim(self):
        print("fish:", self.species, "is swimming")

    def eat(self):
        self.eaten += 1

#-------------------------------------------------------------------------------------------------#
class CarnivoreFish(fish): # хищная рыба
    def __init__(self, species, size):
        super().__init__(species, size)
        self.prey_list = ["stingray", "piranha", "carp", "perches", "shark", "salmon"] # что кушает
        
    def eat(self, food):
        if food in self.prey_list:
            self.size += 5
        else:
            print("CarnivoreFish don't feed on this")
            
    def displayFishInfo(self):
        print(self.size)

#-------------------------------------------------------------------------------------------------#
class HerbivoreFish(fish): # травоядная рыба
    def __init__(self, species, size):
        super().__init__(species, size)
        self.plant_list = ["seaweed"] # что кушает
        
    def eat(self, food):
        if food in self.plant_list:
            self.size += 5
        else:
            print("HerbivoreFish don't feed on this")
            
    def displayFishInfo(self):
        print(self.size)

#-------------------------------------------------------------------------------------------------#
class OmnivoreFish(fish): # всеядная рыба
    def __init__(self, species, size):
        super().__init__(species, size)
        self.all_eating = ["seaweed", "plankton", "piranha"] # кушает всю еду из всех списков
        
    def eat(self, food):
        if food in self.all_eating:
            self.size += 3
        else:
            print("OmnivoreFish don't feed on this")
            
    def displayFishInfo(self):
        print(self.size)

#-------------------------------------------------------------------------------------------------#
        
Carnivore = CarnivoreFish("shark", 23)
# Carnivore.eat("HerbivoreFish")
# Carnivore.displayFishInfo()

Herbivore = HerbivoreFish("blue acara", 2)
#Herbivore.eat("seaweed")
#Herbivore.displayFishInfo()

Omnivore = OmnivoreFish("pike", 5)
#Omnivore.eat("perches")
#Omnivore.displayFishInfo()

allFishes = [Carnivore, Herbivore, Omnivore]
for fish in allFishes:
    fish.eat("seaweed")
