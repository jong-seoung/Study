# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을때, 총 탑승 승객수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다
# 조건2 : 당신은 소요시간 5분~15분 사이의 승객만 매칭해야합니다.

# (출력문예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [0] 2번째 손님 (소요시간 : 9분)
# [ ] 3번째 손님 (소요시간 : 27분)
# [ ] 4번째 손님 (소요시간 : 35분)
# [ ] 5번째 손님 (소요시간 : 34분)
# ...
# [ ] 50번째 손님 (소요시간 : 45분)
# 총 탑승 승객 : 2분

from ast import ImportFrom
from random import randrange

#내가 푼 방법
count=(0)
for total in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15 :
        riding = "o"
    else :
       riding = "x"
    print("[{0}]{1}번째 손님 (소요시간 : {2}분)".format(riding,total,time))
    if riding== "o" :
        count += 1
    else :
        count += 0
print("총 탑승 승객수 : {0}".format(count))

#정답
cnt = 0 #총 탑승객수
for i in range(1,51): #1~50이라는 수 (승객)
    time= randrange(5, 51) # 5분~50분 소요시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 매칭성공, 탑승객수 증가
        print("[0]{0}번째 손님 (소요시간 : {1}분)".format(total,time))
        cnt += 1
    else : # 매칭에 실패할 경우
        print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(total,time))
print("총 탑승 승객수 : {0}".format(cnt))