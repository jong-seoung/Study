import pyautogui

# fw = pyautogui.getActiveWindows() # 현재 활성화된 창 (vs코드)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 25 , fw.top + 20)

# for w in pyautogui.getAllWindows(): #모든 윈도우 가져오기
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: #현재 활성화되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가지고 오기)

if w.isMaximized == False: #현재 최대화가 되지 않았다면
    w.maximize()

pyautogui.sleep(1)

if w.isMinimized == False: #현재 최소화가 되지 않았다면
    w.minimize()

pyautogui.sleep(1)

w.restore() # 원상태복구

w.close() #윈도우 닫기