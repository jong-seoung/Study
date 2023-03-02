# 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) x 22
# 여자 : 남자 : 키(m) X 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)

# 조건2 :  표준 체중은 소수점 둘째자리 까지 표시

# 출력 예제
# 키 175cm의 남자의 표준 체중은 67.38kg입니다.

#내가 푼 방법
def std_weight(height,gender):
    if gender == "남자":
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg입니다.".format(height,gender,round(height * height * 22 / 10000,2)))
        return height * height * 22
    else:
        print("키 {0}cm의 {1}의 표준 체중은 {2}kg입니다.".format(height,gender,round(height * height * 21 / 10000,2)))
    return height * height * 21

std_weight(175,"남자")

#정답
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100 ,gender))
print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height,gender,weight))