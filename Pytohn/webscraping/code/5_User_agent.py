import requests
url = "http://google.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
res = requests.get(url, headers= headers)
print("응답 코드 : ",res.status_code) 

with open("mygoogle1.html","w",encoding="utf8") as f:
    f.write(res.text)