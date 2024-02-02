# def hello(name):
#     print("Hello,",name)
# hello("Johny")
# hello("silverhand")


# xMax=7
# xMin=-9
# yMax=22
# yMin=-8
# x = float(input("Введите X: "))
# y = float(input("Введите Y: "))
# if(x>xMax):
#     print("Не в фигуре")
# elif(y>yMax):
#     print("Не в фигуре")
# elif(x<xMin):
#     print("Не в фигуре")
# elif(y<yMin):
#     print("Не в фигуре")
# else: print("В фигуре")


# def in_out (xMin,xMax,yMax,yMin,x,y):
#     if (xMin<=x<=xMax and yMin<=y<=yMax):
#         print ("The point is inside")
#         inside=True
#     else:
#         print ("The point is outside")
#         inside=False
#     return inside
# r=in_out(7, -9, 22, -8, 0, 0)
# print(r)
# max2(10,-1)
# max2(2,-2)
# max2(10,15)




def max2(n1, n2):
    if(n1>n2):
        max=n1
        print("Max =", max)
    else:
        max=n2
        print("max =", max)
    return max
M=max2(10,5)
print(M)
print(max)
max3=max2(100, max2(0,5))
print(max3)

#     (n2>=n1):
#         max=n2
#         print("Max =", n2)
#         else: #if n1==n2
#             print("Max =", n2)
# max2(10,-1)
# max2(2,-2)
# max2(10,15)