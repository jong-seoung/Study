import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language":"Ko-KR,Ko"
    }
res=requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# with open("movie.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify()) # html 문서를 이쁘게 출력
