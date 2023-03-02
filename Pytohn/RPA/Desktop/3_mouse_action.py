import pyautogui


pyautogui.sleep(3) # 3초 대기
print(pyautogui.position())

pyautogui.click(68,28,duration=1) # 1초 동안 68,28 좌표로 이동후 마우스 클릭

#드래그 드랍 할때 사용
pyautogui.mouseDown()
pyautogui.mouseUp()

#더블 클릭
pyautogui.doubleClick()
pyautogui.click(clicks=500)

# 드ㅡ래그
pyautogui.moveTo(200,200)
pyautogui.mouseDown() # 마우스 버튼을 누른 상태
pyautogui.moveTo(300,300)
pyautogui.mouseUp() # 마우스 버튼을 뗀 상태

# 우클릭, 휠 클릭
pyautogui.sleep(3)
pyautogui.rightClick() # 우클릭
pyautogui.middleClick() # 휠 클릭

# 드래그
pyautogui.moveTo(1344,368)
pyautogui.drag(100,0) # 현재 위치 기준으로 100,0 만큼 드래그
pyautogui.drag(100,0,duration=0.25)
pyautogui.dragTo(1544,368,duration=0.25) # 절대 좌표 기준으로 드래그

pyautogui.scroll(-800) # 양수이면 위 방향으로 음수이면 아래 방향으로 원하는 만큼 이동