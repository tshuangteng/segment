#include <stdio.h>


// 结构体
int main() {
    struct Contacts {
        char name[100];
        int age;
        char mobile[11];
    };

//    struct Contacts person1, person2;  // 和数组变量的初始化一样, 最好先经过初始化或者赋值再使用

    // 初始化结构体
    struct Contacts person1 = {"zs", 30, "123456"};

    // 使用
    printf("Name: %s, Age: %d, Mobile: %s\n", person1.name, person1.age, person1.mobile);


    // 结构体内存对齐
    struct A {
        char a;
        int b;
        short c;
    };

    struct B {
        short c;
        char a;
        int b;
    };

    struct A a;
    struct B b;
    printf("A: %d\n", sizeof(a));  // 12
    printf("B: %d\n", sizeof(b));  // 8

    /*
    1.对于结构体的各个成员，第一个成员的偏移量是0，排列在后面的成员其当前偏移量必须是当前成员类型的整数倍
    2.结构体内所有数据成员各自内存对齐后，结构体本身还要进行一次内存对齐，保证整个结构体占用内存大小是结构体内最大数据成员的最小整数倍
    3.如程序中有#pragma pack(n)预编译指令，则所有成员对齐以n字节为准(即偏移量是n的整数倍)，不再考虑当前类型以及最大结构体内类型
    */

    return 0;

}