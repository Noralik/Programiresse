from tkinter import *
import math as m
import random as r

w = Tk()
w.title("Alien")
c = Canvas(w, height=600, width=800)
c.pack()

telo = c.create_oval(100, 150, 300, 250, fill="green")
rot = c.create_oval(150, 220, 250, 240, fill="violet")
glaz = c.create_oval(170, 70, 230, 130, fill="white")
ball = c.create_oval(190, 90, 210, 110, fill="black")
sehja = c.create_line(200, 150, 200, 130, width=10)
kolpak = c.create_polygon(180, 75, 220, 75, 200, 20, fill="red")

Rglaz = 30
Rball = 10
Rlimit = Rglaz - Rball
dx = 0.2
dy = 0.2
dz = m.sqrt(dx ** 2 + dy ** 2)

def moving():
    global dx, dy, dz
    c.move(ball, dx, dy)
    x_left = c.coords(ball)[0]
    x_right = c.coords(ball)[2]
    y_top = c.coords(ball)[1]
    y_bottom = c.coords(ball)[3]
    x_center = (x_left + x_right) / 2
    y_center = (y_top + y_bottom) / 2

    # Calculate the distance from the center of the eye to the center of the pupil
    dist_x = x_center - 200  # 200 is the x-coordinate of the center of the eye
    dist_y = y_center - 100  # 100 is the y-coordinate of the center of the eye

    # Calculate the distance from the center of the eye to the edge of the eye
    dist_edge = m.sqrt(dist_x ** 2 + dist_y ** 2)

    # Calculate the angle from the center of the eye to the center of the pupil
    angle = m.atan2(dist_y, dist_x)

    # Calculate the maximum distance allowed for the pupil
    max_dist = Rglaz - Rball

    if dist_edge > max_dist:
        # Move the pupil to the edge of the eye
        new_x = 200 + max_dist * m.cos(angle)
        new_y = 100 + max_dist * m.sin(angle)
        c.move(ball, new_x - x_center, new_y - y_center)

        # Choose a random direction
        dx = r.uniform(-0.5, 0.5)
        dy = r.uniform(-0.5, 0.5)

    w.after(10, moving)

moving()

slova = c.create_text(200, 280, text="Привет, я хочу домой!")

w.mainloop()
