#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
# define MAX 10000

int main(void) {

	int line[MAX];

	FILE* file = fopen("test1.txt", "r");
	if (file == NULL) {
		printf("파일 열기 실패 \n");
		return 1;
	}

	while (fgets(line, MAX, file) != NULL) {
		printf("%s", line);
	}

	fclose(file);

}