#include <stdio.h>

int main() {
    // 每一组的字节数相同来确保 内存中的对齐.
    // 延伸: 如果中间的一组字节数比较大, 则应该是从中间开始向2边对齐.
    typedef struct Info {
        char *name;  // 第一组: 8字节(*表示了要取该数据结构下的最大字节数)
        // char name[7];
        int age; // 第二组: 8字节(以最大字节数表示)
        double height;  // 第三组: 8字节 最大字节的单位
        short hobby[4];  // 第四组: 8字节 最大字节的单位
    } info;

    // int info_size = sizeof(struct Info);
    // printf("size of Info: %d\n", info_size);  // 该数据结构的字节数大小为32

    info ht;
    ht.age = 18;
    ht.height = 178;

    // 大字节类型 向 小字节类型 转换 , 导致内存溢出，或者精度问题
    // double *tp1 = (double *) ((char)&ht + 8);  // 强制转换类型, 指针类型(64位系统8字节) 转换为 char类型(1字节) 导致数据丢失.
    // printf("*tp1 = %f", *tp1);

    // ht 数组名表示数组首元素的地址，是指针常量
    double *tp2 = (double *) ((int) &ht + 8);  // 指针常量 强制转换为普通的int数值, 内存中是以16进制(16字节)来表示计算的, 接着加数值8也就是8字节, 才能移动到该数组中的第二个元素.
    double *tp3 = (double *) ((char *) &ht + 16);  // 指针常量 强制转换为char类型的指针, 加16表示 移动16个sizeof(char)单位, 才能移动到该数组的第三个元素.
    double *tp4 = (double *) ((int *) &ht + 2); // 指针常量 强制转换为int类型的指针, 加2表示 移动2个sizeof(int)单位, 才能移动到该数组的第二个元素.

    printf("*tp2 = %d\n", *tp2);
    printf("*tp3 = %f\n", *tp3);
    printf("*tp4 = %d\n", *tp4);
    // *tp2 = 18
    // *tp3 = 178.000000
    // *tp4 = 18


    /*
     总结：指针移动的目的是为了去访问内存地址。
     而内存地址抽象出来的就是数字，所以进行指针访问时，需要移动指针其实就是对内存地址的数值进行加减运算，使指针针指向需要访问数据的内存空间的头位置处
     然后通过强制类型转换（类型匹配时不用强制类型转换），使用想要的解析方法去读取该内存空间的内容。
     */

    return 0;
}