#include<stdio.h>

int main(void) {

	// for 문
	for (int i = 0; i <= 10; i++) {
		printf("%d For\n", i);
	}

	// while 문
	int i = 0;
	while (i <= 10) {
		printf("%d While\n", i);
		i++;
	}

	i = 0;
	do {
		printf("%d do While\n", i);
		i++;
	} while (i <= 10);

	// 2중 반복문 
	for (int i = 1; i <= 3; i++) {
		printf("첫번째 반복문 : %d\n", i);
		
		for (int j = 1; j <= 5; j++) {
			printf("  두번째 반복문 : %d\n", j);
		}
	}

	// 구구단 만들기
	for (int i = 1; i <= 9; i++) {
		printf("%d단 \n", i);
		for (int j = 1; j <= 9; j++) {
			printf("%d x %d = %d\n", i, j, i * j);
		}
	}

	// 피라미드 만들기
	for (int i = 0; i <= 5; i++) {
		for (int j = 0; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}

	// 피라미드 반대로 만들기
	for (int i = 0; i <= 5; i++) {
		for (int k = 0; k <= 5 - i; k++) {
			printf("*");
		}
		for (int j = 0; j < i; j++) {
			printf(" ");
		}
		printf("\n");
	}


	// 피라미드 반대로 만들기 2
	for (int i = 0; i <= 5; i++) {
		for (int k = 0; k < 5 - i; k++) {
			printf(" ");
		}
		for (int j = 0; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}

	// 피라미드 반대로 만들기 3
	for (int i = 0; i <= 5; i++) {
		for (int j = 0; j <= i; j++) {
			printf(" ");
		}
		for (int k = 0; k < 5 - i; k++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}