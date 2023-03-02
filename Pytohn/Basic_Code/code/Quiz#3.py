# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예)
# http://naver.com

# 조건1 : http://을 제외 -> naver.com
# 조건2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 조건3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자내 'e'의 갯수 + "!" 로 구상

# 생성된 비밀번호 예 : nav51!

url = "http://naver.com"
Ex1 = url[7:] #규칙1
Ex2 = Ex1[:Ex1.index(".")] #규칙3-1
i = Ex2[0:3] #규칙3-2
j = len(Ex2) #규칙3-3
k = Ex2.count("e") #규칙3-4
l = "!"
print("{}{}{}{}".format(i,j,k,l))