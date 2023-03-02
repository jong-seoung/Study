from struct import pack
from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

txt = Text(root, width=30, height= 5) #여러줄 입력 가능
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #엔터를 입력 불가 (EX)아이디or 비밀번호 입력창
e.pack()
e.insert(0, "한줄만 입력하세요.")

def btncmd():
    print(txt.get("1.0",END)) # 1:첫번째라인, 0: 0번째 column위치
    print(e.get())

    txt.delete("1.0",END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()