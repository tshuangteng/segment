#include <stdio.h>
#include "windows.h"

// 字节序的引申和判断

BYTE b = 0x12;
WORD w = 0x1234;
DWORD dw = 0x12345678;
char str[] = "abcde";

int main(int argc, char *argv[]) {
    byte lb = b;
    WORD lw = w;
    DWORD ldw = dw;
    char *lstr = str;

    unsigned int c = 257; // 4字节 补码:00000000 00000000 00000001 00000001  (高位  <---  低位)
    unsigned int *a = &c;
    unsigned char *b = (unsigned char *) &c;  // 强制转换类型

    printf("%d\n", *a); // 输出 257
    printf("%d\n\n", *b); // 输出 1  字节小端存储: 低地址存低位数据 , char存储1字节的数据的补码 00000001

    // 内存中的小端存储模式
    //   低地址  --->  高地址
    //   低位  --->  高位

    // 00000001 00000001 00000000 00000000  (int类型 四字节, 转化为10进制为257)
    // 00000001  (char类型 1字节, 转化为10进制为1)


    /*
     * adjust byte big or little endian
     */
//    union {
//        short i;
//        char a[2];
//    } u;
//    u.a[0] = 0x11;
//    u.a[1] = 0x22;
//    printf("0x%x\n\n", u.i);  // 0x2211 是小端



    /*
     * adjust big or little endian
     */
    // method 1
    union {
        int m;
        char n;
    } check_point;

    check_point.m = 1;  // 联合体的访问不论对哪个变量的存取都是从 union 的首地址位置开始
    if (check_point.n == 1) {
        printf("little endian\n\n");
    } else {
        printf("Big endian\n\n");
    }


    // method 2
    int i = 1;
//    printf("%d\n", *(char *) &i);
    (*(char *) &i == 1) ? printf("little endian\n") : printf("big endian\n");

    return 0;
}