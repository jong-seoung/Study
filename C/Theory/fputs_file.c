#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define MAX 10000

int main(void){
	// 파일 입출력
	// 파일에 어떤 데이터를 저장
	// 파일에 저장된 데이터를 불러오기

	// fput, fgets
	char line[MAX];
	FILE* file = fopen("test1.txt", "wb"); // r:읽기 w:쓰기 a:이어쓰기 
	if (file == NULL) {
		printf("파일 열기 실패\n");
		return 1;
	}

	fputs("fputs를 이용해서 글을 적어볼께요. \n", file);
	fputs("잘적히는지 확인해 주세요. \n", file);

	// 파일을 닫지않고 프로그램에 문제가 생기면 데이터 손실 발생가능!
	fclose(file);
	// fprinf, fscanf
}