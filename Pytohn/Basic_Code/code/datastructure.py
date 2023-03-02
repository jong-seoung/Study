#리스트

from traceback import print_tb


subway = [10,20,30]
print(subway)

subway = [ "유재석" , "조세호" , "박명수"]
print(subway)

#조세호씨는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list=[ 3,4,6,1,2,5]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list= [ "조세호", 20 ,True]
print(mix_list)

#리스트 확장
num_list= [1,2,3,4,5]
num_list.extend(mix_list)
print(num_list)

cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) 
# print(cabinet[5]) 변수에 원하는 값이 없으면 오류가 나타나고 프로그램이 중지됨
# print(cabinet.get(5)) 변수에 값이 없으면 none이 표시되고 프로그램이 진행됨
print(cabinet.get(5, "사용가능"))

print(3 in cabinet) # True, False로 표시됨 ( 값이 있으면 True)

# 새로운 손님
print(cabinet)
cabinet["c-20"] = "조세호"

# 원래 있던 값에 넣으면 덮어쓰기 됨

# 간 손님
del cabinet["c-20"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key,value 쌍으로 출력
print(cabinet.items())

# 값 초기화
cabinet.clear()
print(cabinet)

# 튜플
# 리스트와는 다르게 내용 변경과 추가가 불가능함 - 속도가 리스트보다 빨라서 변경되지 않는 목록을 사용할때 튜플을 사용

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") - 튜플은 add가 불가능함

#튜플 사용 예시
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (set)
# 중복이 안됨, 순서 없음
my_set={1,2,3,3,3}
print(my_set)

java= { "유재석", "김태호", "양세형"}
python = {"유재석","박명수"}

#교집합 (java와 python을 모두 할수 있는 개발자)
print(java&python)
print(java.intersection(python))

#합집합 (java나 python중 하나라도 할수 있는 개발자)
print(java | python)
print(java.union(python)) #순서가 없음

#차집합 (java는 할수있지만 python은 할수 없는 개발자)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹은 개발자
java.remove("김태호")
print(java)

#자료구조의 변경
menu={"커피", "우유", "주스"}
print(menu, type(menu))

# 리스트로 변경
menu=list(menu)
print(menu, type(menu))

# 튜플로 변경
menu= tuple(menu)
print(menu, type(menu))

#세트로 변경
menu= set(menu)
print(menu, type(menu))