import tkinter as tk
import random as r

w=tk.Tk()
w.title("GUI #1")
w.attributes("-topmost", True )#okno naverhu



def rnd():
    rnd_nmbr=r.randint(100,50000)
    hi.config(text=str(rnd_nmbr))
    btn.config(text="Call the next number")
hi=tk.Label(text="Hello, username!"); hi.pack()
btn=tk.Button(text="Input your real name!", fg="white", bg="black", command=rnd); btn.pack()
entr=tk.Entry(bg="coral");entr.pack()
name=entr.get()

w.mainloop()