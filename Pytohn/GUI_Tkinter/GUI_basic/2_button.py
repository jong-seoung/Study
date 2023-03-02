from tkinter import *

root = Tk()
root.title ("GUI") #프로그램의 이름

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2") # 여백 설정
btn3.pack() 

btn4 = Button(root, width=10, height=3, text="버튼444444444") # 고정된 크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") #글자색(fg)과 배경색(bg)
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root, image=photo) #내가 원하는 이미지 버튼에 넣기
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text="동작하는 버튼", command=btncmd) # 버튼을 눌렀을때 커맨드 작동시키기
btn7.pack()
root.mainloop()