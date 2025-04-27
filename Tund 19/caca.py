import MyLib as ML
ML.odd(6)
ML.summa(3,8)
from tkinter import *


# window=Tk()
# window.title("Alien")
# c=Canvas(window, height=500, width=500)
# c.pack()
# # drawing=Canvas(window, height=500, width=500)
# # drawing.pack()
# 
# # rect1=drawing.create_rectangle(100, 100, 300, 200)
# # oval1=drawing.create_oval(100, 100, 300, 200)
# # circle=drawing.create_oval(30, 30, 80, 80, width=2, outline="black", fill="grey")
# 
# telo=c.create_oval(100, 150, 300, 250, fill="green")
# rot=c.create_oval(150, 220, 250, 240, fill="red")
# glaz=c.create_oval(170, 70, 230, 130, fill="white")
# zrachok=c.create_oval(190, 90, 210, 110, fill="black")
# sehja=c.create_line(200, 150, 200, 130, width=10)
# kolpak=c.create_polygon(180, 75, 220, 75, 200, 20, fill="orange")
# 
# # c.move(zrachok, -10, 0)
# 
# # def rot_zakryt(event):
# #     c.itemconfig(rot, fill="green")
# # c.bind_all("<Button-1>",rot_zakryt)
# # rot_zakryt()
# # def rot_otkryt(event):
# #     c.itemconfig(rot, fill="green")
# # c.bind_all("<Button-3>",rot_otkryt)
# # rot_otkryt()
# 
# # window.attributes("-topmost", 1)
# # def zrachok_nalevo(event):
# #     c.move(zrachok, -10,0)
# # def zrachok_napravo(event):
# #     c.move(zrachok, 10,0)
#     
# def rot_zakryt(event):
#     c.itemconfig(rot, fill="green", outline="green")
# def rot_otkryt(event):
#     c.itemconfig(rot, fill="red", outline="black")
# 
# 
# def zrachok_dvigat(event):
#     knopka=event.keysym
#     if knopka=="Up":
#         c.move(zrachok, 0, -1)
#     if knopka=="Down":
#         c.move(zrachok, 0, 1)
#     if knopka=="Left":
#         c.move(zrachok, -1, 0)
#     if knopka=="Right":
#         c.move(zrachok, 1, -0)
#     
# c.bind_all("<Key>", zrachok_dvigat)
# c.bind_all("<Button-1>", rot_zakryt)
# c.bind_all("<Button-3>", rot_otkryt)
# slova=c.create_text(400, 100, text="база ответе")
# 
# window.mainloop()


















window=Tk()
window.title("Home")
c=Canvas(window, height=500, width=500)
c.pack()


x1=30; y1=60; x2=130; y2=120
x3=x1+(x2-x1)/2
y3=10
# c.create_rectangle(x1, y1, x2, y2, fill="brown")
# c.create_polygon(x1, y1, x2, y3, x2, y1, fill="orange")

dom=3
radi=3
for j in range (radi):
    for i in range (dom):
        c.create_rectangle(x1+i*120,y1,x2+i*120,y2, fill="brown")
        c.create_polygon(x1+i*120,y1,x3+i*120,y3,x2+i*120,y1, fill="orange")
        
        c.create_rectangle(x1+i*120,y1,x2+i*120,y2, fill="brown")
        c.create_polygon(x1+i*120,y1,x3+i*120,y3,x2+i*120,y1, fill="orange")

window.mainloop()