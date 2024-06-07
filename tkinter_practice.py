import tkinter as tk
from tkinter import *
"""
window = Tk() # Tk클래스를 호출하여 메인 윈도우 객체 생성
label = Label(window, text="Hello tkinter")
label.pack() # 레이블을 창에 배치
window.mainloop()
"""

"""
root = tk.Tk()

test = tk.Label(root, text="Red", bg="red", fg="white")
test.pack(side=tk.BOTTOM)
test = tk.Label(root, text="Green", bg="green", fg="white")
test.pack(side=tk.BOTTOM)
tk.mainloop()
"""

"""
window = Tk()
button = Button(window, text="Click!",
                bg="green", fg="white",
                width=80, height=2)
button.pack()
window.mainloop()
"""

"""
window = Tk()
f = Frame(window)
b1 = Button(f, text="Box 1", bg="red", fg="white")
b2 = Button(f, text="Box 2", bg="green", fg="white")
b3 = Button(f, text="Box 3", bg="orange", fg="white")
b4 = Button(f, text="Box 4", bg="pink", fg="white")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(window, text=" This label is placed above the buttons")
l.pack()
f.pack()
window.mainloop()
"""
"""
def process():
    print("click done.")

window = Tk()
button = Button(window, text="Click!", command=process)
button.pack()
window.mainloop()
"""

"""
window = Tk()
counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = "click counter:" + str(counter)

label = Label(window, text="waiting")
label.pack()
button = Button(window, text="increment", command=clicked).pack()
window.mainloop()
"""

# 함수
def click(n):
    a=ent.get()
    ent.delete(0, END)
    ent.insert(0, str(a)+str(n))

def click_add():
    global first
    global method
    first = int(ent.get())
    method = "add"
    ent.delete(0, END)

def click_sub():
    global first
    global method
    first = int(ent.get())
    method = "sub"
    ent.delete(0, END)

def click_mul():
    global first
    global method
    first = int(ent.get())
    method = "mul"
    ent.delete(0, END)

def click_div():
    global first
    global method
    first = int(ent.get())
    method = "div"
    ent.delete(0, END)

def click_ent():
    global second
    second = int(ent.get())
    ent.delete(0, END)
    print(first, second)
    if method == "add":
        ent.insert(0, first+second)
    elif method == "sub":
        ent.insert(0, first-second)
    elif method == "mul":
        ent.insert(0, first*second)
    elif method == "div":
        ent.insert(0, first/second)

# Making 계산기
root = Tk()
root.title("실습")
root.geometry("320x250")

#첫줄
btn_num=Button(root, text="Num", width=5, height=2)
btn_div=Button(root, text="/", width=5, height=2, command=click_div)
btn_mul=Button(root, text="*", width=5, height=2, command=click_mul)
btn_sub=Button(root, text="-", width=5, height=2, command=click_sub)

btn_num.grid(row=0, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_div.grid(row=0, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_mul.grid(row=0, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_sub.grid(row=0, column=3, sticky=N+E+W+S, padx=2, pady=2)

#둘째줄
btn_7=Button(root, text="7", width=5, height=2, command=lambda: click(7))
btn_8=Button(root, text="8", width=5, height=2, command=lambda: click(8))
btn_9=Button(root, text="9", width=5, height=2, command=lambda: click(9))
btn_add=Button(root, text="+", width=5, height=2, command=click_add)

btn_7.grid(row=1, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_8.grid(row=1, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_9.grid(row=1, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_add.grid(row=1, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)

#셋째줄
btn_4=Button(root, text="4", width=5, height=2, command=lambda: click(4))
btn_5=Button(root, text="5", width=5, height=2, command=lambda: click(5))
btn_6=Button(root, text="6", width=5, height=2, command=lambda: click(6))

btn_4.grid(row=2, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_5.grid(row=2, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_6.grid(row=2, column=2, sticky=N+E+W+S, padx=2, pady=2)

#넷째줄
btn_1=Button(root, text="1", width=5, height=2, command=lambda: click(1))
btn_2=Button(root, text="2", width=5, height=2, command=lambda: click(2))
btn_3=Button(root, text="3", width=5, height=2, command=lambda: click(3))
btn_ent=Button(root, text="enter", width=5, height=2, command=click_ent)

btn_1.grid(row=3, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_2.grid(row=3, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_3.grid(row=3, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_ent.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)

#다섯째줄
btn_0=Button(root, text="0", width=5, height=2, command=lambda: click(0))
btn_dot=Button(root, text=".", width=5, height=2)

btn_0.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S, padx=2, pady=2)
btn_dot.grid(row=4, column=2, sticky=N+E+W+S, padx=2, pady=2)

# text 창
ent=Entry(root, width=30)
ent.grid(row=5, column=0, columnspan=4)
root.mainloop()