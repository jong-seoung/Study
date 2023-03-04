#include<stdio.h>

// 피라미드를 쌓아라
int main(void) {
	int floor;
	printf("몇 층의 피라미드를 만들어? ");
	scanf_s("%d", &floor);

	// 나의 풀이
	for (int i = 1; i <= floor; i++) {
		for (int k = 0; k < floor - i; k++) {
			printf(" ");
		}
		for (int j = 0; j < i; j++) {
			printf("*");
		}
		for (int j = 1; j < i; j++) {
			printf("*");
		}
		printf("\n");
	}

	// 정답
	for (int i = 0; i < floor; i++) {
		for (int k = i; k < floor - 1; k++) {
			printf(" ");
		}
		for (int j = 0; j < i * 2 + 1; j++) {
			printf("*");
		}
		printf("\n");
	}
}
