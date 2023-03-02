import time 
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

p_var1 = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var1)
progressbar.pack()


def btncmd():
    for i in range(101):
        time.sleep(0.01) #0.01초 대기

        p_var1.set(i) # progress bar 의 값 설정
        progressbar.update() # ui 업데이트
        print("{0}% 남았습니다.".format(p_var1.get( )))


btn = Button(root, text="시작", command=btncmd)
btn.pack()
root.mainloop()