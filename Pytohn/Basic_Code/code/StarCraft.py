# 일반 유닛
from random import randint


class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):
        Unit.__init__(self, name, hp,speed) # Unit의 클래스를 상속 받아서 사용

        # self.name = name
        # self.hp = hp
        self.damage = damage

    def Attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("현재 {0}의 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.fly_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.fly_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, fly_speed)

    def move (self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)

    #스팀팩 : 일정시간동안 이동 및 공격 속도를 증가, 체력 10감소
    def stimpack(self):
        if self.hp >=10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다.(HP 10감소)".format(self.name))
        else:
            print("{0} : 스팀팩을 사용할수 없습니다.(최소 HP : 10)".format(self.name))

#탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동불가.
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 2)
        self.seize_developed = False

    def set_seize_developed(self):
        if Tank.seize_developed == False:
            return
        
        #현재 시즈모드가 아닐때 --> 시즈모드
        if self.seize_developed == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        #현재 시즈모드 일때, 시즈 모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        
#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,5,2)
        self.clocked = False # 클로킹 모드 (해제 상태)
    
    def clocking(self):
        if self.clocked == True:  #클로킹 모드 --> 모드 해제
            print("{0} : 클로킹 모드를 해제 합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 시작 합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player :  GG")
    print("[Player]님이 퇴장하셨습니다.")

game_start()
#마린 3기 생성
m1= Marine()
m2= Marine()
m3= Marine()

#탱크 2기 생성
t1=Tank()
t2=Tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
Attack_Unit = []
Attack_Unit.append(m1)
Attack_Unit.append(m2)
Attack_Unit.append(m3)
Attack_Unit.append(t1)
Attack_Unit.append(t2)
Attack_Unit.append(w1)

# 전군 이동
for Unit in Attack_Unit:
    Unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed =True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for Unit in Attack_Unit:
    if isinstance(Unit, Marine):
        Unit.stimpack()
    if isinstance(Unit, Tank):
        Unit.set_seize_developed()
    if isinstance(Unit, Wraith):
        Unit.clocking()

# 전군 공격
for Unit in Attack_Unit:
    Unit.Attack("1시")

# 전군 피해
for Unit in Attack_Unit:
    Unit.damaged(randint(5,21)) #공격은 랜덤으로 받음(5~20)

# 게임 종료
game_over()