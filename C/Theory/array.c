#include<stdio.h>

int main(void) {

	int subway_array[3]; // 여러개의 변수를 함께, 동시에 생성
	subway_array[0] = 30;
	subway_array[1] = 40;
	subway_array[2] = 50;

	for (int i = 0; i < 3; i++) {
		printf("지하철 %d호차에 %d명이 타고있습니다. \n",i+1,subway_array[i]);
	}

	// 값 설정 방법
	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 }; // 값은 반드시 초기화 해야함
	for (int i = 0; i < 10; i++) {
		printf("%d",arr[i]);
	}

	//int size = 10; int arr[size]; 처럼 사용하면 오류 발생 (배열의 크기는 항상 상수로 선언)

	int arr2[10] = { 1,2 }; // 3번째 값 부터는 자동으로 0으로 초기화 됨
	for (int i = 0; i < 10; i++) {
		printf("%d", arr2[i]);
	}

	printf("\n");
	
	// 문자 VS 문자열
	char c = 'a';
	printf("%c\n", c);

	// 문자열 끝에는 끝을 의미하는 NULL문자 \0 이 포함되어야함
	char str[7] = "coding\0";
	printf("%s \n", str);

	char str2[] = "coding";
	printf("%s \n", str2);
	printf("%d \n", sizeof(str2));

	for (int i = 0; i < sizeof(str2); i++) {
		printf("%c\n", str2[i]);
	}

	char kor[] = "한글은 2바이트";
	printf("%s \n", kor);
	printf("%d \n", sizeof(kor));

	char c_array[7] = { 'c','o','d','i','n','g','\0' };
	printf("%s \n", c_array);

	char c_array2[10] = { 'c','o','d','i','n','g'};
	printf("%s \n", c_array2);

	for (int i = 0; i < sizeof(c_array2); i++) {
		printf("%d\n", c_array[i]); //아스키코드
	}

	char name[256];
	printf("이름을 입력하세요 :\n");
	scanf_s("%s",name,sizeof(name));
	printf("%s \n", name);

}