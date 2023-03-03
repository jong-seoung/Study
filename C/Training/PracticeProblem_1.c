#include<stdio.h>

// 프로젝트 1
// 경찰관이 범죄자의 정보를 입수 (조서 작성)
// 이름, 나이, 몸무게, 키, 범죄명을 입력 받기
int main(void) {

	char name[256];
	printf("이름이 뭐에요? ");
	scanf_s("%s", name, sizeof(name));

	int age;
	printf("나이가 어떻게 되세요? ");
	scanf_s("%d", &age);

	float weight;
	printf("몸무게가 어떻게 되세여? ");
	scanf_s("%f", &weight);

	double height;
	printf("키가 어떻게 되세여? ");
	scanf_s("%lf", &height);

	char why[256];
	printf("왜 잡혀 오셨어요? ");
	scanf_s("%s", why, sizeof(why));

	printf("\n\n --- 범죄자 정보 --- \n\n");
	printf("이름 : %s\n", name);
	printf("나이 : %d\n", age);
	printf("몸무게 : %.2f\n", weight);
	printf("키 : %.2lf\n", height);
	printf("범죄명 : %s\n", why);

}