from struct import pack
from tkinter import *
from tokenize import single_quoted

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

listbox = Listbox(root, selectmode="extended", height=0) 
#single : 하나만 선택가능 , extended : 여러개 선택가능 / height는 나타내는 목록의 갯수(0은 갯수만큼 표시)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    # 맨뒤의 항목을 삭제
    # listbox.delete(END) 
    
    # 갯수확인
    # print("리스트에는", listbox.size(),"개가 있어요")

    #항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 :", listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환) Ex)(1,2,3)
    print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()