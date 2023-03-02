import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

#가는 날 선택 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 이번달 27일, 28일 선택
time.sleep(3)
browser.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/div[8]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button')[0].click()
browser.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/div[8]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button')[0].click()

# 출발 지역 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/i').click()
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,"autocomplete_input__1vVkF")
elem.send_keys("김포")
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[8]/div[2]/section/div/a/div/div[1]/i[1]').click()

# 도착 지역 선택
time.sleep(3)
elem2 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/i')
elem2.click()
time.sleep(3)

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[8]/div[1]/div/input').send_keys("제주")
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[8]/div[2]/section/div/a/div/div[1]/i[1]').click()

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

try:
    # 성공시 동작 실행
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_element_located)((By.XPATH,'//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button'))
    print(elem.text)
finally:
    #실행시 브라우저 종료
    browser.quit()
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button')
# print(elem.text)