import pyautogui
# pyautogui.FAILSAFE = False / 마우스가 귀퉁이 밖으로 나가도 종료되지않음 / 추천 하지 않음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep를 적용

# 마우스 위치 및 색을 알려주는 프로그램
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100,100)
    pyautogui.sleep(1)