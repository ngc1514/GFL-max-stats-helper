from tkinter import *

window = Tk()

window.title("GFL Max Stats Comparator")
window.geometry('350x200')

lbl = Label(window, text="TEST", font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    lbl.configure(text="Btn clicked")

btn = Button(window, text="Compare", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()
