# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "000516-1234567"

print("성별 : " + jumin[7])
print("출생년도 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) #처음부터 6자리 직전까지 가지고오기
print("뒤 7자리 : " + jumin[7:]) # 7자리부터 끝까지
print("뒤7자리 (뒤에서부터) : " + jumin[-7:] ) #맨뒤에 7번째부터 끝까지

#문자열처리 함수
Python = "Python is Amazing"
print(Python.lower()) # 전부 소문자로 표시
print(Python.upper()) # 전부 대문자로 표시
print(Python[0].isupper()) # 첫번째 자리 숫자가 대문자인지?
print(len(Python)) # 길이를 알려줌
print(Python.replace("Python","Java")) # Python이란 글자를 Java라는 글자로 바꿔줌

index = Python.index("n") # n이 있는 위치를 알려줌
print(index)
index = Python.index("n",index + 1) # 두번째 n이 있는 위치를 알려줌
print(index)

print(Python.find("n")) # index와 같은 역할을 하지만 원하는 글자가 없을경우 -로 표시해줌

print(Python.count("n")) #n이 몇번 나오는지 알려줌

#문자열 포멧
print("a","b")
print("a"+"b")

# 방법 1
print("나는 %d살입니다." %20) # %d뒤에는 정수 값만 넣을수 있음
print("나는 %s을 좋아해요" %"파이썬") 
print("Apple은 %c로 시작해요" %"A") # %c뒤에는 문자 값만 넣을수 있음
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

#방법2
print("나는{}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

#방법3
print("나는 {age}살이며,{color}색을 좋아해요".format(age= 20, color="빨간"))
print("나는 {age}살이며,{color}색을 좋아해요".format(color="빨간",age = 20))

#방법4 (v 3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요")

#탈출문자
print("백문이 불여일견  \n 백견이 불여일타") # \n은 줄바꿈
print("저는 '백종성' 입니다.")
print('저는 "백종성" 입니다.')
print("저는 \"백종성\" 입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\jongseoung\\Documents\\Python\\SelfStudy>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")

# \b : 백스페이스 열활(한글자 지움)
print("Redd\bApple")

# \t : 탭
print("Red \t Apple")