import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1000X1000")

browser = webdriver.Chrome(options=options) 

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"link_login")
elem.click()

# 3. id, pw 입력
browser.find_element("id","id").send_keys("naver_id")
browser.find_element("id","pw").send_keys("pw")

# 4. 로그인 버튼 클릭
browser.find_element("id","log.login").click()

# 3초 대기
time.sleep(3)

# 5. 아이디를 새로 입력
browser.find_element("id","id").clear() # 기존 입력값을 지움
browser.find_element("id","id").send_keys("my_id")

# 3초 대기
time.sleep(3)

browser.get_screenshot_as_file("naver_login.png")