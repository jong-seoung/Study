#include<stdio.h>

void main() {
	int age = 12;
	printf("%d\n", age);
	age = 13;
	printf("%d\n", age);

	/* �ּ� ó��1 */
	//�ּ� ó��2

	// �Ǽ��� ������ ���� ����
	float f = 46.5f;
	printf("%f\n",f);
	printf("%.2f\n", f);

	double d = 4.428;
	printf("%.2f\n", d);

	// ��� - ������ �ʴ� �� (const�� ���)
	const int YEAR = 2000;
	printf("�¾ �⵵ : %d\n", YEAR);
	// YEAR = 2001; �� �ٲܼ�����

	// printf
	// ����
	int add = 3 + 7; // 10
	printf("3 + 7 = %d\n", add);
	printf("%d + %d = %d\n", 3, 7, 3 + 7);

	// scanf
	// Ű���� �Է��� �޾Ƽ� ����
	int input;
	printf("���� �Է��ϼ��� :");
	scanf_s("%d", &input);
	printf("�Է°��� %d\n", input);

	int one, two, three;
	printf("3���� ������ �Է��ϼ��� : ");
	scanf_s("%d %d %d", &one, &two, &three);
	printf("3���� ������ : %d %d %d \n", one, two, three);

	// ���� - �ѱ���, ���ڿ� - �ѱ��� �̻��� ��������
	char c = 'A';
	printf("%c\n", c);

	char str[256];
	scanf("%s", str, sizeof(str));
	printf("%s\n", str);
	return 0;
}