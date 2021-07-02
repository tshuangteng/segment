#include <stdio.h>

int main() {
    // 数组在内存中的存储
    int a[] = {1, 2, 3};
    char b[] = {'a', 'b', 'c'};  // char b[] = {'a', 'b', 'c', '\0'};
    char c[] = "abc";

    printf("%s\n", a); // 越界
    printf("%d\n", a);
    printf("%d\n", &a);
    printf("%x\n", a);
    printf("%x\n\n", &a);

    // printf("%c\n", b); // 越界
    printf("%s\n", b); // 越界
    printf("%d\n", b);
    printf("%d\n", &b);
    printf("%x\n", b);
    printf("%x\n\n", &b);

    const char *s = c;
    // printf("%c\n", c); // 越界
    // printf("%c\n", s); // 越界
    printf("%d\n", c);
    printf("%d\n", s);
    printf("%s\n", c);
    printf("%s\n", s);
    printf("%x\n", c);
    printf("%x\n", s);
    printf("%c\n", *s++);
    printf("%c\n\n", *s++);

    //    ╔
    //    6422028
    //    6422028
    //    61fe0c
    //    61fe0c
    //
    //    abc╔
    //    6422025
    //    6422025
    //    61fe09
    //    61fe09
    //
    //    6422021
    //    6422021
    //    abc
    //    abc
    //    61fe05
    //    61fe05
    //    a
    //    b

    return 0;
}