#함수
def opena_ccount():
    print("새로운 계좌가 생성되었습니다.")
opena_ccount()

#전달값과 반환값

#입금
def deposite(balance,money):
    print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance+money))
    return balance+money

#출금
def withdraw(balance, money):
    if balance >= money:  #잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 남은 잔액은 {0}입니다.".format(balance))

#출금 수수료
def withdraw_night(balance, money):
    commission = 100 #수수료100원
    return commission, balance - money - commission


balance =  0  #잔액

#1000원 입금
balance = deposite(balance,1000)

#500원 출금
balance = withdraw(balance, 500)

#저녘에는 수수료가 제외되고 출금되게
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}이며, 잔액은 {1}원 입니다.".format(commission, balance))

#1000원 출금 / 잔액이 부족할 경우
balance = withdraw(balance, 1000)

#기본값
def profile(name, age, main_lang):
    print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 27, "자바")

#같은 나이 같은 학년 같은반 같은수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t 나이: {1}\t 주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")

#키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(name="김태호", age=20, main_lang="파이썬")
#순서가 뒤 섞여 있어도 함수가 잘 전달됨

#가변인자 
# *을 사용하여 변수 선언 해주기
def profile(name,age,*language):
    print("이름: {0} \t나이: {1}\t".format(name,age),end="")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"파이썬","자바","c","c++")
profile("김태호",15,"파이썬","자바","","")

#지역변수와 전역변수
gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 공간에 있는 gun을 사용
    gun=gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경계 근무를 나감
print("남은 총 : {0}".format(gun))


#return 사용
gun = 10

def checkpoint_ret(gun, soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))