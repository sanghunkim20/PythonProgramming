import tkinter as tk
from tkinter import *

# Making Calculator
root = Tk()
root.title("실습")
root.geometry("320x250")

# 첫째줄
btn_num = Button(root, text="Num", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_num.grid(row=0, column=0, sticky=N+E+S+W, padx=2, pady=2)
btn_div.grid(row=0, column=1, sticky=N+E+S+W, padx=2, pady=2)
btn_mul.grid(row=0, column=2, sticky=N+E+S+W, padx=2, pady=2)
btn_sub.grid(row=0, column=3, sticky=N+E+S+W, padx=2, pady=2)

# 둘째줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)

btn_7.grid(row=1, column=0, sticky=N+E+S+W, )
