#include <stdio.h>
#include <stdlib.h>


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 函数; 函数头 和 函数体

/*返回值类型 函数名(函数) { 程序语句 }*/
int week(int w) {
    switch (w) {
        case 1:
            printf("Monday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
    }
    return 0;
}

/*
int main() {
    int w = 5;
    week(w);
    week(1);
}
*/


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 值传入: 原函数的数值复制一份后的副本进行操作
int add_(int x) {
    x++;
    printf("sub func %d \n", x);
    return 0;
//    return x;
}

/*
int main() {
    int x = 99;
    add_(x);  // 值传入, 只在该函数中变化.
//    x = add_(x);
    printf("main func %d", x);
    return 0;
}
 */


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 引用传入: 原有函数中的变量直接传入调用操作(使用&取地址,指针的使用; 数组的使用)

/*数组的使用*/
int add_by_list(int x[]) {
    x[0]++;
    printf("sub func %d\n", x[0]);
    return 0;
}

/*
int main() {
    int a[] = {999};
    add_by_list(a);
    printf("main func %d", a[0]);
    return 0;
}
 */

/* 指针的使用 */
int add_by_point(int *x) { // 定义指针变量: int *x 或者 int* x
    (*x)++;
    printf("sub func %d\n", *x);
    return 0;
}

/*int main() {
    int x = 9999;
    add_by_point(&x);
    printf("main func %d", x);
    return 0;
}*/


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// main 函数: 操作系统引导的程序入口
/* int main(int argc, char *argv[]);  或者  int main(int argc, char **argv); */

int main(int argc, char **argv) {
    while (argc--)
        printf("%s\n", *argv++);
//        printf("%d\n", *argv++);
    exit(EXIT_SUCCESS);
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// make编译:  依赖大量的库文件（尤其是非标准库文件），设置一些特殊的系统变量环境等内容

/*
目标:  依赖1， 依赖2， ……
编译命令
 */

/*  makefile 文件示例
n3: n3.c n2.c n1.c
    gcc n3.c n2.c n1.c -o test
*/
