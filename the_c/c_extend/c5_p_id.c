#include<stdio.h>

int main() {
    // int *a[2] = {(int *) 100, (int *)200}, **p1 = a;
    int *i[2] = {0x100000, 0x100008}, **ip = i;  // i中的元素是指向int值的指针, ip是指向指针的指针.
    // 初始化数组i, 放到内存中,地址从0x100000开始. 内容随机不重要.
    // 初始化指针ip, 内存给的随机地址从61fde0开始,占用16字节, 前8字节内容为0x100000, 后8字节61fde8开始内容为0x100008

    int res1 = *ip;
    // 初始化指针res1, 生成随机地址1048576. res1中存的内容, 即*ip的值是ip指针的首位内容0x100000
    int res2 = *ip + 1;
    // 初始化指针res2, 地址移动1个sizeof(int)单位,到1048580. res2中存的内容,即*ip + 1的值是0x100004.

    printf("%d\t", res1);
    printf("%d\t\n", res2);
    // 1048576 1048580


    int res3 = ip;
    // 初始化指针res3, 生成随机地址6421984. res3中存的内容, 即ip的首地址 61fde0

    int res4 = ip + 1;
    // 初始化指针res4, 地址移动1个sizeof(指针)单位,到6421992. res4中存的内容, 即ip+1的值是 61fde8

    int res5 = *(ip + 1);
    // 初始化指针res5,生成随机地址1048584. 存的内容是61fde8地址指向的内容为0x100008

    printf("%d\t", res3);
    printf("%d\t", res4);
    printf("%d\t", res5);
    // 6421984 6421992 1048584


    // int型指针数组的理解: 没有意义,而char类型就可以是字符串的使用

    return 0;
}
