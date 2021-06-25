#include <stdio.h>
#include <string.h>


// union: 不更改变量名, 存储不同类型的变量.(由于C语言的强类型语言,变量只能存储指定类型的元素)
int main_() {

    // 声明
    union Calculation {
        int i;  // 4字节
        float f;  // 4字节
        char str[7];  // 7字节
    };

    union Calculation cal1, cal2, myStr[3];


    // 初始化
    union Calculation cal3 = {1};

    // 使用
    cal1.i = 1;
    cal1.f = 3.14;

    cal1.str[0] = 'w';
    cal1.str[1] = 's';
    cal1.str[2] = 'h';
    cal1.str[3] = 't';
    cal1.str[4] = 'a';
    cal1.str[5] = 'i';
    cal1.str[6] = 'n';
    // cal1.str[7] = '\0';  // 不像单独的char初始化使用 为什么这里没有用到'\0' ????

    printf("cal1.i: %d, cal1.f: %f, cal1.str: %s\n", cal1.i, cal1.f, cal1.str);

    cal1.f = 0.111;
    printf("cal1.i: %d, cal1.f: %f, cal1.str: %s\n", cal1.i, cal1.f, cal1.str);

    strcpy(cal1.str, "None");
    printf("cal1.i: %d, cal1.f: %f, cal1.str: %s\n", cal1.i, cal1.f, cal1.str);

    // union中可以定义多个成员，union的内存大小由最大的成员的大小来决定。
    // union成员共享同一块大小的内存，一次只能使用其中的一个成员(会覆盖其他成员的值)

    return 0;

}


//  union 内存分配理解
int main__() {
    union Data {
        int i;
        double x;  // 最高位 double
        char str[16];
    };

    union Data var, myData[100];
    var.x = 3.21;
    var.x += 0.5;
    printf("%f\n", var.x);   // 3.710000
//    printf("value of i: %d, value of x: %f, value of str: %s\n",var.i, var.x, var.str);

    strcpy(var.str, "Jim");
    printf("%s\n", var.str);  // Jim

    myData[0].i = 50;
//    printf("value of i: %d, value of x: %f, value of str: %s\n",myData->i, myData->x, myData->str);
    printf("%d\n", myData->i);  // 50

    for (int i = 0; i < 50; ++i) {
        myData[i].i = 2 * i;
//        printf("%d\n", myData->i);

    }
    printf("%d\n", myData->i);  // 0
//    printf("value of i: %d, value of x: %f, value of str: %s\n", myData->i, myData->x, myData->str);


    // 该循环从最高位字节开始
    var.x = 1.25;
    for (int i = sizeof(double) - 1; i >= 0; --i) {
        printf("%02X ", (unsigned char) var.str[i]);  // 3F F4 00 00 00 00 00
    }
    printf("\n-------------------\n");
    printf("%f\n", var.x);
    printf("%s\n", var.str);

    union Data tmp;
    printf("%d\n", tmp.i);  // 4

    return 0;
}


// 大小端检测
int main___() {
    union data {
        int n;  // 2 byte
        char ch;  // 1 byte
        short m;  // 2 byte
    };

    union data a;
    printf("%d, %d", sizeof(a), sizeof(union data));
    a.n = 0X12;


    union check {
        int i;
        char ch;
    } c;
    c.i = 1;
    printf("\n%d\n", c.ch);  // 1   所以是小端存储模式

    return 0;
}


// 大小端检测
int main() {
    int test = 0x41424344;  // 16进制到10进制: 1094861636   16进制对应的字符表示: ABCD (ASCII码表)
    char *ptr = (char *) &test;  // 实际上是把 &test 字符指针变量对应的第1个元素的地址赋值给 *ptr  0x44或者0x41(大小端决定)

    printf("int address: %d, value: %d\n", (unsigned int) &test, test);  // 6422032, 1094861636
    printf("====================\n\n");

//    for (int j = 0; j < 4; j++) {
//        printf("char address: %x, value: %c\n", (unsigned int) ptr, *ptr);  // char 1字节1字节查看
//        ptr++;
//    }
//    printf("===================\n\n");

    if (*ptr == 0x44)
        printf("Little-Endian\n");
    else if (*ptr == 0x41)
        printf("Big-Endian\n");
    else
        printf("Error !\n");

    return 0;
}
