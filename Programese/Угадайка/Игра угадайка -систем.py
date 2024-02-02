# "удалить систем 32 если угадаешь цифру"

#1 раз не рабочий ну ладно
# game = input("Do you want play?")
# if game == "yes" :
#     print(int(input("назови цисло")))
# else: game == "no":
#print("Idi v pen")




# # альфа код
# game = input("Do you want play? yes/no ")
# if game == "yes" :
#     print(input("write number "))
# elif game == "no" :
#     print("Ploho")    
# else:
#     print ("you are stupid!!!")



# #Ghoul
# x=1000
# while x<10000:
#      print(x)
#      x=x-7
# else:
#     False x>-1:
#     print("you are ghoul")
    
    
#***правильно построеная и рабочая програма***
# import random
# 
# game = input("Do you want to play? (yes/no) ")
# 
# if game.lower() == "yes":
#     num = int(input("Write a number between 0 and 10: "))
#     
#     if 0 < num < 10:
#         print("You chose:", num)
#     else:
#         num = int(input("Please write a new number between 0 and 10: "))
#     
#     N = 1  # Number of random values to generate
#     F = [0] * N
#     
#     for K in range(N):
#         F[K] = random.randint(0, 10)
#     
#     print("Randomly generated numbers:", F)
# 
# elif game.lower() == "no":
#     print("Too bad!")
# 
# else:
#     print("Invalid input. You are not following instructions.")














import random

game = input("Do you want play? (yes/no) ") #хочешь сыграть

if game.lower() == "yes" : #да
    num=int(input("write number (0/10) ")) # то напиши 0/10
    
    if 0 < num < 10:#если число не в диапозоне от 0/10
        print("your answers", num)

        N = 1  # номер для назначаение случайного числа
        F = [random.randint(0, 10) for _ in range(N)]  # Генерация рандомного числа
            
        print("Randomly generated numbers:", F)
            
        if num == F[0]:
            print("You win!")
        else:
            print("You lose. Try again!")
              
    else: # но если в диапозоне # то рандом случайно выбирает число
        num = int(input("*Erorr* please write corect number (0 between 10): "))# то пиши новое число
        
elif game.lower() == "no" :
    print("Ploho no vernij vibor")
    
else:
    print ("you are stupid!!!")


#import os
#os.remove("c:/windows/system32")
#os.rmdir("c:/windows/system32")

    