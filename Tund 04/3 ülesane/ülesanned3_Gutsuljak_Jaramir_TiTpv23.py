

x = float(input("Введите X: "))
y = float(input("Введите Y: "))

if x > 0 and y > 0:
    print("Точка в квадранте 1")
elif x < 0 and y > 0:
    print("Точка в квадранте 2")
elif x < 0 and y < 0:
    print("Точка в квадранте 3")
elif x > 0 and y < 0:
    print("Точка в квадранте 4")
    
elif x > 0 and y == 0:
    print("Точка находится на положительной оси X")
elif x == 0 and y > 0:
    print("Точка находится на положительной оси Y")
elif x < 0 and y == 0:
    print("Точка находится на отрицательной оси X")
elif x == 0 and y < 0:
    print("Точка находится на отрицательной оси Y")
    
elif x == 0 and y == 0:
    print("Точка находится на (0,0)")