import requests
import re
from bs4 import BeautifulSoup


url="https://search.shopping.naver.com/search/all?query=%EB%85%B8%ED%8A%B8%EB%B6%81&cat_id=&frm=NVSHATC"
headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
res=requests.get(url, headers=headers)
res.raise_for_status()
soup =BeautifulSoup(res.text,"lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())


for item in items:

    #광고 제품은 제외
    ad_badge = item.find("span", attr={"class":"ad-badge-text"})
    if ad_badge:
        print(" 광고 상품 제외합니다.")
        continue

    name = item.find(items[0].find("div", attrs={"class": "name"}).get_text()) # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print(" Apple 제품을 제외합니다.")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
    # 리뷰 100개 이상만 조회
    rate = item.find("strong", attrs={"class":"rating"}) #평점
    if rate:
        rate = rate.get_text()
    else :
        print(" 평점 없는 상품을 제외합니다.")
        rate = "평점 없음"

    rate_cnt = item.find("span", attrs={"class":"rating_total_count"}) # 평점 수
    if rate_cnt:
        rate_cnt = rate.get_text()
        rate_cnt = rate_cnt[1:-1]
        print("리뷰 수", rate_cnt)
    else :
        print(" 평점 없는 상품을 제외합니다.")
        rate_cnt = "평점 없음"

    if float >=4.5 and int(rate_cnt) >= 50:
        print(name,price,rate,rate_cnt)
    