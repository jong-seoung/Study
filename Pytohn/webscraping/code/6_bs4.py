from cgitb import text
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#페이지에 대한 이해도가 높을때
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup에서 제일 처음 발견되는 a를 출력
# print(soup.a.attrs) # a태그가 가지고 있는 속성 정보를 출력
# print(soup.a["href"]) # a의 href의 속성 값 정보 출력

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # class값이 Nbtn_upload인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class값이 Nbtn_upload인 값을 찾아줘
# print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="청춘 블라썸")
print(webtoon)