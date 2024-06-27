def clicked():
    res="Hello {}! now you are dead, you have 40 second".format(inp.get())
    lbl.configure(text=res)
#     i=7
#     while True:
#         i=i+6
#     lbl.configure(text=("Loading= ",i,"%"))

from tkinter import *

window=Tk()
window.title("Death note")
window.geometry("1920x1080")

lbl=Label(window, text="do u want three hundred bucks?", font=("Arial Bold",50))
lbl.grid(column=0, row=0)

inp=Entry(window, width=20)
inp.grid(column=1, row=5)

btn=Button(window, text="GAIN 300 HUNDRED BUCKS", bg="black", fg="green", font=("Arial Bold", 12), command=clicked)
btn.grid(column=2, row=0)






window.mainloop()

# a="Peter Griffin"
# print("Hello i´am {}!".format(a))
