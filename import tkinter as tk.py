import tkinter as tk
from tkinter import * 

# 메소드
def click(n):
    a = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(a)+str(n))

def add():
    global first
    global method
    first = int(ent.get())
    method = "add"
    ent.delete(0, END)

def sub():
    global first
    global method
    first = int(ent.get())
    method = "sub"
    ent.delete(0, END)

def mul():
    global first
    global method
    first = int(ent.get())
    method = "mul"
    ent.delete(0, END)

def div():
    global first
    global method
    first = int(ent.get())
    method = "div"
    ent.delete(0, END)

def click_ent():
    global second
    second = int(ent.get())
    ent.delete(0, END)
    if method == "add":
        ent.insert(0, first+second)
    elif method == "sub":
        ent.insert(0, first-second)
    elif method == "mul":
        ent.insert(0, first*second)
    elif method == "div":
        ent.insert(0, first/second)
    


# 계산기 GUI
root = Tk()
root.title("계산기")
root.geometry("320x250")

#첫줄
btn_num = Button(root, text="num", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2, command=div)
btn_mul = Button(root, text="*", width=5, height=2, command=mul)
btn_sub = Button(root, text="-", width=5, height=2, command=sub)

btn_num.grid(row=0, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_div.grid(row=0, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_mul.grid(row=0, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_sub.grid(row=0, column=3, sticky=N+E+W+S, padx=2, pady=2)

#둘째줄
btn_7 = Button(root, text="7", width=5, height=2, command=lambda: click(7))
btn_8 = Button(root, text="8", width=5, height=2, command=lambda: click(8))
btn_9 = Button(root, text="9", width=5, height=2, command=lambda: click(9))
btn_add = Button(root, text="+", width=5, height=2, command=add)

btn_7.grid(row=1, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_8.grid(row=1, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_9.grid(row=1, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_add.grid(row=1, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)

#셋째줄
btn_4 = Button(root, text="4", width=5, height=2, command=lambda: click(4))
btn_5 = Button(root, text="5", width=5, height=2, command=lambda: click(5))
btn_6 = Button(root, text="6", width=5, height=2, command=lambda: click(6))

btn_4.grid(row=2, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_5.grid(row=2, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_6.grid(row=2, column=2, sticky=N+E+W+S, padx=2, pady=2)

#넷째줄
btn_1 = Button(root, text="1", width=5, height=2, command=lambda: click(1))
btn_2 = Button(root, text="2", width=5, height=2, command=lambda: click(2))
btn_3 = Button(root, text="3", width=5, height=2, command=lambda: click(3))
btn_ent = Button(root, text="enter", width=5, height=2, command=click_ent)

btn_1.grid(row=3, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_2.grid(row=3, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_3.grid(row=3, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_ent.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)

#다섯째줄
btn_0 = Button(root, text="0", width=5, height=2, command=lambda: click(0))
btn_dot = Button(root, text=".", width=5, height=2)

btn_0.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S, padx=2, pady=2)
btn_dot.grid(row=4, column=2, sticky=N+E+W+S, padx=2, pady=2)

# text 창
label = Label(root, text="Result")
ent =Entry(root, width=30)
label.grid(row=5, column=0)
ent.grid(row=5, column=1, columnspan=3)
root.mainloop()