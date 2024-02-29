#combobox
def clicked():
    messagebox.showerror("Error", "Its empty!")

from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox

#размер
window=Tk()
window.title("Combobox/checkbox")
window.geometry("1920x1080")


#выбор ответа 1 2 и. тд
combo=Combobox(window)
combo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, "Text")
combo.current(1)
combo.grid(column=0, row=0)


#sheckbox выбор "галочки"
chk_state=BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="Class", var=chk_state)
chk.grid(column=1, row=1)


#Radiobutton
#1
rad1=Radiobutton(window, text="First", value=1)
rad1.grid(column=2, row=2)
#2
rad2=Radiobutton(window, text="Second", value=2)
rad2.grid(column=3, row=2)
#3
rad3=Radiobutton(window, text="Third", value=3)
rad3.grid(column=4, row=2)
#4
rad4=Radiobutton(window, text="F4", value=4)
rad4.grid(column=5, row=2)
#5
rad5=Radiobutton(window, text="F5", value=5)
rad5.grid(column=6, row=2)

#Scrolled Text
txt=scrolledtext.ScrolledText(width = 40, height = 10)
txt.grid(column=0, row=3)



#from tkinter import messagebox "messagebox"

btn=Button(window,text="click", command=clicked)
btn.grid(column=7, row=4)







window.mainloop()


#https://eaglercraft.com/mc/1.8.8/