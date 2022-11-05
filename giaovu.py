from tkinter import *
from sinhvien import *
from giangvien import *

def giaovu():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    frame1 = Frame(root, bg="cyan3", bd = 5)
    frame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label1 = Label(frame1, text="Giáo vụ khoa", bg='cyan3', fg='black', font=('Courier', 15))
    label1.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    bt1 = Button(root, text="Xem TKB", bg='cyan3', fg='black', command=view)
    bt1.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.1)

    bt2 = Button(root, text="Nhập TKB", bg='cyan3', fg='black', command=input)
    bt2.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.1)

    bt3 = Button(root, text="Sửa TKB", bg='cyan3', fg='black', command=change)
    bt3.place(relx=0.50, rely=0.4, relwidth=0.25, relheight=0.1)

    bt4 = Button(root, text="Xóa TKB", bg='cyan3', fg='black', command=delete)
    bt4.place(relx=0.50, rely=0.6, relwidth=0.25, relheight=0.1)

    root.mainloop()

def view():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="cyan3", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(headingFrame1, text="Xem thời khóa biểu", bg='cyan3', fg='black', font=('Courier', 15))
    label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    bt1 = Button(root, text="TKB sinh viên", bg='cyan3', fg='black', command=view1)
    bt1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    bt2 = Button(root, text="TKB giảng viên", bg='cyan3', fg='black', command=view2)
    bt2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    root.mainloop()

def input():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="cyan3", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(headingFrame1, text="Nhập Thời khóa biểu", bg='cyan3', fg='black', font=('Courier', 15))
    label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    root.mainloop()

def change():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="cyan3", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(headingFrame1, text="Sửa thời khóa biểu", bg='cyan3', fg='black', font=('Courier', 15))
    label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    root.mainloop()
def delete():
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="cyan3", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    label = Label(headingFrame1, text="Xóa Thời khóa biểu", bg='cyan3', fg='black', font=('Courier', 15))
    label.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    root.mainloop()
