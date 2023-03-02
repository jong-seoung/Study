import pyautogui

# file_menu = pyautogui.locateOnScreen("Desktop//file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 화면 해상도, 이미지가 변경되면 오류가 날 가능성이 매우 높음

# 화면에 중복되는 이미지가 여러개 있을 경우 처리법
# for i in pyautogui.locateAllOnScreen("Desktop//file_menu.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# 처음 나오는 이미지만 클릭하고 넘어가는 법
# check_box = pyautogui.locateOnScreen("Desktop//file_menu.png")
# pyautogui.click(check_box)

### 속도 개선
# 1. GrayScale - 흑백으로 만든 후 탐색 
# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png", grayscale=True) # 정확도는 떨어질 수 있음
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("Desktop//trash_icon.png", region=x,y,width,height) # 탐색 시작 위치 x,y
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정 ## pip install opencv-python 설치 필요
# run_btn = pyautogui.locateOnScreen("Desktop//run_btn.png", confidence=0.9) #90퍼센트이상 일치하면 작동
# pyautogui.moveTo(run_btn)

### 자동화 대상이 바로 보여지지 않는 경우

# 1. 계속 기다리기
# notepad = pyautogui.locateOnScreen("Desktop//file_menu_notepad.png")
# if notepad:
#     pyautogui.click(notepad)
# else:
#     print("발견 실패")

# while notepad is None:
#     notepad = pyautogui.locateOnScreen("Desktop//file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(notepad)

# 2. 일정 시간동안 기다리기
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정 
# notepad = None
# while notepad is None:
#     notepad = pyautogui.locateOnScreen("Desktop//file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

# pyautogui.click(notepad)

def find_target(img_file, timeout = 30):
    start = time.time()
    target=None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout =30):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate program.")
        sys.exit()

my_click("Desktop//file_menu_notepad.png", 10)