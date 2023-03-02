import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # indeterminate : 결정되지 않음 / determinate: 결정됨
progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()


def btncmd():
    progressbar.stop() #작동중지

btn = Button(root, text="중지", command=btncmd)
btn.pack()
root.mainloop()