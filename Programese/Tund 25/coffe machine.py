#     def AddH20(self,water_level):
#             self.balance += water_level
#             print("Dobavilis: ", water_level)
#             print(self.balance)
# 
#     def NorH2O(self,water_level):
#             self.balance -= water_level
#             if water_level <=self.balance:
#                 self.balance -= water_level
#                 print("Success")
#                 print(self.balance)
#             else:
#                 print("Error")
#                 print("võtan raha: ", water_level)

# Howmuch = int(input("How much +/-: "))
# YourBalance = int(input("Your Balance: "))
# KKK = int(input("1 / 2 "))

class CoffeeMachine:

    def __init__(self,brand, water_level):
        self.brand = brand
        self.balance = water_level
    
    def H2O(self):
        self.water_level = 650
    
    def cup(self):
        if ChoiceCUP == self.water_level =< 299:
            print("Malo H2O")
        if ChoiceCUP == self.water_level => 300:
            print("ты выбрал  мальенкий размер 300ml ")
        if ChoiceCUP == self.water_level => 500:
            print("ты выбрал  Большой размер 500ml ")
        if ChoiceCUP == water_level => 1000:
            print("Воды не хватило ")
            print("ты выбрал  Гига размер 750ml ")
        
#     def control(self):
#         if KKK==1:
#             O = self.AddH20(int(input("How much? ")))
#         else:
#             P = self.NorH2O(int(input("How much? ")))


ChoiceCUP = int(input("Сколько милитров 300/500/750: "))
acc1 = CoffeeMachine("123456789",ChoiceCUP ) # balance
acc1.cup()
