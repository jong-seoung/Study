#표준입출력

print("python","Java", sep=",")
print("python","Java", sep=" vs ")
print("python","Java","JavaScript", sep=",")
print("python","Java", sep=",",end="?") #end의 문장의 끝부분을 " " 값으로 바꿔달라
print("무엇이 더 재미있을까요?")

from ast import While
from pickle import TRUE
import profile
import sys
print("python","Java", file=sys.stdout) #표준 출력으로 문장이 찍힘
print("python","Java", file=sys.stderr) #표준 에러로 문장이 찍힘

# 시험 성적
scores= {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":") # ljust - ()의 수 만큼 공간을 만들고 왼쪽으로 정렬 / rjust - ()의 수 만큼 공간을 만들고오른쪽으로 정렬 

#은행 대기 순번표
#001,002,003,004,...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # Zfill(3) - 3만큼의 공간을 확보하고 빈공간에는 0으로 채우기

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 {0} 입니다.".format(answer))
print(type(answer)) #사용자 입력을 통해 정해진 값은 항상 문자열 형태로 정해짐

#다양한 출력포멧
# 빈자리는 빈 공간으로 두고, 오른쪽 정렬하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일때는 +로 표시, 음수 일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽으로 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 세자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000))

# 세자리마다 콤마를 찍어주기, +-부호도 붙여주기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))

# 세자리마다 콤마를 찍어주기, +-부호도 붙여주기, 자리수 확보 
print(("{0:^<+30,}").format(10000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))

#파일 입출력

# "w"는 쓰기 용도
score_file = open("score.txt","a",encoding= "utf-8") 
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# "a"는 덮어쓰기 용도
score_file = open("score.txt","a",encoding= "utf-8") 
score_file.write("과학:80")
score_file.write("\n코딩:100")
score_file.close()

# 파일에 있는 내용을 한번에 읽어줌
score_file = open("score.txt","r",encoding="utf-8")
print(score_file.read())
score_file.close()

#파일에 있는 내용을 한줄씩 읽어줌
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline() #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
    if not line:
        break
    print(line,end="")
score_file.close()

# list 형태로 저장
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

#pickle
import pickle
profile_file = open("profile.pickle","wb")
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close

# file에 있는 정보를 profile에 불러오기
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close

#with
#파일을 읽고 쓰는데 두줄로 해결되고 매번 close를 사용하지 않아도 되서 좋음

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt","w",encoding="utf-8") as study_file:
    study_file.write("파이썬 공부를 열심히 하고있어요.")

with open("study.txt","r",encoding="utf-8") as study_file:
    print(study_file.read())