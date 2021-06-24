#include <stdio.h>

/*
 * 多重循环实现9*9乘法表
 */

int main() {
    // for 多重循环
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d * %d = %d ", i, j, i * j);
        }
        printf("\n");
    }


    // do while 多重循环
    int i = 1;
    do {
        int j = 1;
        do {
            printf("%d * %d = %d ", i, j, i * j);
            j++;
        } while (j <= i);
        i++;
        printf("\n");
    } while (i <= 9);

    // while 多重循环

//    int i = 1;
    while (i <= 9) {
        int j = 1;
        while (j <= i) {
            printf("%d * %d = %d ", i, j, i * j);
            j++;
        }
        i++;
        printf("\n");
    }

    return 0;
}