from tkinter import *
import time as t
import random as r
import math as m
w=Tk()
w.title("Limits")
c=Canvas(w, height=1080, width=1920)
c.pack()

# dx=int(input("Шаги по х"))
# dy=int(input("Шаги по у"))

ball=c.create_oval(270, 270, 330, 330, fill="blue", outline="blue", activefill="green")
glaz=c.create_oval(150, 150, 450, 450, outline="blue")
Rglaz=150; Rball=30; Rlimit=Rglaz-Rball

dx=16; dy=9
while True:

# def move():
    c.move(ball, dx, dy)
    xleft=c.coords(ball)[0]; xright=c.coords(ball)[2]
    ytop=c.coords(ball)[1]; ybottom=c.coords(ball)[3]
    x_ball=xleft+30; y_ball=ytop+30
    R=m.sqrt((x_ball-300)**2+(y_ball-300)**2)
    if R>=Rlimit:
        dx=dx*r.randint(-2, 0)
        dy=dy*r.randint(-2,  0)
    w.update()
    t.sleep(0.01)
w.mainloop()
#     if xleft<5 or xright>1920:
#         dx=-dx
#     if ytop<5 or ybottom>1080:
#         dy=-dy
#     w.update()
#     t.sleep(0.01)
# #     if 5<=c.coords(ball)[2]<=(450-dx) and c.coords(ball)[3]=595:
# #         w.after(10, move)
# #     elif c.coords(ball)[2]==595 and c.coords(ball)[3]==595:
# #         dx=-dx; 
# #         
# 
# # bal=c.create_oval(5, 5, 595, 595)
# # move()
# # for i in (1,2,3):
# #     ptint(i)
# #     c.after(100, c.move(ball,10,0))
# w.mainloop()