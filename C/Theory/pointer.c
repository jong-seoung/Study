#include <stdio.h>

void swap(int a, int b);
void swap_addr(int* a, int* b);
void chageArrary(int* ptr);

int main(void) {
    // 포인터
    // 철수 : 101호 -> 메모리 공간의 주소
    // 영희 : 201호
    // 민수 : 301호
    // 각 문앞에 '암호'가 걸려 있음
    int choi = 1;
    int kim = 2;
    int kang = 3;

    printf("choi 주소 : %p , 암호 : %d \n",&choi,choi);
    printf("kim 주소 : %p, 암호 : % d \n", &kim, kim);
    printf("kang 주소 : %p, 암호 : % d \n", &kang, kang);

    // 미션
    // 아파트의 각 집에 방문하여 문에 적힌 암호 확인
    int * mission; //포인터 변수
    mission = &choi;
    printf("미션을 한 주소 : %p, 암호 : %d \n", mission,*mission);

    // kim 방문
    mission = &kim;
    printf("미션을 한 주소 : %p, 암호 : %d \n", mission, *mission);

    // kang 방문
    mission = &kang;
    printf("미션을 한 주소 : %p, 암호 : %d \n", mission, *mission);

    // 두번째 미션 : 각 암호에 3을 곱해라
    mission = &choi;
    *mission = *mission * 3;
    printf("두번째 미션을 한 주소 : %p, 암호 : %d \n", mission, *mission);

    mission = &kim;
    *mission = *mission * 3;
    printf("두번째 미션을 한 주소 : %p, 암호 : %d \n", mission, *mission);

    mission = &kang;
    *mission = *mission * 3;
    printf("두번째 미션을 한 주소 : %p, 암호 : %d \n", mission, *mission);

    // 스파이 등장
    // 미션한 암호 값에서 2를 빼라
    int* spy = mission;
    printf("\n .... 스파이가 미션 수행하는중 ....\n");
    spy = &choi;
    *spy = *spy - 2;
    printf("스파이가 방문한 곳 주소 : %p, 암호 : %d\n", spy, *spy);

    spy = &kim;
    *spy = *spy - 2;
    printf("스파이가 방문한 곳 주소 : %p, 암호 : %d\n", spy, *spy);

    spy = &kang;
    *spy = *spy - 2;
    printf("스파이가 방문한 곳 주소 : %p, 암호 : %d\n", spy, *spy);

    printf("\n .... 바뀐 암호 .... \n");
    printf("choi 주소 : %p , 암호 : %d \n", &choi, choi);
    printf("kim 주소 : %p, 암호 : % d \n", &kim, kim);
    printf("kang 주소 : %p, 암호 : % d \n", &kang, kang);

    // 미션의 주소
    printf("미션한 주소 : %p\n", &mission);
    printf("미션한 주소 : %p\n", &spy);

    // 배열 ?
    printf("\n\n ... 배열 ... \n");
    int arr[3] = { 5,10,15 };
    int * ptr = arr;
    for (int i = 0; i < 3; i++) {
        printf("배열 arr[%d]의 값은 %d입니다.\n", i, arr[i]);
    }
    for (int i = 0; i < 3; i++) {
        printf("포인터 ptr[%d]의 값은 %d입니다.\n", i, ptr[i]);
    }
    ptr[0] = 100;
    ptr[1] = 200;
    ptr[2] = 300;
    for (int i = 0; i < 3; i++) {
        printf("배열 arr[%d]의 값은 %d입니다.\n", i, arr[i]);
        printf("배열 arr[%d]의 값은 %d입니다.\n", i, *(arr + i));
    }
    for (int i = 0; i < 3; i++) {
        printf("포인터 ptr[%d]의 값은 %d입니다.\n", i, ptr[i]);
        printf("포인터 ptr[%d]의 값은 %d입니다.\n", i, *(ptr + i));
    }

    // arr[i] == *(arr + i) 두문장은 똑같은 표현
    // arr == arr 배열의 첫번째 값의 주소와 동일 &arr[0]

    printf("arr 자체의 값 : %p\n", arr);
    printf("arr[0]의 주소 : %p\n", &arr[0]);

    printf("arr 자체의 값이 가지는 주소의 실제 값: %d\n", *arr);
    printf("arr[0]의 실제값 : %d\n", *&arr[0]);
    // *&같이 있으면 아무것도 없는것과 같다.


    printf("\n\n\n\n-----------\n");
    // a와 b의 값을 바꾼다. swap
    int a = 10;
    int b = 20;
    
    printf("a의 주소 : %p\n", &a);
    printf("b의 주소 : %p\n", &b);

    printf("swap 함수 전 => a : %d, b : %d\n", a, b);
    swap(a, b);
    printf("swap 함수 후 => a : %d, b : %d\n", a, b);
    // 값에 의한 복사 -> 값만 복사한다는 의미

    // 주소값 전달
    printf("<주소값 전달 전 주소> => a : %d, b : %d\n", a, b);
    swap_addr(&a, &b);
    printf("<주소값 전달 후 주소> => a : %d, b : %d\n", a, b);


    printf("\n\n\n\n\n\n\n\n\--------------------------------\n\n");
    int arr3[3] = { 10,20,30 };
    // chageArrary(arr3);
    chageArrary(&arr3[0]);
    for (int i = 0; i < 3; i++) {
        printf("%d\n", arr3[i]);
    }
    return 0;
}

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("<swap 함수 안> a : %d, b : %d\n", a, b);
    printf("<swap 함수 안> a의 주소 : %p\n", &a);
    printf("<swap 함수 안> b의 주소 : %p\n", &b);
}

void swap_addr(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("<주소값 전달> swap 함수 안 => a : %d, b : %d\n", *a, *b);
}

void chageArrary(int* arr) {
    arr[2] = 50;
}