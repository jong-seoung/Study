#include<stdio.h>
#include<time.h>

int main(void) {
	// 버스를 탄다고 가정 학생 / 일반인으로 구분
	int age = 15;
	if (age >= 20) {
		printf("일반인 입니다.\n");
	}
	else {
		printf("학생입니다.\n");
	}

	// 초등학생 중학생 고등학생으로 구분
	if (17 <= age && age <= 19) {
		printf("고등학생입니다.\n");
	}
	else if (14 <= age && age<= 16){
		printf("중학생입니다.\n");
	}
	else if (8 <= age && age <= 13){
		printf("초등학생입니다.\n");
	}
	else {
		printf("성인입니다.\n");
	}

	// break / continue
	// 1번부터 30번까지 있는 반에서 1번부터 5번까지 조별 발표를한다.

	for (int i = 1; i <= 30; i++) {
		if (i >= 6) {
			printf("나머지 학생은 집에가세요. \n");
			break;
		}
		printf("%d번 학생은 발표를 하세요. \n",i);
	}

	// 1번부터 30번까지 있는 반에서 7번학생은 아파서 결석
	// 7번학생을 제외하고 6번부터 10번까지 발표를 하세요

	for (int j = 1; j <= 30; j++) {
		if (j >= 6 && j <= 10) {
			if (j == 7) {
				printf("%d번 학생은 결석입니다. \n", j);
				continue;
			}
			printf("%d번 학생은 발표를 하세요. \n", j);
		}
	}

	// && - and / || - or
	int a = 10;
	int b = 10;
	int c = 12;
	int d = 12;
	if (a == b && c == d) {
		printf("a와 b는 같고 c와 d도 같습니다. \n");
	}
	else {
		printf("값이 서로 다릅니다 \n");
	}

	// 가위 0 바위 1 보 2
	srand(time(NULL));
	int i = rand() % 3;
	if (i == 0) {
		printf("가위 \n");
	}
	else if (i == 1) {
		printf("바위 \n");
	}
	else if (i == 2) {
		printf("보 \n");
	}

	// switch
	switch (i) {
	case 0:
		printf("가위 \n");
		break;
	case 1:
		printf("바위 \n");
		break;
	case 2:
		printf("보 \n");
		break;
	default:
		printf("몰라요 \n");
	}

	int num = rand() % 100 + 1; // 1~100사이의 숫자
	printf("숫자 : %d \n", num);
	int answer = 0;
	int chance = 5;

	while (chance > 0) {
		printf("남은 기회 : %d \n", chance--);
		printf("숫자를 맞춰보세요(1~100) : ");
		scanf_s("%d", &answer);

		if (answer > num) {
			printf("DOWN \n");
		}
		else if (answer < num) {
			printf("UP \n");
		}
		else if (answer == num){
			printf("정답입니다. \n");
			break;
		}
		else {
			printf("알수 없는 오류가 발생하였습니다. \n");
		}

		if (chance == 0) {
			printf("모든 기회를 다 사용하셨습니다. \n");
		}
	}

	return 0;
}