#include<stdio.h>

void main() {
	int age = 12;
	printf("%d\n", age);
	age = 13;
	printf("%d\n", age);

	/* 주석 처리1 */
	//주석 처리2

	// 실수형 변수에 대한 예제
	float f = 46.5f;
	printf("%f\n",f);
	printf("%.2f\n", f);

	double d = 4.428;
	printf("%.2f\n", d);

	// 상수 - 변하지 않는 수 (const를 사용)
	const int YEAR = 2000;
	printf("태어난 년도 : %d\n", YEAR);
	// YEAR = 2001; 로 바꿀수없음

	// printf
	// 연산
	int add = 3 + 7; // 10
	printf("3 + 7 = %d\n", add);
	printf("%d + %d = %d\n", 3, 7, 3 + 7);

	// scanf
	// 키보드 입력을 받아서 저장
	int input;
	printf("값을 입력하세요 :");
	scanf_s("%d", &input);
	printf("입력값은 %d\n", input);

	int one, two, three;
	printf("3개의 정수를 입력하세요 : ");
	scanf_s("%d %d %d", &one, &two, &three);
	printf("3개의 정수는 : %d %d %d \n", one, two, three);

	// 문자 - 한글저, 문자열 - 한글자 이상의 여러글자
	char c = 'A';
	printf("%c\n", c);
	
	char str[256];
	scanf_s("%s", str, sizeof(str));
	printf("%s\n", str);
	return 0;
}