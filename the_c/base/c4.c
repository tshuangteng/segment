#include <stdio.h>

// 数组是编程语言中用来存储相同类型元素的集合;

int main() {

    // 数组的初始化: 数组与变量一样,必须经过初始化或者赋值才能使用,否则数组中的元素将是随意存放的.
    int intArry[10];  // 必须指明数组的大小 或者 直接赋值
    int x = 10, intArray_a[x];
    /*int intArray[10]={1,2,3,4,5};*/  // 指定了数组大小,但只给前5个
    int intArray[] = {1, 2, 3, 4, 5};  // 数组一旦声明，其大小是不可以变化
    int intArray_b[20] = {1, 2, 3, 4, 5, [8]=8, 9, 10, 11, [19]=19};  // 跳过中间的位置,给其后的位置赋值,没有赋值的 位置的值是不确定的.


    // 数组的使用: 集合中元素的使用 通过变量名加索引位置的方式.
    intArray_b[8] = 8;


    // 示例
    int a = 10;
    int b[10];
    int c[] = {1, 2, 3, 4, 5};
    int d[10] = {1, 2, 3, 4, 5};
    int e[20] = {1, 2, 3, 4, 5, [8] = 8, 9, 10, 11, [19] = 19};
    int f[a];

    for (int i = 0; i < 10; i++) {
        printf("b[%d] = %d\n", i, b[i]);  // 不赋值的话,数组中存储的数据是不确定的
    }

    for (int i = 0; i < 5; i++) {
        printf("c[%d] = %d\n", i, c[i]);  // 数组的索引是从 0 开始
    }

    for (int i = 0; i < 10; i++) {
        printf("d[%d] = %d\n", i, d[i]);
    }

    for (int i = 0; i < 20; i++) {
        printf("e[%d] = %d\n", i, e[i]);
    }

    for (int i = 0; i < 10; i++) {
        printf("e[%d] = %d\n", i, f[i]);
    }


    // 多维数组: 如果添加一组大括号，那么称之为二维数组，以此类推，就构成了 N 维数组
    int int_Array[2][2];  // 二维数组
    float flo_Array[3][4][5]; // 三维数组

    // 示例
    short m[2][2] = {1, 2, 3, 4};  // 不推荐
    short n[2][2] = {{1, 2},
                     {3, 4}};
    short o[2][2] = {3, 4};  // 不推荐: c[0][0] 和 c[0][1] 两个位置赋值为 3 和 4，其它位置会自动赋值为 0
    short p[2][2] = {{},
                     {3, 4}};


    // 多维数组的使用: 循环嵌套; 有几个维度，就要使用几重的嵌套
    short multi_dimension_a[2][2] = {};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("multi_dimension_a[%d][%d] = %d\n", i, j, multi_dimension_a[i][j]);
        }
    }

    int multi_dimension_b[][2] = {{1, 2},
                                  {3, 4}};
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("multi_dimension_b[%d][%d] = %d\n", i, j, multi_dimension_b[i][j]);
        }
    }

    int multi_dimension_c[3][2][2] = {{{1, 2},  {3,  4}, {}},
                                      {{5, 6},  {7,  8}},
                                      {{9, 10}, {11, 12}}};

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            for (int k = 0; k < 2; k++) {
                printf("multi_dimension_c[%d][%d][%d] = %d\n", i, j, k, multi_dimension_c[i][j][k]);
            }
        }
    }


    // 练习1: 一维数组求和

    short sum = 0;
    short one_dimension[10] = {2, 1, 4, 34, 12, 34, 56, 78, 11, 2};
    for (int i = 0; i < 10; i++) {
        sum += one_dimension[i];
    }
    printf("Array sum: %d\n", sum);


    // 练习2: 交换一个有 N x N 个元素二维数组对角元素
    short td = 0;
    short two_dimension[4][4] = {{1,  2,  3,  4},
                                 {5,  6,  7,  8},
                                 {9,  10, 11, 12},
                                 {13, 14, 15, 16}};
    /*
    C语言中，二维数组是按行排列存放到内存中
        1   2   3   4
        5   6   7   8
        9   10  11  12
        13  14  15  16

    交换后:
        1	5	9	13
        2	6	10	14
        3	7	11	15
        4	8	12	16
     */

    printf("原始二维数组\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("two_dimension[%d][%d] = %d\n", i, j, two_dimension[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 4; i++) {
        for (int j = i; j < 4; j++) {
            x = two_dimension[i][j];
            two_dimension[i][j] = two_dimension[j][i];
            two_dimension[j][i] = x;
        }
    }

    printf("交换后的二维数组\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("two_dimension[%d][%d] = %d\n", i, j, two_dimension[i][j]);
        }
        printf("\n");
    }

    return 0;
}