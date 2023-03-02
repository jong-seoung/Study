import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개를 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Coding", interval=0.25)
# pyautogui.write("코딩 연습") # 한글 처리는 안됨

#t e s t를 입력후 왼쪽으로 두번 오른쪽으로 한번 이동후 l a 입력후 엔터
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=1.25) 

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # 쉬프트를 누른 상태에서
# pyautogui.press("4") # 4번을 누르고
# pyautogui.keyUp("shift") # 쉬프트를 뗀다

# 조합키 (Hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

# 간편한 조합기
# pyautogui.hotkey("ctrl","alt","shift","a")
# pyautogui.hotkey("ctrl","a")

# 한글 입력
# pip install pyperclip
import pyperclip
pyperclip.copy("코딩 연습") #"코딩 연습"글자를 클립보드에 저장
pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙어넣기