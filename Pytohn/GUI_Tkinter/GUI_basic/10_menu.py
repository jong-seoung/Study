from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름
root.geometry("640x480") # 프로그램의 크기

def create_new_file():
    print("새 파일을 만듭니다")
menu = Menu(root)

# file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분선 긋기
menu_file.add_command(label="Open file...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택 1)

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View메뉴 (체크 박스)
menu_View = Menu(menu, tearoff=0)
menu_View.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_View)



root.config(menu=menu)
root.mainloop()