#include<stdio.h>
#include<time.h>
// 물고기가 6마리가있다.
// 이들은 어항에 살고있는데 너무 더워서, 너무 건조해서 물이 아주 빨리 증발한다.
// 물이 다 증발하기 전에 어항에 물을 줘서 물고기를 살려주자
// 물고기는 어느정도 크면 게임이 끝난다

int level;
int arrayFish[6];
int *cursor;

void initData();
void printfFish();
void decreseWater(long PlayTime);
int checkFishAlive();

int main(void) {
	long startTime = 0;
	long totalPlayTime = 0;
	long prevPlayTime = 0;

	int num; // 몇번 어항에 물을 줄것인지 
	initData();
	cursor = arrayFish;

	startTime = clock();
	while (1) {
		printfFish();
		printf("몇번 어항에 물을 주시겠어요?");
		scanf_s("%d", &num);

		// 입력값 체크
		if (num < 1 || num >6) {
			printf("\n입력값이 잘못되었습니다.\n");
			continue;
		}
		// 총 경과 시간
		totalPlayTime = (clock() - startTime) / CLOCKS_PER_SEC;
		printf("총 경과 시간 : %ld초 \n", totalPlayTime);

		// 직전 물을 준 시간
		prevPlayTime = totalPlayTime - prevPlayTime;
		printf("최근 경과 시간 : %ld초 \n", prevPlayTime);

		// 어항의 물을 감소
		decreseWater(prevPlayTime);

		// 사용자가 입력한 어항에 물을 준다.
		// 1. 어항의 물이 0이면 물을 줄수없다.
		if (cursor[num - 1] <= 0) {
			printf("%d 번 물고기는 이미 죽었습니다. \n", num);
		}
		// 2. 어항의 물이 0이 아닌경우 물을 주는데 100을 넘지 않아야한다.
		else if (cursor[num - 1] + 1 <= 100) {
			printf("%d 번 어항에 물을 줍니다 \n\n", num);
			cursor[num - 1] += 10;
		}
		// 3. 레벨업 기능 - 20초 마다 한번씩 수행
		if (totalPlayTime / 20 > level - 1) {
			level++;
			printf("*** 레벨업 *** \n현재 레벨: %d", level);
		}
		if (level == 5) {
			printf("축하합니다. 최고레벨을 달성하였습니다. 게임을 종료합니다.");
			exit(0);
		}

		// 모든 물고기가 죽었는지 확인
		if (checkFishAlive() == 0) {
			printf("모든 물고기가 죽었습니다.");
			exit(0);
		}
		prevPlayTime = totalPlayTime;
	}
	return 0;
}

void initData() {
	level = 1;
	for (int i = 0; i < 6; i++) {
		arrayFish[i] = 100; // 어항의 물 높이
	}
}

void printfFish() {
	printf("%3d번 %3d번 %3d번 %3d번 %3d번 %3d번 \n", 1, 2, 3, 4, 5, 6);
	for (int i = 0; i < 6; i++) {
		printf(" %4d ", arrayFish[i]);
	}
	printf("\n\n");
}

void decreseWater(long PlayTime) {
	for (int i = 0; i < 6; i++) {
		arrayFish[i] -= (level * 3 * (int)PlayTime); // 3은 난이도 조절을 위한 값
		if (arrayFish[i] < 0) {
			arrayFish[i] = 0;
		}
	}
}

int checkFishAlive() {
	for (int i = 0; i < 6; i++) {
		if (arrayFish[i]>0){
			return 1;
		}
	}
	return 0;
}