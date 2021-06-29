#include <stdio.h>


int main()
{
    // int *p1[10];  // 指针数组  *修饰p1[10]数组的内容为指针
    int *(p1[10]);

    int (*p2)[10];  // 数组指针  *修饰p2为指针变量



    // C语言并没有规定变量的存储方式，如果连续定义多个变量，它们有可能是挨着的，也有可能是分散的
    int a = 1, bb = 2, c = 3;
    int *po = &a;
    int i;

    for(i=0; i<8; i++){
        printf("%d, ", *(po+i) );
    }
    printf("\n\n");
    // 1, 40, 8, 0, 6422008, 0, 11801536, 3,  没有意义的错误示范



    /*
     * 数组中的所有元素在内存中是连续排列的，如果一个指针指向了数组中的某个元素，那么加 1 就表示指向下一个元素，减 1 就表示指向上一个元素，
     * 这样指针的加减运算就具有了现实的意义
     *
     * 数组名代表数组的首地址，是指针常量，不能进行自加自减运算。
     */

    int p[4]={1,2,3,4};
//    int *tp = &p;
//    printf("address of p: %d\n", &tp);

    int *ptr1=(int *)(&p+1);
    int *ptr2=(int *)((int)p+1);

    printf("address of p: %d\n", &p);
    printf("address of ptr1: %d\naddress of ptr2: %d\n\n",ptr1,ptr2);

    printf("value1: %x\nvalue2: %x\n\n",ptr1[-1],*ptr2);

//    address of p: 6421888
//    address of ptr1: 6421904  // &p 加1, 即就是加一组数组p, 字节数为16.
//    address of ptr2: 6421889  // (int)p 加1, 即就是加一个字节1.
//
//    value1: 4
//    value2: 2000000



    struct Test
    {
        int Num;
        char *pcName;
        short sDate;
        char cha[2];
        short sBa[4];
    }*sp;

    // 指针变量sp 字节数始终为8 在64位系统下.
    int *sp1 = (int *)(&sp+1);
    int *sp2 = (int *)(sp->sBa+1);
    printf("address of sp: %d\n", &sp);
    printf("address of sp1: %d\naddress of sp2: %d\n\n",sp1,sp2);

    printf("sp1 value: %x\nsp2 value: %x\n\n",sp[-1],*sp2);  // *sp没有初始化 所以没有值.

//    address of sp: 6421864
//    address of sp1: 6421872
//    address of sp2: 268501010  // 未知的内存空间地址, *sp2的定义待明确. 看看就好

    return 0;
}