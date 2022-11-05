from tkinter import *
from tkinter import messagebox
from sinhvien import *
from giangvien import *
from giaovu import *


def run():
    global usrpassEntry, usrnameEntry, root
    root = Tk()
    root.title("Trường Đại học Khoa học Tự nhiên")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    headingFrame1 = Frame(root, bg="deep sky blue", bd = 5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
    headingLabel1 = Label(headingFrame1, 
                            text="Đăng nhập",
                            bg='cyan3', fg='black', font=('Courier', 15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame = Frame(root, bg='cyan3')
    frame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    usrnameLabel = Label(frame, text="Tên đăng nhập: ",bg='cyan3', fg='black')
    usrnameLabel.place(relx=0.1, rely=0.2, relheight=0.16)
    usrnameEntry = Entry(frame)
    usrnameEntry.place(relx=0.3, rely=0.2, relwidth=0.42, relheight=0.16)

    usrpassLabel = Label(frame, text="Mật khẩu: ",bg='cyan3', fg='black')
    usrpassLabel.place(relx=0.1, rely=0.4, relheight=0.16)
    usrpassEntry = Entry(frame, show='*')
    usrpassEntry.place(relx=0.3, rely=0.4, relwidth=0.42, relheight=0.16)

    bt = Button(root, text="Login", command=validateLogin)
    bt.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()

def validateLogin():
    usrname = usrnameEntry.get()
    pw = usrpassEntry.get()

    if usrname == "student":
        if pw == "student123":
            view1()
        else:
            messagebox.showinfo("Lỗi!", "Mật khẩu sai")
    elif usrname == "lecturer":
        if pw == "lecturer123":
            view2()
        else:
            messagebox.showinfo("Lỗi!", "Mật khẩu sai")
    elif usrname == "giaovu":
        if pw == "giaovu123":
            giaovu()
        else:
            messagebox.showinfo("Lỗi!", "Mật khẩu sai")
    else:
        messagebox.showinfo("Lỗi!", "Tài khoản không tồn tại")

    root.destroy()


