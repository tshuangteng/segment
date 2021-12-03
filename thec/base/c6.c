#include <stdio.h>

/*
例如：&a、&b分别表示变量a和变量b的地址。
这个地址就是编译系统在内存中给a、b变量分配的地址。
在C语言中，使用了地址这个概念,应该把变量的值和变量的地址这两个不同的概念区别开来。变量的地址是C编译系统分配的，用户不必关心具体的地址是多少。

变量的地址和变量值的关系
在赋值表达式中给变量赋值，如：a=567; 则，a为变量名，567是变量的值，&a是变量a的地址。

 */


//  C语言指针: 存储的是另外一个变量的地址。变量地址是变量在内存中存储的位置索引
// 见文件: n1.c
int main_() {
/*    int t = 66;
    int b = 100, *a=&b, *c=&t;
    printf("a value = %p, a address = %p, a point value = %d\n", a, &a, *a);
    printf("b value = %d, b address = %p\n", b, &b);
    printf("t value = %d, t address = %p\n", t, &t);
    printf("c value = %p, c address = %p, c point value = %d\n", c, &c, *c);
    printf("---------------------------------------\n");*/

    int *a, b = 100, *c;

    // 定义了一个整数类型的指针 a, 故赋值的时候需要获得变量的地址.
    // 在指针变量名前加 * 来获取相应地址中存储的值

    printf("b value = %d, b address = %p\n", b, &b);
    printf("---------------------------------------\n");

    a = &b;
    printf("a value = %p, a address = %p, a point value = %d\n", a, &a, *a);
    printf("---------------------------------------\n");

    c = a;
    printf("c value = %p, c address = %p, c point value = %d\n", c, &c, *c);
    printf("---------------------------------------\n");
    /*在赋值的时候是将别的变量通过变量名获得的该变量的地址存储到指针变量里，
    而后获取这个被存储到指针变量里的地址的数值，或者继续将该变量的地址赋值给另外一个指针变量。
    指针变量的存在只是一个变量的赋值*/

    return 0;
}


// 枚举: 同常量一样定义后不能修改 (数据的映射)
int main() {
    enum Score {
        Mon = 1,
        Tue = 2,
        Wed = 3,
        Thu = 4,
        Fri = 5,
        Sat = 6,
        Sun = 7,
    };

    enum Score week_day1, week_day2, week_day3;
    week_day1 = Mon;
    week_day2 = Tue;
    week_day3 = Wed;
    printf("week_day1 is number:%d, week_day2 is number:%d,week_day3 is number:%d\n", week_day1, week_day2, week_day3);

    return 0;
}