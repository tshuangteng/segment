#include<stdio.h>

int main() {
    /* ---------- */
    struct A {
        char b;
        int a;  // int字节数为4, 内存连续, 因为int类型在中间, 故2边的数据类型对齐int
        short c;
    };

    //#pragma pack (2) /*指定按2字节对齐*/
    struct B {
        int a; // int字节数为4, 后面的2个数据类型可以凑够4字节进行对齐.
        char b;
        short c;
    };
    //#pragma pack () /*取消指定对齐，恢复缺省对齐*/

    struct C {
        char b;
        short c;
        int a;
    };

    //计算所占字节
    int s1 = sizeof(struct A);
    int s2 = sizeof(struct B);
    int s3 = sizeof(struct C);

    printf("%d\n", s1);
    printf("%d\n", s2);
    printf("%d\n", s3);


    /* ---------- */
    struct STU {
        char name[20];  // 20字节是int类型4字节的倍数
        int age;  // 故中间2组类型对齐为8字节,再相加字符数组类型.
        char sex;
        char num[20];
    };

    typedef struct subject {
        char name[10];  // 大于8字节且不是double字节数的倍数, 故进位到16字节对齐.
        double score;  // 8字节
    } SUB;

    struct array {
//        float f;
        double f;  // 8字节
        char p;
        int arr[3];  // 3组4字节, 后2组对齐double类型相加为8字节, 剩余的第一组4字节再加char类型对齐到8字节
    };

    int struct_array = sizeof(struct STU);
    int struct_array2 = sizeof(SUB);
    int struct_array3 = sizeof(struct array);

    printf("%d\n", struct_array);
    printf("%d\n", struct_array2);
    printf("%d\n", struct_array3);


    /* ---------- */
    void *pointer;  // 64位系统的指针变量所占字节数为8

    struct Test {
        int Num;  // 第一组
        char *pcName;  // 第二组: 以最大的8字节为单位
        short sDate;  // 第三组
        char cha[2];  // 第三组
        short sBa[4];  // 第四组
    } *p;

    int pointer_size = sizeof(pointer);
    int test_size = sizeof(struct Test);

    printf("size of pointer: %d\n", pointer_size);  // 8
    printf("size of Test: %d\n", test_size);  // 4组8字节, 故为32

    return 0;
}
