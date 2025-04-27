# import random
# 
# def бросить_кубик():
#     # Генерация случайного числа от 1 до 6
#     случайное_число = random.randint(1, 6)
#     print(f"Вы бросили кубик и выпало число: {случайное_число}")
# 
# # Вызываем функцию для броска кубика
# бросить_кубик()



# import turtle
# 
# def нарисовать_сердце():
#     # Инициализация черепашки
#     t = turtle.Turtle()
#     t.speed(2)  # Устанавливаем скорость черепашки
# 
#     # Переход к начальной точке
#     t.penup()
#     t.goto(0, -200)
#     t.pendown()
# 
#     # Начало рисования сердца
#     t.begin_fill()
#     t.fillcolor("red")
#     t.left(140)
#     t.forward(224)
#     for _ in range(200):
#         t.right(1)
#         t.forward(2)
#     t.left(120)
#     for _ in range(200):
#         t.right(1)
#         t.forward(2)
#     t.forward(224)
#     t.end_fill()
# 
#     # Завершение работы
#     turtle.done()
# 
# # Вызываем функцию для рисования сердца
# нарисовать_сердце()



# import turtle
# 
# def нарисовать_паука():
#     # Инициализация черепашки
#     t = turtle.Turtle()
#     t.speed(2)  # Устанавливаем скорость черепашки
# 
#     # Рисуем тело паука
#     t.penup()
#     t.goto(0, -50)
#     t.pendown()
#     t.circle(50)
# 
#     # Рисуем голову паука
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.circle(20)
# 
#     # Рисуем лапки паука
#     for _ in range(8):
#         t.penup()
#         t.goto(0, -50)
#         t.pendown()
#         t.right(45)
#         t.forward(50)
# 
#     # Завершение работы
#     turtle.done()
# 
# # Вызываем функцию для рисования паука
# нарисовать_паука()


import turtle
import random

def нарисовать_змею():
    # Инициализация черепашки
    t = turtle.Turtle()
    t.speed(2)  # Устанавливаем скорость черепашки
    turtle.bgcolor("black")  # Устанавливаем цвет фона

    # Функция для рисования квадрата (вкрапления)
    def рисовать_вкрапление():
        t.begin_fill()
        t.color("blue")
        for _ in range(4):
            t.forward(5)
            t.right(90)
        t.end_fill()

    # Рисуем зеленую змею
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.color("green")

    for _ in range(15):
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.left(90)

    # Рисуем вкрапления
    for _ in range(15):
        x = random.randint(-150, 0)
        y = random.randint(-20, 20)
        t.penup()
        t.goto(x, y)
        t.pendown()
        рисовать_вкрапление()

    # Завершение работы
    turtle.done()

# Вызываем функцию для рисования змеи
нарисовать_змею()
