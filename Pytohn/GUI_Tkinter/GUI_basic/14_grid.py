from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")
btn1.grid(row=0 , column=0)
btn2.grid(row=1 , column=1)
root.mainloop()