#include<stdio.h>

/*
 ++a表示取a的地址，增加它的内容，然后把值放在寄存器中；
 a++表示取a的地址，把它的值装入寄存器，然后增加内存中的a的值；

 在非内置类型的时候，尽量使用前置++，因为效率高（后置自增，效率低）
 */

int main() {
    int arr[] = {11, 12, 13, 14, 15};
    int *ptr = arr;  // arr表示的是数组的第一个元素地址(注意不是整个数组)
    *(ptr++) += 100;  // ++在后, 先用++

    printf("%d %d\n", *ptr, *(++ptr));  // printf的两个参数压栈顺序为从右至左，故也先计算*(++ptr).



    char *a[2]={"one","two"},**p=a; // 指针数组

    printf("size of a: %d\n", sizeof(a));  // 占用字节数是2个指针所占的字节大小为16

    printf("%s\t",(*p+1));  // p是指向指针的指针，*p指向a[0]"one" *p+1指向第二个字母n
    printf("%s\t",*(p+1));  // p+1指向a[1] 输出two
    printf("%c\t",**p);  // “one”的第一个字母'o'
    printf("%s\t",*(p++)+1);  // 后++，先用后加，等效于*p+1;p++
    printf("%c\n",**p-1);   // p指向“two”，**p=t,前一个字符是's'

    printf("%s\t",*(--p)+1);  // 先--，p指向"one",向前跳一个字符，输出"ne"
    printf("%s\t",*(++p)+1);  // 先++，p指向"two"向前跳一个字符，输出"wo"
    printf("%c\t",**p);  // 上一次p指向"two",输出't'
    printf("%c\t",**(p--));  // 等效于**p;p--;输出't',p指向one
    printf("%s\n",*p);  // 输出"one"

//    ne      two     o       ne      s
//    ne      wo      t       t       one

    return 0;
}