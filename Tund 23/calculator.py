from tkinter import *
import random as r

Calculator_Math=Tk()
Calculator_Math.title("Calculator")
inputvar=StringVar()
Entry(textvariable=inputvar, width=40).grid(row=0,column=0, columnspan=4)
Button(text="1", width=10, height=5).grid(row=1, column=0)
Button(text="2", width=10, height=5).grid(row=1, column=1)
Button(text="3", width=10, height=5).grid(row=1, column=2)
Button(text="4", width=10, height=5).grid(row=2, column=0)
Button(text="5", width=10, height=5).grid(row=2, column=1)
Button(text="6", width=10, height=5).grid(row=2, column=2)
Button(text="7", width=10, height=5).grid(row=3, column=0)
Button(text="8", width=10, height=5).grid(row=3, column=1)
Button(text="9", width=10, height=5).grid(row=3, column=2)
Button(text="=", width=10, height=5).grid(row=4, column=0)
Button(text="0", width=10, height=5).grid(row=4, column=1)

Button(text="AC", width=10, height=5).grid(row=4, column=2)
Button(text="+", width=10, height=5).grid(row=1, column=4)
Button(text="-", width=10, height=5).grid(row=2, column=4)
Button(text="*", width=10, height=5).grid(row=3, column=4)
Button(text="/", width=10, height=5).grid(row=4, column=4)



Calculator_Math.mainloop()