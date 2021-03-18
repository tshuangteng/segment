#include <stdio.h>  // 头文件,预处理指令 编译时查找所需引用的内容.
#include <stdbool.h>
#define pi 3.141592653535384  // 预处理命令 #define 定义的常量
#define typename(x) _Generic((x),        /* Get the name of a type */             \
                                                                                  \
        _Bool: "_Bool",                  unsigned char: "unsigned char",          \
         char: "char",                     signed char: "signed char",            \
    short int: "short int",         unsigned short int: "unsigned short int",     \
          int: "int",                     unsigned int: "unsigned int",           \
     long int: "long int",           unsigned long int: "unsigned long int",      \
long long int: "long long int", unsigned long long int: "unsigned long long int", \
        float: "float",                         double: "double",                 \
  long double: "long double",                   char *: "pointer to char",        \
       void *: "pointer to void",                int *: "pointer to int",         \
      default: "other")

/*
 * 对于C语言最好的项目就是开发系统
 * 音频和视频的解码器和编码器等；
 * 协议栈的开发。
 */

int main() {
    const float pii = 3.141592;  // c语言中的常量即是字面值,只是用特定的名称代表了这个字面值. 不需要经过声明和初始化

    // 类型转换
    int a = 1, b = 2;
    float c = 3.14159, d = 0;
    printf("a type: %s, b type: %s, c type: %s, d type: %s\n", typename(a), typename(b), typename(c), typename(d));
    a = (float) b + (float) c;  // 显式类型转换
    printf("a=b+c, a=%d\n", a);
    printf("type (b+c): %s\n", typename(b + c));
    d = (int) b + (int) c;
    printf("d=b+c, d=%f\n", d);  // %f 小数点后默认保留6位
    printf("d=b+c, d=%.8f\n", d);

    // 一元运算
    int f, e=10;
    f=--e;  //单独对变量执行自加和自减(不管前后),变量的值都会加一或者减一
    printf("f=--e,f=%d, e=%d\n",f,e);  //自加与自减前置的时候，赋值语句获得的是自加或者自减完成后的数值
    e = 10;
    f=e--;
    printf("f=e--,f=%d, e=%d\n",f,e);  //自加与自减后置的时候，赋值语句获得的是自加或者自减之前的原始数值

    // 位运算
    int x,y,z;
    x=10; 1010;
    y=15; 1111;
    printf("x&y = %d\n",x&y);
    printf("x|y = %d\n", x|y);

    /*
     * 计算机位运算都是基于补码进行的.
     *
     * 00000000 0000000 0000000 00001111  15 的补码
     *
     * 11111111 1111111 1111111 11110000  15的非位 补码
     * 11111111 1111111 1111111 11101111  补码减1
     * 10000000 0000000 0000000 00010000  原码 -16
     */
    printf("~y = %d\n", ~y);
    printf("x << 2 = %d\n", x<<2);
    printf("y>>2 = %d\n", y>>2);

    // 三目运算; bool的运用
    printf("%s\n", (x>y) ? "x > y" : "x < y");

    bool m, n;
    m = false;
    n = true;
    printf("%s\n", (m&n)?"True":"False");
    printf("%s\n", (m|n)?"True":"False");

    // while语句, 先判断再执行
    // 举例: 采用轮询的方式采集端口的信息,不断扫描每个端口的状态. while(1)
    int ht = 3;
    while (ht > 0){
        printf("%d\n", ht);
        ht--;
    }

    // do-while, 先执行一次
    int tt = 4;
    do {
        printf("Number: %d\n", tt);
        --tt;
    } while (tt>0);

    // for, 已知: 循环的控制条件
    for (int i = 1;i<10;i++) {  //循环变量赋初值; 循环条件; 循环变量增值
        printf("%d\n", i);
    }

    /* 文件: n2.c
     * for(){} 多重循环
     * while(){} 多重循环
     * do{}while() 多重循环
     */

//    int ccc;
//    puts("请你猜数字，请输入0-9的数字");
//    scanf("%i",&ccc);
    /*
     * 如果写做scanf("%d",a);我们是把变量a所在的存储空间中的数据作为右值输出，
     * 而在scanf中a变量的值作为键盘终端字符输入存储空间的地址，而这显然是不合理的，
     * 因为我们要把键盘终端输入端的字符存到变量a所在的存储空间，
     * 而不是变量a存储的数据所指向的内存空间~所以写做scanf("%d",&a);
     * //”&“是以一个操作符，可以获取变量a所在的存储空间位置，
     * 而不是变量a所在存储空间中存储的数据~
     */

    int h = 10;
    int *t = &h;  // 定义和赋值; int *t: 定义了一个指针变量t; t=&h,取h的地址赋值给t.

    printf("%d\n", h);  //10
    printf("%d\n", &h);  //6421980
    printf("%d\n", t);  //6421980
    printf("%d\n", *t);  //10; 将t的内容作为地址,通过这个地址再去取对应的值.


    return 0;
}

