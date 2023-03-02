import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 22,21 23,134,208 #1786D0

pixel = pyautogui.pixel(22,21)
print(pixel)

print(pyautogui.PixelMatchesColors(22,21,(23,134,208)))