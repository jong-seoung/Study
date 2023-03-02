from multiprocessing.sharedctypes import Value
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

Values = [str(i) + "일" for i in range(1,32)] # 1~31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=Values ,state="readonly") #state="readonly" 로 하면 읽기 전용으로 바뀌어서 임의로 목록 변경 불가
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

def btncmd():
    print(combobox.get()) #선택된 값 표시

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()