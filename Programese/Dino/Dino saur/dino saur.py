pip install Pillow


import turtle
import random

class Sprite(turtle.Turtle):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.shape(image_path)
        self.penup()
        self.goto(x, y)

class Dino(Sprite):
    def jump(self):
        if self.ycor() == -50:
            for _ in range(20):
                self.sety(self.ycor() + 5) if _ < 10 else self.sety(self.ycor() - 5)
                turtle.update()

class Cactus(Sprite):
    def move(self):
        self.setx(self.xcor() - 5)

# Настройка окна
turtle.bgcolor("white")
turtle.title("Chrome Dino")
turtle.setup(width=800, height=300)

# Динозавр
dino = Dino("dino.png", -300, -50)

# Создание кактусов
cacti = [Cactus("cactus.png", random.randint(200, 400), random.randint(-50, 50)) for _ in range(5)]

# Счетчик очков
score = 0

# Отображение счета
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 150)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Настройка клавиш
turtle.listen()
turtle.onkey(dino.jump, "Up")

# Основной цикл игры
while True:
    for cactus in cacti:
        cactus.move()

        if cactus.xcor() < -400:
            cactus.goto(random.randint(200, 400), random.randint(-50, 50))
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

        if dino.distance(cactus) < 20:
            print(f"Game Over! Score: {score}")
            turtle.bye()

    turtle.update()
