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


def character(n):
    entry.insert(tkinter.END, n)


def result():
    try:
        y = eval(entry.get())
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, y)
    except:
        entry.delete(0, tkinter.END)
        entry.insert(tkinter.END, "syntax error/formula error")


def back():
    b = entry.get()
    a = len(b)
    entry.delete(a - 1, tkinter.END)


def clear():
    entry.delete(0, tkinter.END)


one = Button(frame, text="1", width=3, height=3, padx=8, command=lambda: character(1), activebackground="red",
             activeforeground="white")
one.grid(row=1, column=0)

two = Button(frame, text="2", width=3, height=3, padx=8, command=lambda: character(2), activebackground="red",
             activeforeground="white")
two.grid(row=1, column=1)

three = Button(frame, text="3", width=3, height=3, padx=8, command=lambda: character(3), activebackground="red",
               activeforeground="white")
three.grid(row=1, column=2)

four = Button(frame, text="4", width=3, height=3, padx=8, command=lambda: character(4), activebackground="red",
              activeforeground="white")
four.grid(row=2, column=0)

five = Button(frame, text="5", width=3, height=3, padx=8, command=lambda: character(5), activebackground="red",
              activeforeground="white")
five.grid(row=2, column=1)

six = Button(frame, text="6", width=3, height=3, padx=8, command=lambda: character(6), activebackground="red",
             activeforeground="white")
six.grid(row=2, column=2)

seven = Button(frame, text="7", width=3, height=3, padx=8, command=lambda: character(7), activebackground="red",
               activeforeground="white")
seven.grid(row=3, column=0)

eight = Button(frame, text="8", width=3, height=3, padx=8, command=lambda: character(8), activebackground="red",
               activeforeground="white")
eight.grid(row=3, column=1)

nine = Button(frame, text="9", width=3, height=3, padx=8, command=lambda: character(9), activebackground="red",
              activeforeground="white")
nine.grid(row=3, column=2)

plus = Button(frame, text="+", width=3, height=3, padx=8, activebackground="yellow", command=lambda: character("+"))
plus.grid(row=1, column=3)

minus = Button(frame, text="-", width=3, height=3, padx=8, activebackground="yellow", command=lambda: character("-"))
minus.grid(row=2, column=3)

division = Button(frame, text="/", width=3, height=3, padx=8, activebackground="yellow", command=lambda: character("/"))
division.grid(row=4, column=2)

zero = Button(frame, text="0", width=3, height=3, padx=8, command=lambda: character(0), activebackground="red",
              activeforeground="white")
zero.grid(row=4, column=0)

equal = Button(frame, text="=", width=3, height=3, padx=8, activebackground="yellow", command=lambda: result())
equal.grid(row=4, column=1)

mult = Button(frame, text="x", width=3, height=3, padx=8, activebackground="yellow", command=lambda: character("*"))
mult.grid(row=3, column=3)

Clear = Button(frame, text="clear", width=3, height=5, padx=8, activebackground="pink", command=lambda: clear())
Clear.grid(row=4, column=3, rowspan=2)

bak = Button(frame, text="back space", width=23, height=1, padx=8, activebackground="pink", command=lambda: back())
bak.grid(row=5, column=0, columnspan=3)

win.mainloop()