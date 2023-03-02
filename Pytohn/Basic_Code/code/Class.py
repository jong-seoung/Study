# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
from ast import Pass


name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다".format(name))
print("체력은 {0}, 공격력{1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드/ 시즈모드가 있음
tank_name = "탱크"
tank_hp= 150
tank_damage = 35

tank2_name =  "탱크"
tank2_hp= 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다".format(tank_name))
print("체력은 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(name,location,damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)
attack(tank2_name,"1시",tank2_damage)

# __init__
class Unit:
    def __init__(self, name, hp, damage): # __init__ 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력은 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = Unit("마린",40, 5)
marine2 = Unit("마린",40, 5)
tank = Unit("탱크",150, 35)

# 멤버변수

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80,5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것 (빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))  / wraith1은 클로킹 상태가 아니기때문에 오류가 뜸

# 메소드
class Unit:
    def __init__(self, name, hp, damage): # __init__ 
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력은 {0}, 공격력{1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def Attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.Attack("5시")

#공격을 2번 받는다고 가장
firebat1.damaged(25)
firebat1.damaged(25)

# 상속

class Unit:
    def __init__(self, name, hp, speed): # __init__ 
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):
        Unit.__init__(self, name, hp,speed) # Unit의 클래스를 상속 받아서 사용

        # self.name = name
        # self.hp = hp
        self.damage = damage

#다중 상속

#날수있는 기능을 가진 클라스
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

#발키리 : 공중유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name , "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture= AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500,25,3)

vulture.move("11시")
battlecruiser.move("9시")

#pass

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        Pass

# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

#super

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) #다중 상속을 받을경우 마지막에 상속받는 클라쓰에 대해서만 임의 상수가 호출됨
        self.location = location

