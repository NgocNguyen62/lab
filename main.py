import tkinter as tk
from sinhvien import *
from giangvien import *
from giaovu import *
root = tk.Tk()
root.title("Trường Đại học Khoa học Tự nhiên")
root.minsize(width=800, height=600)
root.geometry("600x500")

headingFrame1 = tk.Frame(root, bg="deep sky blue", bd = 5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel1 = tk.Label(headingFrame1, 
                        text="Chọn đối tượng",
                        bg='deep sky blue', fg='black', font=('Courier', 15))
headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

headingFrame2 = tk.Frame(root)
headingLabel2 = tk.Label(headingFrame2, text = "Chọn đối tượng", font=('Courier', 10))
headingLabel2.place(relx=2, rely=2, relwidth=1, relheight=1)

bt1 = tk.Button(root, text="Sinh viên", bg='sky blue', fg='black', command=view1)
bt1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

bt2 = tk.Button(root, text="Giảng viên", bg='sky blue', fg='black', command=view2)
bt2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

bt3 = tk.Button(root, text="Giáo vụ khoa", bg='sky blue', fg='black', command=giaovu)
bt3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

root.mainloop()