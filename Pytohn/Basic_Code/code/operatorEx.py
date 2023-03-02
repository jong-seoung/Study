#연산자
print(1+1) 
print (3-2)
print(5*2)
print(6/3)


print(2**3) # 제곱수 구하기
print(5%3) # 나머지 구하기
print(5//3) #몫 구하기

#비교 연산자
print(10 > 3) # True
print( 4 >= 7) # False

print(3 == 3) # True
print(3 == 4) # False
print( 3 + 4 == 7) # True

print(1 != 3) # True 
print(not(1 != 3)) #False

#둘다 참일경우 참
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

#둘중 하나만 참이여도 참
print((3>0) or (3>5)) # True
print((3>0) | (3>5)) # True

# 숫자 처리함수
print(abs(-5)) # 절대값
print(pow(4,2)) # 제곱수 4^2
print(max(5,13)) # 최대값
print(min(5,12)) # 최소값
print(round(3.14)) # 반올림

from math import * 
print(floor(4.99)) # 버림
print(ceil (3.14)) # 올림
print(sqrt (16)) # 제곱근

#랜덤함수 - 난수

from random import *

#미만과 이하 잘 보기
print(random()) # 0.0부터 1.0미만의 임의의 값 생성
print(random() * 10 ) # 0.0부터 10.0미만의 임의의 값 생성
print(int(random())) # 0부터 10미만의 임의의 값 생성 - 정수만
print(int(random()* 10 ) + 1 ) # 1부터 10이하의 임의의 값 생성
print(int(random() * 45 ) + 1 ) # 1부터 45이하의 임의의 값을 생성

print(randrange(1,46)) # 1부터 45이하의 임의의 값을 생성
print(randint(1,45)) # 1부터 45이하의 값을 생성해줌