#include<stdio.h>
#include<stdlib.h>


int main() {
    int num = 100, *p, **ptr2ptr;
    p = &num; // p的值是num变量的地址  --> *p 即 num变量的值100
    ptr2ptr = &p;  //  ptr2ptr的值是(num变量的地址)的地址  --> **ptr2ptr=*(*ptr2ptr)=*(p)=num

    printf("Single pointer *p =%d\n", *p);
    printf("Double pointer **ptr2ptr=%d \n", **ptr2ptr);
    printf("Address stored in p variable =%d \n", p);
    printf("Address of p variable=%d\n", &p);
    printf("Address of ptr2ptr=%d\n\n", &ptr2ptr);

    /*
    Single pointer *p =100
    Double pointer **ptr2ptr=100
    Address stored in p variable =6422044
    Address of p variable=6422032
    Address of ptr2ptr=6422024
     */



    /*
     const char *ptr
     char const *ptr
     non-constant 指针 指向 char类型的const的内容
     */

    char a = 'A', b = 'B';
    const char *ptr = &a;
    printf("value pointed to by ptr: %c\n", *ptr);  // A

    /*
     详解:
     *ptr 表示指针变量指向内存中的内容. ---> 该内容是常量const,不能修改
     不能通过*ptr修改 该指针变量所指向的内存中的内容.
     但是, 可以通过修改该指针变量的值, 改变其(该指针)指向的内容.
     */

    //*ptr = b;  // illegal statement (assignment of read-only location *ptr)
    ptr = &b;
    printf("value pointed to by ptr: %c\n\n", *ptr);  // B



    /*
     char *const ptr
     const 指针 指向 char类型的non-constant的内容
     */
    char c = 'C', d = 'D';
    char *const ptr_ = &c;

    printf("value pointed to by ptr_: %c\n", *ptr_);  // C
    printf("address ptr_ is pointing to: %d\n\n", ptr_);  // 6421997
    // 指针变量指向的内容可变, 但是指针变量本身不可变
    *ptr_ = d;
    printf("value pointed to by ptr_: %c\n", *ptr_);  // D
    printf("address ptr_ is pointing to: %d\n\n", ptr_);  // 6421997



    /*
     const char *const ptr
     char const *const ptr
     const 指针 指向 char类型的constant的内容
     */

    char e = 'E', f = 'F';
    const char *const ptr__ = &e;

    printf("value pointed to by ptr__: %c\n", *ptr__);
    printf("address ptr__ is pointing to: %d\n\n", ptr__);
    // 指针变量指向的内容不可变, 同时指针变量本身也不可变.
//    ptr__ = &f;  // error: assignment of read-only variable 'ptr__'
//    *ptr__ = f;  // error: assignment of read-only variable 'ptr__'

    return (0);
}
