from selenium import webdriver
from selenium.webdriver.common.by import By

browser =webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME,"link_login")
elem
elem.click()
browser.back() # 뒤로가기
browser.forward() # 앞으로 가기
browser.refresh() # 새로고침
elem = browser.find_element(By.ID,"query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("구글")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements(By.tag,"a") # 모든 정보 가지고오기 
for e in elem:
    e.get_attribute("href")

elem = browser.find_element('xpath',"//*[@id='search_btn']/span[2]") # xpath로 설정
elem.click() 
browser.quit() # 브라우저 닫기
exit()