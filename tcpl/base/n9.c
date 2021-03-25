#include <stdio.h>
#include <stdlib.h>

// maclloc free使用
int main_() {
    int *x;
    // x = (int *)maclloc(32);  // maclloc 函数的参数是分配的内存的大小,其返回值是一个无类型的指针(显示类型转换)。
    // free(x); // 回收动态分配的内存

    return 0;
}

// 示例
int main() {
    int *x;
    x = (int *)malloc(sizeof(x));  // 对这个指针分配了一块内存
    printf("x value: %p, x address: %p, *x value: %d\n",x, &x,*x);

    *x = 10;
    printf("x value: %p, x address: %p, *x value: %d\n",x, &x,*x);
    free(x); // 回收分配的内存

    return 0;
}




