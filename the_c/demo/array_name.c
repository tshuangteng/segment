#include <stdio.h>

// 数组名在内存中的存储表示

int main() {
    int a[] = {1, 2, 3};
    // char b[] = {'a', 'b', 'c'};
    char b[] = {'a', 'b', 'c', '\0'};
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

    return 0;
}