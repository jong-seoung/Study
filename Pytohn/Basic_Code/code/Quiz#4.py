from cgi import print_directory
from os import lstat
from random import shuffle


# 당신의 학교에서는 파이썬 코딩 대회를 추최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
# 추천 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추천하되 중복불가
# 조건3 random모듈의 shuffle와 sample을 활용

# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다--
from random import *
lst = range(1,21)
lst = list(lst)
shuffle(lst)
winners = sample(lst,4)

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")