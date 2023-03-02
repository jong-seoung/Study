# pip install pyautogui 
import pyautogui

size = pyautogui.size() # 현재 화면의 스크린 사이즈를 가지고옴
print(size) # 가로 세로 크기를 알 수 있음 
# size[0] : 가로 width
# size[1] : 세로 height