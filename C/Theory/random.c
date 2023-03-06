#include<time.h>
#include<stdio.h>
#include<stdlib.h>

int main(void) {
	// srand(time(NULL)); //난수 초기화
	// int num = rand() % 3; // 0~2 까지의 숫자중에서 하나를 뽑아줘

	printf("난수 초기화 이전 \n");
	for (int i = 0; i < 10; i++) {
		printf("%d \n", rand() % 10);
	}

	srand(time(NULL));
	printf("난수 초기화 이후 \n");
	for (int i = 0; i < 10; i++) {
		printf("%d \n", rand() % 10);
	}
	return 0;
}