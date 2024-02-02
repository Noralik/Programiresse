import turtle
import time
import random

wn = turtle.Screen()
wn.title("Змейка")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

grid_size = 20

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Up"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-14, 14) * grid_size, random.randint(-14, 14) * grid_size)

segments = []

def go(direction):
    if head.direction != direction[1] and head.direction != direction[0]:
        head.direction = direction[0]

def move():
    head.setheading(head.towards(food))
    head.forward(grid_size)

def check_collision():
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        reset_game()

    for segment in segments[1:]:
        if head.distance(segment) < 20:
            reset_game()

def reset_game():
    head.goto(0, 0)
    head.direction = "Up"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

def draw_grid():
    grid_pen = turtle.Turtle()
    grid_pen.speed(0)
    grid_pen.color("gray")

    for x in range(-300, 301, grid_size):
        grid_pen.penup()
        grid_pen.goto(x, 300)
        grid_pen.pendown()
        grid_pen.goto(x, -300)

    for y in range(-300, 301, grid_size):
        grid_pen.penup()
        grid_pen.goto(300, y)
        grid_pen.pendown()
        grid_pen.goto(-300, y)

    grid_pen.hideturtle()

wn.listen()
wn.onkey(lambda: go(("Up", "Down")), "w")
wn.onkey(lambda: go(("Down", "Up")), "s")
wn.onkey(lambda: go(("Left", "Right")), "a")
wn.onkey(lambda: go(("Right", "Left")), "d")

while True:
    wn.update()
    draw_grid()
    move()

    if head.distance(food) < 20:
        food.goto(
            random.randint(-14, 14) * grid_size, random.randint(-14, 14) * grid_size
        )

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].pos())

    if len(segments) > 0:
        segments[0].goto(head.pos())

    check_collision()
    time.sleep(0.1)
