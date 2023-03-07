#include<stdio.h>
#include<time.h>

int getRandomNumver(int level);
void showQuestion(int level, int num1, int num2);
void success();
void pail(int count);

int main(void) {
	// 문이 5개가 있고 각 문마다 점점 어려운 수식 퀴즈가 출제 (랜덤방식으로 출제)
	// 맞히면 통과 틀리면 실패
	int count = 0;
	for (int i = 1; i <= 5; i++) {
		int num1 = getRandomNumver(i);
		int num2 = getRandomNumver(i);
		showQuestion(i, num1, num2);

		int answer = -1;
		scanf_s("%d", &answer);

		if (answer == -1) {
			printf("프로그램을 종료합니다. ");
			exit(0);
		}
		else if (answer == num1 * num2) {
			success();
			count++;
		}
		else {
			pail(count);
			break;
		}
	}

}

int getRandomNumver(int level) {
	srand(time(NULL));
	return rand() % (level * 7) + 1;
}

void showQuestion(int level, int num1, int num2) {
	printf("\n\n ######## %d번째 비밀번호 (종료:-1) ######## \n\n",level);
	printf("\n 비밀번호를 입력하세요. \n");
	printf("\n %d X %d ? ", num1, num2);
}

void success() {
	printf(">> GOOD! 정답입니다.  \n");
}

void pail(int count) {
	printf("실패입니다. \n");
	printf("당신은 %d개의 문제를 맞히셨습니다. \n",count);
}