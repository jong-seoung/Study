import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

frame = Frame(root)
frame.pack()

Scrollbar = Scrollbar(frame)
Scrollbar.pack(side="right", fill="y")

#set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height= 10, yscrollcommand= Scrollbar.set)
for i in range(1,32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

Scrollbar.config(command=listbox.yview)
root.mainloop()