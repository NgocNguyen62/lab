from tkinter import *
from tkinter import messagebox
from sinhvien import *
from giangvien import *
from giaovu import *
from login import *

tk = Tk()
tk.minsize(width=800, height=600)
tk.geometry("600x500")

headingFrame = Frame(tk, bg="deep sky blue", bd = 5)
headingFrame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame, 
                            text="Xin chào",
                            bg='cyan3', fg='black', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
bt = Button(tk, text="Login", command=run)
bt.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
tk.mainloop()