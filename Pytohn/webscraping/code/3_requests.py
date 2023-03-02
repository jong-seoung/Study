import requests
res = requests.get("http://google.com")
# res = requests.get("https://www.anyang.ac.kr/main/activities/school-cafeteria.do")
print("응답 코드 : ",res.status_code) # 200이면 정상

# if을 통한 확인
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# res.raise_for_status() # 문제가 생겼을때 오류를 내고 프로그램을 종료 시켜줌
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

#파일로 구글 html 가지고오기
with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)