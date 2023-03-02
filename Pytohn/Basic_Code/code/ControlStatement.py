#if 조건문
from operator import index


weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈" :
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("기온은 어때요?"))
if temp >= 30 :
    print("너무 더워요. 나가지마세요")
elif 10<= temp <30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else :
    print("너무 추워요 나가지마세요")


#for 반복문

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in[0,1,2,3,4] :
    print("대기번호 : {0} ".format(waiting_no))

for waiting_no in range(7) :
    print("대기번호 : {0} ".format(waiting_no))

starbuck = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbuck :
    print("{0}, 커피가 준비되었습니다.".format(customer))

#while

customer = "토르"
index = 5
while index >= 1 :
    print("{0},커피가 준비 되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

#무한 반복
# customer= "아이언맨"
# index=1
# while True :
#     print("{0},커피가 준비되었습니다..호출{1}회".format(customer,index))
#     index -= 1

#조건까지 반복
customer= "토르"
person = "unknown"

while person != customer :
    print("{0},커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# contiue 와 break
absent = [2,3] #결석
no_book = [7] #책을 안가지고 옴
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(no_book))
        break
    print("{0}야, 책읽어봐".format(student))


#한줄로 for문 

#출석 번호가 1 2 3 4, 앞에 100을 붙이기로함 -> 101. 102 ,103, 104
student = [1,2,3,4,5]
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
students=["Iron man", "Thor"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students=["Iron man", "Thor"]
students= [i.upper() for i in students]
print(students)