#include<stdio.h>

// 内存中数据占用的字节数计算

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
        char num[20]; // 20字节
    };

    typedef struct subject {
        char name[10];  // 大于8字节且不是double字节数的倍数, 故进位到16字节对齐.
        double score;  // 8字节
    } SUB;

    struct array {
//        float f;
        double f;  // 8字节
        char p;  // 和后一组类型, 补齐为int的倍数,即为4字节
        int arr[3];  // 3 * 4 = 12字节, 而double是int的倍数. 故 后2组类型补齐到4字节的倍数即可.
    };

    int struct_array = sizeof(struct STU);
    int struct_array2 = sizeof(SUB);
    int struct_array3 = sizeof(struct array);

    printf("%d\n", struct_array);
    printf("%d\n", struct_array2);
    printf("%d\n", struct_array3);


    /* ---------- */
    void *pointer;  // 64位系统的指针变量所占字节数为8字节

    struct Test {
        int Num;  // 第一组 4字节 对齐第二组实际占用8字节
        char *pcName;  // 第二组: 指针变量所占 8字节
        short sDate;  // 第三组 2字节 和第三组共同对齐其他组实际占用4字节
        char cha[2];  // 第三组 2字节 实际占用4字节
        short sBa[4];  // 第四组 8字节
    } *p;

    int pointer_size = sizeof(pointer);
    int test_size = sizeof(struct Test);

    printf("size of pointer: %d\n", pointer_size);  // 8
    printf("size of Test: %d\n", test_size);  // 内存中连续对齐的4组8字节, 故为32

    return 0;
}
