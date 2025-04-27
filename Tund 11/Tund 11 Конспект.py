# # ENTEGER INT целое число "int — целочисленный;"
# a=5
# print(type(a))
# 
# # FLOATNG float дроби  "float — с плавающей запятой;"
# b=5.5
# print(type(b))
# # TUPLE
# c=10,9
# print(type(c))
# 
# # Input "string"=(str)  цисло в текст
# d=input("Введите цисло")
# print(d,type(d))
# 
# e=input("число ")
# e=int(e)
# print(e,type(e))
# 
# f=int(d)
# g=float(d)
# print(f,type(f))
# print(g,type(g))

# # bool — логический; тип данных (правда или ложь)
# a=0
# b=2
# c=10
# d=-5
# print(bool(a), bool(b), bool(c), bool(d))

# #list LOEND список  i , k = index
# a=[2,4,88,-108,78,1,7]
# print(a[0], len(a))
# 
# #разделение операций "чтобы не писать в строку"
# a=0,b=45,c=879

#
# LOK=int(input("Введите число "))
# if True:
#     LOL=[1]
#     print("ula")
# elif False:
#     LOL=[2]
#     print("nop")

# if else elif если 1 условие есть то это но если нет то другое (число +  -  0==0)
# x=int(input("Write number "))
# if x>0:
#     print("число больше нуля")
# elif x<0:
#     print("число меньше нуля")
# else:
#     print("0=0")
    

# #WHILE цикл до
# x=int(input("число "))
# while x<100000000096969696996969696969696969696969696969:
#      print(x)
#      x=x+1
# else:
#     print("Index is maximal")


# for x in (45,99,2) # х - переменная
#     print (x)
#     
#for x in range (0,5,1):
#     print(x)

# #логическая матаматика
# a=8
# b=8
# print(a+b, a-b, a*b, a**b, a/b, a//b, a%b)
# # (+) сложение
# # (-) вычитание
# # (*) умножение
# # (**) возведение в степень
# # (/) деление
# # (//) деление до целых
# # (%) поиск остатка
# print(a==b, a>b, a<b)
# # (==) проверка равенстива
# # (>) а больше б
# # (<) а меньше б
# # (корень) а**1/2 = a**0,
# 
# #import math импорт раздел матам
# import math as m  #as нужен для обозначение библеотеке math=m
# print(m.sqrt(a), m.sin(b)) #корень матам / синус (b) math

# #вводить новую переменую Темп (кортедж) 
# a=5; b=2
# a, b = b,a
# print(a,b)
# 
# A=[2,4,8]
# B=A
# print(A); print(B)
# A[0]=100
# print(A); print(B)
# 
# for x in A:
#     print(x)

#рандомные цисла в списке размер списка сам пишешь
N=int(input("Ввести размер списка "))
import random
F=[0]*N
for K in range (N):
    F[K]=random.randint(-10,10) #диапозон списка
print(F)

