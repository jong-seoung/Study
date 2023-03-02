# 메모장 만들기 

# title : 제목 없음 - windows 메모장
# 메뉴 : 파일 , 편집 , 서식, 보기, 도움말
# 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리
#  - 열기 : mynote.txt 파일 내용 열어서 보여주기
#  - 저장 : mynote.text 파일에 현재 내용 저장
#  - 끝내기 : 프로그램 종료
# 프로그램 시작 시 본문은 비어 있는상태
# 하단 statues 바는 필요 없음
# 프로그램 크기, 위치는 자유롭게 하되, 크기 조정 가능해야함
# 본문 우측에 상하 스크롤바 넣기
from genericpath import isfile
import os
from tkinter import *

#열기, 저장 파일 이름
filename = "mynote.txt"

root = Tk()
root.title ("제목 없음 - windows 메모장") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기
root.resizable(True, True)

# 메뉴 구현
menu = Menu(root)

def open_file():
    if os.path.isfile(filename):
        with open(filename,"r",encoding="utf-8") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

def save_file():
    with open(filename,"w",encoding= "utf-8") as file:
        file.write(text.get("1.0", END))


    
    

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = open_file)
menu_file.add_command(label="저장", command = save_file)
menu_file.add_command(label="끝내기", command = root.quit)
menu.add_cascade(label="파일", menu = menu_file)

menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


#스크롤 바 만들기
Scrollbar = Scrollbar(root)
Scrollbar.pack(side="right", fill="y")


# 본문 영역
text = Text(root, yscrollcommand= Scrollbar.set)
text.pack(fill="both",expand= True)

Scrollbar.config(command=text.yview)
root.config(menu=menu)
root.mainloop()