import tkinter
from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("CALCULATOR")
win.geometry("400x350")
frame = tkinter.Frame(master=win, bg="#9917ED", padx=30, pady=2)
frame.pack()
entry = tkinter.Entry(master=frame, borderwidth=3, width=23, font=('arial', 15, 'bold'))
entry.grid(row=0, column=0, pady=7, ipady=15, columnspan=4)



win.mainloop()