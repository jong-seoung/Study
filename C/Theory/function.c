#include<stdio.h>

// 선언
void p(int num);
void function_without_return();
int function_with_return();
void function_without_params();
int function_with_params(int num1,int num2, int num3);
int apple(int total, int ate);
int add(int num1, int num2);
int sub(int num1, int num2);
int mul(int num1, int num2);
int div(int num1, int num2);

int main(void) {
	// function
	// 계산기

	int num = 2;
	p(num);

	// 2+3은?
	num = num + 3;
	p(num);

	// 5-1은?
	num = num - 1;
	p(num);

	// 4x3은?
	num = num * 3;
	p(num);

	// 12 % 6 은?
	num = num / 6;
	p(num);

	// 함수의 종류
	// 반환값이 없는 함수 - void
	function_without_return();

	// 반환값이 있는 함수
	int ret = function_with_return();
	p(ret);

	// 전달값이 없는 함수
	function_without_params();

	// 전달값이 있는 함수
	function_with_params(1,2,3);

	// 전달값과 반환값이 둘다 있는 함수
	int apple_ret = apple(5, 2);  // 5개의 사과중에서 2개를 먹었어요.
	printf("전달값, 반환값 / 사과 갯수 : %d \n", apple_ret);
	printf("사과 %d개중에서 %d개를 먹으면 %d개가 남아요. \n", 10, 4, apple(10, 4));

	// 계산기함수
	num = 2;
	num = add(num, 3);
	p(num);

	num = sub(num, 1);
	p(num);

	num = mul(num, 3);
	p(num);

	num = div(num, 6);
	p(num);
	return 0;
}

void p(int num) {
	printf("num은 %d 입니다. \n", num);
}

void function_without_return() {
	printf("반환값이 없는 함수 입니다. \n");
}

int function_with_return() {
	printf("반환값이 있는 함수입니다. \n");
	return 10;
}

void function_without_params() {
	printf("전달값이 없는 함수입니다. \n");
}

int function_with_params(int num1, int num2, int num3) {
	printf("전달값이 있는 함수이며 전달 받은 값은 %d %d %d 입니다. \n",num1,num2,num3);
}

int apple(int total, int ate) {
	return total - ate;
}

int add(int num1, int num2) {
	return num1 + num2;
}

int sub(int num1, int num2) {
	return num1 - num2;
}

int mul(int num1, int num2) {
	return num1 * num2;
}

int div(int num1, int num2) {
	return num1 / num2;
}