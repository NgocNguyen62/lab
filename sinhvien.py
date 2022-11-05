from tkinter import *
from PIL import ImageTk, Image

def view1():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="cyan3", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(headingFrame1, text="Thời khóa biểu sinh viên", bg='cyan3', fg='black', font=('Courier', 15))
    label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    quitBt = Button(root, text="Quit", command=root.destroy)
    quitBt.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()