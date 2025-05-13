from tkinter import *

w = Tk()
c = Canvas(w, width=1920, height=1080) 
c.pack()

kvadrat=c.create_rectangle(1, 1, 600,300, fill="blue")
blue1=c.create_rectangle(1,1, 500,300, fill="yellow")

yel2=c.create_rectangle(1, 1, 400,300, fill="blue")
pp=c.create_rectangle(1,1, 300,300, fill="yellow")

yel2=c.create_rectangle(1, 1, 200,300, fill="blue")
pp=c.create_rectangle(1,1, 100,300, fill="yellow")

ok = c.create_polygon(800,745,406,706,940,560, fill="red", outline="black")
ok = c.create_polygon(800,745,203,350,940,560, fill="black", outline="black")


etrer=c.create_rectangle( 1, 350, 400, 600 ,fill="black")
etrer=c.create_rectangle( 200, 350, 400, 475 ,fill="yellow")
etrer=c.create_rectangle( 1, 600, 200, 475 ,fill="yellow")

etrehpkftopmfgjhopimfr=c.create_rectangle( 1, 700, 600, 1000 ,fill="red")
etrehpkftopmfgjhopimfr=c.create_line( 300, 700, 300, 1000 , fill="yellow", width=50)
jfhjblfgdpihuk=c.create_line( 1, 851l, 600, 850 , fill="yellow", width=50)

w.mainloop()
